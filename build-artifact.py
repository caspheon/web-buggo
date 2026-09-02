"""Gera dist/buggo-pitch.html: o mesmo deck, porém com as imagens e o vídeo
embutidos em base64 e sem o esqueleto <html>/<head>/<body> — o formato que o
Artifact do Claude publica. Uso: python build-artifact.py"""

import base64
import mimetypes
import pathlib
import re

raiz = pathlib.Path(__file__).parent
fonte = (raiz / "index.html").read_text(encoding="utf-8")

titulo = re.search(r"<title>.*?</title>", fonte, re.S).group(0)
links = "\n".join(re.findall(r'<link[^>]+rel="stylesheet"[^>]*>', fonte))
estilo = re.search(r"<style>.*?</style>", fonte, re.S).group(0)
corpo = re.search(r"<body>(.*)</body>", fonte, re.S).group(1)


def embutir(m):
    atributo, caminho = m.group(1), raiz / m.group(2)
    tipo = mimetypes.guess_type(caminho.name)[0] or "application/octet-stream"
    dados = base64.b64encode(caminho.read_bytes()).decode("ascii")
    return '%s="data:%s;base64,%s"' % (atributo, tipo, dados)


corpo = re.sub(r'(src|poster)="(assets/[^"]+)"', embutir, corpo)

saida = raiz / "dist" / "buggo-pitch.html"
saida.parent.mkdir(exist_ok=True)
saida.write_text("\n".join([titulo, links, estilo, corpo]), encoding="utf-8")
print("%s — %.1f MB" % (saida, saida.stat().st_size / 1024 / 1024))

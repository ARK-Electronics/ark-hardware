#!/usr/bin/env python3
"""Build ARK product datasheets from products/<KEY>.toml.

Usage: uv run --no-project --with weasyprint==70.0 python datasheets/build.py [--out DIR] [--flat] [KEY ...]

With no KEY, builds every product. Writes each PDF to the product's `out` path under the repo root,
or under DIR with --out. --flat writes DIR/<file name> instead, for review copies.
See README.md for the data format and the content standard.
"""
import html as _html
import pathlib
import re
import sys
import tomllib

from weasyprint import HTML

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ASSETS = HERE / "assets"
PHOTOS = HERE / "photos"
PRODUCTS = HERE / "products"
BOILERPLATE = "Specifications are subject to change without notice."


def esc(s):
    # Keep values glued to their units so "±8 g" never wraps between the two.
    return re.sub(r"(?<=\d) (?=[a-zA-Z°Ω%])", " ", _html.escape(s))


def rows(pairs):
    return "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in pairs)


def li(items):
    # A leading "– " makes an item a sub-point of the one before it.
    return "".join(
        f'<li class="subitem">{esc(i[2:])}</li>' if i.startswith("– ") else f"<li>{esc(i)}</li>" for i in items
    )


def td(v, cls=""):
    # Unmeasured values stay loud so a draft can't pass for a release.
    if v.startswith("TBD"):
        return f'<td class="tbd {cls}"><span>{esc(v)}</span></td>'
    return f'<td class="{cls}">{esc(v)}</td>' if cls else f"<td>{esc(v)}</td>"


def table(cls, head, body):
    th = "".join(f"<th>{esc(h)}</th>" for h in head)
    tr = "".join("<tr>" + "".join(td(v) for v in r) + "</tr>" for r in body)
    return f'<table class="{cls}"><tr>{th}</tr>{tr}</table>'


def h2(title, first, new_page):
    style = ' style="margin-top:0; break-before:page"' if new_page else ' style="margin-top:0"' if first else ""
    return f"<h2{style}>{esc(title)}</h2>"


def note(s):
    return f'<p class="connote">{esc(s["note"])}</p>' if s.get("note") else ""


def range_table(s):
    blocks, cols = s["blocks"], s["cols"]
    top = "".join(f'<th class="blk" colspan="{len(cols)}">{esc(b["name"])}</th>' for b in blocks)
    sub = "".join(('<th class="blk">' if i == 0 else "<th>") + f"{esc(c)}</th>" for _ in blocks for i, c in enumerate(cols))
    body = "".join(
        f"<tr><td>{esc(row)}</td>"
        + "".join(td(v, "blk" if i == 0 else "") for b in blocks for i, v in enumerate(b["grid"][r]))
        + "</tr>"
        for r, row in enumerate(s["rows"])
    )
    corner = f'<th rowspan="2">{esc(s["corner"])}</th>'
    cg = '<colgroup><col class="c0">' + "<col>" * (len(blocks) * len(cols)) + "</colgroup>"
    return f'<table class="rng">{cg}<tr>{corner}{top}</tr><tr class="sub">{sub}</tr>{body}</table>'


def grid(cells, per):
    # Blanks pad the last row so every cell keeps the same width.
    cells = cells + ["<div></div>"] * (-len(cells) % per)
    return "".join(f'<div class="pinrow">{"".join(cells[i:i + per])}</div>' for i in range(0, len(cells), per))


def pinouts(s):
    cells = [
        f'<div><h3 class="pin">{esc(c["title"])}</h3>{table("pins pinx", s["head"], c["rows"])}{note(c)}</div>'
        for c in s["connectors"]
    ]
    return grid(cells, s.get("per_row", 3))


def columns(s):
    cells = [f'<div><h3 class="pin">{esc(c["title"])}</h3>{SECTION[c["kind"]](c)}{note(c)}</div>' for c in s["parts"]]
    return grid(cells, s.get("per_row", 2))


def figure(s):
    return f'<img class="figure" src="{(PHOTOS / s["src"]).as_uri()}" style="width:{s.get("width", 538)}pt">'


SECTION = {
    "table": lambda s: table(s.get("cls", ""), s["head"], s["rows"]),
    "compare": lambda s: table("cmp", [""] + s["cols"], s["rows"]),
    "range": range_table,
    "notes": lambda s: f'<ul class="sq">{li(s["items"])}</ul>',
    "pinouts": pinouts,
    "figure": figure,
    "columns": columns,
}


def docline(p):
    year = p["date"][:4]
    return f'{p["doc_id"]} | Version {p["version"]}, {p["date"]} | {p["sources"]} {BOILERPLATE} © {year} ARK Electronics LLC.'


def render(p):
    secs = "".join(
        h2(s["title"], i == 0, s.get("new_page", False)) + SECTION[s["kind"]](s) + note(s)
        for i, s in enumerate(p["sections"])
    )
    specs = "".join(f'<table class="spec"><tr><th colspan="2">{esc(g["group"])}</th></tr>{rows(g["rows"])}</table>' for g in p["specs"])
    res = "".join(f"<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>" for k, v in p["resources"])
    frame = " framed" if p.get("photo_frame") else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{esc(p['title'])} Datasheet</title>
<link rel="stylesheet" href="datasheet.css"></head><body>
<div class="hdr"><img src="ark_logo.png"><span>{esc(p['title'].upper())} · DATASHEET V{esc(p['version'])} · HW REV {esc(p['rev'])}</span></div>
<div class="kicker">{esc(p['kicker'])}</div>
<h1>{esc(p['title'])}</h1>
<div class="sub">{esc(p['subtitle'])}</div>
<div class="cols">
 <div class="main">
  {''.join(f'<p>{esc(x)}</p>' for x in p['intro'])}
  <h2>KEY FEATURES</h2>
  <ul class="sq">{li(p['features'])}</ul>
  <h2>SPECIFICATIONS</h2>
  {specs}
 </div>
 <div class="side">
  <img class="photo{frame}" src="{(PHOTOS / p['photo']).as_uri()}">
  <table class="spec glance"><tr><th colspan="2">AT A GLANCE</th></tr>{rows(p['glance'])}</table>
  <div class="box"><h3>COMPLIANCE &amp; SOURCING</h3><ul>{li(p['compliance'])}</ul></div>
  <div class="box tint"><h3>ORDERING &amp; RESOURCES</h3><table class="res">{res}</table></div>
 </div>
</div>
<div class="p2">
{secs}
 <div class="doc">{esc(docline(p))}</div>
</div>
</body></html>"""


def load(key):
    p = tomllib.loads((PRODUCTS / f"{key}.toml").read_text())
    p.setdefault("out", f"{key}/datasheet/{key}_Datasheet.pdf")
    return p


def main():
    args = sys.argv[1:]
    flat = "--flat" in args
    if flat:
        args.remove("--flat")
    out = ROOT
    if "--out" in args:
        i = args.index("--out")
        out = pathlib.Path(args[i + 1])
        del args[i:i + 2]
    for key in args or sorted(f.stem for f in PRODUCTS.glob("*.toml")):
        p = load(key)
        rel = pathlib.Path(p["out"])
        dst = out / (rel.name if flat else rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        HTML(string=render(p), base_url=str(ASSETS) + "/").write_pdf(dst)
        print(dst)


if __name__ == "__main__":
    main()

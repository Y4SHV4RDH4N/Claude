import re
CSS = r"""
:root{--bg:#000;--panel:#0d0d0d;--panel2:#161616;--line:#3a3a3a;--fg:#f2f2f2;--dim:#a8a8a8;--hi:#fff}
*{box-sizing:border-box}
html{background:#000}
body{margin:0;background:#000;color:var(--fg);font-family:Helvetica,"Helvetica Neue",Arial,sans-serif;font-size:14px;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}
main{max-width:920px;margin:0 auto;padding:28px 20px 60px}
h1{font-size:40px;letter-spacing:-1px;margin:0 0 6px;line-height:1.05}
h2{font-size:26px;margin:0 0 4px;letter-spacing:-.5px}
h3{font-size:16px;margin:22px 0 8px;text-transform:uppercase;letter-spacing:1.5px;border-bottom:1px solid var(--line);padding-bottom:5px}
h4{font-size:14px;margin:14px 0 4px}
.part{page-break-before:always;border-top:3px solid #fff;padding-top:14px;margin-top:34px}
.part:first-of-type{page-break-before:auto}
.tag{display:inline-block;border:1px solid #fff;padding:1px 8px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;margin-right:6px}
.sub{color:var(--dim);margin:0 0 14px}
p{margin:6px 0}
ul,ol{margin:6px 0 6px 20px;padding:0}li{margin:2px 0}
.box{background:var(--panel);border:1px solid var(--line);padding:12px 14px;margin:10px 0;page-break-inside:avoid}
.formula{background:var(--panel2);border:1px solid #fff;padding:10px 14px;margin:10px 0;page-break-inside:avoid}
.formula .t{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--dim);margin-bottom:6px}
.formula .row{display:flex;flex-wrap:wrap;gap:6px 30px;align-items:center;margin:4px 0}
.formula .row>div{white-space:nowrap}
.warn{border-left:4px solid #fff;background:var(--panel);padding:8px 12px;margin:10px 0;page-break-inside:avoid}
.warn b:first-child{text-transform:uppercase;letter-spacing:1px;font-size:11px}
.ex{border:1px solid var(--line);margin:16px 0;background:var(--panel)}
.ex .q{padding:10px 14px;background:#1f1f1f;border-bottom:1px solid var(--line)}
.ex .q .n{font-weight:bold;letter-spacing:1px;text-transform:uppercase;font-size:11px;display:block;margin-bottom:3px}
.ex .s{padding:10px 14px}
.ex .s .st{margin:5px 0}
.lvl{float:right;border:1px solid #fff;font-size:10px;padding:0 6px;letter-spacing:1px;text-transform:uppercase}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13px;page-break-inside:avoid}
th,td{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}
th{background:#222;font-weight:bold}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
.ans{display:inline-block;border:2px solid #fff;padding:2px 10px;margin:6px 0;font-weight:bold}
.f{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;margin:0 3px;line-height:1.25}
.f>span:first-child{border-bottom:1px solid #fff;padding:0 4px 1px}.f>span:last-child{padding:1px 4px 0}
.k{font-style:italic}
.toc a{color:#fff;text-decoration:none;border-bottom:1px dotted #777}
.toc li{margin:3px 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.small{font-size:12px;color:var(--dim)}
.check li{list-style:none;margin-left:-16px}.check li:before{content:"\2610  "}
hr{border:0;border-top:1px solid var(--line);margin:16px 0}
@page{size:A4;margin:12mm;background:#000}
@media print{.part{page-break-before:always}}
@media(max-width:640px){.grid2{grid-template-columns:1fr}h1{font-size:30px}}
"""
def macro(s):
    # {{num|den}} -> fraction ; iterate for nesting
    for _ in range(3):
        s = re.sub(r"\{\{([^{}|]+)\|([^{}]+)\}\}", r'<span class="f"><span>\1</span><span>\2</span></span>', s)
    return s
def F(title, *rows):
    r = "".join(f'<div class="row">' + "".join(f"<div>{x}</div>" for x in row.split(" ;; ")) + "</div>" for row in rows)
    return f'<div class="formula"><div class="t">{title}</div>{r}</div>'
def EX(n, lvl, q, *steps, ans=None):
    st = "".join(f'<div class="st">{x}</div>' for x in steps)
    a = f'<div class="ans">{ans}</div>' if ans else ""
    return f'<div class="ex"><div class="q"><span class="lvl">{lvl}</span><span class="n">{n}</span>{q}</div><div class="s">{st}{a}</div></div>'
def W(label, txt): return f'<div class="warn"><b>{label}. </b>{txt}</div>'
def T(head, rows, num=()):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f'<td{" class=n" if i in num else ""}>{x}</td>' for i, x in enumerate(r)) + "</tr>" for r in rows)
    return f"<table><tr>{h}</tr>{b}</table>"
def UL(*x): return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"

body = []
A = body.append
exec(open(__file__.replace("build.py", "content.py")).read())
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Service Operations Midterm Study Guide</title><style>{CSS}</style></head><body><main>{macro("".join(body))}</main></body></html>"""
open(__file__.replace("build.py", "service-ops-midterm-study-guide.html"), "w").write(html)
print("ok", len(html))

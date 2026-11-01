"""Her ders klasörü: veri/{course.json,cards.json,quiz.json,notlar.md} -> index.html + anki-kartlar.csv; ayrıca ana sayfa."""
import csv, json, pathlib, re, html as H

root = pathlib.Path(__file__).parent
tpl = (root / "_arac" / "template.html").read_text(encoding="utf-8")
js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<" + chr(92) + "/")
gens = set(re.findall(r"^  (\w+):\{label:", tpl, re.M))
hub = []
for d in sorted(root.iterdir()):
    v = d / "veri"
    if not (v / "course.json").exists():
        continue
    course = json.loads((v / "course.json").read_text(encoding="utf-8"))
    cards = json.loads((v / "cards.json").read_text(encoding="utf-8"))
    quiz = json.loads((v / "quiz.json").read_text(encoding="utf-8"))
    notes = (v / "notlar.md").read_text(encoding="utf-8")
    course["id"] = d.name
    for q in quiz:
        assert 0 <= q["a"] < len(q["o"]) and q["d"] in map(int, course["ders"]), q["q"]
    for c in cards:
        assert c["d"] in map(int, course["ders"]), c["f"]
    assert set(course.get("gen", [])) <= gens, course.get("gen")
    out = (tpl.replace("/*TITLE*/", H.escape(course["title"])).replace("/*COURSE*/", js(course))
              .replace("/*CARDS*/", js(cards)).replace("/*QUIZ*/", js(quiz)).replace("/*NOTES*/", js(notes)))
    (d / "index.html").write_text(out, encoding="utf-8")
    with open(d / "anki-kartlar.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        for c in cards:
            w.writerow([c["f"], c["b"], f"{course['title'].split(' ')[0]} {course.get('unit', 'Ders')}{c['d']} " + c["t"].replace(" ", "_")])
    hub.append((d.name, course, len(cards), len(quiz)))
    print(d.name, len(cards), "kart", len(quiz), "soru")

items = "".join(f'<a class="c" href="{n}/index.html"><b>{H.escape(c["title"])}</b><span>{len(c["ders"])} {c.get("unit", "ders").lower()} · {k} kart · {q} soru{" · alıştırma üretici" if c.get("gen") else ""}</span></a>' for n, c, k, q in hub)
(root / "index.html").write_text(f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Çalışma Sistemi</title>
<style>:root{{--bg:#faf8f4;--card:#fff;--ink:#1d1b18;--mute:#6b665d;--line:#e4dfd5;--accent:#c2410c}}@media(prefers-color-scheme:dark){{:root{{--bg:#171512;--card:#211e1a;--ink:#f1ede4;--mute:#a39c8e;--line:#35302a;--accent:#fb923c}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,sans-serif}}.w{{max-width:640px;margin:0 auto;padding:32px 16px}}h1{{font:700 26px Georgia,serif;margin:0 0 4px}}p{{color:var(--mute)}}
.c{{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0;text-decoration:none;color:var(--ink)}}.c:hover{{border-color:var(--accent)}}.c b{{display:block;font-size:18px}}.c span{{color:var(--mute);font-size:14px}}</style></head>
<body><div class="w"><h1>Çalışma Sistemi</h1><p>Ders seç: notlar, aralıklı tekrar kartları, test, sınırsız alıştırma soruları ve günlük plan.</p>{items}</div></body></html>''', encoding="utf-8")

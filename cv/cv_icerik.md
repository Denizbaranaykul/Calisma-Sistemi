# CV — Deniz Baran Aykul (Remote Full Stack Developer — famelink.ai)

> Notlar (CV'ye girmez):
> - Köşeli parantezli her şey `[...]` doldurulmalı ya da satırıyla birlikte silinmeli. `[X]` = bilinmeyen sayı, uydurma.
> - `[?]` işaretli beceriler repolarda kanıtlanmadı; gerçekten kullanabiliyorsan işareti kaldır, yoksa sil.
> - Doğum tarihi (21.09.2004) uluslararası/ATS pratiği gereği bu İngilizce CV'de YOK. Türkçe bir CV istenirse
>   iletişim satırına "Doğum tarihi: 21.09.2004" eklenebilir (Türkiye'de yaygın, zorunlu değil). Fotoğraf da İngilizce CV'ye konmaz.
> - Hedef: tek sayfa A4. Sığmazsa ilk kısılacak yer 4. proje (Study System), sonra Interests satırı.
> - "Live" linklerini göndermeden önce tarayıcıda açıp kontrol et.

---

# DENIZ BARAN AYKUL
**Full Stack Developer (JavaScript · Firebase · Node.js)**

[City], Turkey · Open to remote · [email@example.com] · [+90 5XX XXX XX XX]
github.com/Denizbaranaykul · [linkedin.com/in/...] · [portfolio URL, if any]

## Summary
Management Information Systems student (3rd year) who builds and ships web applications end to end, from UI to authentication, database and deployment. Founder of my university's Software Development Community, whose live platform (with an AI assistant built on Gemini) I developed and maintain.

## Projects

**PAU Software Development Community Platform** — Live: pauyazilimgelistirme.com.tr · github.com/Denizbaranaykul/[Yaz-l-m_toplulugu]
*JavaScript (ES modules), HTML/CSS, Firebase Auth, Cloud Firestore, Firebase Remote Config, Google Gemini API*
- Built and maintain the community's web platform (public site, blog, membership applications, training module and role-based admin panel) on Firebase Auth and Firestore, used by [X] members.
- Integrated a Gemini 2.5 Flash AI assistant grounded on a custom community-knowledge prompt, with API-key rotation on HTTP 429 rate limits managed through Firebase Remote Config.
- Designed an assignment workflow where members submit work, admins grade (0–100) and resolve appeals via batched Firestore writes, and scores feed a leaderboard; [X] submissions processed.

**Finance Tracker — personal budgeting web app** — Live: denizbaranaykul.github.io/finansal-takip · github.com/Denizbaranaykul/finansal-takip
*JavaScript, Firebase Auth, Cloud Firestore, Chart.js, HTML/CSS*
- Developed a budgeting app with email/password auth and per-user Firestore collections for full CRUD on income and expense transactions, filtered by period, type and category.
- Visualized spending with Chart.js (category breakdown, monthly trend) and added CSV import/export for bulk data entry.
- Built a data-layer abstraction that falls back to a LocalStorage demo mode when no Firebase config is present, plus an admin task center with its own charts; responsive mobile layout.

**ZNG Elektrik Enerji — Corporate Website** — [Live URL / "client project"] · github.com/Denizbaranaykul/zng
*Node.js (zero-dependency static site generator), JavaScript, CSS*
- Wrote a zero-dependency Node.js build pipeline that renders 60+ bilingual (TR/EN) pages from data modules and templates, with a local dev server.
- Planned a Wix-to-static migration that keeps legacy URL slugs and redirects to preserve existing search rankings; [result, e.g. "load time reduced from X s to Y s" — only if measured].

**Study System — offline learning tool generator** — [private repo / link if made public]
*Python, JavaScript, HTML/CSS, LocalStorage*
- Built a Python generator that turns JSON/Markdown course data into self-contained single-page study apps with spaced-repetition flashcards, quizzes, progress tracking and Anki CSV export (6 courses, 500+ cards, ~390 questions).
- Implemented randomized practice generators with step-by-step solutions and an interactive AVL-tree rotation exercise that validates the final tree.

## Leadership
**Founder, President and Vice President** — Software Development Community, Pamukkale University · [2025] – [Present]
- Founded the community in 2025; served as President ([dates]) and Vice President ([dates]).
- Organized [X] workshops/events for [X] members; [one more concrete outcome, e.g. "ran a [X]-week training program with graded assignments"].
- Designed and shipped the community's web platform and AI assistant (see Projects).

## Education
**B.Sc. Management Information Systems** — Pamukkale University, Denizli, Turkey · [2024] – [2028] (expected)
3rd year · GPA: [X.XX/4.00 — omit if below ~3.0] · Relevant coursework: Data Structures, E-Commerce, Statistics, Strategic Management, [Database Management Systems?], [Systems Analysis & Design?]

## Technical Skills
- **Languages:** JavaScript (ES6+, ES modules), HTML5, CSS3, Python, [SQL ?], [TypeScript ?]
- **Backend & Data:** Firebase (Authentication, Cloud Firestore, Remote Config), Node.js (build tooling, fs, ES modules), REST API integration, [Express ?], [relational DB design ?]
- **Frontend:** Vanilla JS SPA architecture, responsive design, Chart.js, [React ?]
- **AI:** Google Gemini API (prompt design, rate-limit handling)
- **Tools:** Git, GitHub, GitHub Pages, custom-domain DNS setup, pandas, AI-assisted development (Claude Code) [keep only if comfortable discussing it]
- **Languages (spoken):** Turkish (native), English ([level, e.g. B2 / professional working])

## Interests
Basketball, boxing.

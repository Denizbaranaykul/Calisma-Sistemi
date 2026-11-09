# GitHub repo kararı — famelink.ai (Remote Full Stack Developer) başvurusu

İnceleme tarihi: 2026-11-05. Kaynak: GitHub API (public 4 repo), yerel klonlar (`C:\codes\finansal-takip`, `C:\codes\gardirop`, `C:\codes\Calisma-Sistemi`). Private 28 repo görülemedi.

## 1. Her repo gerçekte ne?

| Repo | Ne yapıyor | Teknoloji | Full stack mi? | Canlı demo | Olgunluk |
|---|---|---|---|---|---|
| **Yaz-l-m_toplulugu** | PAÜ Yazılım Geliştirme Topluluğu sitesi: tanıtım, blog, üyelik başvuru formu, giriş, eğitim modülü (soru/ödev gönderme, itiraz, liderlik tablosu), rol kontrollü yönetici paneli (ödev puanlama 0–100, listeler), Gemini 2.5 Flash tabanlı topluluk asistanı (özel prompt + 429'da API anahtarı rotasyonu, anahtarlar Remote Config'ten) | Vanilla JS (ES modules), HTML, CSS, Firebase Auth + Firestore + Remote Config, Gemini REST API | Kısmen: frontend + BaaS (Auth/DB). Kendi sunucu kodu yok | **Var:** pauyazilimgelistirme.com.tr (özel alan adı, GitHub Pages) | En olgun proje. ~49 commit (39 sen, 8 "claude", 2 AHMETBNL), 2025-09'dan beri aktif. README yok |
| **finansal-takip** | Kişisel bütçe/harcama takip uygulaması: e-posta/şifre ile kayıt-giriş, kullanıcı başına Firestore koleksiyonunda gelir/gider CRUD, dönem/tür/kategori filtreleri, Chart.js grafikleri (kategori dağılımı, aylık trend), CSV içe/dışa aktarma, Firebase ayarlı değilse LocalStorage demo moduna düşen servis katmanı, yönetici görev merkezi (+grafikler) | Vanilla JS, Firebase Auth + Firestore, Chart.js 4, HTML/CSS (~8.900 satır) | Kısmen: frontend + BaaS | **Var:** denizbaranaykul.github.io/finansal-takip | İyi; 4 commit, tek günlük yoğun çalışma. README yok. Firebase proje adı `todoapp-90b16` (eski projeden kalma) |
| **main** | finansal-takip'in eski/erken kopyası ("Bütçem & Harcama Takip"), aynı dosya yapısı, aynı Firebase projesi, admin paneli yok | Vanilla JS, Firebase, Chart.js | Aynı | Yok (Pages 404) | 2 commit, mükerrer |
| **zng** | ZNG Bilişim Elektrik Enerji firması için kurumsal site. Sıfır bağımlılıklı Node.js statik site üreticisi (`build.mjs`): veri modüllerinden (hizmetler, projeler, içerik) TR/EN ~60+ sayfa üretir, yerel sunucu (`serve.mjs`). Wix'ten taşıma için eski Türkçe URL'ler korunmuş (SEO) | Node.js (ESM), JS, CSS | Hayır (statik site + build aracı) | Yok: github.io/zng sadece README'yi gösteriyor; firmanın asıl alanı zngelektrikenerji.com (hâlâ Wix olabilir) | Yayına hazır değil: README'deki yapılacaklar açık (projeler örnek içerik, form servisi yok). Tek commit ("first commit") |
| **Calisma-Sistemi** (private, yerel) | Ders çalışma sistemi: Python `build.py` JSON/Markdown ders verisinden her ders için tek dosyalık çevrimdışı HTML uygulaması üretir; aralıklı tekrar kartları, test, rastgele sayılı alıştırma üreticileri, etkileşimli AVL döndürme, ilerleme (LocalStorage), Anki CSV. 6 ders, 531 kart, 394 soru | Python, JS, HTML/CSS | Hayır | Yok | Çalışır durumda, README'li. Ders slaytlarından türetilmiş içerik barındırıyor |
| **gardirop** (yerel, remote yok) | Sadece Flutter `build/` çıktısı var, kaynak kod yok | Flutter/Dart (?) | Değerlendirilemedi | Yok | Değerlendirilemedi; kaynak muhtemelen başka yerde / private repolardan biri |

Not: Hiçbir projede kendi yazdığın bir backend (Express/NestJS/Django vb. + SQL veritabanı + REST API) yok; "backend" tarafı Firebase (BaaS). Bu bir full stack ilanı için en büyük boşluk — aşağıdaki "Öneri" bölümüne bak.

## 2. Karar tablosu

| Repo | Karar | Gerekçe |
|---|---|---|
| Yaz-l-m_toplulugu | **PİNLE (1.)** | Canlı, özel alan adlı, gerçek kullanıcılı, auth + rol + DB + AI entegrasyonu. famelink AI şirketi olduğu için Gemini asistanı doğrudan ilgi çeker. Liderlik hikâyesiyle bağlantılı |
| finansal-takip | **PİNLE (2.)** | Canlı demo, temiz CRUD + auth + grafik + CSV; "uçtan uca uygulama" göstergesi |
| zng | **GÖSTER (müşteri izni varsa PİNLE 3.)** | Node.js build aracı ve SEO odaklı taşıma düşüncesi güzel; ama yayında değil, içerik örnek. Gerçek bir firmanın markası/bilgileri var → yayınlamadan önce firmadan izin al. İzin yoksa private yap ve CV'de "client project (private)" yaz |
| main | **GÖSTERME** (archive veya private yap, ya da sil) | finansal-takip'in mükerrer, eski hâli; profilde kalabalık ve "main" adı kötü izlenim veriyor. Tutmak istersen yeni ad: `budget-tracker-prototype` + archive |
| Calisma-Sistemi | **GÖSTERME (şimdilik private kalsın)**; istersen motoru ayrı repo yapıp PİNLE | Teknik olarak ilginç (Python generator, spaced repetition, AVL alıştırması), ama ders slaytlarından türetilmiş içerik telif açısından riskli. Öneri: `_arac/template.html` + `build.py` + 1 örnek (kendi yazdığın) dersle `study-system-generator` adlı public repo |
| gardirop | **Karar yok** | Kaynak kod yerelde yok. Private repolar arasındaysa aşağıdaki kriterlerle değerlendir; çalışan bir Flutter uygulamasıysa mobil yetkinlik olarak değerli (CV'ye "Flutter [?]" ancak o zaman) |

## 3. Önerilen yeniden adlandırma ve description (İngilizce, 1 satır)

> Uyarı: Repo adını değiştirmek GitHub Pages adresini değiştirir (`github.io/<eski-ad>` kırılır; GitHub git URL'lerini yönlendirir ama Pages'i yönlendirmez). Özel alan adlı repo (topluluk sitesi) etkilenmez. finansal-takip'i yeniden adlandırırsan CV ve README'deki demo linkini güncelle.

| Mevcut ad | Önerilen ad | Description | Topics |
|---|---|---|---|
| Yaz-l-m_toplulugu | `pau-software-community` | Web platform for Pamukkale University Software Development Community: Firebase auth, assignments & leaderboard, admin panel, Gemini AI assistant. | firebase, firestore, gemini-api, javascript, community |
| finansal-takip | `finance-tracker` (veya adı koru) | Personal budget tracker with Firebase Auth/Firestore, Chart.js analytics, CSV import/export and an offline demo mode. | firebase, chartjs, javascript, budgeting |
| zng | `zng-corporate-site` | Bilingual (TR/EN) corporate website built with a zero-dependency Node.js static site generator, SEO-preserving Wix migration. | nodejs, static-site-generator, seo, i18n |
| main | `budget-tracker-prototype` (archive) | Early prototype of finance-tracker (archived). | — |
| Calisma-Sistemi (motoru) | `study-system-generator` | Python generator for offline study apps: spaced-repetition flashcards, quizzes, randomized practice and an interactive AVL rotation exercise. | python, spaced-repetition, education |

Her birinin "About" kısmındaki Website alanına canlı linki ekle (topluluk: pauyazilimgelistirme.com.tr, finansal-takip: denizbaranaykul.github.io/finansal-takip).

## 4. README'lerde eksik olanlar (dört public reponun hiçbirinde README yok, zng hariç — o da Türkçe ve müşteriye yönelik)

Her gösterilecek repo için İngilizce README şablonu:
1. Başlık + tek cümlelik açıklama + **Live demo** linki
2. Ekran görüntüsü veya kısa GIF (en az 1–2 tane; recruiter kodu değil bunu görür)
3. Features listesi
4. Tech stack
5. Architecture / folder structure (kısa)
6. Getting started (çalıştırma adımları, Firebase config nasıl verilir)
7. Security notes (aşağıya bak)
8. Roadmap / known limitations, lisans

Repo bazında ek eksikler:
- **Yaz-l-m_toplulugu:** README yok; `scratch/rename_imports.ps1` gibi geçici dosyalar repoda — kaldır veya `.gitignore`'a ekle. 13 MB, büyük kısmı fotoğraflar; görselleri sıkıştır (WebP/AVIF). **Güvenlik:** Gemini API anahtarları Remote Config üzerinden istemciye iniyor, yani tarayıcıdan okunabilir durumda — anahtarları bir Cloud Function (veya küçük bir Node/Express proxy) arkasına taşı. Bu, hem güvenlik açığını kapatır hem de projeye gerçek bir backend katmanı ekler (CV'de "serverless backend" maddesi olur). Admin rol kontrolünün Firestore Security Rules ile de zorlandığından emin ol ve kuralları (`firestore.rules`) repoya ekle.
- **finansal-takip:** README yok; Firebase proje adı `todoapp-90b16` → yeni proje veya en azından README'de açıkla. `firestore.rules` dosyası ekle. Yerel klasördeki `python.py` (Excel'den Gemini'ye prompt yapıştıran pyautogui otomasyonu) bu projeyle ilgisiz — commit etme. Demo hesabı/demo modu README'de anlatılsın ki recruiter kayıt olmadan deneyebilsin.
- **zng:** İngilizce README bölümü; GitHub Pages şu an README'yi yayınlıyor — ya `dist/`'i Pages'e bağla (Settings → Pages → GitHub Actions veya `/dist`), ya Pages'i kapat. `.claude/launch.json` repoda; kaldırılabilir. Müşteri izni olmadan public tutma.
- **main:** README yazmaya değmez; archive et.

## 5. Private 28 repo için eleme kriterleri

Her repo için sırayla sor; ilk "hayır"da dur.

**Kesin GİZLE (private kalsın veya archive):**
- Ders ödevi, lab, sınav hazırlığı, ders notu (özellikle hoca/slayt içeriği barındıranlar — telif ve kopya riski)
- Tutorial / kurs takip projesi (to-do app, YouTube klonu vb.) ve fork'a kendi katkısı olmayanlar
- 1–2 commit'lik, yarım bırakılmış, çalışmayan veya "test", "deneme", "main", "asdf" gibi adlı repolar
- Başka bir public reponun eski kopyası (ör. `main`)
- İçinde gizli anahtar, şifre, `.env`, kişisel veri veya müşteri verisi olanlar (önce temizle — not: git geçmişinden de silinmesi gerekir, anahtarları ayrıca iptal et)
- Müşteri/şirket projesi ve izin yoksa

**GÖSTER (public yap):**
- Çalışıyor, kendi fikrin/katkın belirgin, README'si var veya yazılabilir
- Bir teknolojiyi CV'de iddia etmeni sağlıyor (ör. SQL veritabanlı bir backend, Flutter uygulaması, TypeScript/React)

**PİNLE (en fazla 6, ideali 3–4):**
- Canlı demo/deploy var + README + ekran görüntüsü
- Frontend + backend + veritabanı içeren (full stack ilanı için öncelik) veya AI entegrasyonu olan (famelink için öncelik)
- Son 12 ayda aktif, anlamlı commit geçmişi olan
- CV'deki proje bölümüyle bire bir eşleşen

**Ek kontrol listesi (public yapmadan önce):**
- [ ] `git log -p | grep -iE "api[_-]?key|secret|password|token"` ile geçmişte sızıntı var mı
- [ ] Description + topics + website alanı dolu
- [ ] Repo adı İngilizce, kebab-case, anlamlı
- [ ] Commit mesajları çok kötüyse (ör. "asd") sorun değil ama pinlenen repolarda dikkat çekmesin
- [ ] AI destekli geliştirme: topluluk reposunda "claude" kullanıcısının 8 commit'i görünüyor. Bu gizlenecek bir şey değil (famelink AI şirketi), ama mülakatta her satırı açıklayabilir olmalısın

## 6. Profil düzeyinde öneriler
- **Profil README'si** (`Denizbaranaykul/Denizbaranaykul` reposu): 2 satır tanıtım, pinlenen projeler, iletişim. Yok gibi görünüyor.
- **Eksik halka: gerçek backend.** Başvurudan önce/sonra küçük ama tam bir proje önerisi: Node.js + Express (veya NestJS) + PostgreSQL + REST API + JWT auth + Docker + bir yere deploy (Render/Railway/Fly). famelink'e uyan konu: "creator/influencer kampanya takip" veya "sosyal medya içerik analizi + LLM özeti". En hızlı yol: topluluk sitesindeki Gemini çağrısını bir Node/Express veya Cloud Functions proxy'sine taşımak.
- Pinleme sırası: 1) pau-software-community 2) finance-tracker 3) zng-corporate-site (izinliyse) 4) private'tan çıkacak en iyi full stack/Flutter projesi.

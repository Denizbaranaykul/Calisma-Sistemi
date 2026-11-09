# Başvuru paketi eleştirisi — famelink.ai "Remote Full Stack Developer"

Değerlendiren bakış açısı: teknik işe alım + senior full stack mühendis. İnceleme tarihi: 2026-11-05.
İncelenen: `cv_icerik.md`, `repo_karari.md`, `basvuru_eposta.md`. Doğrulama: GitHub API + raw dosyalar (Yaz-l-m_toplulugu, zng), yerel `C:\codes\finansal-takip`, canlı siteler (curl).

---

## 0. Önce bilmen gereken iki gerçek (her şeyi değiştiriyor)

**a) famelink.ai bir "creator/influencer marketplace" değil.** Sitenin kendi tanımı: *"Pioneering Conversational AI Experiences"* — AI companionship, immersive roleplay, sosyal etkileşim. Yani şirket **sohbet tabanlı LLM ürünleri** yapıyor. Sonuçları:
- E-postadaki `"matching brands with creators"` önerisi yanlış; gönderilirse araştırma yapmadığın anlaşılır.
- Senin en güçlü kozun Firebase değil, **Gemini tabanlı sohbet asistanı**. Ama şu hâliyle (aşağıda) bir conversational-AI şirketinin mülakatında ilk soruda zayıf kalır: tek tur, geçmiş yok, streaming yok, system instruction yok.

**b) Topluluk sitesindeki AI asistanının kodu, mülakatta seni zora sokacak kadar açık.** Doğrulandı (`js/main/yapay-zeka.js`):
- Gemini API anahtarları Remote Config'ten **tarayıcıya iniyor** ve `?key=${currentKey}` ile doğrudan istemciden çağrılıyor. Herkes DevTools'tan anahtarları kopyalayabilir.
- "429'da anahtar rotasyonu" = birden fazla ücretsiz anahtarla Google'ın kotasını aşmak. CV'de bunu **başarı** olarak yazmak, deneyimli bir mühendise "kota/ToS dolanıyor ve anahtarları açığa bırakıyor" diye okunur. Bu madde şu hâliyle **eksi puan**.
- Prompt: `Topluluk bilgisi:\n${communityInfo}\n\nSoru: ${userMessage}` — tek tur, konuşma geçmişi yok, `systemInstruction` kullanılmıyor, prompt injection'a karşı hiçbir şey yok.

---

## KRİTİK

### K1. AI asistanı maddesi: güvenlik açığını özellik gibi sunuyor
**Sorun:** "API-key rotation on HTTP 429 rate limits managed through Firebase Remote Config" ifadesi, anahtarların istemcide olduğunu ve kota dolanıldığını ilan ediyor. famelink gibi LLM API maliyetini bizzat ödeyen bir şirket için bu kırmızı bayrak.
**Öneri (başvurudan ÖNCE, 1 gün):** Gemini çağrısını bir **Firebase Cloud Function (Node.js)** arkasına taşı:
- Anahtar Secret Manager'da (`defineSecret`), istemci sadece `/chat` endpoint'ini çağırır.
- Firebase Auth ID token doğrulaması + kullanıcı başına basit rate limit (Firestore'da sayaç).
- Anahtar rotasyonunu kaldır; tek anahtar + düzgün 429 backoff.
- Bonus (yarım gün): son N mesajı `contents` dizisine ekleyerek **çok turlu konuşma**, `systemInstruction` ile persona, `streamGenerateContent` ile **streaming** yanıt.
- Eski anahtarları Google AI Studio'da **iptal et** (Remote Config'ten silmek yetmez; zaten sızmış sayılır).

Bu tek iş hem güvenlik açığını kapatır hem "full stack" iddiasına gerçek bir backend katmanı ekler hem de famelink'in tam iş alanına (conversational AI) birebir oturur.
**Yeniden yazılmış madde (iş bittikten sonra):**
> - Built a multi-turn Gemini 2.5 Flash chat assistant behind a Node.js Cloud Function (auth-verified REST endpoint, server-side secrets, per-user rate limiting, streamed responses).

**İş bitmeden gönderilecekse** (dürüst minimum):
> - Integrated a Gemini 2.5 Flash chat assistant with a custom knowledge prompt; currently moving API calls to a server-side Cloud Function.

Rotasyon kelimesini hiçbir sürümde kullanma.

### K2. "Full Stack Developer" başlığı kanıtsız
**Sorun:** Dört public repoda da kendi yazdığın sunucu kodu, REST API, SQL veya test yok. Backend = Firebase (BaaS) + istemci tarafı kurallar. Başlıktaki "Node.js" da yalnızca bir statik site üreticisinden (zng) geliyor. Bir senior 30 saniyede repolara bakıp bunu görür; başlıktaki iddia ile repolar arasındaki fark güveni düşürür.
**Öneri:** Başlığı kanıta göre kur, eksikliği gizleme:
> **Full Stack Developer — JavaScript · Firebase · Node.js · LLM APIs**

ve Summary'de çerçevele:
> Builds and ships production web apps on serverless backends (Firebase Auth, Firestore, Cloud Functions) and integrates LLM APIs; currently deepening relational backend skills (Node.js/Express, PostgreSQL).

"Serverless/BaaS backend" dürüst ve savunulabilir bir ifade; "full stack" kelimesini tutmak için **K1'deki Cloud Function şart**. Mülakatta "Firebase dışında backend yazdın mı?" sorusuna hazır cevap: "Hayır, Cloud Functions ile sunucu tarafı yazdım; Express + PostgreSQL ile X projesine başladım" — ama ancak gerçekten başladıysan.

### K3. Güvenlik/yetki: admin kontrolleri istemcide, kurallar repoda yok
**Doğrulanan bulgular:**
- **finansal-takip:** Admin yetkisi `firebase-service.js` içindeki sabit `ADMIN_EMAILS` listesiyle (`daykul75@gmail.com`, `admin@todoapp.com`...) istemcide belirleniyor. `firestore.rules` repoda yok. Kişisel Gmail adresin public kodda.
- **Topluluk sitesi:** Kayıt sırasında `role: "student"` istemciden yazılıyor; admin kontrolü `userDoc.data().role !== 'admin'` ile yine istemcide. Kurallar repoda yok → bir reviewer "kullanıcı kendi dokümanına `role: 'admin'` yazabilir mi?" diye sorar.
- **Topluluk admin paneli:** Öğrencinin gönderdiği alanlar (`data.odevKodu`, `data.adSoyad` vb.) `card.innerHTML = \`...${data...}\`` ile kaçışsız basılıyor → **stored XSS** (öğrenci, admin'in tarayıcısında kod çalıştırabilir). Puan 0–100 aralığı istemcide bile doğrulanmıyor (sadece `isNaN`).
- EmailJS servis/template ID'leri ve fallback alıcı olarak kişisel Gmail adresi kodda.

**Not:** Firebase web `apiKey` (`AIzaSy...` firebase-config.js'te) gizli değildir; açık olması normal. Sorun Gemini anahtarları ve kurallar.
**Öneri (başvurudan önce, 2–3 saat):**
1. Her iki projeye `firestore.rules` ekle: kullanıcı yalnızca kendi `users/{uid}` dokümanını okuyabilsin, `role` alanını **değiştiremesin**; admin kontrolü `get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin'` ile kurallarda.
2. `innerHTML` + kullanıcı verisi olan yerlerde `textContent` / `createElement` kullan.
3. Kişisel e-posta adresini koddan çıkar.
Bunlar CV'ye madde bile olur: *"Enforced role-based access with Firestore Security Rules."* — ama ancak yaptıktan sonra.

### K4. GitHub profil adı "haaland"
**Sorun:** API'de profil `name: "haaland"`, bio boş, blog boş; commit'lerin bir kısmı "Haaland/haaland" adıyla. CV'deki linke tıklayan recruiter, adayın adını değil bir futbolcunun adını görüyor.
**Öneri:** Profil adı → "Deniz Baran Aykul", bio → "MIS student · JavaScript/Firebase · LLM apps", website → pauyazilimgelistirme.com.tr veya LinkedIn. `git config --global user.name "Deniz Baran Aykul"`. Profil README'si (repo_karari.md'de zaten önerilmiş) 10 dakikalık iş.

### K5. Doldurulmamış `[X]` metrikleri ve uydurma riski
**Sorun:** "used by [X] members", "[X] submissions processed", "Organized [X] workshops". Bunlar gerçek sayı değilse madde çöker; tahmin yazmak mülakatta yakalanır (topluluk küçük, sorulur).
**Öneri:** Firestore'dan gerçek sayıları çek (`users`, `submissions` koleksiyon sayıları — konsoldan 2 dakika). Sayı yoksa maddeyi sayısız yaz; asla yuvarlayıp şişirme. Küçük ama gerçek sayı (ör. "40+ members, 120 submissions") büyük ve belirsiz bir iddiadan daha iyidir.

---

## ÖNEMLİ

### Ö1. 6 saniyelik ilk izlenim
**Recruiter'ın gördüğü (mevcut sıra ile):** İsim → "Full Stack Developer (JavaScript · Firebase · Node.js)" → 3. sınıf öğrenci → Summary → ilk proje "PAU Software Development Community" + canlı link. Bu iyi: canlı ve özel alan adlı bir ürün ilk satırlarda.
**Kaçırdığı:**
- **AI/LLM** kelimesi başlıkta yok; famelink için en önemli sinyal 3. satırın ortasında gömülü.
- **React / TypeScript** hiç yok → ATS ve recruiter ilk filtrede "uymuyor" diyebilir. Bu dürüst bir eksik; uydurma değil, kapatılması gereken bir boşluk (bkz. Ö6).
- **Skills bölümü en altta.** Senin verdiğin şablona göre Skills, Projects'ten **önce** gelmeli. Şu anki sıra: Summary → Projects → Leadership → Education → Skills → Interests. Düzelt: Header → Summary → Skills → Projects → Leadership → Education → Languages.
- Ne zaman/kaç saat çalışabileceği CV'de yok; remote + öğrenci ilanlarında recruiter ilk bunu arar. Header'a ekle: `Open to remote · 25–30 h/week` (gerçek sayıyı yaz).

### Ö2. Summary çok uzun ve klişe ("end to end, from UI to ...")
**Sorun:** 2 cümle ama ~50 kelime; "builds and ships web applications end to end" her junior CV'sinde var. Kurucu bilgisi Leadership ile tekrar ediyor.
**Yeniden yazım (2 satır):**
> MIS student (3rd year) who ships live web apps on Firebase and Node.js and integrates LLM APIs. Built and run the AI-assisted platform of the software community I founded at Pamukkale University.

### Ö3. Proje maddeleri — madde madde
**Topluluk platformu**
- Mevcut 1: "Built and maintain the community's web platform (public site, blog, membership applications, training module and role-based admin panel) on Firebase Auth and Firestore, used by [X] members." → Çok uzun (2+ satır), parantez içi liste.
  > - Built and run the community's live platform (blog, applications, training module, admin panel) on Firebase Auth/Firestore for [N] members.
- Mevcut 2 (AI): bkz. K1.
- Mevcut 3: "Designed an assignment workflow where members submit work, admins grade (0–100) and resolve appeals via batched Firestore writes, and scores feed a leaderboard" → doğrulandı (`writeBatch` + `increment`), ama "batched Firestore writes" detayı yanlış yere vurgu. Sonuç yok.
  > - Designed a submit → grade → appeal workflow with atomic Firestore batch writes and a live leaderboard; [N] submissions graded.

**Finance Tracker**
- Doğrulandı: auth, CRUD, Chart.js, CSV import/export, LocalStorage demo modu, admin görev merkezi. Ama **8.900 satırlık bir uygulamanın tamamı 2 günde (26–27 Eyl 2026), 4 commit'te** yazılmış. Bir senior bunu görünce "AI üretmiş" der; sorun değil, ama her satırı açıklayabilir olmalısın (bkz. E1).
- Canlı demo Firebase'e bağlı olduğu için **demo modu canlıda çalışmıyor**; recruiter kayıt olmak zorunda. CV'deki "falls back to a LocalStorage demo mode" iddiası canlı linkte görülemez. Çözüm: README + giriş ekranında "Try demo" butonu (demo hesabı veya `?demo=1` ile LocalStorage moduna zorla).
- Admin "task center"ın bir bütçe uygulamasında ne işi olduğu belirsiz; maddeyi kalabalıklaştırıyor, sil.
  > - Built a budgeting app with Firebase Auth and per-user Firestore data: CRUD, period/category filters, CSV import/export.
  > - Added Chart.js analytics (category split, monthly trend) and a storage abstraction with an offline LocalStorage demo mode.

**ZNG**
- Doğrulandı: `dist/` altında 63 sayfa, TR/EN, sıfır bağımlılık. Ama: tek commit, yayında değil (github.io/zng sadece README), projeler "örnek içerik", firmanın sitesi hâlâ ayrı. "Planned a Wix-to-static migration" = yapılmamış iş. "[load time reduced from X to Y]" ölçülmediyse kesinlikle yazma.
  > - Building a bilingual (TR/EN) corporate site for an electrical contractor with a zero-dependency Node.js static site generator (63 pages from data modules).
  > - Preserved legacy Wix URL slugs for SEO continuity during the planned migration.
  Müşteri izni yoksa link verme: `Client project (private)`. Yer darsa bu projeyi tamamen çıkar — full stack/AI ilanına katkısı en düşük olan bu.

**Study System**
- Doğrulandı (531 kart, 394 soru, AVL alıştırması). Teknik olarak ilginç ama private, ilana alakasız (Python + statik HTML) ve içerik ders slaytlarından türetilmiş. Link verilemiyorsa CV'de "kanıtsız proje" olarak durur.
- **Öneri:** Tek sayfaya sığdırmak için ilk çıkarılacak proje. Kalacaksa tek madde:
  > - Wrote a Python generator that compiles JSON/Markdown course data into offline study apps (spaced repetition, quizzes, AVL rotation exercise; 500+ cards).

### Ö4. Skills bölümü: `[?]`'ler ve ilan anahtar kelimeleri
**Sorun:** `[SQL ?]`, `[TypeScript ?]`, `[Express ?]`, `[React ?]`, `[relational DB design ?]` — repolarda hiçbirinin kanıtı yok. Yazarsan teknik görevde/mülakatta açık verirsin; yazmazsan ATS'den geçmeyebilirsin. Çözüm yazmak değil, **küçük bir kanıt üretmek** (Ö6).
"REST API integration" dürüst (Gemini REST, EmailJS) — kalsın. "Vanilla JS SPA architecture" abartılı; topluluk sitesi çok sayfalı (`sayfalar/*.html`), SPA değil.
**Yeniden yazım (sadece kanıtlananlar):**
> **Languages:** JavaScript (ES2020+, ES modules), HTML, CSS, Python
> **Backend & Data:** Firebase (Auth, Firestore, Remote Config, Cloud Functions*), Node.js, REST APIs
> **AI/LLM:** Google Gemini API, prompt design, chat UX
> **Frontend:** Responsive UI, Chart.js, DOM/ES modules
> **Tools:** Git, GitHub Pages, DNS/custom domains, pandas

*Cloud Functions yalnızca K1 yapıldıysa. React/TypeScript gerçekten küçük bir projede kullanıldıysa eklenir.

### Ö5. Leadership bölümü
"Founder, President and Vice President" tek satırda üç unvan kafa karıştırıcı; ayrıca "Designed and shipped the community's web platform (see Projects)" tekrar — sil.
> **Founder & President** — Software Development Community, Pamukkale University · 2025 – Present
> - Founded the community and grew it to [N] members; ran [N] workshops and a [N]-week training track with graded assignments.

(Başkan yardımcılığına geçiş tarihleri gerekiyorsa ikinci satır: "President (2025–26), Vice President (2026–present)".)

### Ö6. Başvurudan önce en çok değer katacak 1–2 küçük iş (öncelik sırasıyla)
1. **Gemini proxy (Cloud Function, Node.js) + çok turlu konuşma + streaming** — K1. 1–1,5 gün. Güvenlik + backend + conversational AI üçünü birden kapatır. En yüksek getiri.
2. **README + Security Rules + XSS düzeltmesi** pinlenen iki repoya — K3 + repo_karari §4. 3–4 saat. Ekran görüntüsü + "Live demo" + "Architecture" (bir paragraf: client → Firebase Auth → Firestore rules → Cloud Function → Gemini).
3. (Vakit kalırsa, başvurudan sonra) Chat istemcisini **TypeScript** ile yeniden yazmak veya küçük bir React + TS sohbet arayüzü — React/TypeScript boşluğunu dürüstçe kapatır. Tam bir Express + PostgreSQL projesi daha değerli ama başvuruyu bekletmeye değmez.

---

## KÜÇÜK

### Kü1. Tek sayfaya sığar mı?
Mevcut hâliyle **sığmaz** (4 proje × 2–3 madde, uzun maddeler, Interests, 2 satırlık header). Kesilecekler:
- Study System (veya tek madde), ZNG'yi 2 → 1–2 kısa madde.
- **Interests satırı** ("Basketball, boxing") — sil; bilgi taşımıyor.
- **"AI-assisted development (Claude Code)"** Tools satırında — CV'den çıkar; e-posta/mülakatta konuşulacak bir şey (bkz. E1). Tools listesinde bir ürün adı olarak durması "kodu ben yazmadım" diye de okunabilir, "AI ile verimli çalışıyorum" diye de; bağlamsız risklidir.
- "Relevant coursework" içinde Strategic Management ve E-Commerce işe yaramıyor; Data Structures + (alındıysa) Database Systems, Systems Analysis yeter. Alınmadıysa `[?]` olanları sil.
- GPA < 3.0 ise yazma (not zaten var, doğru).
- Proje başlık satırları çok uzun (isim + "Live:" + tam GitHub URL'si). PDF'te köprü olarak ver: `Live | Code` — sadece iki kelime, tıklanabilir.

### Kü2. "Languages (spoken)" Skills içinde
Şablon gereği ayrı **Languages** bölümü (tek satır) en altta: `Turkish (native) · English (B2)`. İngilizce seviyeni abartma; remote bir ekipte ilk görüşmede anlaşılır.

### Kü3. Biçim/dil detayları
- Header'da `[City]` → "Denizli, Turkey". Telefon formatı `+90 5XX XXX XX XX` tamam.
- Tarih biçimini tek tip yap: `Sep 2025 – Present`.
- Her madde tek satır: şu an 1., 3. ve AI maddeleri A4'te 2 satıra taşar.
- "ES modules" iki kez geçiyor (stack satırı + Skills); bir kez yeter.
- Teknoloji satırlarında "JavaScript (ES modules), HTML/CSS" herkes için aynı → kaldır, sadece ayırt edici olanları yaz (Firebase Auth · Firestore · Gemini API).

### Kü4. Repo kararları — katılıyor muyum?
- **Pin sırası (topluluk → finance-tracker → zng):** Katılıyorum, ama zng'yi ancak müşteri izni + Pages'te gerçek `dist/` yayını varsa pinle. Tek commit'lik ve README'si müşteriye Türkçe yazılmış, yayında olmayan bir repo pinde zayıf durur. 3. pin yerine K1'den çıkacak **Cloud Function/chat** işi (aynı repoda `functions/` klasörü yeterli) daha güçlü bir hikâye.
- **zng müşteri izni:** Kesinlikle katılıyorum. Ek olarak: repoda `.claude/launch.json` var, firmanın telefon/adres bilgileri `src/data/site.mjs`'de. İzin yoksa hemen private yap; CV'de "Client project (private)".
- **main'i arşivleme:** Katılıyorum; arşivlemek yerine **private yapmak** daha temiz (archive'lanmış repo profilde yine görünür). Yeni ad vermeye gerek yok.
- **İsim değişiklikleri:** `Yaz-l-m_toplulugu` → `pau-software-community` kesinlikle (mevcut ad Türkçe karakter bozulması gibi görünüyor, "Yaz-l-m"). Özel alan adlı olduğu için Pages kırılmaz — ama CNAME dosyasının kaldığını yeniden adlandırmadan sonra kontrol et. `finansal-takip` → `finance-tracker`: demo URL'si kırılır; CV/README güncellenecekse yap, yoksa adı koru — bu düşük öncelik.
- **Calisma-Sistemi'ni private tutmak:** Katılıyorum (telif). CV'de link verilemeyen projenin yerini bu yüzden kısalt.
- **Eklenecek:** Profil adı "haaland" (K4) repo_karari'nde yok; en ucuz ve en görünür düzeltme.

### Kü5. E-posta taslağı
**Uzunluk:** İngilizce gövde ~170 kelime — iyi aralıkta (150–200). Kısaltmaya gerek yok, ama içerik değişmeli.
**Konu satırı:** "Application: Remote Full Stack Developer — Deniz Baran Aykul" — doğru ama sıradan. Fark yaratan bir sinyal ekle:
> Remote Full Stack Developer — Deniz Baran Aykul (built a live Gemini chat assistant)

**İlk cümle:** "I'm applying for..." — boşa giden cümle; konu satırı zaten söylüyor. Doğrudan en güçlü kanıtla başla:
> Hi Atalay, I built and run a live Gemini-powered chat assistant for my university's software community (pauyazilimgelistirme.com.tr), and I'd like to bring that work to FameLink's conversational AI products as a remote full stack developer.

**İçerik:**
- `[e.g. "matching brands with creators"]` → **sil**; FameLink conversational AI (companionship, roleplay, social interaction) yapıyor. Doğrusu: "Conversational AI is exactly where I want to grow — I'm especially interested in how you handle long-term memory and persona consistency." (Somut bir merak, jenerik coşkudan iyidir.)
- "ship-it mindset", "hands-on" → klişe; sil.
- Topluluk maddesinde "rate-limit-aware key rotation" → sil (K1). K1 bittiyse: "...a Gemini assistant served through a Node.js Cloud Function with multi-turn context and streaming."
- Finance Tracker satırı kalabilir; "demo account: ..." eklenirse recruiter gerçekten dener.
- Kapanışta müsaitlik **sayıyla**: "Available ~25 h/week now, full-time from [ay]." Belirsiz bırakma.
- "happy to do a technical task" — iyi, kalsın.
- Türkçe sürümde "Atalay Bey" tonu uygun; İngilizce ilana Türkçe yazma kuralı doğru.

---

## Etik ve güvenlik

### E1. AI yardımıyla yazılmış kod
**Durum:** Topluluk reposunda 8 commit yazar adı "Claude"; finansal-takip 8.900 satır / 2 gün; zng tek commit ve repoda `.claude/` klasörü. Bir senior bunu 1 dakikada görür.
**Öneri:** Gizleme — FameLink zaten AI şirketi; gizlemeye çalışmak ortaya çıkınca dürüstlük sorununa dönüşür. Ama CV'nin Tools satırında bir ürün adı olarak da koyma. Doğru yer: mülakat ve README.
- README'ye bir satır: *"Built with AI-assisted development (Claude Code); architecture, data model, security rules and reviews are my own."* — **sadece doğruysa**.
- Mülakata hazırlık: her pinlenen repodan rastgele bir dosya açıp "bu fonksiyon ne yapıyor, neden böyle, nasıl test ederdin, neyi değiştirirdin" sorularını yüksek sesle cevaplayabilmelisin. Özellikle: Firestore rules, batch write neden atomik, XSS neden oluşuyordu, Cloud Function'da secret nasıl yönetiliyor. Cevaplayamadığın kod senin aleyhine kanıttır.
- Mülakatta önerilen cümle: "I use Claude Code daily for scaffolding and refactors; I design the data model and security, review every diff, and I can walk you through any file."

### E2. Açık anahtarlar ve kişisel veri
- **Gemini anahtarları:** İstemciye iniyor → sızmış kabul et, **iptal et ve yenisini sadece sunucuda tut** (K1). Bu yapılmadan siteyi CV'de öne çıkarmak, kötüye kullanım faturasını/kota yasağını davet eder.
- **Firebase web apiKey:** Gizli değil; ama Firebase Console'da API key'i HTTP referrer (alan adın) ile kısıtla ve App Check'i aç.
- **EmailJS** servis/template ID'leri istemcide → EmailJS panelinden izinli origin'i kısıtla; aksi hâlde başkası senin hesabından e-posta gönderebilir.
- **Kişisel Gmail** iki repoda kodda (admin listesi, e-posta fallback). Kaldır.
- **Geçmiş temizliği:** Bir şeyi koddan silmek git geçmişinden silmez. Anahtarlar için çözüm geçmişi yeniden yazmak değil, **iptal etmek**.
- `python.py` (Excel → Gemini'ye pyautogui ile prompt yapıştıran otomasyon) finansal-takip klasöründe izlenmeyen dosya; commit edilmediğinden emin ol (şu an edilmemiş — doğru).

---

## Kontrol listesi (gönderimden önce)
- [ ] Gemini anahtarlarını iptal et; Cloud Function proxy + çok turlu sohbet (K1)
- [ ] `firestore.rules` + XSS düzeltmesi + kişisel e-postaları kaldır (K3)
- [ ] GitHub profil adı/bio (K4)
- [ ] Gerçek sayılar veya sayısız madde (K5)
- [ ] Bölüm sırası: Skills Projects'ten önce; Interests ve Claude Code satırı yok; `[?]`'ler silindi
- [ ] İki pinli repoya README + ekran görüntüsü + demo erişimi
- [ ] E-postada FameLink'in gerçek alanı (conversational AI), konu satırı ve ilk cümle değişti
- [ ] PDF tek sayfa, tüm linkler tıklanabilir ve tarayıcıda test edildi

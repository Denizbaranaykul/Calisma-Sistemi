# Konu 1 — Giriş: Betimsel istatistik, veri seti, değişken, ana kütle

## Dersin çerçevesi
- Ders = **betimleyici (betimsel) istatistik + olasılık**. Olasılık matematiğin ayrı bir dalı; çıkarımsal istatistiği anlamak için ikisi birlikte gerekir.
- **Uygulamalı istatistik** çalışıyoruz (matematiksel/teorik istatistik değil). İki kol: **betimsel** (veriyi özetle) ve **çıkarımsal** (örneklemden ana kütleye genelle; gelecek dönem).
- Veri **hazır** varsayılır: veri toplama/temizleme, ölçme kalitesi, geçerlik-güvenirlik ve eksik veri bu dersin konusu değil (gerçek araştırmada mutlaka sorgulanır).
- İstatistik ≠ makine öğrenmesi: ML/veri bilimi veri toplama, büyük veri ve **tahmin** ağırlıklıdır; genelleme derdi yoktur. Dinamik/ısı haritası/keman (violin) grafikleri bu alanlardan yaygınlaştı.

## Veri seti yapısı
- **Satır = gözlem (analiz) birimi** (öğrenci, firma, ülke, ürün...). **Sütun = değişken**.
- **ID (kimlik) değişkeni:** gözlemleri ayırt etmek ve veri setlerini birleştirmek için; gerçek değişken değil, **yardımcı** değişken. Örnek: ülkeler için enflasyon ve kaza verisini ID ile eşleştirip birleştirirsin.
- Analiz biriminin neyin özelliği olduğuna bak: ciro **firmanın** özelliğidir, müdürün değil.

## Kavramsal vs operasyonel tanım
- **Kavramsal tanım:** kavramı başka kavramlarla anlatır (sözlük/bilimsel tanım). Bilimde ortak tek tanım yoktur → hangi teoriyi aldığını belirt.
- **Operasyonel (işlemsel) tanım:** kavramı **nasıl ölçtüğünü** anlatır. Örnek: derse devam = 14 haftalık yoklama sayısı (0-14); akademik başarı = tarih final notu (0-100); enflasyon = sepetteki ürünlerin fiyat oranlarının ağırlıklı ortalaması.
- Halk dili tuzağı: "enflasyon düştü" ≠ "fiyatlar düştü"; fiyat artış **hızı** düştü. Fiyatlar düşerse enflasyon negatiftir.

## Değişken olmanın koşulları
1. Ölçülebilir hale getirildi ve fiilen ölçüldü
2. Araştırmada bir **rol** var (bağımlı / bağımsız ...)
3. **Farklı değerler alıyor** (herkes aynı değeri aldıysa değişken değil; bilim sabiti açıklamaz)
- **Bağımlı (Y, çıktı):** nedenini merak ettiğin değişken. **Bağımsız (X, öncül, ML'de feature):** Y'nin nedeni olabileceğini düşündüğün değişken.

## Ana kütle, örneklem, istatistik, parametre
- **Ana kütle (popülasyon):** genellemek istediğin tüm varlıklar; büyüklüğünü **araştırmacı amacına göre** seçer. **Örneklem:** ana kütleden seçilen küçük kısım. Ana kütlenin tamamına ulaşabiliyorsan örnekleme gerek yok.
- **İstatistik** = örneklemden hesaplanan değer. **Parametre** = ana kütleye ait değer (gerçekte genelde bilinmez).
- **Çıkarımsal istatistik:** örneklem istatistiğinden ana kütle parametresine ilişkin tahmin/genelleme (hata payı ve güven aralığıyla; örnek: %35 çıktı → %95 güvenle %32-%39).
- **%5 kuralı:** örneklem ana kütlenin ~%5'inden küçükse ana kütleyi sonsuz kabul etmek sonuçları bozmaz. Örneklem ne kadar büyük olursa iyi; ama ana kütleye göre küçük kalmalı → bunun için ana kütleyi yeterince büyük seç.
- Bu derste ayrım yapmıyoruz = veri setini **ana kütle** kabul ediyoruz.
- **Meta-analiz:** birçok araştırmanın sonuçlarını birleştirip analiz etmek.

## Betimleme araçları
1. **İstatistiksel tablolar** (frekans, çapraz tablo) 2. **Grafikler** (histogram, nokta/lollipop...) 3. **Sayısal göstergeler (istatistikler)** — asıl araç (ortalama vb.).
- Ortalama gibi tek bir sayı grubun "genel seviyesini" verir; bireyi gruba, grupları birbirine kıyaslamayı mümkün kılar. Ama "A sınıfı ortalaması yüksek" demek her A öğrencisinin her B öğrencisinden iyi olduğu anlamına gelmez.

---

# Konu 2 — Tanımlar, değişken rolleri, nedensellik, ölçüm düzeyleri

## Terimler
- **Terim** = kelimenin kendisi, **kavram** = anlatmaya çalıştığı soyut anlam. Operasyonel tanımın Türkçesi: işlemsel tanım.
- Kavramları belirleyip sınırlarını çizmek önemli (derse devam = sadece fiziksel bulunma mı, aktif katılım mı?).

## Özellik → değişken yolu
- Özellik/kavram → tanımla → ölçülebilir kıl → ölç → rol ata → **değişken**. Ölçülebilir kılmak çoğu zaman **derinlik kaybı** demektir (basitleştirme).
- Birden fazla değişken olsa da **tek tek** ele almak = **tek değişkenli (univariate) istatistik**.
- Analiz birimi çalışmaya göre değişir: aynı enflasyon verisinde birim ülke (bir yıl için) ya da yıl (tek ülke için) olabilir.
- Excel tablosu = **veri matrisi / spreadsheet**.

## Nedensellik
- Bilimsel araştırmanın temel amacı: X'in Y'nin nedeni olup olmadığını göstermek. Bu zordur; "neden" tanımında döngüsellik/felsefi sorun vardır.
- **Karşıt olgusallık (counterfactual):** X olmasaydı Y olmazdı → X, Y'nin nedeni. (Alkollü kaza örneği.) Kusursuz değil (boşanmanın nedeni evlilik mi?).
- İstatistik yalnızca **ilişki** olup olmadığını gösterir; nedensel yorum teori, tasarım, mantıkla yapılır.
- **Korelasyon** = ilişkinin özel bir sayısal ölçüsü (Pearson). **Korelasyon nedensellik değildir.**
- **Tahmin (prediction):** nedeni bilmesek de X ile Y'yi öngörmek. Makine öğrenmesi sadece tahminle ilgilenir; klasik bilim açıklamayı da ister.
- Başka roller: kontrol, aracı, düzenleyici, araç değişken (ileride).

## Ölçme ne demektir?
- (1) Varlıkta özelliğin olup olmadığını (2) varsa **standart bir birimle** hangi düzeyde olduğunu **sayısallaştırmak**.
- Anlamlı **birim sistemi** + **karşılaştırma mekanizması** gerekir (metre/prototip, iki kefeli terazi). Prototipler artık evrensel sabitlere bağlandı (ışık hızı vb.).
- Geniş tanım (**Stevens, 1946**): kurallara uyarak varlıklara sayı atamak. Bu yüzden 4 ölçüm düzeyi vardır.

## Stevens'ın 4 ölçüm düzeyi (kıdemli → basit)
| Düzey | Özellik | Sıfır | Yapılabilen işlem |
|---|---|---|---|
| **Oran (ratio)** | Anlamlı birim, farklar eşit anlamlı | **Gerçek yokluk** | Toplama, çıkarma, **oranlama (kaç katı)** |
| **Aralık (interval)** | Eşit aralıklı, anlamlı birim | Keyfi (yokluk değil) | Toplama, çıkarma; **oranlama yok** |
| **Sıralı (ordinal)** | Anlamlı sıra, artan sayılar | — | Büyük/küçük karşılaştırma; farkın anlamı yok |
| **Sınıflayıcı (nominal)** | Kategoriye sayı/etiket | — | Sadece eşit / eşit değil (mod) |
- **Oran örnekleri:** boy, kütle, maaş, uzunluk. 0 TL maaş = maaş yok; 60 bin, 30 binin 2 katı.
- **Aralık örnekleri:** Celsius/Fahrenheit sıcaklık (0 °C yokluk değil), takvim yılı. 4 °C → 8 °C "2 kat sıcak" denemez; Kelvin ise oran ölçeğidir (0 K gerçek sıfır).
- **Sıralı örnekleri:** eğitim düzeyi (ilkokul=1...), yarış sırası, F1 puanı, askeri rütbe. 1→2 ile 4→5 arası farkın aynı olduğu söylenemez.
- **Nominal örnekleri:** plaka kodu, cinsiyet, medeni hal. Sayılar yalnızca etikettir.
- Oran ölçümü aralığın, aralık da diğerlerinin tüm özelliklerini taşır. **Oran + aralık = metrik (sayısal, kantitatif)** değişkenler.
- Neden önemli: hangi istatistiksel analizin yapılabileceğini belirler.

---

# Konu 3 — Veri türleri, tek değişkenli betimleme, frekans tablosu

## Sayı kümeleri (hatırlatma)
- Doğal sayılar (0 dahil kabul) ⊂ tam sayılar (Z) ⊂ **rasyonel** (a/b, b≠0) ⊂ **reel** (sayı doğrusu; π, √2 irrasyonel) ⊂ karmaşık.
- "Negatif olmayan tam sayılar" = doğal sayılar. İsimlendirme geleneği: non-parametrik, non-lineer.

## Kesikli vs sürekli
- **Kesikli (discrete):** değerler arasında boşluk var (1 ile 2 arasında değer yok). **Sürekli:** reel sayı doğrusunda boşluk yok.
- Gerçek hayatta ölçüm aletlerinin hassasiyeti sınırlı olduğu için hiçbir veri tam sürekli değildir; ama yeterince ince ölçüm varsa **sürekliymiş gibi** kabul edilir → matematik kolaylaşır. (Dikdörtgen masa örneği: gerçek hayatta kusurlu ama a×b formülü yeterince iyi.)
- Olasılıkta karşılığı: kesikli ve sürekli olasılık dağılımları.

## Sayma ve ölçme
- Sayma verisi: sayarak elde edilen, **az sayıda farklı değer** alan, bazen bir değerde aşırı yığılma olan değişken (kaç kardeş, kaç alttan ders). Gerçek hayatta ölçme de bir tür saymayı içerir; ama "sayma verisi" deyince bu dar anlam kastedilir.

## Dikotomik (iki şıklı) değişken
- En az 2 kategori gerekir (tek şıklı değişken değildir). Nominal ölçüm; 0/1 kodlamak matematiksel avantaj sağlar (hangisine 0 vereceğin önemsiz).
- **Dikotomize etmek:** aslında çok şıklı/metrik olanı iki şıklı yapmak (ehliyet sınavı geçti/kaldı). Basit ama **bilgi kaybı** → pek önerilmez.
- Kategoriler **birbirini dışlamalı** ve **kapsayıcı** olmalı. Anket sorusunu cevaplayanların nasıl anlayacağına göre yaz ("dul" belirsiz → "şu an evli misin?").
- Günlük dilde "dikotomi" = olmayan ikili ayrım dayatmak ("ya seversin ya terk edersin").

## Tek değişkenli betimleme: frekans tablosu
- **Frekans (sıklık):** bir skorun veri setinde kaç kez görüldüğü. Skor = bir gözlem biriminin değişkendeki değeri.
- **Pay (proportion, parçanın bütüne oranı)** = frekans / toplam gözlem (N). Payların toplamı **1**. **Yüzdelik** = pay × 100. (Hoca başına öğrenci gibi başka oranlar "parça/bütün" değildir.)
- **Kümülatif frekans / pay / yüzdelik:** küçükten büyüğe birikimli toplam; son satır N, 1, %100. "En fazla 3 dersi olanların oranı" tek bakışta okunur. "3'ten fazla" = 1 − kümülatif pay. İlgi eşiği büyük değerlerdeyse tabloyu büyükten küçüğe sırala.
- **Yüzdelik dilim (percentile):** üniversite sınavında %1'lik dilim = en iyi %1 (%99'u geçtin).
- Tablo büyüklüğünü gözlem sayısı değil, **farklı değer sayısı** belirler (1 milyon öğrenci de olsa 11 değerli değişken için 11 satır).
- **Lollipop grafiği:** x ekseninde skor, y ekseninde frekans; nokta + çubuk. Aslında "x'in dağılımı" (teknik adı frekans dağılımı).
- Frekans tablosu en yaygın betimleme aracı olmasına rağmen ana oyuncu **sayısal göstergelerdir** (tablo ve grafik yardımcı).

## Yazım ve yuvarlama kuralları (sınav için!)
- Ondalık ayırıcı **virgül**, binlik ayırıcı nokta (Türkiye). Excel/kod ortamında yerel ayara dikkat.
- **Nihai cevabı virgülden sonra 3. basamağa yuvarla.** 4. basamak ≥5 ise yukarı, ≤4 ise aynen. **Ara işlemlerde yuvarlama yok** (hesap makinesindeki tüm basamaklar).
- Sondaki sıfırlar yazılmayabilir (92,300 = 92,3). Adımları göster (12/6 → direkt 2 yazma).
- Payları **oran** olarak yaz (0,20); sadece % yazma. Hepsi aynı basamak sayısında olsun. **0,05'i 0,5 yazma** (sık hata).
- Türkçede **%23** (önce sembol), İngilizcede 23%. Para: sembol kullanılırsa başa (₺1000), alt birim (kuruş, cent) sona.
- Excel iş hayatında çok önemli.


# Konu 4 — Grafikler: lolipop, histogram, sütun grafiği, gruplanmış veri
*Kaynak: 2026 öğrenci el notları (4.–5. hafta).*

## Betimleme araçları ve yönleri (hatırlatma)
- Değişkenler tek tek ele alınıyorsa **tek değişkenli (univariate)** betimleme yapılır. Araçlar: **tablo** (frekans, çapraz), **grafik**, **sayısal göstergeler (istatistik)**.
- Hangi yönlerden betimleriz? **1) Merkezi eğilim (konum)**, **2) değişkenlik**, **3) dağılımın şekli**.
- **Dikotomi:** iki şıklı sınıflandırma (geçti–kaldı, ehliyet sınavı); çok şıklıya **politomi (polytomous)** denir. Dikotomi bir amaç doğrultusunda basitleştirmedir, bilgiyi çöpe atar. *Medeni hal (evli/bekâr/dul) dikotomik değildir.* "Dul" belirsiz (eşi vefat etmiş mi, boşanmış mı?) → şıklar belirsizlik bırakmamalı.

## Frekans tablosu (tam hali)
| x | Frekans | Pay | Yüzde | Kümülatif frekans | Kümülatif pay | Kümülatif yüzde |
|---|---|---|---|---|---|---|
| 0 | 20 | 0,20 | %20 | 20 | 0,20 | %20 |
| 1 | 15 | 0,15 | %15 | 35 | 0,35 | %35 |
| 2 | 15 | 0,15 | %15 | 50 | 0,50 | %50 |
| … | … | … | … | … | … | … |
| 10 | 10 | 0,10 | %10 | 100 | 1 | %100 |

- **Pay = oran = nispi frekans** = hücre frekansı / toplam gözlem sayısı (parçanın bütüne oranı). Teknik raporda **pay** gösterilir; sınavda **oran** şeklinde sorulur.
- **Gözlem sayısı = frekanslar toplamı.** 100 satır × 1 sütunluk ham veri → 11 satır × 2 sütunluk özet.
- Türkçede yüzde işareti **başa** (%23), İngilizcede sona (23%). Ondalık ayraç virgüldür.
- **Kural 1:** nihai sonucu virgülden sonra **3. basamağa** yuvarla (4. basamak 5 ve üstüyse 3. basamak 1 artar: 92,57439 → 92,574; 92,57469 → 92,575). Ara işlemde yuvarlama yok.
- **Kural 2:** 92,3 = 92,30 = 92,300; sondaki sıfırları yazmayabilirsin. Sonucu kesir halinde bırakma.

## Grafik türleri
- **Lolipop grafiği:** x ekseninde skorlar, y ekseninde frekans (kaç tane olduğu); her skorda bir çubuk + nokta. Grafiğin gösterdiği şey "frekans dağılımı" denir ama aslında **x değişkenine ait skorların dağılımıdır**.
- **Histogram:** en çok kullanılan grafik; **metrik (interval–rasyo)** veriler için. Sütunlar **bitişiktir**. Histogramda **alan oranı** gösterir — yükseklik değil **alan** önemlidir.
- **Sütun (çubuk, bar) grafiği:** **nominal veya ordinal** veriler için; sütunlar **arasında boşluk** bırakılır.
- **Pasta grafiği:** kullanımı **tercih edilmemesi gereken** grafik (alanları kıyaslamak zordur).
- Histogram okuyucuyu yanıltabilir: bitişik sütunlar "buçuklu değer de var" izlenimi verebilir.
- **Teamül (gelenek):** frekansı 0 olan skor sütunu silinir. **Teknik kural:** histogramda boşluk olmaz → boş kategori komşusuyla birleştirilir. Örn. 6 ve 7'yi birleştirince taban 2 birim olur; alan korunacağı için **yükseklik yarıya** düşer (alan 6 ise yükseklik 3).

## Gruplanmış veri
- Çok sayıda farklı skor varsa (0–100 arası 101 sütun) skorlar aralıklara **gruplanır** (ör. 5'lik: 1–5, 6–10, …; 20 grup). Her grubun **orta değeri** grup adı olabilir. Bu **suni bir ayrıştırmadır**; amaç az sütunla kolay anlaşılır grafik. Kaç sütun olacağı amaca göre değişir (SPSS'te aralığa **bin** denir).
- Metrik veri baştan gruplanmış toplanmışsa (maaş: 2 bin TL'lik aralıklar) buna **gruplanmış veri** denir.
- Sınavda ham veri yerine **frekans tablosu** veya **histogram** verilebilir; ikisi arasında **geçiş** yapabilmelisin.

# Konu 5 — Merkezi eğilim (konum): ortalama, medyan, mod
*Kaynak: 2026 5. hafta notları + 2025 4.–5. hafta notları.*

## Aritmetik ortalama
- Tüm gözlenen değerleri topla, **gözlem sayısına** böl: **μx = (X₁ + X₂ + … + X_N) / N = ΣXᵢ / N**.
- Gösterimler: **x̄** örneklem ortalaması; **μx (mu) / Mx** ana kütle ortalaması. N: ana kütle büyüklüğü, n: örneklem büyüklüğü. **Bu dönem elimizdeki veriler hep ana kütle kabul edilir.**
- *Çamlık örneği (oda sayısı, N = 12):* 0, 7, 1, 2, 3, 3, 1, 6, 2, 2, 2, 1 → toplam 30 → **μ = 30/12 = 2,5**. (Kınıklı'da N = 50.)
- **Frekans tablosundan ortalama:** μ = Σ (skor × frekans) / N. Alttan ders örneği: 0×35 + 1×24 + 2×17 + 3×12 + 4×8 + 5×3 + 6×1 = 147 → 147/100 = **1,47**.
- **Paylarla ortalama:** μ = Σ xᵢ · p(xᵢ) (k = farklı skor sayısı).
- **Ağırlıklı ortalama:** vize %40 (50), final %60 (70) → 50×0,4 + 70×0,6 = 20 + 42 = **62** (basit ortalama 60 olurdu). Ağırlıklar toplamı 1 değilse ağırlık toplamına bölünür.
- Ortalamadan sapmaların toplamı **her zaman 0**'dır. Ortalama sınıfı temsil eden **idealize** değerdir; "herkes bunu alıyor" ya da "çoğunluk bu civarda" demek **değildir**.

## Medyan ve mod
- **Medyan (ortanca):** veriler sıralanınca ortadaki değer; N çiftse ortadaki iki değerin ortalaması (3 ve 4 → 3,5).
- **Mod (tepe değeri):** en sık görülen değer. Kategorik (nominal) değişkende kullanılabilen tek konum ölçüsüdür (Bölüm: **Mod = YBS** — sınavda kategoriyi **yazıyla** yaz, kodla değil!). Histogramda en kolay görülen değerdir.
- **Robust (dirençli):** uç değerler ortalamayı çok etkiler, medyanı neredeyse hiç etkilemez. *Kantindeki arkadaş grubuna Elon Musk gelirse* ortalama gelir uçar, medyan değişmez. Yine de çoğunlukla ortalama kullanılır; uç değerler ayıklanıp ortalama alınır (bilim insanı uç değerleri merak etmelidir).
- **Ortalamaları eşit üç sınıf (MA = MB = MC = 50):** A: 0,0,0,100,100,100 (kutuplaşma); B: 47…53 (az değişkenlik); C: hepsi 50 (homojen). Ortalama aynı, dağılım çok farklı → **değişkenliğe** de bakmak gerekir.

# Konu 6 — Değişkenlik: ranj, OMS, kareler toplamı, varyans, standart sapma
*Kaynak: 2025 5.–6. hafta notları + 4 Kasım 2026 ders kaydı (bu yıl işlendi).*

## Ranj
- **Ranj = max − min** (B sınıfı: 53 − 47 = 6). İki şekilde söylenir: "skorlar 60 ile 80 arasında" ya da "ranj 20".
- Zayıf göstergedir: yalnızca iki değeri kullanır, aradaki skorları yok sayar.

## Ortalama mutlak sapma (OMS)
- **Sapma skoru dᵢ = Xᵢ − μ.** Sapma 0 ise öğrenci tam ortalamayı almıştır; + ise ortalamanın üstü, − ise altı.
- Sapmaların toplamı 0 olduğu için **mutlak değer** alınır; gözlem sayıları farklı gruplar adil kıyaslansın diye N'e bölünür: **OMS = Σ|Xᵢ − μ| / N**.

## Kareler toplamı, varyans, standart sapma
- Matematikte mutlak değer yerine **kare** tercih edilir. **Kareler toplamı SS = Σ(Xᵢ − μ)²**.
- **Varyans = SS / N** (σ², Var(x)). Birimi orijinal birimin **karesidir** (cm → cm²), yorumlamak zordur.
- **Standart sapma σ = √Varyans = √(SS/N)** → orijinal birime döner.
- *Tarih sınavı (N = 10):* 80, 30, 50, 40, 60, 70, 70, 20, 70, 30 → toplam 520, **μ = 52**; Σ|d| = 180 → **OMS = 18**; **SS = 3960**; **varyans = 396**; **σ ≈ 19,900**.
- Excel: `=ORTALAMA()`, `=VAR.P()`, `=STDSAPMA.P()`, `=KAREKÖK()`, `=YUVARLA(x;3)`. Türkçe Excel'de ayraç `;`. Sabit hücre `$C$3` ile dolarlanır; formül sürüklenince göreli adresler kayar.
- N yerine N−1 de görülebilir (örneklem); bu dönem önemli değil.
- **σ sıfıra yaklaştıkça** skorlar ortada yığılır (herkes benzer). σ = 20 olan sınıf σ = 5 olan sınıftan daha heterojendir.
- **Maksimum standart sapma:** ortalama 50, N = 6, skorlar 0–100 → üçü 0, üçü 100 (kutuplaşma) → her sapma ±50, SS = 15000, varyans 2500, **σ = 50**.
- Çoğu veri setinde skorların büyük bölümü **μ ± σ** arasındadır (μ = 52, σ = 20 → 32 ile 72 arası).

## Ders kaydından (4 Kasım dersi): neden kare, neden karekök?
- **Mutlak değerin sorunu:** matematiksel istatistikçilere göre mutlak değer fonksiyonunda **köşe** oluşur, köşede **türev alınamaz** → ileri analizlerde işe yaramaz. Çözüm: sapmaların mutlak değeri yerine **karesini** almak (eksiler yine artı olur, ama sayılar da büyür — bu bazen avantaj sayılır).
- **Kareler toplamı (SS, "sum of squares")** = Σ dᵢ². Gözlem sayısının etkisini içerdiği için farklı büyüklükteki sınıfları kıyaslamada tek başına uygun değil → N'e bölünür → **varyans** (Var(x), σ²). Varyans en önemli değişkenlik göstergelerinden biridir; çıkarımsal istatistikte arka planda hep o kullanılır.
- *B sınıfı örneği (47, 48, 49, 51, 52, 53; μ = 50):* sapmalar −3, −2, −1, +1, +2, +3 → kareler 9, 4, 1, 1, 4, 9 → **SS = 28**, **varyans = 28/6 = 4,667**; OMS = 12/6 = **2**.
- **Birim sorunu:** sapma skoru orijinal birimdedir (maaş sapması +12.000 TL = ortalamadan 12.000 TL fazla). Karesi alınınca birim de kare olur (TL², cm²) → anlamsız. Varyansın **bir bütün olarak** karekökü alınınca birim geri gelir → **standart sapma (σ, küçük sigma)**. (Büyük sigma Σ toplama işaretidir, karıştırma.)
- **SS, varyans ve σ "üç ayrı istatistik değil, bir istatistiğin üç versiyonu"dur.** Betimlemede en kolay yorumlanan σ'dır; bölme ve karekök bazı matematiksel özellikleri kaybettirdiği için bilgisayar arka planda varyans/SS ile çalışır.
- **Semboller:** ana kütle → Yunan harfi (μ, σ); örneklem → Latin harfi (x̄, s). Örneklemde varyans **N−1**'e bölünür (gelecek dönemin konusu). SPSS gibi paket programlar ve istatistik fonksiyonlu hesap makineleri genelde **örneklem formülüyle** çalışır; Excel'de ikisi ayrı (VAR.P / VAR.S).
- **Sınav:** akıllı olmayan hesap makinesi kullanılabilir ama **işlemler gösterilmek zorunda**.
- **Değer aralığı:** σ ve varyans **en az 0** (herkes aynı puanı alırsa ranj, OMS, σ hepsi 0), **üst sınırı yok** (veriye göre). "σ şundan büyükse değişkenlik çoktur" diye evrensel bir eşik yoktur; ölçülen şeye göre değişir. 0–100 notlarda μ = 50 iken en büyük σ = 50 (yarısı 0, yarısı 100).
- Değişkenlik istatistikleri: ranj, OMS, kareler toplamı, varyans, standart sapma (+ ileride **çeyrekler arası açıklık**). Diğer adları: **saçılma, yayılma (spread)**.

### Değişkenliğe neden bakarız? (3 rol)
1. **Ortalamanın temsil gücünü gösterir.** σ küçükse ortalama sınıfı iyi temsil eder (herkes ortalamaya yakın); σ büyüdükçe ortalamaya güvenme. D sınıfında (yarısı 0, yarısı 100) ortalama 50 ama 50'ye yakın alan bir kişi bile yok → bu yüzden raporlarda **ortalama verilirse yanında mutlaka standart sapma** verilmeli.
2. **Bilimsel merakın merkezidir.** Bilim, gözlenen **değişkenliğin nedenlerini** açıklamaya çalışır (neden bazı öğrenciler 53, bazıları 47 alıyor?). Değişkenlik yoksa (herkes aynıysa) bilimsel soru da yoktur — "evrenin sabiti" olur. Makine öğrenmesi ve veri analizinin merkezi de budur. Önce merak etmeye değer bir değişkenlik var mı diye bakılır.
3. **Pratik karar verdirir; bazen amaç düşük değişkenliktir.** *Deterjan paketleme makinesi:* A ve B makineleri ortalama 500 g dolduruyor; A'nın σ = 2 g, B'nin σ = 20 g. B bazı paketlere 520 g (şirket zarar eder), bazılarına 480 g (müşteri kazıklanır, ceza riski) koyar → **σ'sı düşük A makinesi** tercih edilir. (Havayolunun kahvaltıdan iki zeytini kaldırarak milyonlar kazanması: küçük farklar ölçekle büyür.)
- *Düşünme ödevi:* Ortalamaları aynı A, B, C, D, E sınıflarından çocuğunu hangisine yazdırırdın? (Gelecek ders açıklanacak.)

# Konu 7 — Dağılımın şekli, normal dağılım ve z skoru
*Kaynak: 2025 6.–7. hafta notları (önden çalışma).*

## Dağılımın üç özelliği
1. **Konum** (ortalama, mod, medyan) 2. **Değişkenlik** (ranj, OMS, standart sapma) 3. **Şekil/biçim/form**.
- **Nitel şekil soruları:** Tek tepeli mi? Simetrik mi? Uç değer var mı? Tepesiz, U şeklinde, tek skorda (genelde 0'da) yığılma olabilir (ameliyat sayısı).
- **Çarpıklık:** simetrik değilse çarpıktır; yön **kuyruğa** (azar azar azalan tarafa) göre söylenir. **Sağa çarpık:** mod < medyan < ortalama (uç değerler ortalamayı kuyruğa çeker). Medyan her zaman mod ile ortalamanın arasındadır.
- Simetrik ve tek tepeli dağılımda **mod = medyan = ortalama**. Medyan ile ortalama birbirinden ne kadar uzaksa simetri o kadar bozuktur.
- Alt veya üst sınırı olan ölçümlerde (kira, gelir — finansal konular) çarpıklık normaldir; en sık görülen **sağa çarpıklık**tır.
- **Tavan etkisi:** üst limitten kaynaklanan yığılma (çok kolay sınavda herkes 100). **Taban etkisi:** alt limitten kaynaklanan yığılma. Sınır değerlerde yığılma sağlıklı bir ölçüm değildir (10 kg'lık tartıda 20 kg).
- **Uç (ekstrem) değer:** yalnızca çok yüksek/düşük değer değil, **veri yığınından kopuk** değerdir. Uç değer varsa: 1) veri girişi hatası mı? 2) ana kütle dışından biri mi karıştı? İkisi de değilse sırf uç diye silinmez.

## Normal (Gauss) dağılım
- En meşhur **sürekli** dağılım; **tek tepeli, çan şeklinde, ortalamaya göre simetrik**; iki ucu **asimptotik** (x eksenine hiç değmez, −∞'dan +∞'a).
- **Ortalama = mod = medyan** (tepe noktası).
- İki **parametresi** vardır: **μ** (konumu, sağa-sola kaydırır; −∞, +∞) ve **σ** (genişliği; 0'dan büyük). Aynı σ, farklı μ → aynı şekil kaymış; aynı μ, farklı σ → geniş olanın σ'sı büyük.
- **Standart normal dağılım:** μ = 0, σ = 1.

## z skoru (standart skor)
- **zᵢ = (Xᵢ − μ) / σ** → birimsiz; ortalamadan **kaç standart sapma** yukarıda/aşağıda olduğunu gösterir.
- μ = 55, σ = 12: X = 81 → z = **+2,167**; X = 40 → z = **−1,250**; X = 79 → z = **+2,000**.
- z skorlarının ortalaması her zaman **0**, standart sapması **1**'dir. z dönüşümü **şekli değiştirmez**, birimi değiştirir (çarpıksa çarpık kalır).

## Normal dağılımın görgül kuralları
- **μ ± 1σ:** alanın yaklaşık **%68**'i (her yarı %34).
- **μ ± 2σ:** yaklaşık **%95** (gerçek değer ±1,96σ; bu dönem %95 kabul edilir).
- **μ ± 3σ:** yaklaşık **%99,7** (hiçbir zaman %100 olmaz).
- Örnek: μ = 55, σ = 10 → 55–65 arası **%34**; 65–75 arası (z: +1 ile +2) **%13,5** → 4000 öğrencide **540** kişi.

# Uygulama veri seti — Futbol-00.xlsx
*310 futbolcu; değişkenler: Yaş, Maç sayısı, Gol sayısı, Pozisyon, Milli (milli maçı var/yok), Uyruk (Norwegian/Foreign), Ayak (right/left-both).*

| Değişken | Ölçüm düzeyi | Ortalama | Medyan | Mod | Min–Max | σ |
|---|---|---|---|---|---|---|
| Yaş | Rasyo | 25,545 | 25 | 22 | 17–38 | 4,204 |
| Maç sayısı | Rasyo (sayma) | 181,806 | 167 | 168 | 10–584 | 109,068 |
| Gol sayısı | Rasyo (sayma) | 23,303 | 15 | 5 | 0–191 | 26,489 |

- **Pozisyon** (nominal): Defans 113, Orta saha 89, Kanat 59, Forvet 49 → **mod = Defans** (pay 0,365).
- **Milli** (dikotomik nominal): milli maçı olan 58, olmayan 252. **Uyruk:** Norveçli 214, yabancı 96. **Ayak:** sağ 229, sol/her ikisi 81.
- Gol sayısında **ortalama (23,3) > medyan (15) > mod (5)** → **sağa çarpık** dağılım (az sayıda golcü ortalamayı yukarı çekiyor). Yaşta ortalama ≈ medyan → yaklaşık simetrik.
- Alıştırma: Excel'de Pozisyon için frekans tablosu (frekans, pay, yüzde, kümülatif) ve Gol için histogram çiz; `=ORTALAMA`, `=ORTANCA`, `=ENÇOK_OLAN`, `=STDSAPMA.P` ile tablodaki değerleri doğrula.

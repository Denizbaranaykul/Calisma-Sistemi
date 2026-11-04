# Çalışma Sistemi (6 ders)

`index.html` dosyasını aç, dersi seç. Her ders kendi klasöründe ve internet gerekmez.

| Ders | Klasör | Kaynak | İçerik | Alıştırma üreticisi |
|---|---|---|---|---|
| Pazarlama | `pazarlama/` | Ders kayıtları (1–5) | 5 ders · 100 kart · 60 soru | ücretli arama: TBM/bütçe, tıklama oranı, uzun kuyruk, eşleşme tipleri, negatif kelime |
| İstatistik | `istatistik/` | Kayıtlar (değişkenlik dersi dahil) + 2026 el notları + 2025 notları + Futbol veri seti | 7 konu · 98 kart · 80 soru | frekans, ortalama/medyan/mod, ağırlıklı ortalama, ranj/OMS/varyans/s.sapma, z skoru, görgül kural |
| Örgütsel Davranış | `orgutsel/` | Ders kayıtları (1–3) | 3 ders · 56 kart · 38 soru | — |
| Stratejik Yönetim | `stratejik/` | Kayıtlar + Bölüm 1–4 slaytları | 8 konu · 117 kart · 98 soru | pazar gelişim hızı, GSYİH/GSMH, varlık/yetenek sınıflama, değer zinciri sınıflama |
| Veri Yapıları | `veri_yapilari/` | Ders PDF'leri | 5 konu · 51 kart · 37 soru | **AVL döndürme (etkileşimli)**, ağaç dolaşma, BST, ağaç terimleri, infix→postfix/prefix, postfix hesaplama, yığın/kuyruk |
| E-Ticaret | `e-ticaret/` | Slayt fotoğrafları (106 + 115 adet) | 5 hafta (2–6) · 109 kart · 81 soru | dönüşüm oranı, AOV, CAC, sepet terk, iade ve zamanında teslimat oranı; faaliyet sınıflandırma (e-işletmecilik / e-ticaret / e-perakendecilik) |

Her ders klasöründe: `index.html` (plan, notlar, aralıklı tekrar kartları, test, alıştırma, ilerleme), `anki-kartlar.csv` (Anki'ye `;` ayraçlı, UTF-8 aktar) ve `veri/` (düzenlenebilir kaynak).

## Alıştırma sekmesi
Test sorularından farklı olarak bu sorular **her açılışta rastgele sayılarla yeniden üretilir** — sınırsızdır. Cevabı yazarsın, "Kontrol et" doğru/yanlış ve adım adım çözümü gösterir. Ondalıkta virgül veya nokta kullanılabilir; nihai cevap 3 basamağa yuvarlanır. Başarı oranı İlerleme sekmesinde görünür.

**AVL döndürme (Veri Yapıları):** verilen diziyi tek tek ekleyerek AVL ağacına yerleştirirsin. İstediğin düğüme dokunup **sağa / sola döndür**: döndürülen düğüm yukarı çıkar, ebeveyni aşağı iner. İpucu gösterilmez (denge faktörleri isteğe bağlı açılır), döndürme sayılmaz; hepsini ekleyince **Kontrol et** son ağacın doğru AVL ağacı olup olmadığına bakar.

## Veriyi düzenleme
`veri/notlar.md`, `cards.json`, `quiz.json`, `course.json` dosyalarını düzenle, sonra bir üst klasörde:
```
python build.py
```
Her ders için `index.html` ve CSV'yi yeniden üretir, ana sayfayı günceller. Yeni ders eklemek için `veri/` klasörüyle yeni bir klasör aç. `course.json` içinde `unit` ("Ders"/"Konu"/"Hafta") etiketi, `gen` ise alıştırma üreticilerinin listesidir (tanımları `_arac/template.html` içindeki `GEN`).

## Çalışma yöntemi
1. Dersin "Plan" sekmesini sırayla izle.
2. Notu bir kez oku → kapat → hatırladığını kâğıda yaz → kartlarla sına.
3. Kartta "Bilemedim / Zor / Bildim" dürüst işaretle (Leitner kutuları, 1-14 gün aralık).
4. Testte yanlışlar "Yanlışlarım"a düşer. Hesap konularında Alıştırma sekmesiyle pekiştir.
5. İlerleme her ders için ayrı, tarayıcıda saklanır.

## Dikkat
- Transkriptler otomatik yazıya çevrilmiş; bazı terimler bozuk. Notlar bağlamdan düzeltildi, ama sınavdan önce slayt/kitapla karşılaştır.
- Hocaların "sınavda çıkar" vurguları notlarda işaretli (özellikle Stratejik: stratejik bilinç ve stratejistler; İstatistik: yuvarlama ve yazım kuralları).
- Bazı kayıtlar konunun ortasından başlıyor (Pazarlama 1, Örgütsel 2); eksik girişler notlarda yok.
- İstatistik Konu 6 (değişkenlik) artık bu yılın ders kaydıyla destekli; Konu 7 (normal dağılım, z skoru) hâlâ geçen yılın notlarından, önden çalışma niteliğinde.
- Örgütsel: normlar dersinin kaydı yok (Ders 3 oradan devam ediyor). Stratejik: vize kapsamı hocaya göre konu slaytının 30. sayfasına kadar; kahve zinciri vakasındaki bakım-onarım sorusunun cevabı kayıtta net duyulmuyor.
- Veri Yapıları: stack slaytının son sayfasında prefix/postfix yer değiştirmiş; notlarda düzeltildi.
- E-Ticaret: fotoğraflarda bazı bölümler eksik (Hafta 3'te 6–9, Earl'ün 6 aşamalı modeli); notlarda işaretli.
- Eski `Pazarlama-Calisma-Sistemi/` klasörü bu yapıyla değiştirildi (içeriği `pazarlama/` içinde). İlerleme kayıtları ayrı olduğundan yalnızca birini kullan.

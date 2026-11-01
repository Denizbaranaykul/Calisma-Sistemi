# Çalışma Sistemi (6 ders)

`index.html` dosyasını aç, dersi seç. Her ders kendi klasöründe ve internet gerekmez.

| Ders | Klasör | Kaynak | İçerik | Alıştırma üreticisi |
|---|---|---|---|---|
| Pazarlama | `pazarlama/` | Ders kayıtları | 3 ders · 75 kart · 37 soru | — |
| İstatistik | `istatistik/` | Kayıtlar + 2026 el notları + 2025 notları + Futbol veri seti | 7 konu · 89 kart · 71 soru | frekans, ortalama/medyan/mod, ağırlıklı ortalama, ranj/OMS/varyans/s.sapma, z skoru, görgül kural |
| Örgütsel Davranış | `orgutsel/` | Ders kayıtları | 2 ders · 41 kart · 24 soru | — |
| Stratejik Yönetim | `stratejik/` | Kayıtlar + Bölüm 1–4 slaytları | 6 konu · 94 kart · 75 soru | pazar gelişim hızı, GSYİH/GSMH ve üretim faktörleri |
| Veri Yapıları | `veri_yapilari/` | Ders PDF'leri | 5 konu · 51 kart · 37 soru | ağaç dolaşma, BST, ağaç terimleri, infix→postfix/prefix, postfix hesaplama, yığın/kuyruk |
| E-Ticaret | `e-ticaret/` | Slayt fotoğrafları (106 adet) | 4 hafta · 60 kart · 41 soru | dönüşüm oranı, AOV, CAC, sepet terk oranı |

Her ders klasöründe: `index.html` (plan, notlar, aralıklı tekrar kartları, test, alıştırma, ilerleme), `anki-kartlar.csv` (Anki'ye `;` ayraçlı, UTF-8 aktar) ve `veri/` (düzenlenebilir kaynak).

## Alıştırma sekmesi
Test sorularından farklı olarak bu sorular **her açılışta rastgele sayılarla yeniden üretilir** — sınırsızdır. Cevabı yazarsın, "Kontrol et" doğru/yanlış ve adım adım çözümü gösterir. Ondalıkta virgül veya nokta kullanılabilir; nihai cevap 3 basamağa yuvarlanır. Başarı oranı İlerleme sekmesinde görünür.

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
- İstatistik Konu 6–7 (değişkenlik, normal dağılım, z skoru) geçen yılın notlarından; bu yıl henüz işlenmediyse önden çalışma niteliğinde.
- Veri Yapıları: stack slaytının son sayfasında prefix/postfix yer değiştirmiş; notlarda düzeltildi.
- E-Ticaret: fotoğraflarda bazı bölümler eksik (Hafta 3'te 6–9, Earl'ün 6 aşamalı modeli); notlarda işaretli.
- Eski `Pazarlama-Calisma-Sistemi/` klasörü bu yapıyla değiştirildi (içeriği `pazarlama/` içinde). İlerleme kayıtları ayrı olduğundan yalnızca birini kullan.

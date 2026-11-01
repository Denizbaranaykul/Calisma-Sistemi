# Konu 1 — Bağlı listeler (Linked List)

## Bağlı liste nedir?
- Aynı kümeye ait veri parçalarının bellekte **sanal olarak** birbirine bağlanmasıyla oluşur.
- Bileşenler: **düğüm (node)** = veri bloğu + **bağlantı işaretçisi (link/next)**.
- **Head:** ilk elemanı gösterir. **Tail:** son elemanı gösterir (son düğümün next'i NULL).
- Ekleme ve silme kolaydır: yalnızca linkler değiştirilir (dizideki gibi kaydırma yok).
- Kullanım: dinamik bellek tahsisi, yığın ve kuyruk gerçekleştirme, hash tablolarında çarpışma (collision) çözümü, metin editörleri (her satır bir düğüm), tarayıcı listeleri, graf/yol temsili, veri akışı işleme.

## Türler
| Tür | Açıklama |
|---|---|
| **Tek yönlü (singly)** | Her düğüm yalnızca bir sonrakini gösterir. En yaygın tür. |
| **Çift yönlü (doubly)** | Her düğüm hem öncekini (prev) hem sonrakini (next) gösterir; ileri-geri gezinme. |
| **Çevrimsel (circular)** | Son düğüm ilk düğüme bağlanır; NULL yok, başlangıç/son yok. |
| **Karma (hybrid)** | Farklı türlerin birleşimi. |

## Temel işlemler
1. **Boş liste:** head ve tail NULL.
2. **Ekleme:** başa, sona veya sıralı (ortaya). Adımlar: yeni düğüm oluştur → bağlantıları ayarla → işaretçileri güncelle.
3. **Silme:** düğümü bul → bağlantıyı kopar (öncekinin next'ini sonrakine yönlendir) → belleği iade et. Baştan, sondan, tümü veya istenen düğüm silinebilir.
4. **Arama** ve 5. **Sıralama** (Merge/Quick Sort düğümleri yeniden bağlayarak verimli olabilir).

## Çift yönlü bağlı liste
- Her düğüm iki bağlantı içerir; **aradan ekleme/silme kolay**.
- Kullanım: **undo/redo**, tarayıcı **geri/ileri** (current.prev / current.next), medya oynatıcı önceki/sonraki şarkı, **LRU cache** (hash table ile birlikte; ortadan O(1) silme), metin editörleri, navigasyon, bellek blokları, pencereler arası gezinme.
- **Avantaj:** referansı bilinen ortadaki düğümü **O(1)**'de silebilir; ileri-geri gezinme. **Dezavantaj:** ekstra prev işaretçisi → daha fazla bellek; ekleme/silmede daha çok işaretçi güncellemesi.
- Silme tek yönlüye göre daha verimlidir çünkü önceki düğüme doğrudan erişim vardır (tek yönlüde öncekini bulmak için baştan taramak gerekir).

## Çevrimsel bağlı liste
- Hiç NULL yok, her düğüm başlangıç ya da son olabilir; sona gelince otomatik başa dönülür.
- Kullanım: işletim sisteminde süreçlere döngüsel erişim (round-robin), çok oyunculu oyunlarda sıra değişimi.

---

# Konu 2 — Yığın (Stack)

## Kavram
- **LIFO / FILO** (Last In First Out / First In Last Out). Bellek üzerinde kurulmuş mekanizma.
- **Stack pointer (top):** ekleme yapılacak boş hücreyi / en üstü gösterir.
- İşlemler: **push()** ekle, **pop()** en son ekleneni çıkar, **top()/peek()** en üsttekine bak, **count()** eleman sayısı, **isEmpty()** boş mu.

## Kullanım alanları
- Günlük hayat: şarjör, yemekhane tepsileri, el feneri pilleri.
- Bilgisayar: **undo/redo**, web geri butonu, **fonksiyon çağrıları (call stack)** ve **özyineleme (recursion)**, bellek yönetimi, **geri izleme (backtracking)** (labirent, sudoku, satranç), derleyicide **parantez dengeleme** ve **infix→postfix/prefix** dönüşümü, **DFS** (derinlik öncelikli arama), thread'lerin kendi stack'i, kesme (interrupt) durumunun saklanması, JVM/.NET CLR gibi stack tabanlı sanal makineler, Assembly PUSH/POP.

## Uygulamalar
- **Parantez kontrolü:** açılan parantezi push et; kapanan gelince stack boşsa ya da tepedeki eşleşmiyorsa → dengesiz; eşleşirse pop. Sonda stack boşsa dengeli. `{[()]}` → True, `{([)]}` → False.
- **Palindrom kontrolü:** karakterleri stack'e atıp ters sırayla çıkararak karşılaştır.

## Matematiksel notasyonlar
- **Infix:** operatör operandların arasında: `2 + 4 * 6`. Öncelik ve parantez gerekir: (2+4)*6 = 36, 2+(4*6) = 26. Derleyici için zordur → prefix/postfix'e çevrilir.
- **Prefix (Polonya):** operatör önce: `+2*46 = 26`, `*+246 = 36`.
- **Postfix (Ters Polonya):** önce operandlar sonra operatör: `246*+ = 26`, `24+6* = 36`.

| Infix | Prefix | Postfix |
|---|---|---|
| A + B | +AB | AB+ |
| A + B * C | +A*BC | ABC*+ |
| (A + B) * C | *+ABC | AB+C* |
| A + B * C + D | ++A*BCD | ABC*+D+ |
| (A + B) * (C + D) | *+AB+CD | AB+CD+* |
| A * B + C * D | +*AB*CD | AB*CD*+ |
| A + B + C + D | +++ABCD | AB+C+D+ |
| (X + Y) * ((A + B) / C) | *+XY/+ABC | XY+AB+C/* |

- **Dikkat (slayt hatası):** Stack sunumunun son örneğinde prefix ve postfix etiketleri **ters** yazılmış. Doğrusu: prefix `*+XY/+ABC`, postfix `XY+AB+C/*`. Aynı sayfadaki `456*+` ifadesi de **postfix**'tir (prefix değil).
- **Postfix hesaplama (stack ile):** soldan sağa oku; sayıysa push; operatörse iki kez pop, işlemi yap (ikinci çıkan **sol** operand), sonucu push. `456*+` → push 4, 5, 6 → `*`: 5*6=30 → `+`: 4+30 = **34**.
- **Infix→postfix (stack ile):** operandları doğrudan çıktıya yaz; operatörü, tepedeki operatörün önceliği kendisininkinden büyük ya da eşitse onları çıktıya pop ettikten sonra push et; `(` push, `)` gelince `(`'e kadar pop et; sonda kalanları pop et. (Öncelik: `* /` > `+ -`.)
- **Çalışma ödevi — Hanoi Kuleleri:** her hamlede tek disk; büyük disk küçüğün üstüne konamaz; en üstteki disk alınır. (n disk için en az 2ⁿ − 1 hamle.)

---

# Konu 3 — Kuyruk (Queue)

## Kavram
- **FIFO / LILO** (First In First Out). Veri **arkadan (rear)** girer, **önden (front)** çıkar.
- İşlemler: **enqueue()** ekle, **dequeue()** çıkar, **peek()** ilk elemanı gör, **clear()** temizle, **count()** say.
- Kullanım: işletim sisteminde **CPU zamanlayıcı (Round-Robin)**, I/O ve yazıcı kuyruğu, ağ paketleri (router/switch), **mesaj kuyrukları (RabbitMQ, Kafka)**, **BFS** (genişlik öncelikli arama), banka/çağrı merkezi simülasyonu, asenkron görevler, **üretici–tüketici** problemi.

## Tasarım yaklaşımları
1. **Dizi üzerinde kaydırmalı:** tek indis; her dequeue'dan sonra tüm elemanlar sola kaydırılır → basit ama **maliyetli**.
2. **Dizi üzerinde çevrimsel (dairesel / halka bellek):** **iki indis (front, rear)**; dizinin son elemanından sonra ilk elemana dönülür; **kaydırma yok**, bellek verimli.
3. **Bağlı liste ile:** dinamik bellek yönetimi.

## Öncelikli kuyruk (Priority Queue)
- İşletim sistemindeki süreçlerin önceliği varsa kullanılır. Öncelik yoksa FIFO; öncelik varsa FIFO olmaksızın öncelik sırasına göre yerleştirilir (önceliksiz → sona, öncelikli → önceliğine göre yerine).
- Genellikle **bağlı liste** ile gerçekleştirilir.

## Stack vs Queue
| | Stack | Queue |
|---|---|---|
| Mantık | LIFO | FIFO |
| Ekleme/çıkarma | Aynı uçtan (top) | Ekleme rear, çıkarma front |
| Arama algoritması | DFS | BFS |
| Örnek | Undo, call stack | Yazıcı kuyruğu, CPU zamanlama |

---

# Konu 4 — Ağaçlar ve ikili ağaçlar

## Ağaç (Tree)
- Verilerin bellekte **hiyerarşik**, ağaç görünümlü sanal bağlanması.
- Kullanım: dosya sistemleri (klasör yapısı), veritabanı dizinleme (**B-Tree / B+Tree**, MySQL), Dijkstra/Prim/Kruskal (spanning tree), derleyicilerde **soyut sözdizim ağacı (AST)**, **Huffman** sıkıştırma (ZIP, JPEG, MP3), **karar ağaçları** (makine öğrenmesi), oyun ağaçları (satranç, Go).
- **Avantaj:** dengeli ağaçta arama **O(log₂N)** (n=1000 için bağlı listede ~1000, ağaçta <10 işlem); özyinelemeli tasarım kolay. **Dezavantaj:** daha fazla bellek, çok işaretçi ve değişken.

## Temel kavramlar
- **Kök (root):** en tepedeki tek düğüm; önce kök oluşturulur. **Yaprak (leaf, terminal/harici):** çocuğu olmayan düğüm.
- **Kenar (edge):** düğümler arası bağlantı. **Yol (path):** bağlantı dizisi.
- **Çocuk (child), ebeveyn (parent; kök hariç her düğümün bir ebeveyni var), kardeş (sibling; aynı ebeveyn).**
- **Torun (descendant):** bir düğümden yaprağa kadar yoldaki düğümler (en yakını child). **Ata (ancestor):** bir düğümden köke kadar yoldaki düğümler (en yakını parent).
- **Dahili düğüm:** en az bir çocuğu olan düğüm. **Derece (degree):** çocuk/alt ağaç sayısı (yaprakta 0). Tüm düğümlerin derecesi eşitse **homojen ağaç**.
- **Seviye (level):** kök ile düğüm arasındaki kenar sayısı **+ 1** (kök = 1). **Derinlik (depth):** kök ile düğüm arasındaki kenar sayısı (kök = 0). **Yükseklik (height):** düğümden yaprağa en uzun yoldaki kenar sayısı; kökün yüksekliği = ağacın yüksekliği.
- **Alt ağaç (subtree):** bir düğüm ve torunları. **Orman (forest):** ağaçlar kümesi.
- Gösterim: bağlı liste (esnek), dizi (hızlı erişim), işaretçi tabanlı (parent + child işaretçileri).
- **Soru-cevap örneği:** A kökü; A'nın çocukları B, C; B'nin çocukları D, E, F; E'nin çocuğu G; G'nin çocukları H, I → düğüm sayısı 9, yapraklar C, D, F, H, I; H'nin ataları G, E, B, A; B'nin torunları E, G, H, I (slayta göre; D ve F de B'nin torunudur); E'nin kardeşleri D, F; seviye sayısı 5; yükseklik 4.

## İkili ağaç (Binary Tree)
- Her düğüm **en fazla 2** çocuk (sol ve sağ). Bilgisayar biliminde en yaygın veri yapısı.
- **Full (tam/dolu):** her düğümün 0 ya da 2 çocuğu var. Her zaman: **yaprak sayısı = dahili düğüm sayısı + 1**.
- **Complete (eksiksiz):** son seviye hariç tüm seviyeler dolu, son seviye düğümleri soldan sağa (sola yaslı).
- **Balanced (dengeli):** her düğümün alt ağaçları arasındaki yükseklik farkı en fazla 1.
- **Degenerate / pathological (dejenere):** her ebeveynin tek çocuğu var (bağlı listeye benzer).
- **Perfect (mükemmel):** tüm dahili düğümlerin 2 çocuğu var ve tüm yapraklar aynı seviyede. Perfect ağaç aynı zamanda full, complete ve balanced'tır.

## Dolaşma (traversal)
| Yöntem | Sıra | Not |
|---|---|---|
| **Preorder** | kök – sol – sağ | ağacı kopyalamak için ideal |
| **Inorder** | sol – kök – sağ | BST'de küçükten büyüğe sıralı verir |
| **Postorder** | sol – sağ – kök | ağacı silmek için kullanılır |
- Ders örneği (1 kök; 2, 3 çocukları; 2'nin solu 4; 3'ün çocukları 5, 6; 5'in çocukları 7, 8): preorder 1,2,4,3,5,7,8,6 · inorder 4,2,1,7,5,8,3,6 · postorder 4,2,7,8,5,6,3,1.
- Soru 3 (A; B, C; B'nin solu D; C'nin çocukları E, F; E'nin sağı G; F'nin çocukları H, I): preorder A,B,D,C,E,G,F,H,I · inorder D,B,A,E,G,C,H,F,I · postorder D,B,G,E,H,I,F,C,A.
- İpucu: preorder'ın ilk elemanı ve postorder'ın son elemanı her zaman **kök**tür.

---

# Konu 5 — İkili arama ağacı (BST) ve AVL

## BST
- Parent ile child arasında **büyüklük-küçüklük** ilişkisi vardır (sıradan ikili ağaçta yoktur). Her düğüm için: **sol alt ağaçtaki tüm değerler < düğüm ≤ sağ alt ağaçtaki değerler** (derste eşitler sağa).
- Her alt ağaç yine BST'dir (özyinelemeli). **Inorder dolaşma küçükten büyüğe sıralı veri verir** → **Tree Sort**.
- Kullanım: arama yoğun uygulamalar, veritabanı indeksleme (dengeli türevleri AVL, Red-Black, B/B+ Tree), telefon rehberi, sözlük, derleyici sembol tablosu, **aralık sorguları** ("10 ile 30 arasındakiler").
- Arama ortalama **O(log n)**; sıralı veri eklenirse ağaç **dejenere** olur ve O(n)'e düşer → bu yüzden dengeli ağaçlar geliştirildi.

## BST ekleme
- İlk eleman kök olur. Sonraki her değer kökten başlayarak karşılaştırılır: **küçükse sola, büyük veya eşitse sağa**; boş yer bulununca yerleşir.
- Soru 5: [10, 12, 5, 4, 20, 8, 7, 15, 13] → kök 10; sol 5 (sol 4, sağ 8 → 8'in solu 7); sağ 12 (sağ 20 → 20'nin solu 15 → 15'in solu 13).

## BST silme (3 durum)
1. **Yaprak:** doğrudan sil, parent'ın işaretçisi NULL.
2. **Tek çocuklu:** parent'ın işaretçisini silinen düğümün çocuğuna yönlendir; alt ağaç parent'a bağlanır (sol/sağ fark etmez).
3. **İki çocuklu:** **sağ alt ağacın minimumu (inorder successor)** ya da **sol alt ağacın maksimumu (inorder predecessor)** bulunur, değeri silinecek düğüme kopyalanır, sonra o düğüm durum 1 veya 2 ile silinir.

## AVL ağacı (Adelson-Velsky ve Landis)
- Kendi kendini dengeleyen BST. Her düğümde **denge (balans) faktörü BF = h_sol − h_sağ ∈ {−1, 0, +1}**.
- BF **+2 / −2** olursa ağaç dengesizdir → **döndürme (rotasyon)**. Döndürme **O(1)** (yalnızca işaretçi değişikliği). Arama/ekleme/silme her durumda **O(log n)**.
- **4 durum:**
  - **Sağ-sağ (RR) → sola döndürme:** BF = −2, sağ çocuk yukarı çıkar, eski kök onun sol çocuğu olur.
  - **Sol-sol (LL) → sağa döndürme:** BF = +2, sol çocuk yeni kök olur; yeni kökün sağ alt ağacı varsa eski köke sol çocuk olarak bağlanır (azalan sırada eklemede sık).
  - **Sol-sağ (LR) → önce sol çocukta sola, sonra düğümde sağa döndürme** (çift döndürme).
  - **Sağ-sol (RL) → önce sağ çocukta sağa, sonra düğümde sola döndürme** (LR'nin ayna görüntüsü).
- Örnek [1..7] sırayla: normal BST bağlı listeye dönerdi; AVL'de kök **4**, yükseklik 3 (ders slaytı; kenar sayısıyla 2), 7 düğüm.
- Soru 6: 3, 2, 1 → 1 eklenince 3'te denge bozulur, tek döndürme → kök 2. 4 eklenir. 5 → 3'te dengesizlik, tek döndürme. 6 → 2'de (kök) dengesizlik, tek döndürme → kök **4** (sol 2: 1, 3; sağ 5: 6).
- Soru 7 (devam: 7, 16, 15, 14, 13, 12, 11, 10, 8, 9): 7 → 5'te dengesizlik, tek döndürme; 16 sorunsuz; 15 → 7'de dengesizlik, **tek döndürme yetmez → ikili (çift) döndürme**; 14 → ikili döndürme; 13 → tek döndürme (kök **7** olur); 12, 11, 10 → tek döndürmeler; 8 ve 9 eklenince yine döndürme.

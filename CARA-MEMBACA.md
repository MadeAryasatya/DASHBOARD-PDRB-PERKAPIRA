# Cara Membaca Data & Grafik Dashboard PDRB Per Kapita

## 1. Angka apa yang sedang dilihat?

**PDRB per kapita** = seluruh nilai barang & jasa yang diproduksi di suatu
wilayah dalam setahun (PDRB), dibagi jumlah penduduknya. Sederhananya:
*"berapa besar kue ekonomi wilayah ini per satu penduduk"*.

Tiga hal penting sebelum menafsirkan:

1. **Satuan: ribu rupiah per orang per tahun.**
   Contoh baris tabel: Kab. Morowali 2025 = `1.072.574` ribu Rp ≈ **Rp1,07 miliar
   per penduduk per tahun**. Median nasional 53.988 ribu Rp ≈ Rp54 juta.

2. **PDRB per kapita BUKAN pendapatan penduduk.**
   Nilai produksi tercatat di lokasi pabrik/tambang, tapi keuntungannya banyak
   mengalir ke pemilik modal di luar daerah. Morowali (smelter nikel) dan
   Mimika (tambang Freeport) memuncaki daftar bukan karena warganya paling
   sejahtera, melainkan karena nilai produksi per penduduknya sangat besar.
   Untuk kesejahteraan warga, angka ini perlu disandingkan dengan indikator
   lain (pengeluaran per kapita, kemiskinan, IPM).

3. **ADHB = atas dasar harga berlaku (nominal), termasuk inflasi.**
   Kenaikan dari tahun ke tahun adalah gabungan pertumbuhan ekonomi riil +
   kenaikan harga. Jadi "+8% per tahun" tidak berarti ekonominya tumbuh riil 8%.

## 2. Cara membaca tabel "Seluruh kabupaten/kota"

| Kolom | Artinya |
|---|---|
| 2021–2023 | Angka final BPS |
| 2024* | Angka **sementara** — masih bisa direvisi BPS |
| 2025** | Angka **sangat sementara** — proyeksi awal, paling mungkin direvisi |
| "–" | Data belum tersedia (provinsi pemekaran Papua baru punya data sejak 2023) |
| **Δ p.a.** | Pertumbuhan **nominal rata-rata per tahun**, dihitung dari tahun pertama yang tersedia sampai 2025 (CAGR) |

Contoh membaca Δ p.a.: Morowali naik dari 601.783 (2021) ke 1.072.574 (2025).
Rata-rata per tahun = (1.072.574 ÷ 601.783)^(1/4) − 1 = **+15,5%/tahun**.

Angka Δ p.a. yang ekstrem biasanya bercerita: Halmahera Tengah **+51,1%/tahun**
(166 ribu → 871 ribu dalam 4 tahun) adalah efek beroperasinya kawasan industri
nikel — lonjakan basis produksi, bukan pertumbuhan "normal".

Interaksi:
- **Klik judul kolom** untuk mengurutkan (klik lagi untuk membalik arah).
- **Kotak pencarian** menyaring nama kab/kota atau provinsi.
- **Dropdown provinsi** menampilkan satu provinsi saja — berguna untuk
  membandingkan kesenjangan antarkab/kota di dalam provinsi yang sama.

## 3. Cara membaca grafik "Tren 2021–2025"

- **Satuannya berbeda dari tabel: juta rupiah** (bukan ribu), supaya sumbu
  tidak penuh angka panjang. Label "DKI Jakarta 367,7" = 367,7 juta =
  367.687 ribu Rp di tabel. (1 juta = 1.000 ribu.)
- **Satu garis = satu provinsi** (angka rata-rata provinsi, bukan kab/kota).
  Warna garis sama dengan warna chip di atas grafik; nama + nilai 2025
  tertera di ujung kanan tiap garis.
- **Arahkan kursor ke area grafik** untuk melihat nilai semua garis pada tahun
  tertentu (garis putus-putus vertikal menandai tahun yang disorot).
- **Maksimal 6 provinsi** agar tetap terbaca. Tambah lewat dropdown, hapus
  lewat tanda × di chip.
- Yang dibaca dari bentuk garis:
  - **Kemiringan** = kecepatan pertumbuhan nominal. Garis DKI yang curam dan
    posisinya jauh di atas menunjukkan gap absolut yang terus melebar terhadap
    provinsi lain, meski persentase pertumbuhannya bisa saja mirip.
  - **Garis hampir datar di posisi rendah** (mis. NTT) = tumbuh lambat dari
    basis kecil — kandidat prioritas pembangunan (bandingkan slide
    "pertumbuhan diprioritaskan di wilayah lower-middle income").
  - **Garis bergelombang/menurun** biasanya wilayah berbasis komoditas —
    nilainya ikut naik-turun harga tambang (contoh: Kaltim 2022→2025).
- Ingat: titik 2024 dan 2025 memakai angka sementara — kemiringan di ujung
  kanan bisa berubah saat BPS merevisi.

## 4. Cara membaca peta & kategori pendapatan

- Warna = kategori estimasi ala Bank Dunia setelah nilai dikonversi ke US$
  dengan kurs di kotak input (default Rp16.300/US$):
  **biru tua pekat** High (>$13.935) · **biru sedang** Upper-middle
  ($4.496–13.935) · **biru muda** Lower-middle ($1.136–4.495) ·
  **abu-abu** data belum tersedia.
- Ini estimasi kasar: ambang resmi Bank Dunia memakai **GNI per kapita
  (metode Atlas)**, bukan PDRB, dan kurs sangat memengaruhi hasil — geser
  kursnya untuk melihat betapa sensitifnya kategori di dekat ambang
  (mis. Kaltim yang berada persis di sekitar batas High/Upper-middle).

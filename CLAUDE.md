# Project: Dashboard PDRB Per Kapita Indonesia 2021–2025

Ringkasan teknis untuk konteks cepat. Detail metodologi ada di README.md dan CARA-MEMBACA.md.

## Apa ini

Dashboard web satu-file (HTML+CSS+JS vanilla, tanpa dependensi/CDN) berisi PDRB per kapita
ADHB 2021–2025 dari BPS (Tabel 153–190): 38 provinsi, 514 kabupaten/kota.
Bahasa UI: Indonesia. Mendukung tema terang/gelap otomatis.

## Lokasi & deployment

| Tempat | Isi |
|---|---|
| `D:\INTERNSHIP\DASHBOARD MAIN` | Folder ini — proyek utama (git repo) |
| GitHub | https://github.com/MadeAryasatya/DASHBOARD-PDRB-PERKAPIRA (branch `main`) |
| GitHub Pages | https://madearyasatya.github.io/DASHBOARD-PDRB-PERKAPIRA/ (dari `index.html`) |
| Artifact Claude | https://claude.ai/code/artifact/5b1d486c-c561-453d-9905-3110494d2fe2 |
| `D:\INTERNSHIP\DASHBOARD` | Versi lain: `PDRB-Dashboard.xlsx` (dashboard Excel berformula) + `powerbi\` (proyek PBIP, CSV long, TopoJSON, panduan) |
| File Excel user | `C:\Users\User\Downloads\PRDB PERKAPITA 2025 (1).xlsx` — kolom 2025 terisi + sheet "Data PDF 2021-2025" |

PENTING: `index.html` = salinan identik `pdrb-dashboard.html` (untuk Pages).
Kalau salah satu diedit, salin ulang ke yang lain sebelum commit.

## Alur data (kalau data perlu diperbarui)

1. Sumber: 4 PDF BPS di `C:\Users\User\Downloads\PDRB_203_210.pdf` dst. (Tabel 153–190).
2. `scripts/extract_pdrb.py` → `data/pdrb_data.json`. Trik penting: PDF berwatermark
   diagonal "www.bps.go.id" (Arial-Bold ≥20pt) yang menyisipi huruf ke angka —
   filter: hanya karakter `upright` dan `size < 15`. Tanda "–" di PDF = data belum ada (None).
3. Merge duplikat pemekaran Papua (26 wilayah muncul 2×: provinsi induk 2021–2022,
   provinsi baru 2023–2025) → `data/dash_data.json` (38 prov + 514 kab/kota).
4. Peta: `data/id38.geojson` → `scripts/make_map.py` (proyeksi equirectangular,
   Douglas-Peucker) → `data/map_paths.json`.
5. `dash_data.json` ditanam ke HTML menggantikan placeholder `__DATA__`;
   `map_paths.json` menjadi `const MAP`. (Di file jadi, keduanya sudah tertanam.)

## Anatomi pdrb-dashboard.html (urutan section)

1. **KPI** (`#kpis`) — 4 kartu: tertinggi (Morowali 1.072.574), terendah (Puncak Jaya 7.521),
   median (53.988), rasio (142,6×).
2. **Peta koroplet** (`#map`, fungsi `renderMap`) — warna = kategori pendapatan.
3. **Bar provinsi** (`#provBars`, `renderProv`) + pemilih tahun (`#provYear`) +
   **kategori pendapatan** (`#incSummary`) + input kurs (`#kurs`, default 16300,
   ambang Bank Dunia FY2026: LM 1136 / UM 4496 / High 13935 US$).
4. **Tren** (`#lineChart`, `renderLine`) — chip multi-select maks 6 provinsi;
   label ujung kanan anti-tabrakan (jarak minimal 27px — jangan dikecilkan lagi).
5. **Top/Bottom 15 kab/kota** (`#kkBars`, `renderKK`).
6. **Tabel 514 baris** (`renderTable`) — cari, filter provinsi, sortir, kolom Δ p.a. (CAGR).

Satuan: tabel & bar = **ribu Rp**; grafik tren = **juta Rp**. Warna via CSS custom
properties di `:root` (light) + `@media prefers-color-scheme: dark` + override `[data-theme]`.

## Gotcha yang pernah kejadian (jangan diulang)

- **Live Server**: kalau HTML tidak punya `</body>`, Live Server menyuntik skrip
  reload-nya sebelum `</svg>` pertama → merusak halaman. File di repo ini SUDAH
  dibungkus `<html><body>` lengkap, jadi aman. Jangan hapus tag pembungkusnya.
- File ini mandiri — jangan menambah CDN/font eksternal (versi Artifact diblokir CSP).
- Angka 2024 = sementara, 2025 = sangat sementara; provinsi pemekaran Papua
  tidak punya data 2021–2022 (tampil "–", jangan dianggap bug).
- Nama PDF BPS "Kab. Bireun" = "Kab. Bireuen" (ejaan beda, sudah ditangani fuzzy match).

## Cara melapor bug (untuk pemilik proyek)

Sebutkan: (1) nama section dari daftar anatomi di atas, (2) langkah yang memicu
(mis. "pilih tahun 2021 lalu ganti kurs"), (3) screenshot + pesan error Console
(F12 → tab Console) kalau ada.

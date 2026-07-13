# Dashboard PDRB Per Kapita Indonesia 2021–2025

Dashboard interaktif PDRB per kapita atas dasar harga berlaku (ADHB) untuk
38 provinsi dan 514 kabupaten/kota, dibangun dari publikasi BPS
*Produk Domestik Regional Bruto Kabupaten/Kota di Indonesia 2021–2025* (Tabel 153–190).

**Versi online (Artifact):** https://claude.ai/code/artifact/5b1d486c-c561-453d-9905-3110494d2fe2

## Cara membuka

Klik dua kali `pdrb-dashboard.html` — semua data dan peta sudah tertanam di dalam
satu file, tidak butuh internet atau server.

## Isi folder

| Path | Keterangan |
|---|---|
| `pdrb-dashboard.html` | Dashboard lengkap (HTML + CSS + JS + data tertanam) |
| `scripts/extract_pdrb.py` | Ekstraksi 38 tabel dari 4 PDF BPS (pdfplumber; menyaring watermark diagonal berdasarkan ukuran font) |
| `scripts/build_excel.py` | Mengisi kolom 2025 di file Excel dan menambah sheet "Data PDF 2021-2025" |
| `scripts/make_map.py` | Konversi GeoJSON 38 provinsi → path SVG ringkas (proyeksi equirectangular + simplifikasi Douglas-Peucker) |
| `data/pdrb_data.json` | Hasil ekstraksi mentah per tabel (termasuk baris ringkasan) |
| `data/dash_data.json` | Data siap-dashboard: 38 provinsi + 514 kab/kota (duplikat pemekaran Papua sudah digabung) |
| `data/map_paths.json` | Path SVG peta per provinsi |
| `data/id38.geojson` | Sumber batas 38 provinsi ([denyherianto/indonesia-geojson-topojson-maps-with-38-provinces](https://github.com/denyherianto/indonesia-geojson-topojson-maps-with-38-provinces)) |

Versi Excel (`PDRB-Dashboard.xlsx`) dan paket Power BI (proyek PBIP, CSV, peta
TopoJSON, panduan) berada di folder terpisah: `D:\INTERNSHIP\DASHBOARD`.

## Catatan data

- Satuan nilai: **ribu rupiah per kapita**. 2024 angka sementara (*), 2025 angka sangat sementara (**).
- Wilayah pemekaran Papua tercatat di provinsi barunya; nilai 2021–2022 diambil dari tabel provinsi induk.
- Kategori pendapatan pada peta/grafik provinsi adalah estimasi: PDRB per kapita dikonversi ke US$
  (kurs bisa diubah di dashboard, default Rp16.300) lalu dibandingkan ambang Bank Dunia FY2026.
  Ambang resmi memakai GNI per kapita (metode Atlas), jadi hasilnya indikatif.

## Regenerasi dari sumber

Butuh Python 3 dengan `pdfplumber`, `openpyxl`, lalu:

1. `python scripts/extract_pdrb.py pdrb_data.json` — ekstrak ulang dari PDF (path PDF di dalam skrip)
2. `python scripts/build_excel.py` — isi ulang file Excel
3. `python scripts/make_map.py` — bangun ulang path peta dari `id38.geojson`
4. Sisipkan `dash_data.json` dan `map_paths.json` ke placeholder `__DATA__` / `const MAP` di HTML

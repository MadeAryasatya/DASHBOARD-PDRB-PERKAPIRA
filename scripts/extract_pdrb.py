# -*- coding: utf-8 -*-
import pdfplumber, re, json, sys
from pdfplumber.utils import extract_text as ex_text

files = [
    r'C:\Users\User\Downloads\PDRB_203_210.pdf',
    r'C:\Users\User\Downloads\PDRB_211_220.pdf',
    r'C:\Users\User\Downloads\PDRB_221_230.pdf',
    r'C:\Users\User\Downloads\PDRB_231_240.pdf',
]

num = r'(\d{1,3}(?:\.\d{3})+|\d+|[\-‐-―−…�])'
row_re = re.compile(
    r'^(?:\d{2}\.\s*)?((?:Kab\.|Kota)\s*\D+?)\s+' + r'\s+'.join([num]*5) + r'\s*$'
)
sum_re = re.compile(r'^(Jml Kab\./Kota.*?|Provinsi/Province.*?)\s+' + r'\s+'.join([num]*5) + r'\s*$')
prov_re = re.compile(r'di Provinsi\s+(.+?)\s*$')

def to_int(s):
    if not re.search(r'\d', s):
        return None  # missing value marker
    return int(s.replace('.', ''))

tables = []  # list of dicts: tabel_no, provinsi, rows=[(name, v21..v25, is_summary)]
for f in files:
    with pdfplumber.open(f) as pdf:
        for p in pdf.pages:
            # table body is Times New Roman ~7.2pt; the diagonal watermark is Arial-Bold 20pt+
            chars = [c for c in p.chars if c.get('upright') and c.get('size', 0) < 15]
            txt = ex_text(chars)
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            tabel_no = None
            provinsi = None
            for l in lines:
                m = re.search(r'Tabel/Table\s+(\d+)', l)
                if m: tabel_no = int(m.group(1))
                m = prov_re.search(l)
                if m and provinsi is None:
                    provinsi = m.group(1).strip()
            rows = []
            for l in lines:
                m = row_re.match(l)
                if m:
                    name = re.sub(r'\s+', ' ', m.group(1)).strip()
                    vals = [to_int(m.group(i)) for i in range(2, 7)]
                    rows.append((name, vals, False))
                    continue
                m = sum_re.match(l)
                if m:
                    label = re.sub(r'\s+', ' ', m.group(1)).strip()
                    vals = [to_int(m.group(i)) for i in range(2, 7)]
                    rows.append((label, vals, True))
            tables.append({'tabel': tabel_no, 'provinsi': provinsi, 'rows': rows})

total_rows = sum(len(t['rows']) for t in tables)
kabkota = sum(1 for t in tables for r in t['rows'] if not r[2])
print('tables:', len(tables), 'total rows:', total_rows, 'kab/kota rows:', kabkota)
for t in tables:
    ks = sum(1 for r in t['rows'] if not r[2])
    ss = sum(1 for r in t['rows'] if r[2])
    print(f"Tabel {t['tabel']} {t['provinsi']}: {ks} kab/kota, {ss} summary")

with open(sys.argv[1] if len(sys.argv) > 1 else 'pdrb_data.json', 'w', encoding='utf-8') as fh:
    json.dump(tables, fh, ensure_ascii=False, indent=1)

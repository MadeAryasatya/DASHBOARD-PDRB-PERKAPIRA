# -*- coding: utf-8 -*-
# GeoJSON -> compact SVG paths (equirectangular, Douglas-Peucker simplified)
import json, math

g = json.load(open('id38.geojson', encoding='utf-8'))

W = 1000.0
lons, lats = [], []
for f in g['features']:
    geom = f['geometry']
    polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
    for poly in polys:
        for x, y in poly[0]:
            lons.append(x); lats.append(y)
lon0, lon1 = min(lons), max(lons)
lat0, lat1 = min(lats), max(lats)
SC = W / (lon1 - lon0)
H = (lat1 - lat0) * SC
def proj(lon, lat):
    return ((lon - lon0) * SC, (lat1 - lat) * SC)

def dp(pts, eps):
    if len(pts) < 3: return pts
    keep = [False]*len(pts); keep[0] = keep[-1] = True
    stack = [(0, len(pts)-1)]
    while stack:
        i0, i1 = stack.pop()
        ax, ay = pts[i0]; bx, by = pts[i1]
        dx, dy = bx-ax, by-ay
        L2 = dx*dx + dy*dy
        dmax, imax = -1.0, -1
        for i in range(i0+1, i1):
            px, py = pts[i]
            if L2 == 0:
                d = math.hypot(px-ax, py-ay)
            else:
                t = ((px-ax)*dx + (py-ay)*dy) / L2
                t = max(0.0, min(1.0, t))
                d = math.hypot(px-(ax+t*dx), py-(ay+t*dy))
            if d > dmax: dmax, imax = d, i
        if dmax > eps:
            keep[imax] = True
            stack.append((i0, imax)); stack.append((imax, i1))
    return [p for p, k in zip(pts, keep) if k]

def ring_area(pts):
    s = 0.0
    for i in range(len(pts)-1):
        s += pts[i][0]*pts[i+1][1] - pts[i+1][0]*pts[i][1]
    return abs(s)/2

EPS = 0.7        # px tolerance
AMIN = 2.0       # px^2: drop islets smaller than this

NAME_FIX = {'Daerah Istimewa Yogyakarta': 'DI Yogyakarta'}
out = []
for f in g['features']:
    name = NAME_FIX.get(f['properties']['PROVINSI'], f['properties']['PROVINSI'])
    geom = f['geometry']
    polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
    d = []
    for poly in polys:
        ring = [proj(x, y) for x, y in poly[0]]
        if ring_area(ring) < AMIN: continue
        ring = dp(ring, EPS)
        if len(ring) < 4: continue
        seg = 'M' + f'{ring[0][0]:.1f} {ring[0][1]:.1f}'
        px, py = ring[0]
        for x, y in ring[1:-1]:
            seg += f'l{x-px:.1f} {y-py:.1f}'
            px, py = x, y
        seg += 'Z'
        d.append(seg)
    if not d:
        print('WARN: no rings for', name)
    out.append({'n': name, 'd': ''.join(d)})

js = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
open('map_paths.json', 'w', encoding='utf-8').write(js)
print('provinces:', len(out), '| H =', round(H, 1), '| bytes:', len(js.encode('utf-8')))
print('largest path:', max(len(o['d']) for o in out), '| names ok:', sorted(o['n'] for o in out)[:5])

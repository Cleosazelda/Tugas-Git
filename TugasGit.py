data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

panen_padi=[]
panen_kedelai=[]

for i,j in data_panen.items():
    panen_padi.append(j['hasil_panen']['padi'])

for i,j in data_panen.items():
    panen_kedelai.append(j['hasil_panen']['kedelai'])

total_padi=sum(panen_padi)
total_kedelai=sum(panen_kedelai)

print(f"total jumlah padi: {total_padi}")
print(f"total jumlah kedelai: {total_kedelai}")
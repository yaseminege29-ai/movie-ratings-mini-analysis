# Movie Ratings – Mini Veri Analizi

Bu proje, küçük bir film listesi üzerinde **Pandas kullanarak temel veri analizi** adımlarını uygulamak için hazırlandı.

## 📂 Veri Seti

- Dosya: `movies.csv`
- Sütunlar:
  - `title` — Film adı
  - `rating` — 0–10 arası puan
  - `genre` — Film türü
  - `year` — Çıkış yılı

## 🧪 Yapılan Analizler

`analysis.py` dosyasında şu işlemler yapıldı:

- Veriyi CSV'den okuma
- İlk 5 satırı görüntüleme (`head`)
- Veri tipi & null kontrolü (`info`)
- Temel istatistikler (`describe`)
- Ortalama puan hesaplama
- 8.0 ve üzeri filmleri filtreleme
- Türlere göre ortalama puan
- En yüksek puanlı filmi bulma
- Yıllara göre puan ortalaması

## ▶️ Çalıştırma

```bash
python analysis.py

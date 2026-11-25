# YönetAI — Yeni Nesil Site ve Apartman Yönetimi

YönetAI V14, mobil öncelikli **mavi-beyaz** tasarım sistemiyle hazırlanmış bir etkileşimli site yönetimi ön yüz prototipidir.

## Canlı demo

- Git bağlı yeni sürüm: Vercel `yonetai` projesi
- Önceki V14 yayını: https://yonetai-v14-premium.vercel.app

## Kurulum

Bu sürüm statik HTML, CSS ve vanilla JavaScript kullanır; ek bağımlılık yoktur.

```bash
python -m http.server 8080
```

Tarayıcıdan `http://localhost:8080` adresini açın.

## Ekranlar

- Yönetici: genel bakış, aidat ve tahsilat, finans, bağımsız bölümler, uzaktan sayaç izleme, arıza talepleri, duyurular, ziyaretçi işlemleri ve raporlar.
- Sakin: aidat detayları, ödeme simülasyonu, ziyaretçi davetleri, duyurular, sayaç ve talep ekranları.
- Saha ekibi: iş emri ve sayaç kontrol iş akışlarının demo görünümleri.

**Tüm veriler temsili örnek veridir.** İşlemler yalnızca tarayıcı içinde simüle edilir veya tarayıcı depolamasında tutulur. Gerçek banka/kart tahsilatı, merkezi veri tabanı, üretim düzeyi kimlik doğrulama, yetkilendirme, fiziksel sayaç veya muhasebe entegrasyonu mevcut değildir. Bu haliyle gerçek sakin verileriyle kullanılmamalıdır.

## Tasarım sistemi

- Ana mavi: `#116CD5`
- Derin lacivert: `#0A2953`
- Açık zemin: `#F5F8FC`
- Tipografi: DM Sans + Manrope
- Mobil ve masaüstü görünümler
- Mimari görseller: üretilmiş temsili konsept fotoğraflar (harici CDN URL’leri), gerçek siteden çekilmiş görüntüler değildir.

## Dosyalar

`index.html`, `style.css`, `app.js` — düzenlenebilir kaynak kodları.

## Üretim öncesi gereksinimler

Güvenli kimlik doğrulama, sunucu tarafında site/daire bazlı yetki denetimi, veritabanı, ödeme sağlayıcısı entegrasyonu, KVKK veri yönetimi, sayaç gateway/doğrulama altyapısı, denetim kayıtları ve uçtan uca testler gerekir.

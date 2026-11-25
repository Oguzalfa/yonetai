# YönetAI V15 — Site ve Apartman Yönetimi

YönetAI, yönetici, site sakini ve saha ekibi için hazırlanan **mobil öncelikli, etkileşimli ürün ön izlemesidir**. Marka renkleri derin lacivert `#0A2953`, kurumsal mavi `#116CD5`, kırık beyaz `#F5F8FC` ve beyazdır. Profesyonel görünümü, doğru içerik hiyerarşisini, tutarlı ikon dilini ve gerçekçi akışları önceliklendirir.

## Canlı uygulama

[https://yonetai.vercel.app](https://yonetai.vercel.app) — GitHub `Oguzalfa/yonetai` üzerinden Vercel production.

## Modüller

**Yönetici:** yönetim özeti, bağımsız bölümler, aidat/tahsilat, finans ve raporlar, örnek banka hareketi eşleştirme, su/elektrik/doğalgaz sayaç merkezi, arıza ve iş emirleri, ziyaretçi yönetimi, taşınma ve izinler, ortak alan rezervasyonları, duyurular, anketler, belgeler ve karar özetleri, hizmet pazarı, sürüm bilgisi.

**Sakin:** ana sayfa, ödeme ön izlemesi, talepler, kendi sayaç kayıtları, duyurular, ziyaretçi daveti, ortak alan rezervasyon başvurusu ve iptali, taşınma bildirimi, belge görüntüleme, anket katılımı, hizmetler ve yardım.

**Saha:** saha özeti, görevler, sayaç kontrol listesi, taşınma takvimi, duyurular ve yardım.

### Örnek etkileşimler

- Rezervasyon başvurusu → tarih/saat çakışma kontrolü → yönetici onayı veya reddi → sakin iptali
- Taşınma bildirimi → yönetici onayı veya reddi
- Anket oluşturma → sakin görüşü → katılım oranı → anketi kapatma
- Daire/tahakkuk kaydı → örnek banka hareketi eşleştirme (tutar doğrulama)
- Arıza talebi → atama → işlemde → tamamlandı
- Duyuru ve belge özeti ekleme → kayıtta görüntüleme
- Global arama → eşleşen daire, talep veya duyuru ekranına yönlendirme
- CSV dışa/içe aktarma (örnek sayaç verisi), yazdırma, örnek kod kopyalama

**Uyarı:** Bu ekranlar gerçek kullanıcı yönetimi, kimlik doğrulama, ödeme, bankacılık, SMS/e-posta, turnike kontrolü veya sayaç donanımına **bağlı değildir**. Roller yalnızca arayüzü gösterir ve güvenlik yetkisi sağlamaz. Kayıtlar `localStorage` üzerinde aynı tarayıcıya özeldir. Resmî yönetim/hukuki/muhasebe işlemi olarak kullanmayın. Gerçek daire ve sakinlerin kişisel verilerini bu prototipe girmeyin.

## Geliştirme

Ek bağımlılık olmadan çalışır:

```bash
python -m http.server 8080
```

`http://localhost:8080` adresinde açın. Kaynak kod `index.html`, `style.css`, `app.js` dosyalarıdır. Vektör marka varlıkları `logo.svg`, `logo-lockup.svg`, `favicon.svg` dosyalarındadır.

## QA

`tests/smoke.py` Playwright/Chromium kurulu ortamda çalıştırılır. Yönetici menülerini, rol geçişlerini, rezervasyon/onay, belge ve anket etkileşimlerini, örnek banka eşleştirmesini, arama ekranını ve 320/375/390/430/768/1024/1440 px genişliklerinde taşma denetimini kapsar.

## Üretime çıkış ön koşulları

Kimlik doğrulama ve sunucu tarafı yetki, PostgreSQL/Neon veri modeli, işlem günlüğü, ödeme kuruluşu entegrasyonu, banka hareketi doğrulama ve mutabakatı, uzaktan sayaç donanım köprüsü, veri kalite/kalibrasyon, KVKK aydınlatma ve saklama kuralları, iş kuralları, entegrasyon testleri, veri içe alma/taşıma ve felaket kurtarma gerekir.

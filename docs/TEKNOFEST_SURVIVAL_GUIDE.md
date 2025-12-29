# 🦅 Teknofest "Survival Guide": Yarışma Hayatta Kalma Rehberi

> **"Savaş, generallerin planladığı gibi, askerlerin yaşadığı gibi değildir."**

Bu rehber, teknik bilgilerin ötesinde, bir Teknofest yarışmacısının bilmesi gereken **"yazılı olmayan kurallar"**, **kriz yönetimi taktikleri** ve **jüri psikolojisi** üzerine tüyolardan oluşur.

---

## 🎭 Bölüm 1: Jüriyi "Tavlama" Sanatı

Raporlarınız teknik birer makale değil, projenizi "satan" birer broşürdür. Jüriler binlerce rapor okuyor. Sıkıcı olan kaybeder.

### Altın Kurallar:
1.  **Görsel > Metin:** Kimse 5 sayfa düz yazı okumak istemez. Mimarinizi, veri hazırlığınızı şemalarla (bkz: README'deki Mermaid diyagramları) anlatın.
2.  **"Hata Yaptık" Demekten Korkmayın:** "Modelimiz %99.9 başarı gösterdi" derseniz inanmazlar. "İlk denemede %70 aldık, şu veri artırma tekniğiyle %85'e çıkardık" derseniz **mühendislik sürecinize** saygı duyarlar.
3.  **Yerliliğe Vurgu:** Kullandığınız açık kaynak kütüphaneleri belirtin ama mümkünse "Biz de üzerine şu modülü ekledik" diyerek yerli katkınızı öne çıkarın.

---

## 🚨 Bölüm 2: Felaket Senaryoları (Kriz Masası)

Final günü veya demo öncesi işler ters gidebilir. Panik yapmayın, şu protokolü uygulayın:

### Senaryo A: Demo Günü Model Çalışmıyor!
*   **Çözüm:** Asla "Canlı demo" yapmayın :) Önceden kaydedilmiş bir video veya hazırlanmış çıktılar (pre-computed results) her zaman B planı olarak USB belleğinizde dursun.
*   **Mazeret:** "İnternet bağlantısı yavaş olduğu için sunucuya bağlanamıyoruz, işte offline sonuçlarımız."

### Senaryo B: Eğitim Süresi Yetmiyor!
*   **Çözüm:** Epoch sayısını düşürün ve `EarlyStopping` kullanın. Modeli "Transfer Learning" ile (daha önce eğitilmiş ağırlıklarla) başlatın. Sıfırdan eğitim (training from scratch) yarışma için risktir.

### Senaryo C: Takım Üyesi Ayrıldı
*   **Çözüm:** GitHub commit geçmişi sizin tapunuzdur. Kimin ne yaptığı orada bellidir. Kalan sağlar bizimdir, görev dağılımını revize edin ve yola devam edin.

---

## 💻 Bölüm 3: Donanım Kısıtları (Fakir ama Gururlu GPU'lar)

Herkesin A100 GPU'su yok. Düşük donanımla devler liginde oynamak için:

1.  **Gradient Accumulation:** Batch size'ı küçültün (ömr: 2), ama gradyanları biriktirerek sanal olarak büyük batch size etkisine ulaşın.
2.  **Mixed Precision (FP16):** Modeli 32-bit yerine 16-bit float ile eğitin. RAM kullanımı yarıya düşer, hız 2 kat artar.
3.  **Kaggle/Colab:** Kendi bilgisayarınızı yakmayın. Google Colab veya Kaggle Kernels ücretsiz GPU verir. Notebook'larınızı oraya taşıyın.

---

## 🏆 Son Söz

Teknofest sadece bir yarışma değil, bir **dayanıklılık testidir**. Kodunuz çalışmayabilir, veriniz bozuk çıkabilir. Önemli olan sorunu nasıl çözdüğünüzdür.

**Asla pes etmeyin. Jürinin karşısına çıktığınızda, gözlerinizdeki ışık modelinizin Accuracy değerinden daha önemlidir.**

Başarılar! 🚀

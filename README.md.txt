# 🌡️ Sıcaklık Veri Alıcı Uygulaması

Bu proje, Arduino üzerinden LM35 sıcaklık sensöründen gelen verileri **Python GUI** arayüzü ile okuyup, kullanıcı tarafından belirlenen sıcaklık aralıklarına göre LED ve fan kontrolü sağlar.

## 🛠 Özellikler

- Seri port üzerinden Arduino ile bağlantı
- Kullanıcıdan min ve max sıcaklık değeri alma
- Eski sıcaklık değerlerini arayüzde gösterme
- Bağlan ve bağlantıyı kes butonları
- LM35 sıcaklık sensöründen anlık veri okuma
- 4 LED (Isıtıcı, Mavi, Sarı, Fan) kontrolü
- Arduino bağlı değilken bile arayüzün çalışabilmesi

## 🖥 Kullanılan Teknolojiler

- Python 3
- customtkinter
- pyserial
- Arduino Uno + LM35

## 🔧 Kurulum

1. Bu repoyu indir:
   ```bash
   git clone https://github.com/kullanici_adi/proje_adi.git

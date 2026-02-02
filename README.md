# 📡 ROS2 Projesi

> **Gelişmiş robotik uygulamalar için modern, modüler ve esnek bir altyapı!**

---

## 🎯 Proje Hakkında

Bu proje, Robot Operating System 2 (ROS2) kullanılarak geliştirilmiş, yeni nesil robotik uygulamaların ihtiyaçlarını karşılamak üzere hazırlanan bir platformdur. Gerçek zamanlı iletişim, dağıtık mimari, güvenlik ve genişletilebilir yapı ile hem profesyoneller hem de araştırmacılar için idealdir.

---

## ⭐️ Özellikler

- 🔹 **Modüler ve Genişletilebilir Mimari**
- 🔹 **Çoklu Platform Desteği** (Ubuntu Linux, macOS, Windows)
- 🔹 **Gerçek Zamanlı Uygulama Uyumu**
- 🔹 **Sensör ve Aktüatör Desteği**
- 🔹 **Aktif Topluluk ve Dokümantasyon**
- 🔹 **Yüksek Güvenlik ve Performans**

---

## 🖥️ Desteklenen İşletim Sistemleri ve Gereksinimler

Projenin sağlıklı çalışabilmesi için **Ubuntu 20.04 (Focal Fossa)** veya **Ubuntu 22.04 (Jammy Jellyfish)** tavsiye edilmektedir.

Alternatif olarak:
- **macOS Monterey/Ventura** (deneysel destek)
- **Windows 10/11** (deneysel destek)

**Temel Gereksinimler:**
- [ROS2 Foxy, Galactic, Humble veya Rolling](https://docs.ros.org/en/rolling/Installation.html)
- C++ (gerekirse) ve/veya Python 3
- `rostest`, `colcon`, `rosdep` araçları
- Paket bağımlılıklarının yüklenmesi

---

## ⚡️ Kurulum Adımları

### 1. ROS2'nun Kurulması

Linux için:
```bash
# Sistem güncelleme
sudo apt update && sudo apt upgrade -y

# Gerekli temel paketler
sudo apt install curl gnupg2 lsb-release -y

# ROS2 repository anahtarlarını ekleyin (Ubuntu 22.04 örnek)
sudo apt update && sudo apt install software-properties-common -y
sudo add-apt-repository universe
sudo apt update && sudo apt install ros-humble-desktop -y

# rosdep ve diğer araçlar
sudo apt install python3-rosdep python3-colcon-common-extensions -y

# rosdep'i başlatın
sudo rosdep init
rosdep update
```

### 2. Projeyi Klonlama ve Kurma

```bash
git clone https://github.com/faikaktss/ROS2.git
cd ROS2

rosdep install --from-paths src --ignore-src -r -y

colcon build

source install/setup.bash
```

> **Not:** Farklı bir işletim sistemi kullanıyorsanız [ros.org](https://docs.ros.org) üzerindeki dökümantasyona göz atınız.

---

## 🚀 Kullanım

Bir ROS2 düğümünü başlatmak için:
```bash
ros2 run <paket_adı> <düğüm_adı>
```
Ya da başlatma dosyası ile:
```bash
ros2 launch <paket_adı> <launch_dosyası.launch.py>
```

Yardım veya detaylar için:
```bash
ros2 --help
```

---

## 🗂️ Proje Yapısı

```plaintext
src/      # Kaynak kodlar ve ROS2 paketleri
launch/   # Başlatma dosyaları
config/   # Konfigürasyon dosyaları
scripts/  # Yardımcı betikler
```

---

## 🤝 Katkıda Bulunmak İçin

1. Projeyi fork’layın.
2. Kendi branch’inizde geliştirin (`feature/özellik-adı`).
3. Değişikliklerinizi ekleyin ve commit’leyin.
4. Pull Request gönderin.

_Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına göz atın._

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasını inceleyebilirsiniz.

---

## 💬 İletişim ve Destek

Her türlü soru, görüş ve öneriniz için [faikaktss](https://github.com/faikaktss) ile iletişime geçebilirsiniz.

> **Daha fazla bilgi için:**  
> - [ROS2 Belgeleri](https://docs.ros.org)  
> - [Resmi ROS2 Dağılım Listeleri ve Platform Destekleri](https://docs.ros.org/en/rolling/Releases.html)

---

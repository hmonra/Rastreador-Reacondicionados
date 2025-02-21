# 🛒 Refurbished Product Tracker 🚀

This repository contains an automated Python bot to track and purchase REFURBISHED graphics cards from **PcComponentes**, using Selenium and Telegram notifications.

## 🚀 Features
- 🌐 Automated navigation with Selenium.
- 🔄 Automatic stock detection for specific products.
- 🛡️ Avoids products with certain restrictions (LHR, laptops, unwanted versions).
- 📩 Instant notifications via Telegram.
- 🏷️ Automatic purchases and cart management.

---

## 📋 Requirements

To run this bot, you need to have the following dependencies installed:

```bash
pip install -r requirements.txt
```

✅ **Basic requirements:**
- Python 3.x
- Google Chrome
- ChromeDriver

---

## 📄 Installation

1️⃣ **Clone this repository:**
```bash
git clone https://github.com/hmonra/rastreador-reacondicionados.git
cd rastreador-reacondicionados
```

2️⃣ **Create your virtual environment:**
```bash
python -m venv env
source env/bin/activate  # Linux & MacOS
env\Scripts\activate    # Windows
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

✅ **PC Componentes Credentials:**
- Modify the login functions in `main.py` and add your email and password.

✅ **Telegram Tokens:**
- Configure your Telegram bot tokens and chat ID to receive stock and purchase notifications.

✅ **ChromeDriver:**
- Ensure the ChromeDriver path is correctly configured on your system.

---

## ▶️ Execution

To start the bot, simply run:
```bash
python main.py
```

⚠️ The bot will open multiple Chrome windows, so make sure not to close any of them.

---

## 📬 Notifications

The bot will send automatic notifications via Telegram in the following cases:
- ✅ Product found.
- 🚀 Product added to the cart.
- 🔴 Product out of stock.

---

## 📜 License

This project is under the MIT license - feel free to use and improve it! 🚀

---

## 🤝 Contributions

Contributions are welcome! Please open an issue or a pull request if you want to improve this project. 🎉

---

## 📧 Contact

If you have any questions or suggestions, don’t hesitate to write to me!

---

## 📦 requirements.txt

```
selenium
pyautogui
```

---

✨ Thank you for trying out this bot! I hope you get your GPUs quickly and without any problems. 🚀


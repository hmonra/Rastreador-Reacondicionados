# 🛒 Rastreador de Reacondicionados 🚀

Este repositorio contiene un bot automatizado en Python para rastrear y comprar tarjetas gráficas REACONDICIONADAS en **PcComponentes**, utilizando Selenium y notificaciones de Telegram.

## 🚀 Características
- 🌐 Navegación automatizada con Selenium.
- 🔄 Detección automática de stock en productos específicos.
- 🛡️ Evita productos con ciertas restricciones (LHR, portátiles, versiones no deseadas).
- 📩 Notificaciones instantáneas a través de Telegram.
- 🏷️ Compras automáticas y gestión de carrito.

---

## 📋 Requisitos

Para ejecutar este bot, necesitas tener instaladas las siguientes dependencias:

```bash
pip install -r requirements.txt
```

✅ **Requisitos básicos:**
- Python 3.x
- Google Chrome
- ChromeDriver

---

## 📄 Instalación

1️⃣ **Clona este repositorio:**
```bash
git clone https://github.com/hmonra/rastreador-reacondicionados.git
cd rastreador-reacondicionados
```

2️⃣ **Crea tu entorno virtual:**
```bash
python -m venv env
source env/bin/activate  # Linux & MacOS
env\Scripts\activate    # Windows
```

3️⃣ **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración

✅ **Credenciales de PC Componentes:**
- Modifica las funciones de login en `main.py` y añade tu correo y contraseña.

✅ **Tokens de Telegram:**
- Configura los tokens del bot de Telegram y el chat ID para recibir notificaciones de stock y compra.

✅ **ChromeDriver:**
- Asegúrate de que la ruta del ChromeDriver esté correctamente configurada en tu sistema.

---

## ▶️ Ejecución

Para iniciar el bot, simplemente ejecuta:
```bash
python main.py
```

⚠️ El bot abrirá múltiples ventanas de Chrome, así que asegúrate de no cerrar ninguna de ellas.

---

## 📬 Notificaciones

El bot enviará notificaciones automáticas vía Telegram en los siguientes casos:
- ✅ Producto encontrado.
- 🚀 Producto añadido al carrito.
- 🔴 Producto fuera de stock.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT - ¡siéntete libre de usarlo y mejorarlo! 🚀

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request si deseas mejorar este proyecto. 🎉

---

## 📧 Contacto

Si tienes alguna pregunta o sugerencia, ¡no dudes en escribirme!

---

## 📦 requirements.txt

```
selenium
pyautogui
```

---

✨ ¡Gracias por probar este bot! Espero que consigas tus GPUs rápidamente y sin problemas. 🚀


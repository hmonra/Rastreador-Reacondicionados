# Librerias
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
import pyautogui

boton_condiciones = 'acceptConditionsCheckbox'
boton_comprar = 'sc-iqHYmW.zvotO'

# Opciones de navegación
options = webdriver.ChromeOptions()

hostname = "195.114.204.198"
port = "58542"
proxy_username = "LavgL2K3IJ"
proxy_password = "kPj8SHOM2y"

# options.add_argument('--proxy-server={}'.format(hostname + ":" + port))


def enter_proxy_auth():
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)

options.page_load_strategy = 'normal'
options.add_argument('--start')
options.add_argument('--disable-extensions')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-software-rasterizer")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--allow-insecure-localhost')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument("--incognito")
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')
options.add_argument("--force-device-scale-factor=1")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--ignore-certificate-errors")
options.add_argument("enable-features=NetworkServiceInProcess")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("disable-features=NetworkService")

options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")
# options.add_argument("user-agent=Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36")
"""
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
"""

driver = webdriver.Chrome(executable_path=r'C:\Users\er_ki\OneDrive\Escritorio\chromedriver_win32 (2)\chromedriver.exe',
                          options=options)
driver.execute_script("window.open('');")
driver.execute_script("window.open('');")
driver.execute_script("window.open('');")


# PRODUCTO QUE SE AÑADIRÁ AL CARRO PARA PODER CARGAR ENLACE SUMMARY
summary_item = 'https://www.pccomponentes.com/cart/addItem/10431340'

# HORA INICIO SCRIPT
hora_inicial = datetime.now()


# BOT "LDLC"
def telegram_bot_sendtext(bot_message):
    bot_token = 'TOKEN_BOT' # SUSTITUIR POR EL TOKEN DEL BOT
    bot_chatID = 'CHAT_ID' # SUSTITUIR POR EL ID DEL CHAT
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    driver.get(send_text)


# BOT "STOCKAUTOBUY"
def telegram_bot_sendtext2(bot_message):
    bot_token = 'TOKEN_BOT' # SUSTITUIR POR EL TOKEN DEL BOT
    bot_chatID = 'CHAT_ID' # SUSTITUIR POR EL ID DEL CHAT
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    driver.get(send_text)


def campeo():
    global cuadro_cesta, cuadro_cesta2
    driver.switch_to.window(driver.window_handles[3])
    print("Cambio pestaña y pulso botón de iniciar sesión...")
    WebDriverWait(driver, 15) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.hopIa-D'))).click()
    print("Login en PCC OK...")
    cuadro_verificacion = WebDriverWait(driver, 40) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'login-form')))
    cuadro_verificacion = cuadro_verificacion.text
    # print(cuadro_verificacion)
    if "El e-mail o la contraseña no son correctos." in cuadro_verificacion:
        print("Problema con verificación de login, reintentando...")
        login()
    else:
        print("Login aceptado...")
    cuadro_login_bis = WebDriverWait(driver, 40) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-user-menu.js-user-menu')))
    cuadro_login_bis = cuadro_login_bis.text
    print(cuadro_login_bis)
    print("Login confirmado...")
    if "USUARIO@" not in cuadro_login_bis: # SUSTITUIR POR USUARIO CON EL @ DETRÁS
        print("Detectado cierre automático de sesión, volviendo a loguear...")
        login()
    else:
        print("-- Sesión OK --")
    driver.switch_to.window(driver.window_handles[2])
    # DETERMINANDO SI ES PRODUCTO RASTRILLO O REACONDICIONADO
    driver.get(enlacerastrillo)
    WebDriverWait(driver, 40) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contenedor-principal"]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div/a'))).click()
    if driver.find_elements(By.XPATH, '//*[@id="pcc-datasheet-condition-info"]/div/div/div[2]/div/ul'):
        detalle_rastrillo = WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.XPATH, '//*[@id="pcc-datasheet-condition-info"]/div/div/div[2]/div/ul')))
        detalle_rastrillo = detalle_rastrillo.text
        print("Enlace en uso, modifico posición inicial...")
        telegram_bot_sendtext("*‼️ GPU RASTRILLO, DESCARTADA ‼️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰``` ```" + detalle_rastrillo + "``` ```" + " 🟠RASTRILLO🟠")

        # CIERRO SESION
        driver.switch_to.window(driver.window_handles[3])
        driver.get('https://www.pccomponentes.com/')
        WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
            (By.CLASS_NAME, 'c-user-menu__line.js-user-panel'))).click()
        print("Pulso cuadro login...")
        WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
            (By.CLASS_NAME, 'qa-user-login.qa-user-login-sub-6.GTM-logout'))).click()
        print("Cierro sesión...")
        # PREPARO PAGINA LOGIN
        print("Preparando página login...")
        driver.switch_to.window(driver.window_handles[3])
        # Accediendo a web para login
        print("Accediendo a página para hacer login...")
        driver.get('https://www.pccomponentes.com/login')
        time.sleep(1)
        if driver.current_url == 'https://www.pccomponentes.com/login':
            # Se hace login
            print("Introduciendo credenciales...")
            WebDriverWait(driver, 15) \
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('USUARIO') # AQUI AÑADIR USUARIO
            print("Añado correo...")
            WebDriverWait(driver, 15) \
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA') # AQUI AÑADIR CONTRASEÑA
            print("Añado contraseña...")
            time.sleep(1)
        else:
            print("Falso positivo, la cuenta sigue logueada...")
        return
    else:
        a_string = nombre_producto
        a_string = a_string.replace("á", "a")
        a_string = a_string.replace("é", "e")
        a_string = a_string.replace("í", "i")
        a_string = a_string.replace("ó", "o")
        a_string = a_string.replace("ú", "u")
        a_string = a_string.replace("--", "-")
        a_string = a_string.replace(" + ", "-")
        a_string = a_string.replace(" ", "-")
        a_string = a_string.replace("\"", "")
        a_string = a_string.replace(".", "")
        a_string = a_string.replace(" ", "")
        a_string = a_string.replace("/", "-")
        print(a_string)
        enlace_reacondicionado = ("https://www.pccomponentes.com/" + a_string + "-reacondicionado")
        a_string = enlace_reacondicionado
        a_string = a_string.replace("--", "-")
        a_string = a_string.replace("+", "")
        a_string = a_string.replace(" ", "")
        enlace_reacondicionado_final = a_string
        print(enlace_reacondicionado_final.lower())
        print("Producto futuro reacondicionado...")
        telegram_bot_sendtext("*‼️ Campeando GPU ‼️*  ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰``` ```" + " 🟢REACONDICIONADO🟢``` ```" + enlace_reacondicionado_final.lower())
        driver.get(enlace_reacondicionado_final)
        enlace_uso_final = enlace_reacondicionado_final
    codigo_articulo = WebDriverWait(driver, 40) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'codigo-articulo-pc')))
    codigo_articulo = codigo_articulo.text
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + codigo_articulo
    veces_refresco = 0
    ###
    print("Accediendo a: " + enlace_compra)
    ###
    while True:
        try:
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == 'https://www.pccomponentes.com/cart/summary':
                print("-- Página summary OK --")
            else:
                print("--Perdida página summary, creando de nuevo--")
                summary()
        except TimeoutException:
            print("")
            print("Url Time out..")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.back()
            driver.refresh()
            continue
        try:
            driver.switch_to.window(driver.window_handles[2])
            time.sleep(1.6)
            driver.get(enlace_compra)
            current_time = datetime.now().time()
            if driver.current_url == 'https://www.pccomponentes.com/cart/shopping_basket':
                cuadro_cesta2 = WebDriverWait(driver, 45) \
                .until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-crrszt.mAqxU.sc-deRBqk.kVbguc')))
                cuadro_cesta2 = cuadro_cesta2.text
                if "0" not in cuadro_cesta2:
                    print("#########                  #########")
                    print("######### STOCK ENCONTRADO #########")
                    print("####", cuadro_cesta2, "######")
                    print("#########                  #########")
                    comprar()
                    inicio()
                    break
                else:
                    veces_refresco = veces_refresco + 1
                    print("🔴 No hay stock :(      Hora:", current_time)
            else:
                cuadro_cesta = WebDriverWait(driver, 45) \
                    .until(EC.element_to_be_clickable((By.CLASS_NAME, 'h3.m-b-1')))
                cuadro_cesta = cuadro_cesta.text
                print(cuadro_cesta)
                if "0" not in cuadro_cesta:
                    print("#########                  #########")
                    print("######### STOCK ENCONTRADO #########")
                    print("####", cuadro_cesta, "######")
                    print("#########                  #########")
                    comprar()
                    inicio()
                    break
                else:
                    veces_refresco = veces_refresco + 1
                    print("🔴 No hay stock :(      Hora:", current_time)
        except TimeoutException:
            print("")
            print("Url Time out..")
            driver.delete_all_cookies()
            print("Borrando todas las cookies...")
            print("Volviendo a escanear...")
            print("")
            driver.switch_to.window(driver.window_handles[0])
            driver.get(enlace_compra)
            continue
        if veces_refresco == 43:
            print("Refrescado enlace 2 minutos, no aparece en stock, paso a siguiente enlace...")
            telegram_bot_sendtext("*❌ Refrescado enlace 2 minutos, no aparece stock ❌* ``` ```" + nombre_producto + " " + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")

            # CIERRO SESION
            driver.switch_to.window(driver.window_handles[3])
            driver.get('https://www.pccomponentes.com/')
            WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-user-menu__line.js-user-panel'))).click()
            print("Pulso cuadro login...")
            WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'qa-user-login.qa-user-login-sub-6.GTM-logout'))).click()
            print("Cierro sesión...")

            # PREPARO PAGINA LOGIN
            print("Preparando página login...")
            driver.switch_to.window(driver.window_handles[3])
            # Accediendo a web para login
            print("Accediendo a página para hacer login...")
            driver.get('https://www.pccomponentes.com/login')
            time.sleep(1)
            if driver.current_url == 'https://www.pccomponentes.com/login':
                # Se hace login
                print("Introduciendo credenciales...")
                WebDriverWait(driver, 15) \
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('USUARIO') # AQUI AÑADIR USUARIO
                print("Añado correo...")
                WebDriverWait(driver, 15) \
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA') # AQUI AÑADIR CONTRASEÑA
                print("Añado contraseña...")
                time.sleep(1)
            else:
                print("Falso positivo, la cuenta sigue logueada...")
            break
        else:
            print("Refrescado enlace: ", veces_refresco)


def comprar():
    print(nombre_producto)
    print("Paso a pestaña summary...")
    driver.switch_to.window(driver.window_handles[1])
    # Botón pagar y finalizar
    print("Pulsando botón de pagar y finalizar...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, boton_comprar))).click()
    print("Pulsado botón de pagar y finalizar...")
    payment_time = datetime.now().time()
    time.sleep(30)
    if driver.current_url == 'https://www.pccomponentes.com/cart/':
        telegram_bot_sendtext2("*❌ Intento de compra realizado, sin stock ❌* ``` ```" + nombre_producto + " " + enlacerastrillo)
        print("Compra no realizada, el stock ha volado... :( ", payment_time)
    else:
        if driver.current_url == 'https://www.pccomponentes.com/cart/summary':
            telegram_bot_sendtext2("*❌ Intento de compra realizado ❌* ``` ```" + nombre_producto + " " + enlacerastrillo)
            print("Compra no realizada, algo ha fallado... :( ", payment_time)
        else:
            telegram_bot_sendtext2("*✅ Compra realizada ✅* ``` ```" + nombre_producto + " " + enlacerastrillo)
            print("Compra finalizada :D    ", payment_time)


def login():
    # Borrando cookies
    driver.delete_all_cookies()
    print("Borrando todas las cookies...")
    # Accediendo a web para login
    print("Accediendo a página para hacer login...")
    driver.get('https://www.pccomponentes.com/login')
    time.sleep(1)
    if driver.current_url == 'https://www.pccomponentes.com/login':
        # Se hace login
        print("Introduciendo credenciales...")
        WebDriverWait(driver, 15) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('USUARIO') # AQUI AÑADIR USUARIO
        WebDriverWait(driver, 15) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA') # AQUI AÑADIR CONTRASEÑA
        time.sleep(1)
        WebDriverWait(driver, 15) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.hopIa-D'))).click()
        print("Login en PCC OK...")
        time.sleep(1)
        cuadro_verificacion = WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'login-form')))
        cuadro_verificacion = cuadro_verificacion.text
        # print(cuadro_verificacion)
        if "El e-mail o la contraseña no son correctos." in cuadro_verificacion:
            print("Problema con verificación de login, reintentando...")
            login()
        else:
            print("Login confirmado...")

    else:
        print("Falso positivo, la cuenta sigue logueada...")


def summary():
    print("Login para precargar página summary...")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    login()
    time.sleep(2)
    print("Añado un producto para poder acceder al enlace summary...")
    driver.get(summary_item)
    cuadro_summary_item = WebDriverWait(driver, 30) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-ha-dWBB.cucndA')))
    cuadro_summary_item = cuadro_summary_item.text
    print(cuadro_summary_item)
    time.sleep(1)
    print(summary_item)
    print("Cambio pestaña y accedo a enlace summary...")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.pccomponentes.com/cart/summary')
    time.sleep(2)
    # Botón entiendo y acepto las condiciones
    print("Cargada página summary...")
    print("Dejo pulsado botón de acepto las condiciones...")
    time.sleep(15)
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, boton_condiciones))).click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    print("Vacío el carrito...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'GTM-carrito-vaciarcarrito'))).click()
    time.sleep(1)


def inicio():
    # CARGO PAGINA SUMMARY
    print("Login para precargar página summary...")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    login()
    time.sleep(2)
    print("Añado un producto para poder acceder al enlace summary...")
    driver.get(summary_item)
    cuadro_summary_item = WebDriverWait(driver, 30) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-ha-dWBB.cucndA')))
    cuadro_summary_item = cuadro_summary_item.text
    print(cuadro_summary_item)
    time.sleep(1)
    print(summary_item)
    print("Cambio pestaña y accedo a enlace summary...")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.pccomponentes.com/cart/summary')
    time.sleep(2)
    # Botón entiendo y acepto las condiciones
    print("Cargada página summary...")
    print("Dejo pulsado botón de acepto las condiciones...")
    time.sleep(15)
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, boton_condiciones))).click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    print("Vacío el carrito...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.dJJQhN'))).click()
    time.sleep(1)

    # CIERRO SESION
    driver.switch_to.window(driver.window_handles[3])
    driver.get('https://www.pccomponentes.com/')
    WebDriverWait(driver, 40) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-user-menu__line.js-user-panel'))).click()
    print("Pulso cuadro login...")
    WebDriverWait(driver, 40) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'qa-user-login.qa-user-login-sub-6.GTM-logout'))).click()
    print("Cierro sesión...")

    # PREPARO PAGINA LOGIN
    print("Preparando página login...")
    driver.switch_to.window(driver.window_handles[3])
    # Accediendo a web para login
    print("Accediendo a página para hacer login...")
    driver.get('https://www.pccomponentes.com/login')
    time.sleep(1)
    if driver.current_url == 'https://www.pccomponentes.com/login':
        # Se hace login
        print("Introduciendo credenciales...")
        WebDriverWait(driver, 15) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('USUARIO') # AQUI AÑADIR USUARIO
        print("Añado correo...")
        WebDriverWait(driver, 15) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA') # AQUI AÑADIR CONTRASEÑA
        print("Añado contraseña...")
        time.sleep(1)
    else:
        print("Falso positivo, la cuenta sigue logueada...")


alcance = 5
pos_actual = 1799025
pos_ini = 1799025

inicio()

while True:
    try:
        driver.switch_to.window(driver.window_handles[0])
        enlacerastrillo = ("https://www.pccomponentes.com/rastrillo/" + pos_actual.__str__())
        time.sleep(1.5)
        driver.get(enlacerastrillo)
        print(enlacerastrillo)
    except TimeoutException:
        print("")
        print("Url Time out..")
        driver.delete_all_cookies()
        print("Borrando todas las cookies...")
        print("Volviendo a escanear...")
        print("")
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        continue
    try:
        print("-- Posición inicial ", pos_ini, "--")
        print("Script corriendo desde: ", hora_inicial)
        contenedor_principal = WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'contenedor-principal')))
        contenedor_principal = contenedor_principal.text
    except TimeoutException:
        print("")
        print("Url Time out..")
        print("URL: https://www.pccomponentes.com/premium")
        driver.delete_all_cookies()
        print("Borrando todas las cookies...")
        print("Volviendo a escanear...")
        print("")
        driver.switch_to.window(driver.window_handles[0])
        driver.back()
        driver.refresh()
        continue
    if "Código de error 404" in contenedor_principal:
        current_time = datetime.now().time()
        print("Enlace sin asignar, escaneando... ", current_time)
        pos_actual = pos_actual + 1
    else:
        cuadro_categoria = WebDriverWait(driver, 40) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
            (By.CLASS_NAME, 'navegacion-secundaria__migas-de-pan')))
        cuadro_categoria = cuadro_categoria.text
        print(cuadro_categoria)
        if "Tarjetas Gráficas" in cuadro_categoria:
            nombre_producto = WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'h4')))
            nombre_producto = nombre_producto.text
            precio_producto = WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'precio-main')))
            precio_producto = precio_producto.text
            print(nombre_producto)
            if '3070' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'LHR' in nombre_producto or 'Rev' in nombre_producto or '2.0' in nombre_producto or '3.0' in nombre_producto or 'Ti' in nombre_producto or 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext("*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext("*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if '1660 SUPER' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext(
                        "*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext("*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if '3060 Ti' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'LHR' in nombre_producto or 'Rev' in nombre_producto or '2.0' in nombre_producto or '3.0' in nombre_producto or 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext(
                        "*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext("*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if '3080' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'LHR' in nombre_producto or 'Rev' in nombre_producto or '2.0' in nombre_producto or '3.0' in nombre_producto or 'Ti' in nombre_producto or 'Ryzen' in nombre_producto or 'Intel' in nombre_producto or '12GB' in nombre_producto or 'V2' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext("*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext("*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if 'RX 5700' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext("*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext(
                        "*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if 'RX 5600' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext(
                        "*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext("*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if 'RTX 2060' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'LHR' in nombre_producto or '12GB' in nombre_producto or 'Rev' in nombre_producto or '2.0' in nombre_producto or '3.0' in nombre_producto or 'Ti' in nombre_producto or 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext(
                        "*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext(
                        "*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
            if 'RX 580' in nombre_producto:
                print("### GPU ENCONTRADA ###")
                if 'Ryzen' in nombre_producto or 'Intel' in nombre_producto:
                    print("GPU con LHR, descartada...")
                    telegram_bot_sendtext(
                        "*⚠️ Encontrado portatil, o GPU con LHR, compra descartada ⚠️* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                else:
                    telegram_bot_sendtext(
                        "*🔍 Encontrada GPU, Empiezo a campearla 🔎* ``` ```" + nombre_producto + " " + enlacerastrillo + " " + "``` ``` 💰 Precio: " + precio_producto + " 💰")
                    campeo()
        else:
            print("Producto no es una GPU, sigo escaneando...")
        pos_ini = pos_actual + 1
        pos_actual = pos_ini
    if pos_actual > pos_ini + alcance:
        print("Pasado rango de alcance, reiniciando...")
        pos_actual = pos_ini

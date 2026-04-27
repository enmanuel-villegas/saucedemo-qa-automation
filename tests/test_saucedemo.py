# ============================================================
# QA Portfolio Project — Saucedemo.com
# Automatizacion con Python + Selenium WebDriver
# Autor: [Tu Nombre]
# Fecha: Abril 2025
# ============================================================

import unittest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ── CONFIGURACION GLOBAL ─────────────────────────────────────
BASE_URL        = "https://www.saucedemo.com"
USER_VALID      = "standard_user"
PASS_VALID      = "secret_sauce"
USER_INVALID    = "usuario_invalido"
PASS_INVALID    = "contrasena_incorrecta"
SCREENSHOTS_DIR = "screenshots"

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SCREENSHOTS_DIR}/FAIL_{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"  Screenshot guardado: {filename}")


class SaucedemoTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "safebrowsing.enabled": False
        })
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def do_login(self, username=USER_VALID, password=PASS_VALID):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def test_01_login_exitoso(self):
        """TC-001: Login exitoso con credenciales validas."""
        print("\n> TEST 01: Login exitoso con credenciales validas")
        try:
            self.do_login(USER_VALID, PASS_VALID)
            self.assertIn("inventory", self.driver.current_url,
                "ERROR: No se redirigió al catalogo.")
            menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
            self.assertTrue(menu_btn.is_displayed(),
                "ERROR: Menu hamburguesa no visible.")
            cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            self.assertTrue(cart_icon.is_displayed(),
                "ERROR: Icono del carrito no visible.")
            print("  PASS - Login exitoso. Header visible.")
        except AssertionError as e:
            take_screenshot(self.driver, "test_01")
            raise e

    def test_02_login_fallido(self):
        """TC-002: Login fallido con credenciales invalidas."""
        print("\n> TEST 02: Login fallido con credenciales invalidas")
        try:
            self.do_login(USER_INVALID, PASS_INVALID)
            self.assertNotIn("inventory", self.driver.current_url,
                "ERROR: El sistema permitio acceso invalido.")
            error_msg = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            self.assertIn("Username and password do not match", error_msg.text,
                "ERROR: Mensaje de error incorrecto.")
            print("  PASS - Mensaje de error visible correctamente.")
        except AssertionError as e:
            take_screenshot(self.driver, "test_02")
            raise e

    def test_03_agregar_producto_carrito(self):
        """TC-013: Agregar un producto al carrito."""
        print("\n> TEST 03: Agregar producto al carrito")
        try:
            self.do_login()
            add_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".inventory_item:first-child button")
                )
            )
            add_btn.click()
            badge = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            self.assertEqual(badge.text, "1",
                f"ERROR: Badge muestra '{badge.text}' en lugar de '1'.")
            print("  PASS - Producto agregado. Badge muestra 1.")
        except AssertionError as e:
            take_screenshot(self.driver, "test_03")
            raise e

    def test_04_flujo_checkout_completo(self):
        """TC-018 al TC-022: Flujo completo de checkout."""
        print("\n> TEST 04: Flujo completo de checkout")
        try:
            self.do_login()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".inventory_item:first-child button")
                )
            ).click()
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            self.assertIn("cart", self.driver.current_url,
                "ERROR: No se navego al carrito.")
            self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
            self.assertIn("checkout-step-one", self.driver.current_url,
                "ERROR: No se navego al formulario.")
            self.driver.find_element(By.ID, "first-name").send_keys("Juan")
            self.driver.find_element(By.ID, "last-name").send_keys("Perez")
            self.driver.find_element(By.ID, "postal-code").send_keys("10101")
            self.driver.find_element(By.ID, "continue").click()
            self.assertIn("checkout-step-two", self.driver.current_url,
                "ERROR: No se navego al resumen.")
            self.driver.find_element(By.ID, "finish").click()
            confirm_header = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            self.assertIn("Thank you", confirm_header.text,
                "ERROR: Mensaje de confirmacion incorrecto.")
            print(f"  PASS - Checkout completo. Mensaje: {confirm_header.text}")
        except AssertionError as e:
            take_screenshot(self.driver, "test_04")
            raise e

    def test_05_logout(self):
        """TC-005: Logout exitoso del sistema."""
        print("\n> TEST 05: Logout del sistema")
        try:
            self.do_login()
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
            ).click()
            logout_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            )
            logout_btn.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
            self.assertIn(
                self.driver.current_url,
                [BASE_URL + "/", BASE_URL],
                "ERROR: No se redirigió al login."
            )
            username_field = self.driver.find_element(By.ID, "user-name")
            self.assertEqual(username_field.get_attribute("value"), "",
                "ERROR: Campo username no vacio despues del logout.")
            print("  PASS - Logout exitoso. Redirigido a login.")
        except AssertionError as e:
            take_screenshot(self.driver, "test_05")
            raise e


if __name__ == "__main__":
    print("=" * 60)
    print("  QA AUTOMATION - Saucedemo.com")
    print("  Python + Selenium WebDriver")
    print("=" * 60)
    unittest.main(verbosity=2)
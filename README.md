# 🧪 Saucedemo QA Portfolio Project

**Manual Testing + Selenium Automation | Enmanuel Villegas Duarte**

---

## 📌 Descripción

Proyecto de QA completo sobre la aplicación web [Saucedemo.com](https://www.saucedemo.com), desarrollado como portfolio profesional demostrando habilidades de **QA Manual** y **automatización con Selenium**.

Este proyecto replica el flujo de trabajo real de un QA Engineer junior: planificación, diseño de casos de prueba, ejecución manual, reporte de bugs y automatización de casos críticos.

---

## 🗂️ Estructura del Repositorio

```
saucedemo-qa-automation/
├── docs/
│   ├── TestPlan_Saucedemo.docx       # Test Plan completo
│   └── CasosDePrueba_Saucedemo.xlsx  # Casos de prueba + Bug Reports + Dashboard
├── tests/
│   └── test_saucedemo.py             # Suite de automatización con Selenium
├── evidencias/
│   ├── BUG-001.png
│   ├── BUG-002.png
│   └── ...                           # Screenshots de bugs encontrados
├── screenshots/                      # Capturas automáticas en fallos de automation
├── requirements.txt
└── README.md
```

---

## 📋 Fase 1 — QA Manual

### Aplicación bajo prueba
| Campo | Detalle |
|---|---|
| URL | https://www.saucedemo.com |
| Tipo | E-commerce web application |
| Navegador | Google Chrome 124+ |
| Usuario de prueba principal | standard_user / secret_sauce |

### Artefactos generados

**Test Plan** (`docs/TestPlan_Saucedemo.docx`)
- Objetivo, alcance y tipos de prueba definidos
- Criterios de entrada, salida y suspensión
- Ambiente de pruebas, riesgos y cronograma
- Clasificación de severidad de bugs (S1-S4)

**Casos de Prueba** (`docs/CasosDePrueba_Saucedemo.xlsx`)
- 27 casos de prueba estructurados en 5 módulos
- Campos: ID, precondiciones, pasos, resultado esperado, resultado real, estado, severidad, prioridad
- Dashboard automático con métricas de ejecución

### Resumen de ejecución — standard_user

| Módulo | Casos | Resultado |
|---|---|---|
| M-01 Autenticación | 6 | ✅ 6 Pass |
| M-02 Catálogo de Productos | 6 | ✅ 6 Pass |
| M-03 Carrito de Compras | 5 | ✅ 5 Pass |
| M-04 Checkout | 7 | ✅ 7 Pass |
| M-05 Navegación General | 3 | ⚠️ 2 Pass / 1 Fail |
| **Total** | **27** | **✅ 26 Pass / ❌ 1 Fail** |

### Bug Reports

**Bug encontrado con standard_user:**

| Bug ID | Título | Severidad | Estado |
|---|---|---|---|
| BUG-008 | Botones no regresan a 'Add to cart' después de Reset App State | Minor | Abierto |

**Bugs encontrados en prueba exploratoria con problem_user:**

| Bug ID | Título | Severidad | Estado |
|---|---|---|---|
| BUG-001 | Los filtros no funcionan correctamente con problem_user | Major | Abierto |
| BUG-002 | Imagen incorrecta en productos con problem_user | Minor | Abierto |
| BUG-003 | Botón 'Add to cart' no responde para algunos productos | Critical | Abierto |
| BUG-004 | Redirección incorrecta en el detalle de productos | Critical | Abierto |
| BUG-005 | Botón 'Remove' no funciona en la página de catálogo | Critical | Abierto |
| BUG-006 | El campo 'Last Name' sobrescribe el valor de 'First Name' | Critical | Abierto |
| BUG-007 | Enlace 'About' no funciona correctamente | Media | Abierto |

---

## ⚙️ Fase 2 — Automatización con Selenium

### Tecnologías
- **Python 3.14**
- **Selenium WebDriver 4.x**
- **unittest** (framework de testing)

### Tests automatizados

| Test | Descripción | TC Relacionado |
|---|---|---|
| test_01_login_exitoso | Verifica redirección al catálogo con credenciales válidas | TC-001 |
| test_02_login_fallido | Verifica mensaje de error con credenciales inválidas | TC-002 |
| test_03_agregar_producto_carrito | Verifica badge del carrito al agregar producto | TC-013 |
| test_04_flujo_checkout_completo | Flujo completo: login → producto → checkout → confirmación | TC-018 al TC-022 |
| test_05_logout | Verifica cierre de sesión y redirección al login | TC-005 |

### Resultado de la ejecución

```
============================================================
  QA AUTOMATION - Saucedemo.com
  Python + Selenium WebDriver
============================================================

> TEST 01: Login exitoso con credenciales validas
  PASS - Login exitoso. Header visible.
> TEST 02: Login fallido con credenciales invalidas
  PASS - Mensaje de error visible correctamente.
> TEST 03: Agregar producto al carrito
  PASS - Producto agregado. Badge muestra 1.
> TEST 04: Flujo completo de checkout
  PASS - Checkout completo. Mensaje: Thank you for your order!
> TEST 05: Logout del sistema
  PASS - Logout exitoso. Redirigido a login.

Ran 5 tests in ~48s — OK (5/5)
```

---

## 🚀 Cómo ejecutar los tests

### 1. Clonar el repositorio
```bash
git clone https://github.com/enmanuelvillegas/saucedemo-qa-automation.git
cd saucedemo-qa-automation
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

### 3. Ejecutar los tests
```bash
python tests/test_saucedemo.py
```

> Chrome se abre automáticamente y ejecuta los 5 tests. Si algún test falla, se guarda un screenshot automático en la carpeta `screenshots/`.

---

## 🛠️ Herramientas utilizadas

| Herramienta | Uso |
|---|---|
| Selenium WebDriver | Automatización de pruebas |
| Python unittest | Framework de testing |
| Google Chrome | Navegador de pruebas |
| Microsoft Excel | Casos de prueba y Bug Reports |
| Microsoft Word | Test Plan |
| GitHub | Control de versiones y portfolio |

---

## 👤 Autor

**Enmanuel Villegas Duarte**   
📧 [enmanuel.villegas.duarte@outlook.com]
---

*Proyecto desarrollado como proyecto personal - QA Portfolio.*

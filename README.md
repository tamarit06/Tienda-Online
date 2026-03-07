# 🛍️ Tienda Online con Django

Aplicación web de **tienda online** desarrollada con **Python y Django**, que permite mostrar productos con imágenes, precios y gestionarlos fácilmente desde un panel de administración.

Este proyecto fue creado como práctica de **desarrollo backend y despliegue de aplicaciones web**, incluyendo la publicación del proyecto en un servidor.

---

# 🚀 Demo

🌐 Sitio web:
https://tamarit06.pythonanywhere.com

---

# 📸 Características

* Visualización de productos en la página principal
* Imágenes, nombres y precios de productos
* Carrito de compras en el frontend
* Panel de administración para gestionar productos
* Subida de imágenes de productos
* Archivos estáticos (CSS, JavaScript)
* Despliegue del proyecto en producción

---

# 🛠️ Tecnologías utilizadas

* **Python**
* **Django**
* **HTML**
* **CSS**
* **JavaScript**
* **SQLite**

---

# 📂 Estructura del proyecto

```
Tienda-Online
│
├── backend
│   ├── backend/        # configuración principal de Django
│   ├── tienda/         # aplicación de productos
│   ├── static/         # archivos estáticos (css, js)
│   ├── staticfiles/    # archivos generados para producción
│   └── manage.py
│
└── README.md
```

---

# ⚙️ Instalación

### 1️⃣ Clonar el repositorio

```
git clone https://github.com/TU-USUARIO/Tienda-Online.git
```

### 2️⃣ Entrar al proyecto

```
cd Tienda-Online/backend
```

### 3️⃣ Crear entorno virtual

```
python -m venv venv
```

### 4️⃣ Activar entorno virtual

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

### 5️⃣ Instalar dependencias

```
pip install django pillow
```

### 6️⃣ Aplicar migraciones

```
python manage.py migrate
```

### 7️⃣ Crear superusuario

```
python manage.py createsuperuser
```

### 8️⃣ Ejecutar servidor

```
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000
```

---

# 🔑 Panel de administración

Django incluye un panel de administración que permite gestionar los productos.

Acceso:

```
/admin
```

Desde ahí se pueden:

* crear productos
* editar productos
* subir imágenes
* eliminar productos

---

# ☁️ Despliegue

El proyecto fue desplegado en **PythonAnywhere**.

Pasos principales para el despliegue:

* subir el proyecto desde GitHub
* configurar entorno virtual
* instalar dependencias
* ejecutar migraciones
* configurar WSGI
* ejecutar `collectstatic`
* configurar archivos estáticos

---

# 📚 Objetivo del proyecto

Este proyecto fue desarrollado para practicar:

* desarrollo backend con **Django**
* manejo de **modelos y base de datos**
* configuración de **archivos estáticos**
* despliegue de aplicaciones web

---

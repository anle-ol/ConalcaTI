# Plataforma CONALCA - Sistema de Gestión de Viajes

Sistema web interno para la gestión de registros de viajes de la empresa de logística CONALCA. Desarrollado con Django y Tailwind CSS, permite la validación y análisis de viajes de vehículos.

## Características

- ✅ Gestión completa de registros de viajes
- ✅ Sistema de autenticación basado en usuarios de Django
- ✅ Filtros avanzados (Placa, Rango de fechas, Estado de validación)
- ✅ Validación dinámica sin recargar página (AJAX)
- ✅ Exportación de datos en formato CSV y Excel
- ✅ Interfaz responsive con colores corporativos
- ✅ Ordenamiento automático por fecha de inicio (descendente)

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd ConalcaTI
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración Inicial

### 1. Ejecutar migraciones

Crear las tablas en la base de datos SQLite:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario y contraseña.

### 3. Generar datos de prueba (opcional)

Para generar 50 registros aleatorios de prueba coherentes con el sector logístico colombiano:

```bash
python manage.py generar_datos_prueba
```

Este comando creará registros con:
- Placas en formato colombiano (ABC-123)
- Clientes colombianos realistas
- Fechas en los últimos 90 días
- Números de entregas y facturación realistas
- Observaciones variadas

## Ejecutar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Uso del Sistema

### Iniciar Sesión

1. Accede a `http://127.0.0.1:8000/login/`
2. Ingresa las credenciales del usuario creado con `createsuperuser`
3. Serás redirigido a la lista principal de viajes

### Gestión de Viajes

#### Filtros Disponibles

- **Placa**: Búsqueda parcial por número de placa
- **Fecha Desde / Hasta**: Rango de fechas para filtrar por fecha de inicio
- **Estado de Validación**: Filtrar por Validado, No Validado o Todos

#### Validar Viajes

- Usa el switch en la columna "Validado" para marcar/desmarcar viajes
- La actualización se realiza sin recargar la página (AJAX)

#### Exportar Datos

1. Aplica los filtros deseados
2. Haz clic en "Exportar CSV" o "Exportar Excel"
3. El archivo descargado incluirá solo los datos filtrados
4. El archivo no incluye el campo "observación" según los requerimientos

## Integración con Power BI

### Paso 1: Exportar Datos desde la Plataforma

1. Accede a la plataforma web
2. Aplica los filtros necesarios para tu análisis
3. Haz clic en "Exportar Excel" o "Exportar CSV"
4. Guarda el archivo en una ubicación accesible

### Paso 2: Cargar Datos en Power BI

1. Abre Power BI Desktop
2. Selecciona **Obtener datos** > **Archivo** > **Excel** (o **Texto/CSV**)
3. Navega y selecciona el archivo exportado
4. En la ventana de vista previa, selecciona la hoja/tabla con los datos
5. Haz clic en **Cargar** o **Transformar datos** si necesitas limpiar los datos

### Paso 3: Crear Visualizaciones

#### Gráfico de Barras - Vehículos por Día

1. En el panel de **Visualizaciones**, selecciona el gráfico de barras
2. Arrastra el campo **Fecha Inicio** al eje X (o usa una columna calculada con solo la fecha)
3. Arrastra el campo **Código** o **Placa** al eje Y (o usa un conteo de registros)
4. Ajusta el formato según tus necesidades

**Nota:** Si necesitas agrupar por día, crea una columna calculada:
```DAX
Fecha = DATE(YEAR([Fecha Inicio]), MONTH([Fecha Inicio]), DAY([Fecha Inicio]))
```

#### Tarjetas de Entregas y Facturación

1. Selecciona el visual **Tarjeta** en el panel de visualizaciones
2. Para la tarjeta de entregas:
   - Arrastra el campo **Número Entregas** y selecciona **Suma** o **Promedio**
3. Para la tarjeta de facturación:
   - Arrastra el campo **Facturación** y selecciona **Suma** o **Promedio**
4. Personaliza el formato (moneda, decimales, etc.)

### Paso 4: Crear un Dashboard

1. Organiza tus visualizaciones en una página
2. Añade títulos y descripciones
3. Usa filtros de página para interactividad
4. Publica el dashboard en Power BI Service si es necesario

## Estructura del Proyecto

```
conalca_prueba/
├── conalca_project/          # Configuración del proyecto Django
│   ├── settings.py           # Configuración principal
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuración WSGI
│   └── asgi.py               # Configuración ASGI
├── viajes/                   # Aplicación principal
│   ├── models.py             # Modelo Vehiculo
│   ├── views.py              # Vistas (lista, login, exportación)
│   ├── urls.py               # URLs de la aplicación
│   ├── forms.py              # Formularios
│   ├── admin.py              # Configuración del admin
│   └── management/
│       └── commands/
│           └── generar_datos_prueba.py  # Script de datos de prueba
├── templates/                # Plantillas HTML
│   ├── base.html             # Layout base
│   ├── registration/
│   │   └── login.html        # Página de login
│   └── viajes/
│       └── lista.html        # Lista principal de viajes
├── static/                   # Archivos estáticos
│   └── viajes/
│       └── js/
│           └── main.js       # JavaScript para validación
├── manage.py                 # Script de gestión Django
├── requirements.txt          # Dependencias del proyecto
└── README.md                # Este archivo
```

## Colores Corporativos

- **Naranja Principal**: `#FF7900` - Usado para botones de acción y elementos destacados
- **Gris Oscuro**: `#333333` - Usado para textos y navegación

## Tecnologías Utilizadas

- **Backend**: Django 4.2+
- **Base de Datos**: SQLite
- **Frontend**: Tailwind CSS (CDN)
- **Exportación**: openpyxl (Excel), csv nativo (CSV)
- **JavaScript**: Fetch API para AJAX

## Notas Importantes

- El campo "observación" no se muestra en la tabla principal, pero está disponible en el modelo
- La tabla se ordena automáticamente por fecha de inicio (más recientes primero)
- Todos los datos exportados respetan los filtros aplicados en la vista
- El sistema requiere autenticación para acceder a las funcionalidades

## Solución de Problemas

### Error al ejecutar migraciones

Asegúrate de estar en el directorio correcto y de tener Django instalado:
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Error 404 al acceder a las URLs

Verifica que el servidor esté corriendo y que estés usando la URL correcta:
```bash
python manage.py runserver
```

### Problemas con la exportación Excel

Asegúrate de tener `openpyxl` instalado:
```bash
pip install openpyxl
```

## Soporte

Para más información o soporte, contacta al equipo de desarrollo.

---

**Desarrollado para CONALCA** - Sistema de Gestión de Viajes

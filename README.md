# Descargador de Reportes Bancarios ASFI

Este script en Python está diseñado para descargar automáticamente reportes bancarios del sistema ASFI (Autoridad de Supervisión del Sistema Financiero). Permite obtener una variedad de informes relacionados con el desempeño financiero de diversas entidades bancarias.

## Requisitos

Asegúrate de tener instalada la librería `requests`. Puedes instalarla usando el siguiente comando:

```bash
pip install requests
```
## Uso
Ejecuta el script proporcionado en tu entorno de Python.
Ingresa el año para el cual deseas obtener los reportes (por ejemplo, 2023).
El script creará una carpeta llamada reportes en la ubicación actual y subcarpetas para cada mes y tipo de reporte.
Descargará automáticamente los archivos ZIP correspondientes a los reportes desde el sitio web de ASFI y los almacenará en las carpetas adecuadas.

## Notas
El script utiliza nombres predefinidos para los tipos de reportes y los meses del año.
Los reportes se descargarán en formato ZIP y se organizarán en la estructura de carpetas mencionada anteriormente.
Asegúrate de tener una conexión a Internet activa mientras se ejecuta el script para que pueda acceder y descargar los archivos desde el sitio web de ASFI.

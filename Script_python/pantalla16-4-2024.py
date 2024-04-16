import csv
import http.server
import os
import random
import socketserver
import webbrowser

# Nombre del archivo de texto
nomarxiu = 'S30-SOW1092.TXT'
# Delimitador del archivo CSV
cardelimitador = ';'

# Lista de fondos disponibles
opciones_fondos = ['Wallpaper3_1920x1080.png', 'Wallpaper5_1920x1080.png', 'Wallpaper7_1920x1080.png']

# Seleccionar aleatoriamente un fondo de la lista
fondo_seleccionado = random.choice(opciones_fondos)

# Estilos CSS personalizables
css_styles = f"""
<style>
    body {{
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        color: white;
        background-image: url('{fondo_seleccionado}');
        background-size: cover;
        background-repeat: repeat; /* Cambiado a 'repeat' */
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100vh;
    }}
    table {{
        border-collapse: collapse;
        width: WIDTH%;
        max-width: 95%;
        border-radius: 20px;
        overflow: hidden;
        table-layout: auto;
    }}
    th, td {{
        border: 1px solid #fff;
        padding: 12px;
        text-align: left;
        font-size: 30px;
        font-family: "Arial", sans-serif;
        font-weight: bold;
        color: #FFA500;
    }}
    th {{
        background-color: #333;
    }}
    tr:nth-child(even) {{
        background-color: rgba(255, 255, 255, 0.2);
    }}
    tr:hover {{
        background-color: rgba(255, 255, 255, 0.3);
    }}
    .message {{
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }}
    #fixed-header {{
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #333;
        padding: 10px 0;
        text-align: center;
        z-index: 1000; /* Asegura que el encabezado fijo esté encima de la tabla desplazable */
    }}
    #scrolling-table {{
        margin-top: 100px; /* Espacio entre el encabezado fijo y la tabla desplazable */
        overflow-y: auto;
        max-height: calc(100vh - 100px); /* Altura máxima para que la tabla sea desplazable */
        width: 100%;
    }}
</style>
"""

# Función para cargar el contenido del archivo CSV y generar el HTML correspondiente
def generar_html():
    rows_html = []
    c = 0
    with open(nomarxiu, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=cardelimitador)
        for i, row in enumerate(csv_reader):
            if i == 0:  # Ignorar la primera línea del archivo CSV
                continue
            # Formatear la fila como una fila de una tabla HTML
            row_html = '<tr>' + ''.join([f'<td>{cell}</td>' for cell in row]) + '</tr>'
            rows_html.append(row_html)
            c += 1
    return rows_html, c

# Generar el código HTML completo
def generar_codigo_html():
    rows_html, c = generar_html()
    contenido_html = ''.join(rows_html)
    fixed_header_html = """
    <div id="fixed-header">
        <p>Estado 51 JOB pendientes de embozado</p>
        <p>FECHA, NOMBRE JOB, NRO. EXTENSION, DESCRIPCION, TIPO PROCESO, CANT. TARJETAS, ESTADO</p>
        <p>Tablero de visualización de procesos de embozado</p>
        <p>63 archivos pendiente de embozado</p>
    </div>
    """
    html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>FISERV</title>
    {css_styles.replace('WIDTH', '80').replace('FONT_SIZE', '18')}
</head>
<body>
{fixed_header_html}
<div id="scrolling-table">
    <table>
        <thead>
            <tr>
                <th>FECHA</th>
                <th>NOMBRE JOB</th>
                <th>NRO. EXTENSION</th>
                <th>DESCRIPCION</th>
                <th>TIPO PROCESO</th>
                <th>CANT. TARJETAS</th>
                <th>ESTADO</th>
            </tr>
        </thead>
        <tbody>
            {contenido_html}
        </tbody>
    </table>
</div>
<div style="text-align: center; margin-top: 20px;">
    <p>{c} archivos pendientes de embozado</p>
    <p>EMVlab 2.0</p>
    <p>Estado 51 JOB pendientes de Embozado</p>
</div>
</body>
</html>
"""
    return html_code

# Guardar el código HTML en un archivo local
def guardar_html():
    output_file_path = 'output.html'
    with open(output_file_path, 'w') as html_file:
        html_file.write(generar_codigo_html())
    return output_file_path

# Abrir el archivo HTML generado en el navegador web predeterminado
def abrir_navegador(file_path):
    webbrowser.open(f'http://localhost:8000/{file_path}')

# Configurar el servidor web
def iniciar_servidor():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Servidor iniciado en el puerto", PORT)
        print(f"Puedes ver el archivo HTML en http://localhost:{PORT}/output.html")
        httpd.serve_forever()

# Generar y guardar el HTML, luego abrirlo en el navegador y iniciar el servidor
output_file_path = guardar_html()
abrir_navegador(output_file_path)
iniciar_servidor()

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
css_styles = """
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        color: white;
        background-image: url('FONDO');
        background-size: cover;
        display: flex;
        flex-direction: column; /* Alinear elementos en columna */
        align-items: center; /* Centrar elementos horizontalmente */
    }
    table {
        border-collapse: collapse;
        width: WIDTH%;
        max-width: 95%; /* Cambiar según se desee */
        border-radius: 20px;
        overflow: hidden;
        table-layout: auto; /* Texto se ajusta automáticamente al tamaño de la tabla */
    }
    th, td {
        border: 1px solid #fff;
        padding: 12px;
        text-align: left;
        font-size: 30px; /* Cambiar el tamaño de la fuente a 20 píxeles */
        font-family: "Arial", sans-serif; /* Cambiar la fuente a Arial */
        font-weight: bold; /* Hacer el texto en negrita */
        color: #FFFFFF; /* Cambiar el color del texto a naranja */
    }
    th {
        background-color: #333;
    }
    tr:nth-child(even) {
        background-color: rgba(255, 255, 255, 0.2);
    }
    tr:hover {
        background-color: rgba(255, 255, 255, 0.3);
    }
    .message {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }
</style>
"""

# Función para cargar el contenido del archivo CSV y generar el HTML correspondiente
def generar_html():
    rows_html = []
    c = 0
    with open(nomarxiu, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=cardelimitador)
        for i, row in enumerate(csv_reader):
            if i == 0:  # Agregar la primera línea como títulos
                titulos = row
                continue
            # Formatear la fila como una fila de una tabla HTML
            row_html = '<tr>' + ''.join([f'<td>{cell}</td>' for cell in row]) + '</tr>'
            rows_html.append(row_html)
            c += 1
    return titulos, rows_html, c

# Generar el código HTML completo
def generar_codigo_html():
    titulos, rows_html, c = generar_html()
    titulos_html = '<tr>' + ''.join([f'<th>{titulo}</th>' for titulo in titulos]) + '</tr>'
    contenido_html = ''.join(rows_html)
    html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>FISERV</title>
    {css_styles.replace('FONDO', fondo_seleccionado).replace('WIDTH', '80').replace('FONT_SIZE', '18')}
</head>
<body>
    <h1 style="text-align: center; margin-bottom: 20px;">Tablero de Visualización de Procesos de Embozado</h1>
    <h1 style="text-align: center; margin-bottom: 20px;">Cantidad Procesos pendientes {c} </h1>
    <table>
        <thead>
            {titulos_html}
        </thead>
        <tbody>
            {contenido_html}
        </tbody>
    </table>
    <div style="text-align: center; margin-top: 20px;">
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

 


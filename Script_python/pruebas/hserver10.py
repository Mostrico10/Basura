import csv
import http.server
import socketserver
import random
import webbrowser
import os

# Nombre del archivo de texto
nomarxiu = 'S30-SOW1092.TXT'
# Delimitador del archivo CSV
cardelimitador = ';'

# Lista de fondos disponibles
opciones_fondos = ['Wallpaper3_1920x1080.png', 'Wallpaper5_1920x1080.png', 'Wallpaper7_1920x1080.png']

# Seleccionar aleatoriamente un fondo de la lista
fondo_seleccionado = random.choice(opciones_fondos)

# Leer el archivo CSV y generar las líneas de texto HTML
with open(nomarxiu, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=cardelimitador)
    lines_html = []
    for row in csv_reader:
        # Formatear la fila como un párrafo HTML encuadrado por el delimitador ";"
        line_html = f'<p class="line">{cardelimitador} {" ".join(row)} {cardelimitador}</p>'
        lines_html.append(line_html)

# Estilos CSS para mejorar la visualización del texto #box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
css_styles = f"""
<style>
    body {{
        margin: 0;
        padding: 0;
        font-family: Amasis MT Pro Black,  Bold Italic;
        font-size: 35px;
        color: white;
        background-image: url('{fondo_seleccionado}');
        background-size: cover;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}
    .board {{
        border: 5px solid #ccc;
        background-color: rgba(255, 255, 255, 0.1);
        padding:30px;
        box-shadow:0 0 3px 10px rgba(23, 9, 26);
        
        
        width: 80%;
        max-width: 800px;
        position: relative;
    }}
    .line {{
        margin: 10px 0;
        padding: 5px;
        border-bottom: 1px solid #ccc;
        position: relative;
        animation: slide-in 1s forwards;
    }}
    .line:before {{
        content: "";
        position: absolute;
        top: 50%;
        left: -5px;
        transform: translateY(-50%);
        width: 20px;
        height: 20px;
        background-color: #ccc;
        border-radius: 50%;
    }}
    @keyframes slide-in {{
        from {{
            opacity: 0;
            transform: translateX(-100%);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
</style>
"""

# JavaScript para animar el desplazamiento del texto
js_script = """
<script>
    window.onload = function() {
        var lines = document.querySelectorAll('.line');
        var delay = 0;
        lines.forEach(function(line) {
            line.style.animationDelay = delay + 's';
            delay += 0.5;
        });
    }
</script>
"""

# Generar el código HTML completo
html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Procesos de Embozado</title>
   
    {css_styles}
</head>
<body>
    <div class="board">
        <h1>Tablero de Visualización Procesos de Embozado</h1>
            <marquee style="border:#B0AEAE 2px SOLID">FIRST DATA IS NOW FISERV.</marquee><marquee bgcolor="#FE7217">  ESTADO 51 JOB PENDIENTES DE EMBOZADO </marquee><footer><a href ="javascript:location.reload()">Actualizar</a></footer>
        {''.join(lines_html)}
    </div>
    {js_script}
   
</body>

</html>
"""

# Guardar el código HTML en un archivo local
output_file_path = 'output.html'
with open(output_file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_code)

print("Archivo HTML generado correctamente.")

# Obtener la ruta del archivo HTML generado
file_path = os.path.abspath(output_file_path)

# Abrir el archivo HTML generado en el navegador web predeterminado
webbrowser.open(f'file://{file_path}')

# Configurar el servidor web
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor web
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor iniciado en el puerto", PORT)
    print(f"Puedes ver el archivo HTML en http://localhost:{PORT}/{output_file_path}")
    httpd.serve_forever()

 


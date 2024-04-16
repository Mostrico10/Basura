import csv
import http.server
import socketserver
import random
import webbrowser

nomarxiu = 'S30-SOW1092.TXT'
cardelimitador = ';'

# Definir las opciones de fondos disponibles
opciones_fondos = ['Wallpaper3_1920x1080.png', 'Wallpaper5_1920x1080.png', 'Wallpaper6_1920x1080.png', 'Wallpaper7_1920x1080.png']

# Seleccionar aleatoriamente una opción de fondo
fondo_seleccionado = random.choice(opciones_fondos)

# Leer el archivo CSV y generar las filas HTML
with open(nomarxiu, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=cardelimitador)
    rows_html = []
    for row in csv_reader:
        row_html = f"<tr><td>{row[0]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
        rows_html.append(row_html)

# Generar el código HTML completo
html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Procesos Embozado</title>
    <style>
        /* Estilos CSS */
        body {{
            margin: 0;
            padding: 0;
            font-size: 2vw;
            font-family: "Arial Black";
            color: #FFFFFF;
            background-image: url('{fondo_seleccionado}');
            background-repeat: no-repeat;
            background-attachment: fixed;
            border: 10px solid black;
            line-height: 2em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        table, th, td {{
            border: 1px solid black;
            padding: 15px;
            text-align: left;
        }}
        tr:hover {{
            background-color: #EBF8FC;
        }}
        #main-header {{
            background: #0A0A0A;
            color: white;
            width: 100%;
            left: 0;
            top: 0;
            position: fixed;
            text-align: center;
            padding-top: 20px;
            z-index: 1000; /* Asegura que el encabezado esté por encima de todo */
        }}
    </style>
</head>
<body>
    <header id="main-header">
        <h1>Procesos de Embozado</h1>
        <table>
            <tr>
                <th>FECHA</th>
                <th>NRO. EXTENSION</th>
                <th>DESCRIPCION</th>
                <th>TIPO PROCESO</th>
                <th>CANT. TARJETAS</th>
            </tr>
            {''.join(rows_html)}
        </table>
    </header>

    <marquee bgcolor="#FE7217">ESTADO 51 JOB PENDIENTES DE EMBOZADO</marquee>
    <marquee style="border:#B0AEAE 2px SOLID">FIRST DATA IS NOW FISERV.</marquee>

    <a href="javascript:location.reload()">Actualizar</a>
    <script src="file:///C:/xampp/htdocs/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function () {{
            var myInterval;
            myInterval = setInterval(function () {{
                var iScroll = $(window).scrollTop();
                if (iScroll + $(window).height() == $(document).height()) {{
                    clearInterval(myInterval);
                }} else {{
                    iScroll = iScroll + 200;
                    window.scrollTo(0, iScroll);
                }}
            }}, 3000);
        }});
    </script>

    <script>
        setTimeout(function() {{
            location.reload();
        }}, 480000);
    </script>

    <center>
        <p>Total Registros Pendientes : {len(rows_html)}</p>
        <p>EMVlab 2.0</p>
        <p>Estado 51 JOB pendientes de Embozado</p>
    </center>
</body>
</html>
"""

# Guardar el código HTML en un archivo local
with open('output.html', 'w') as html_file:
    html_file.write(html_code)

print("Archivo HTML generado correctamente.")

# Configurar el servidor web
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor web
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor iniciado en el puerto", PORT)
    url = f"http://localhost:{PORT}/output.html"
    print("Abriendo", url, "en el navegador...")
    webbrowser.open(url)
    httpd.serve_forever()

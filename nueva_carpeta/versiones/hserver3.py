import csv
import http.server
import socketserver

nomarxiu = 'S30-SOW1092.TXT'
cardelimitador = ';'

# Abrir el archivo CSV en modo lectura
with open(nomarxiu, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=cardelimitador)

    # Crear una lista para almacenar filas HTML
    rows_html = []

    # Recorrer las filas del archivo CSV
    for row in csv_reader:
        # Crear una fila HTML para cada fila del CSV
        row_html = f"<tr><td>{row[0]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td></tr>"
        rows_html.append(row_html)

# Generar el código HTML completo
html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Procesos Embozado</title>
    <style>
        /* Tu estilo CSS aquí */

        /************
        // GENERAL
        ************/
        body {{
            margin: 0;
            padding: 0;
            font-size: 2vw;  /* Utilizando unidades vw para hacer el texto adaptable */
            font-family: "Arial Black";
            color: #FFFFFF;
            background-image: url('Wallpaper3_1920x1080.png');
            background-repeat: no-repeat;
            background-attachment: fixed;
            tr:hover {{
                background-color: #EBF8FC;
            }}
            border: 10px solid black;
            line-height: 2em;
        }}

        div {{
            position: absolute;
        }}

        #caja1 {{
            z-index: 5;
            top: 1em;
            left: 8em;
        }}

        #caja2 {{
            z-index: 15;
            top: 5em;
            left: 5em;
        }}

        #caja3 {{
            z-index: 25;
            top: 2em;
            left: 2em;
        }}

        /************
        // CABECERA
        ************/
        #main-header {{
            background: #0A0A0A;
            color: white;
            height: 80px;
            width: 100%;
            left: 0;
            top: 0;
            position: fixed;
        }}

        #main-header a {{
            background-image: url('Wallpaper3_1920x1080.png');
            color: white;
            element {{
                border: 10px solid black;
            }}
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        table, th, td {{
            border: 1px solid black;
        }}

        th, td {{
            padding: 15px;
            text-align: left;
        }}
    </style>

    <!-- Agregar jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>

<body>
    <header id="main-header">
        <meta name="Author" content="Gabriel Vietri" />
        <div></div>
        <a id="logo-header" href="#">
            <div id="caja1"></div>
        </a>
        <nav>
            <ul></ul>
        </nav>
    </header>

    <table>
        <tr>
            <th>ESTADO 51 JOB PENDIENTES DE EMBOZADO</th>
        </tr>
        <tr>
            <th>FECHA</th>
            <th>EXTENSION</th>
            <th>DESCRIPCION</th>
            <th>TARJETAS</th>
            <th>ESTADO</th>
        </tr>
        {''.join(rows_html)}
    </table>

    <marquee bgcolor="#FE7217">ESTADO 51 JOB PENDIENTES DE EMBOZADO</marquee>
    <marquee style="border:#B0AEAE 2px SOLID">FIRST DATA IS NOW FISERV.</marquee>

   <a href ="javascript:location.reload()">Actualizar</a>
   <script>setTimeout('document.location.reload()',480000) </script>
    <script>
        $(document).ready(function () {{
            var myInterval = false;

            myInterval = setInterval(function () {{
                var iScroll = $(window).scrollTop();

                if (iScroll + $(window).height() == $(document).height()) {{
                    clearInterval(myInterval);
                }} else {{
                    iScroll = iScroll + 2000;

                    $('html, body').animate({{
                        scrollTop: iScroll
                    }}, 3000);
                }}
            }}, 3000);
        }});
    </script>

    <script>
        $('html, body').animate({{ scrollTop: 1 }}, 'fast');
    </script>

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
    print(f"Puedes ver el archivo HTML en http://localhost:{PORT}/output.html")
    httpd.serve_forever()

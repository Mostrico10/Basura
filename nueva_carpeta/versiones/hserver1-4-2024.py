import csv
import webbrowser

# Definir el nombre del archivo y el delimitador
nomarxiu = 'S30-SOW1092.TXT'
cardelimitador = ';'

# Leer el archivo CSV y obtener las líneas
with open(nomarxiu, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=cardelimitador)
    lines = list(csv_reader)

# Calcular el número total de líneas del archivo
total_lines = len(lines)

# Definir los datos fijos que deben aparecer en la parte superior
top_data = ["FECHA", "NOMBRE JOB", "NRO. EXTENSION", "DESCRIPCION", "TIPO PROCESO", "CANT. TARJETAS", "ESTADO"]
total_pendientes = total_lines - 1  # Restar 1 para excluir la fila de encabezado
emv_version = "EMVlab 2.0"

# Generar el HTML
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Aeropuerto</title>
    <style>
        /* Estilo CSS para el fondo de la página */
        body {{
            background-image: url('Wallpaper3_1920x1080.png'); /* Fondo de pantalla */
            margin: 0;
            padding: 0;
            font-size: 30pt;
            font-family: Arial Black;
            color: #FFFFFF;
        }}

        /* Estilo CSS para el cartel del aeropuerto */
        .airport-sign {{
            position: relative;
            overflow: hidden;
            height: 100px; /* Altura del cartel */
            width: 100%; /* Ancho del cartel */
            background-color: #00204e; /* Color de fondo del cartel */
            color: white; /* Color del texto */
            font-family: Arial, sans-serif; /* Fuente del texto */
            font-size: 24px; /* Tamaño de fuente del texto */
            text-align: center; /* Alineación del texto */
            line-height: 100px; /* Altura de línea */
            white-space: nowrap; /* Evitar el salto de línea */
            animation: scrollRight 20s linear infinite; /* Animación de desplazamiento hacia la derecha */
        }}

        @keyframes scrollRight {{
            from {{
                transform: translateX(100%);
            }}
            to {{
                transform: translateX(-100%);
            }}
        }}

        /* Estilo CSS para la tabla */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }}

        th, td {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }}

        th {{
            background-color: #f2f2f2;
        }}

        tr:hover {{
            background-color: #EBF8FC;
        }}
    </style>
</head>
<body>
"""

# Mostrar los datos fijos en la parte superior
html_content += f"<div class='top-data'>\n"
html_content += f"<p>TOTAL JOB PENDIENTES : {total_pendientes}</p>\n"
html_content += f"<p>FECHA  NOMBRE  EXTENSION DESCRIPCION TIPO PROCESO CANT.TARJETAS  ESTADO </p>\n"
html_content += f"</div>\n"

# Mostrar las líneas del archivo CSV como tablas
current_line = 0
while current_line < total_lines:
    html_content += "<table class='airport-sign'>\n"
    html_content += "<tr>\n"
    for item in top_data:
        html_content += f"<th>{item}</th>\n"
    html_content += "</tr>\n"
    for row in lines[current_line:current_line + 10]:
        html_content += "<tr>\n"
        for item in row:
            html_content += f"<td>{item.strip()}</td>\n"
        html_content += "</tr>\n"
    html_content += "</table>\n"
    current_line += 10

# Cerrar el HTML
html_content += """
</body>
</html>
"""

# Escribir el contenido HTML en un archivo
with open('output.html', 'w') as html_file:
    html_file.write(html_content)

# Abrir el archivo HTML en un navegador web
webbrowser.open('output.html')

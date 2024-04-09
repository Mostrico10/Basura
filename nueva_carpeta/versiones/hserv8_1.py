import csv
import webbrowser

# Definir el nombre del archivo y el delimitador
nombre_archivo = 'S30-SOW1092.TXT'
delimitador = ';'

# Abrir el archivo CSV en modo lectura
with open(nombre_archivo, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=delimitador)
    
    # Inicializar contador
    c = -1 #el valor del contador lo inicio en -1 porque el archivo que recorre el primer registro corresponde al titulo FECHA  NOMBRE  EXTENSION  DESCRIPCION TIPO PROCESO   CANT.TARJETAS  ESTADO
    
    
    # Abrir el archivo HTML en modo escritura
    with open('output.html', 'w') as archivo_html:
        # Escribir el encabezado HTML
        archivo_html.write("<!DOCTYPE html>\n")
        archivo_html.write("<html>\n")
        archivo_html.write("<head>\n")
        archivo_html.write("<style>\n")
        archivo_html.write("/* Estilos CSS aquí */\n")
        archivo_html.write("body {\n")
        archivo_html.write("background-image: url('Wallpaper3_1920x1080.png');\n")
        archivo_html.write("color: white;\n")
        archivo_html.write("font-family: Arial, Helvetica, sans-serif;\n")
        archivo_html.write("}\n")
        archivo_html.write(".mask1 {\n")
        archivo_html.write("width: 532px;\n")
        archivo_html.write("-webkit-mask-image: linear-gradient(90deg, rgba(255, 0, 0, 0.00) 0%, #F00 25%, #F00 75%, rgba(255, 0, 0, 0.00) 100%);\n")
        archivo_html.write("mask-image: linear-gradient(90deg, rgba(255, 0, 0, 0.00) 0%, #F00 25%, #F00 75%, rgba(255, 0, 0, 0.00) 100%);\n")
        archivo_html.write("}\n")
        archivo_html.write(".move {\n")
        archivo_html.write("width: 100%;\n")
        archivo_html.write("color: white;\n")
        archivo_html.write("font-size: 35px;\n")
        archivo_html.write("font-style: normal;\n")
        archivo_html.write("font-weight: 700;\n")
        archivo_html.write("line-height: 32px;\n")
        archivo_html.write("white-space: nowrap;\n")
        archivo_html.write("overflow: hidden;\n")
        archivo_html.write("box-sizing: border-box;\n")
        archivo_html.write("}\n")
        archivo_html.write(".move p\n")
        archivo_html.write("{\n")
        archivo_html.write("display: inline-block;\n")
        archivo_html.write("padding-left: 100%;\n")
        archivo_html.write("animation: move 8s linear infinite;\n")
        archivo_html.write("}\n")
        archivo_html.write("@keyframes move {\n")
        archivo_html.write("0% { transform: translate(0, 0); }\n")
        archivo_html.write("100% { transform: translate(-100%, 0); }\n")
        archivo_html.write("}\n")
        archivo_html.write("</style>\n")
        archivo_html.write("</head>\n")
        archivo_html.write("<body>\n")
        archivo_html.write("<h1 style='text-align:center;'>PROCESOS DE EMBOZADO </h1>\n")
        archivo_html.write("<div class=\"mask1\">\n")
        archivo_html.write("<div class=\"move\">\n")
        archivo_html.write("<h1 EMVlab 2.0\n </h1>\n")

        

         

        # Escribir el contenido del archivo CSV dentro de la sección de movimiento
        for fila in lector_csv:
            archivo_html.write("<p>" + ' '.join(fila) + "</p>\n")
            # Incrementar contador
            c += 1

        archivo_html.write("</div>\n")
        archivo_html.write("</div>\n")
        # Escribir el total de elementos
        archivo_html.write("<div class=\"mask1\">\n")
        archivo_html.write("<div class=\"move\">\n")
        archivo_html.write("<h2 style='text-align:center;'>TOTAL DE TRABAJOS PENDIENTES: " + str(c) + "</h2>\n")
        archivo_html.write("<center>\n")
        archivo_html.write(" TOTAL TRABAJOS PENDIENTES:" + str(c) + "\n")
        archivo_html.write("</center>\n")
        
        # Cerrar el cuerpo y el HTML
        archivo_html.write("</body>\n")
        archivo_html.write("</html>\n")

# Abrir el archivo HTML en un navegador web
webbrowser.open('output.html')

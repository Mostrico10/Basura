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
        justify-content: center;
        align-items: center;
        height: 100vh;
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
        font-size: FONT_SIZEpx; /* Cambiar según se desee */
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
    
    /* Estilo para el contenedor de la animación */
    .marquee-container {
        width: 100%;
        overflow: hidden;
        position: relative;
    }
    
    /* Estilo para el contenido animado */
    .marquee-content {
        position: absolute;
        top: 0;
        left: 100%;
        white-space: nowrap;
        animation: marquee 20s linear infinite;
    }
    
    /* Definición de la animación marquesina */
    @keyframes marquee {
        0% { left: 100%; }
        100% { left: -100%; }
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
    <div class="marquee-container">
        <div class="marquee-content">
            <table>
                <thead>
                    {titulos_html}
                </thead>
                <tbody>
                    {contenido_html}
                </tbody>
            </table>
        </div>
    </div>
    <br>
    <center>
    <p>{c} archivos pendientes de embozado</p>
    <p>EMVlab 2.0</p>
    <p>Estado 51 JOB pendientes de Embozado</p>
    </center>
</body>
</html>
"""
    return html_code

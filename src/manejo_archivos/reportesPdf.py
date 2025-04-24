from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from src.utils.util_functions import (
    getCaloriasPorEstudiante,
    promedioCaloriasPorActividad,
    diasConMasActividades,
    actividadesOrdenadasPorFecha
)

from src.utils.utils_pdf import link_callback

def generar_reporte_pdf(nombre_archivo):
    """
    Genera un PDF de reporte usando Jinja2 + xhtml2pdf.
    """
    # 1. Renderiza la plantilla a HTML con Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('reporte_template.html')
    html_renderizado = template.render(
        calorias_por_estudiante=getCaloriasPorEstudiante(),
        promedio_por_actividad=promedioCaloriasPorActividad(),
        dias_con_mas_actividades=diasConMasActividades(),
        actividades_ordenadas=actividadesOrdenadasPorFecha()
    )

    # 2. Convierte el HTML a PDF
    with open(nombre_archivo, "wb") as salida_pdf:
        pisa_status = pisa.CreatePDF(
            src=html_renderizado,          # HTML como string
            dest=salida_pdf,               # archivo destino
            link_callback=link_callback    # para cargar CSS e imágenes
        )

    # 3. Verifica errores
    if pisa_status.err:
        print(f"❌ Error al generar PDF (código {pisa_status.err})")
    else:
        print(f"✅ Reporte generado: {nombre_archivo}")
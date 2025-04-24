import os
from urllib.parse import urlparse
from xhtml2pdf import pisa

def link_callback(uri, rel):
    """
    Convierte un URI de recurso estático en una ruta de archivo absoluta.
    """
    # Si es un recurso externo, lo dejamos pasar
    parsed = urlparse(uri)
    if parsed.scheme in ('http', 'https'):
        return uri

    # Construye la ruta absoluta
    path = os.path.join(os.getcwd(), uri)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Recurso no encontrado: {path}")
    return path

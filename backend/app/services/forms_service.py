from PyPDF2 import PdfReader
from io import BytesIO

def check_forms(pdf_bytes: bytes) -> dict:
    try:
        reader = PdfReader(BytesIO(pdf_bytes))
        has_forms = bool(reader.get_fields())
        return {"has_forms": has_forms}
    except Exception as e:
        return {"error": str(e)}

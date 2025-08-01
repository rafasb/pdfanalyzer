from PyPDF2 import PdfReader
from io import BytesIO

def check_forms(pdf_bytes: bytes) -> dict:
    try:
        reader = PdfReader(BytesIO(pdf_bytes))
        fields = reader.get_fields()
        has_forms = bool(fields)
        num_fields = len(fields) if fields else 0
        field_names = list(fields.keys()) if fields else []
        field_types = [fields[name].get('/FT', 'Unknown') for name in field_names] if fields else []
        return {
            "has_forms": has_forms,
            "num_fields": num_fields,
            "field_names": field_names,
            "field_types": field_types
        }
    except Exception as e:
        return {"error": str(e)}

from PyPDF2 import PdfReader
from io import BytesIO

def check_signatures(pdf_bytes: bytes) -> dict:
    try:
        reader = PdfReader(BytesIO(pdf_bytes))
        has_signatures = False
        # PyPDF2: Las firmas suelen estar en los campos de tipo /Sig
        if reader.trailer.get("/AcroForm"):
            fields = reader.get_fields()
            if fields:
                for field in fields.values():
                    if field.get("/FT") == "/Sig":
                        has_signatures = True
                        break
        return {"has_signatures": has_signatures}
    except Exception as e:
        return {"error": str(e)}

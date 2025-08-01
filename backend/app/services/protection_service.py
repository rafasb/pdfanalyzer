import pikepdf
from io import BytesIO

def check_protection(pdf_bytes: bytes) -> dict:
    try:
        with pikepdf.open(BytesIO(pdf_bytes)) as pdf:
            encrypted = pdf.is_encrypted
            return {"encrypted": encrypted, "password_required": encrypted}
    except pikepdf.PasswordError:
        return {"encrypted": True, "password_required": True}
    except Exception as e:
        return {"error": str(e)}

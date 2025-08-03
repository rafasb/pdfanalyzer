import pikepdf
from io import BytesIO

def check_protection(pdf_bytes: bytes) -> dict:
    try:
        with pikepdf.open(BytesIO(pdf_bytes)) as pdf:
            encrypted = pdf.is_encrypted
            protections = pdf.allow.modify_form
            forms = pdf.acroform.exists
            return {"encrypted": encrypted, "password_required": encrypted, "form": forms ,"editable_forms": protections}
    except pikepdf.PasswordError:
        return {"encrypted": True, "password_required": True}
    except Exception as e:
        return {"error": str(e)}

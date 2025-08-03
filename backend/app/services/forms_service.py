
import fitz  # PyMuPDF

def check_forms(pdf_bytes: bytes) -> dict:
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        field_names = []
        field_types = []
        field_signed = []
        closed = doc.is_closed
        form = doc.is_form_pdf
        for page in doc:
            widgets = page.widgets()
            if widgets:
                for widget in widgets:
                    field_names.append(widget.field_name)
                    field_types.append(widget.field_type)
                    field_signed.append(widget.is_signed)
        has_forms = len(field_names) > 0
        num_fields = len(field_names)
        return {
            "closed": closed,
            "form": form,
            "has_forms": has_forms,
            "num_fields": num_fields,
            "field_names": field_names,
            "field_types": field_types,
            "field_signed": field_signed
        }
    except Exception as e:
        return {"error": str(e)}

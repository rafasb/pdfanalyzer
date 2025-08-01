import fitz  # PyMuPDF

def extract_metadata(pdf_bytes: bytes) -> dict:
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            meta = doc.metadata or {}
            return {
                "author": meta.get("author"),
                "title": meta.get("title"),
                "creationDate": meta.get("creationDate"),
                "modDate": meta.get("modDate"),
                "producer": meta.get("producer"),
                "page_count": doc.page_count
            }
    except Exception as e:
        return {"error": str(e)}

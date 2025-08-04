from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.metadata_service import extract_metadata
from services.protection_service import check_protection
from services.forms_service import check_forms
from services.signature_service import check_signatures

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Validar tipo de archivo
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")
    # Validar tamaño (ejemplo: máximo 10MB)
    if file.size and file.size > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Archivo demasiado grande")
    # Guardar o procesar el archivo aquí
    return {"filename": file.filename, "message": "Archivo recibido correctamente"}

@router.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")
    pdf_bytes = await file.read()
    metadata = extract_metadata(pdf_bytes)
    protection = check_protection(pdf_bytes)
    forms = check_forms(pdf_bytes)
    signatures = check_signatures(pdf_bytes)
    result = {
        "filename": file.filename,
        "metadata": metadata,
        "protection": protection,
        "forms": forms,
        "signatures": signatures
    }
    return JSONResponse(content=result)

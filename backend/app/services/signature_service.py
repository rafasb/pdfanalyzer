from pyhanko.pdf_utils.reader import PdfFileReader
from io import BytesIO

def check_signatures(pdf_bytes: bytes) -> dict:
    try:
        pdf_stream = BytesIO(pdf_bytes)
        reader = PdfFileReader(pdf_stream, strict=False)
        signatures = []
        
        # Usar la propiedad embedded_signatures que está cacheada en el reader
        if hasattr(reader, 'embedded_signatures'):
            embedded_sigs = reader.embedded_signatures
            
            for i, sig in enumerate(embedded_sigs):
                try:
                    # Extraer información básica de la firma sin validarla
                    signer_info = {
                        "field_name": f"Signature_{i+1}",
                        "signature_object": str(type(sig).__name__),
                        "has_signature": True
                    }
                    
                    # Intentar extraer información adicional si está disponible
                    if hasattr(sig, 'field_name'):
                        signer_info["field_name"] = sig.field_name
                    
                    if hasattr(sig, 'signer_cert'):
                        try:
                            cert = sig.signer_cert
                            if cert and hasattr(cert, 'subject'):
                                subject = cert.subject
                                signer_info["signer_common_name"] = subject.native.get("common_name")
                                signer_info["signer_organization"] = subject.native.get("organization_name")
                        except Exception:
                            pass
                    
                    
                    # if hasattr(sig, 'signing_time'):
                    #     try:
                    #         if sig.signing_time:
                    #             signer_info["signing_time"] = sig.signing_time.isoformat()
                    #     except Exception:
                    #         pass
                    
                    signatures.append(signer_info)
                    
                except Exception as sig_error:
                    # Si hay error procesando esta firma, al menos reportamos que existe
                    signatures.append({
                        "field_name": f"Signature_{i+1}",
                        "has_signature": True,
                        "error": str(sig_error)
                    })
        
        return {
            "has_signatures": bool(signatures),
            "signatures": signatures
        }
    except Exception as e:
        return {"error": str(e)}

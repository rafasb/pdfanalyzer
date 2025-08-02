# Lectura de Firmas Digitales en PDF (Autofirma)

Para leer los datos de una firma digital en un PDF, especialmente si ha sido firmado con un programa como **Autofirma**, necesitarás una librería de Python que pueda analizar la estructura interna de los archivos PDF y las firmas digitales incrustadas.

---

## Librerías y Métodos Recomendados

Las firmas digitales en PDF suelen seguir estándares como **PAdES** (PDF Advanced Electronic Signatures), que a su vez se basan en **PKCS#7** o **CMS** (Cryptographic Message Syntax). Autofirma es compatible con varios formatos de firma, incluido PAdES, por lo que es probable que las firmas generadas sigan este estándar.

A continuación se presentan algunas de las librerías de Python más adecuadas para esta tarea:

### PyHanko

Esta es una de las librerías más potentes y completas para manejar firmas digitales en PDF en Python. Está diseñada específicamente para trabajar con los estándares de firma más comunes.

**¿Qué métodos probar?**

- `pyhanko.pdf_utils.reader.PdfFileReader`: Para abrir el PDF.
- `pyhanko.sign.fields.SignatureFormField`: Para buscar los campos de firma en el documento.
- `pyhanko.sign.validation.validate_pdf_signature`: Método clave para validar la firma y obtener un informe detallado (información del firmante, cadena de certificación, validez del sello de tiempo, etc.).

**Ejemplo de validación**
```python
from pyhanko.keys import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature

root_cert = load_cert_from_pemder('path/to/certfile')
vc = ValidationContext(trust_roots=[root_cert])

with open('document.pdf', 'rb') as doc:
    r = PdfFileReader(doc)
    sig = r.embedded_signatures[0]
    status = validate_pdf_signature(sig, vc)
    print(status.pretty_print_details())
```

### Endesive

Otra librería de código abierto que se centra en el manejo de firmas digitales en varios formatos, incluyendo PDF. Es una buena alternativa para la validación y extracción de datos.

**¿Qué métodos probar?**

- `endesive.pdf.verify.verify`: Permite verificar una firma PDF y obtener información sobre el certificado, el estado de la firma y el hash del documento.

### Spire.PDF for Python

Es una librería comercial, pero ofrece una amplia gama de funcionalidades para trabajar con PDF, incluida la extracción y validación de firmas digitales.

**¿Qué métodos probar?**

- `PdfDocument.Form.SignatureField`: Para acceder a los campos de firma.
- `PdfSignature.VerifySignature()`: Para validar la firma y obtener información sobre su estado.

---

## Enfoque de la Programación

El flujo de trabajo general para tu script sería el siguiente:

1. **Instalar la librería**  
   Por ejemplo:
   ```bash
   pip install pyhanko
   ```
   (o la que elijas).

2. **Cargar el PDF**  
   Abre el archivo PDF firmado.

3. **Localizar las firmas**  
   Itera a través de los campos de formulario del PDF para encontrar los campos de firma (`/Sig` o `/Signature`).

4. **Extraer y validar la información**  
   Una vez que encuentres un campo de firma, utiliza el método de validación de la librería para obtener los datos.

   La información que puedes extraer incluye:
   - **Datos del firmante:** Nombre, organización, etc., del certificado digital.
   - **Validez del certificado:** Si ha caducado, si está en la lista de revocados (CRL).
   - **Validez de la firma:** Si el contenido del PDF se ha modificado después de la firma.
   - **Sello de tiempo:** Si la firma incluye un sello de tiempo, puedes verificar cuándo se realizó.

---

## Un Detalle Importante sobre Autofirma

Autofirma, como herramienta oficial del Gobierno de España, es muy probable que genere firmas compatibles con los estándares de validación más estrictos. Las librerías mencionadas están bien equipadas para trabajar con este tipo de firmas. La clave es que el documento firmado tiene incrustado el certificado digital y la información necesaria para que estas librerías puedan procesarla.
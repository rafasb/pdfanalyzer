import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_pdf_valid():
    pdf_bytes = b'%PDF-1.4\n%Fake PDF file for test\n'
    response = client.post(
        "/upload",
        files={"file": ("test.pdf", io.BytesIO(pdf_bytes), "application/pdf")}
    )
    assert response.status_code == 200
    assert response.json()["filename"] == "test.pdf"

def test_upload_pdf_invalid_type():
    response = client.post(
        "/upload",
        files={"file": ("test.txt", io.BytesIO(b"text"), "text/plain")}
    )
    assert response.status_code == 400
    assert "Solo se permiten archivos PDF" in response.text

def test_analyze_pdf_valid():
    pdf_bytes = b'%PDF-1.4\n%Fake PDF file for test\n'
    response = client.post(
        "/analyze",
        files={"file": ("test.pdf", io.BytesIO(pdf_bytes), "application/pdf")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test.pdf"
    assert "metadata" in data
    assert "protection" in data
    assert "forms" in data
    assert "signatures" in data

def test_analyze_pdf_invalid_type():
    response = client.post(
        "/analyze",
        files={"file": ("test.txt", io.BytesIO(b"text"), "text/plain")}
    )
    assert response.status_code == 400
    assert "Solo se permiten archivos PDF" in response.text

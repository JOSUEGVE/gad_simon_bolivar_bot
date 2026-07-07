from main import validar_cedula, registrar_tramite
import pytest

def test_validar_cedula():
    assert validar_cedula("1234567890") == True
    assert validar_cedula("123") == False

def test_registrar_tramite_error():
    with pytest.raises(ValueError):
        registrar_tramite("Juan", "123", "Certificado")
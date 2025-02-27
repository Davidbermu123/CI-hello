from programa import es_primo  # Importa la función desde el archivo primos.py

def test_primos_basicos():
    """Prueba números primos básicos"""
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(5) == True
    assert es_primo(7) == True
    assert es_primo(11) == True

def test_no_primos():
    """Prueba números que no son primos"""
    assert es_primo(1) == False
    assert es_primo(4) == False
    assert es_primo(6) == False
    assert es_primo(9) == False
    assert es_primo(10) == False

def test_numeros_grandes():
    """Prueba números grandes"""
    assert es_primo(97) == True  # Primo
    assert es_primo(100) == False  # No primo
    assert es_primo(101) == True  # Primo

def test_numeros_negativos_y_cero():
    """Prueba con números negativos y cero"""
    assert es_primo(-1) == False
    assert es_primo(-10) == False
    assert es_primo(0) == False

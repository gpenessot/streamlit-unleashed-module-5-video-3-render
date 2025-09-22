from app import get_title

def test_get_title():
    """
    Teste si la fonction get_title retourne la bonne chaîne de caractères.
    C'est un test simple pour valider que pytest fonctionne dans notre pipeline.
    """
    assert get_title() == "Analyse de Données Interactive"
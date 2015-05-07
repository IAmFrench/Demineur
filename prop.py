def difficulte('niveau'):
    """
    3 niveaux de difficulté
        "facile" -> 9x9
        "intermediaire" -> 16x16
        "expert" -> 30x16
    """
    if niveau=='facile':
        return('9x9')
    elif niveau=='intermediaire':
        return('16x16')
    elif niveau=='expert':
        return('30x16')
    else :
        return('Erreur')

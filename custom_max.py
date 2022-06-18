def custom_max(n1:int, n2:int):
    """Dado dos numeros retorna el maximo de ambos 

    Args: 
        n1(int): Primer numero a comparar
        n2(int): Segundo numero a comparar 

    Returns: 
        int: Mayor de ambos 
    """
    if n1 >= n2:
        return n1
    elif n2 > n1:
        return n2 
    raise Exception("Algo salio mal")

def max_de_tres(n1: int, n2: int, n3: int):
    """Dados tres numeros, returna el maximo de ambos

    Args:
        n1(int): Primer numero a comparar
        n2(int): Segundo numero a comparar
        n3(int): Tercer numero a comparar 

    Returns: 
        int: Mayor de los tres numeros
    """
    n = custom_max(n1,n2)
    n_final = custom_max(n,n3)

    return n_final

print(max_de_tres(1,1,1))

import pandas as pd

def creat_example() -> pd.DataFrame:
    """ Create a dataframe example

    Returns:
        pd.DataFrame: Names and description
    """
    tabela = pd.DataFrame ({
        'Nome': ['Renata', 'Anderson', 'Henrique'],
        'Nota1': [10, 5, 9],
        'Nota2': [7, 3, 9],
    })

    return tabela
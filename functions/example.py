import pandas as pd

def create_example_dataframe() -> pd.DataFrame:
    """
    Create an example DataFrame.

    Returns:
        pd.DataFrame: _description_
    """
    tabela = pd.DataFrame({
        "product": ["Café", "Guaraná", "Pastel"],
        "price": [10, 7, 6],
        "quantity": [1, 2, 3],
    })
    
    return tabela
create_example_dataframe()
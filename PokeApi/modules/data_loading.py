from sqlalchemy import create_engine
from config.settings import config

def load_data_to_db(dataframe, table_name):
    engine = create_engine(config.DB_CONNECTION_STRING)
    dataframe.to_sql(table_name, engine, if_exists='replace', index=False)

# Example usage
if __name__ == "__main__":
    import pandas as pd
    sample_df = pd.DataFrame({
        "name": ["bulbasaur", "ivysaur"],
        "url": ["https://pokeapi.co/api/v2/pokemon/1/", "https://pokeapi.co/api/v2/pokemon/2/"],
        "name_length": [9, 7]
    })
    load_data_to_db(sample_df, "pokemon")

import pandas as pd
from sqlalchemy import create_engine

SAMPLE_TABLES = {
    "Contacts": "samples/contact.csv",
    "Orders": "samples/order.csv",
    "Products": "samples/order.csv",
    "Cities": "samples/city.csv",
}


def setup_db():
    engine = create_engine('sqlite://', echo=False)
    for name, filename in SAMPLE_TABLES.items():
        df = pd.read_csv(filename)
        df.to_sql(name, con=engine)
    return engine

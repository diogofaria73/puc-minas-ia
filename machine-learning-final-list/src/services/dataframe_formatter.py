import pandas as pd


def header_formatter(df: pd.DataFrame) -> pd.DataFrame:
    # Update the column names, remove spaces replacing to underscore, remove / and () replacing to underscore and put all in lower case
    df.columns = df.columns.str.replace(' ', '_').str.replace(
        '/', '_').str.replace('(', '').str.replace(')', '').str.lower()

    return df

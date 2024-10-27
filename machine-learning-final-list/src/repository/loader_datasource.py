import pandas as pd


def load_csv_data(file_path) -> pd.DataFrame | None:
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}")
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {str(e)}")

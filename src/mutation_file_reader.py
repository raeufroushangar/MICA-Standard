import os
import pandas as pd

def read_mutation_data(file_path):
    """
    Read mutation positions and impact scores from a CSV file.

    Args:
    - file_path (str): Path to the input CSV file.

    Returns:
    - list of tuples: List of (mutation_position, impact_score) tuples if successful.
    - str: Error message if any issue occurs.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
        
        # Check if the file path is a file
        if not os.path.isfile(file_path):
            return "File not found."
        
        # Check the file extension to ensure it is a CSV file
        if not file_path.endswith('.csv'):
            return "Invalid file format. Only CSV files are supported."

        # Read the CSV file
        df = pd.read_csv(file_path, keep_default_na=False)
        
        # Check if the DataFrame has the required columns
        if 'mut_positions' not in df.columns or 'impact_score' not in df.columns:
            return "Parsing error. The file must contain 'mut_positions' and 'impact_score' columns."
        
        # Check if the DataFrame is empty
        if df.empty:
            return "File is empty."
        
        # Check data types of the columns
        if not pd.api.types.is_integer_dtype(df['mut_positions']):
            return "Data type error. The 'mut_positions' column must contain integers."
        if not (pd.api.types.is_float_dtype(df['impact_score']) or pd.api.types.is_integer_dtype(df['impact_score'])):
            return "Data type error. The 'impact_score' column must contain floats or integers."
        
        # Ensure there are no missing values
        if df['mut_positions'].isnull().any() or df['impact_score'].isnull().any():
            return "Data error. The 'mut_positions' and 'impact_score' columns must not contain missing values."
        
        # Extract mutation positions and impact scores as a list of tuples
        mutations = list(df[['mut_positions', 'impact_score']].itertuples(index=False, name=None))
        
        return mutations
    
    except pd.errors.ParserError:
        return "Parsing error. Please check the file format and content."
    except Exception as e:
        return f"{str(e)}"

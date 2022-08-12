import pandas as pd

def scaler_nD(txt, sep, esc, newtxt):
    """Takes a file into a DataFrame and multiplies the columns by a scalar, 
    then prints head of DataFrame

    Args:
        txt (.csv, .txt): File to import as DataFrame
        sep (str): Type of delimiter of file
        esc (int): Scalar to multiply on each column
        newtxt (str): Name for the output file

    Returns:
        DataFrame : returns modified DataFrame
    """

    data = pd.read_csv(txt, sep = sep, index_col = False)

    for col in data.columns:
        data[col] = data[col] * esc

    print(data.head())
    data.to_csv(newtxt, sep='\t', index=False)

    return data

scaler_nD("vectortest2D.txt", "\t", 2, "newdata.txt")


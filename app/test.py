import pandas as pd

def csv_to_dict(uploaded_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file, header=None, names=["Feature", "Value"])

    # Strip any leading/trailing whitespace from the feature names (in case there is any)
    df['Feature'] = df['Feature'].str.strip()

    # Convert the DataFrame to a dictionary
    data_dict = dict(zip(df["Feature"], df["Value"]))
    
    return data_dict

data = csv_to_dict('app/test_data.csv')



print(data)
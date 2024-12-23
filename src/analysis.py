import csv
import sys
import requests
from config import API_KEY
from utils import read_csv_to_dataframe
import seaborn as sns






def main():
    if len(sys.argv) != 2:
        print("Usage: python src/analysis.py data/products.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    df = read_csv_to_dataframe(file_path)
    # Analysis
    # lets see how the dataset looks like-
    print(df)
    # I can notice there was some error while extracting the data set from the pdf document
    # provided by 10eqs as the last column of supplier is not extarcted from the pdf
    col_names = df.columns.to_list()
    print(col_names)
    # check for null values
    print(df.isnull().sum())
    # As we can see there are 2 NaN/null values present in our_price and restock_threshold feature so we are just going
    # to drop those row
    df.dropna(inplace=True)
    print(df.isnull().sum())

    # I will use seaborn to check for correlations between features so we can do some feature 
    # engineering
    print(df.corr())
    sns.pairplot(df)

    # From the pairplot we can observe that there is a strong correlation between current stock and 
    # restock_threshold for Chamomile Tea (30 bags)




def fetch_data():
    url = "https://api.example.com/data"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


if __name__ == "__main__":
    main()
    # data = fetch_data()
    # print(data)

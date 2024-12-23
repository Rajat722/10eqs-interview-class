import csv
import sys
import requests
from config import API_KEY
from utils import read_csv_to_dataframe







def main():
    if len(sys.argv) != 2:
        print("Usage: python src/analysis.py data/products.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    products_df = read_csv_to_dataframe(file_path)
    


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
    data = fetch_data()
    print(data)

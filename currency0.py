import requests

def main():
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP,CAD,EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful!")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
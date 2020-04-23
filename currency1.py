import requests

def main():
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP,CAD,EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful!")
    data = res.json()
    rates = data["rates"]
    print(rates)
    rateGBP = data["rates"]["GBP"]
    rateCAD = data["rates"]["CAD"]
    rateEUR = data["rates"]["EUR"]
    print(f"1 USD is equal to {rateGBP} GBP")
    print(f"1 USD is equal to {rateCAD} CAD")
    print(f"1 USD is equal to {rateEUR} EUR")

if __name__ == "__main__":
    main()
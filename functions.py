import pandas as pd

df = pd.read_csv("Task4a_data.csv")

gbp_rate = df["USD - GBP"][0]
usd_rate = df["GBP - USD"][0]


def convert_usd_to_gbp(amount_local, rate):
    """ Takes in amount in USD and returns amount in GBP """
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)


# Add function below to convert GBP to USD
def convert_gbp_to_usd(amount_local, rate):
    amount_usd = amount_local * rate
    return round(amount_usd, 2)


amount = float(input("Enter amount in USD: "))
print(convert_gbp_to_usd(amount, usd_rate))

amount = float(input("Enter amount in USD: "))
print(convert_usd_to_gbp(amount, gbp_rate))
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
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe from the csv file given in the task
df = pd.read_csv("Task4a_data.csv")

# Convert the date column to datetime format so Python can recognise it as a date
df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

# Creates an empty graph window
plt.figure(figsize=(12, 6))

# Plot x and y axis - and give a label to graph
plt.plot(df['Date'], df['GBP - USD'], label='GBP to USD trend')

# Gives the graph window a title
plt.title("GBP rates to USD over time")
# Gives a label to x axis
plt.xlabel('Date')
# Gives a label to y axis
plt.ylabel('GBP to USD rates')
# Gives users legend menu
plt.legend()
# Creates grid lines on the graph
plt.grid(True)
# Rotate the dates by 45 degress to make it easier to read
plt.xticks(rotation=45)
# Prevents overlapping of elements
plt.tight_layout()
# Displays the graph
plt.show()
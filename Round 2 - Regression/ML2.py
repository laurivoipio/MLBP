import pandas as pd # import Pandas library (and defining shorthand "pd") for reading and manipulating the data files
from matplotlib import pyplot as plt # import and define shorthand "plt" for library "pyplot" providing plotting functions
from IPython.display import display, HTML
import numpy as np   # import and define shorthand "np" for library "numpy" for advanced mathematical operations in python

# def solution1():
#     # We assign Global variables for testing purposes
#     global df_bc, df_eth, bitcoin, ethereum, axis, best_alpha
    # read in historic Bitcoin and Ethereum statistics data from the files "BTC-USD.csv" and "ETH-USD.csv"

df_bc = pd.read_csv("BTC-USD.csv", parse_dates=['Date'])
df_eth = pd.read_csv("ETH-USD.csv", parse_dates=['Date'])

# read the dates for the individual records from column "Date"
bitcoin_date = df_bc.Date.values
ethereum_date = df_eth.Date.values

### STUDENT TASK ###
## read in closing prices for Bitcoin and Ethereum from the column "Close" and computed the rescaled values  
## Replace '...' with your solution.
#bitcoin = [...]
#ethereum = [...]

# YOUR CODE HERE

#print(df_bc.iloc[0,0])
print(len(df_bc))
print(len(df_eth))
#print(np.min(df_bc))
#print(np.min(df_eth))
bitcoin = []
bit_close = []

index = 0
while index < len(df_bc):
    bit_close.append(df_bc.iloc[index, 4])
    index +=1
b_max = np.float64(np.max(bit_close))
b_min = np.float64(np.min(bit_close))
print(b_max)
print(b_min)
index = 0
while index < len(df_bc):
    if (b_max - b_min) != 0:
        x = np.float64(((df_bc.iloc[index,5]-b_min)/(b_max - b_min)))
        bitcoin.append(x)
    else:
        bitcoin.append(0)
    index += 1
print(len(bitcoin))

index = 0
bit_min= np.min(bitcoin)
ethereum = []
eth_close = []

while index < len(df_eth):
    eth_close.append(df_eth.iloc[index, 4])
    
    index +=1
e_max = np.float64(np.max(eth_close))
e_min = np.float64(np.min(eth_close))
print("eth max", e_max)
print("eth min", e_min)
index = 0
while index < len(df_eth):
    if (e_max - e_min) != 0:
        x = np.float64(((df_eth.iloc[index,5]-e_min)/(e_max - e_min)))
        ethereum.append(x)
    else:
        ethereum.append(bit_min)
    index += 1
# print(len(ethereum))
# print("eth max", np.max(ethereum))
# print("bit max", np.max(bitcoin))
# print("eth min", np.min(ethereum))
# print("bit min", np.min(bitcoin))

    #raise NotImplementedError()

# Show cryptocurrency prices over transaction date
axis = plt.gca()
plt.plot(bitcoin_date,bitcoin, label=("Bitcoin")) 
plt.plot(ethereum_date,ethereum, label=("Ethereum"))
plt.title(r'$\bf{Figure\ 2.}$ Normalized cryptocurrency prices')
plt.xlabel('Date')
plt.ylabel('Normalized price')
plt.xticks(rotation=20)
plt.legend()

plt.show()
assert len(bitcoin) == 948,"Your bitcoin data is incorrect length"
assert len(ethereum) == 948, "Your ethereum data is incorrect length"
assert np.max(bitcoin) == np.max(ethereum), "Incorrect max values after normalisation"
assert np.min(bitcoin) == np.min(ethereum), "Incorrect min values after normalisation"







# # Run test that check that plot renders correctly. Requires plotchecker to be installed.
# from plotchecker import LinePlotChecker
# pc = LinePlotChecker(axis)
# pc.assert_num_lines(2)
# pc.find_permutation('title',r'$\bf{Figure\ 2.}$ Normalized cryptocurrency prices')
# pc.find_permutation('xlabel','Date')
# pc.find_permutation('ylabel','Normalized price')
# pc.assert_labels_equal(['Bitcoin','Ethereum'])

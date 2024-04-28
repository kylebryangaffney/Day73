import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0, parse_dates=["DATE"])
df = df.dropna()
print(df.head())
print(df.tail())
print(df.shape)

entries_per_language = df.count()

posts_per_languate = df.groupby('TAG').sum(numeric_only=True)

months_of_data = df.groupby("TAG").count()

date_time = df["DATE"][1]

## update the date format from string. 
## Not neccasarry because of the parse_dates=["date"] in the initial function call
df.DATE = pandas.to_datetime(df.DATE)

pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(pivoted_df)
print(pivoted_df.head())
print(pivoted_df.tail())
print(pivoted_df.shape)
print(pivoted_df.count())
## replace NAN with 0. null is not 0
pivoted_df.fillna(0, inplace=True)
pivoted_df = pivoted_df.fillna(0) 

## build graph in matplotlib.pyplot
newgraph = plt.plot(pivoted_df.index, pivoted_df["c++"])
## updating visual representation paramaters
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for i in pivoted_df.columns:
        plt.plot(pivoted_df.index, pivoted_df[i], 
             linewidth=3, label=pivoted_df[i].name)
 
plt.legend(fontsize=16) 

## build the graph using averages to smooth out the data visually
roll_df = pivoted_df.rolling(window=6).mean()
## reprint the same graph with the averaged data
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for i in roll_df.columns:
    plt.plot(roll_df.index, roll_df[i], 
             linewidth=3, label=roll_df[i].name)
 
plt.legend(fontsize=16)
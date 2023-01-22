# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns;
import numpy as np
# %%
with open("data/movies.csv", "r") as movies:
    file = pd.read_csv(movies)

plt.figure(figsize=(18,8))
sns.heatmap(file.corr(),annot=True,cmap='RdYlGn')

# %% 

numpyarray = file.to_numpy()
print(len(numpyarray[np.where(numpyarray[:,2] < '1940-01-01')]))
movies1927 = numpyarray[np.where(numpyarray[:,2] < '1927-01-01')]
movies1937 = numpyarray[np.where((numpyarray[:,2] < '1937-01-01' ) & (numpyarray[:,2] > '1927-01-01'))]
movies1947 = numpyarray[np.where((numpyarray[:,2] < '1947-01-01') & (numpyarray[:,2] > '1937-01-01'))]
movies1957 = numpyarray[np.where((numpyarray[:,2] < '1957-01-01') & (numpyarray[:,2] > '1947-01-01'))]
movies1967 = numpyarray[np.where((numpyarray[:,2] < '1967-01-01') & (numpyarray[:,2] > '1957-01-01'))]
movies1977 = numpyarray[np.where((numpyarray[:,2] < '1977-01-01') & (numpyarray[:,2] > '1967-01-01'))]
movies1987 = numpyarray[np.where((numpyarray[:,2] < '1987-01-01') & (numpyarray[:,2] > '1977-01-01'))]
movies1997 = numpyarray[np.where((numpyarray[:,2] < '1997-01-01') & (numpyarray[:,2] > '1987-01-01'))]

movies2007 = numpyarray[np.where((numpyarray[:,2] < '2007-01-01') & (numpyarray[:,2] > '1997-01-01'))]
movies2017 = numpyarray[np.where((numpyarray[:,2] < '2017-01-01') & (numpyarray[:,2] > '2007-01-01'))]


# %% 
dates_array = np.array([">1917", "1917-1927","1927-1937","1937-1947","1947-1957","1957-1967",
                        "1967-1977","1977-1987","1987-1997","1997-2007"])
print(dates_array)

movies1927Cleaned = movies1927[np.where(movies1927[:,3] > 0.0)]
movies1927Average = movies1927Cleaned[:,3].mean()
print(movies1927Average)


movies1937Cleaned = movies1937[np.where(movies1937[:,3] > 0.0)]
movies1937Average = movies1937Cleaned[:,3].mean()

movies1947Cleaned = movies1947[np.where(movies1947[:,3] > 0.0)]
movies1947Average = movies1947Cleaned[:,3].mean()
movies1957Cleaned = movies1957[np.where(movies1957[:,3] > 0.0)]
movies1957Average = movies1957Cleaned[:,3].mean()

movies1967Cleaned = movies1967[np.where(movies1967[:,3] > 0.0)]
movies1967Average = movies1967Cleaned[:,3].mean()
movies1977Cleaned = movies1977[np.where(movies1977[:,3] > 0.0)]
movies1977Average = movies1977Cleaned[:,3].mean()
movies1987Cleaned = movies1987[np.where(movies1987[:,3] > 0.0)]
movies1987Average = movies1987Cleaned[:,3].mean()
movies1997Cleaned = movies1997[np.where(movies1997[:,3] > 0.0)]
movies1997Average = movies1997Cleaned[:,3].mean()
movies2007Cleaned = movies2007[np.where(movies2007[:,3] > 0.0)]
movies2007Average = movies2007Cleaned[:,3].mean()
movies2017Cleaned = movies2017[np.where(movies2017[:,3] > 0.0)]
movies2017Average = movies2017Cleaned[:,3].mean()

allMoviesAverage = np.array([movies1927Average,movies1937Average,
                             movies1947Average,movies1957Average,
                             movies1967Average,movies1977Average,
                             movies1977Average,
                             movies1987Average,movies1997Average,
                             movies2017Average,movies2007Average]).mean()*2
groupedMoviesAverage = np.array([movies1927Average,movies1937Average,
                             movies1947Average,movies1957Average,
                             movies1967Average,movies1977Average,
                             movies1987Average,movies1997Average,
                             movies2007Average,movies2017Average])*2


allMoviesLength = len(numpyarray)


groupedMoviesLength = np.array([len(movies1927Cleaned),len(movies1937Cleaned),
                             len(movies1947Cleaned),len(movies1957Cleaned),
                             len(movies1967Cleaned),len(movies1977Cleaned),
                             len(movies1987Cleaned),len(movies1997Cleaned),
                             len(movies2007Cleaned),len(movies2017Cleaned)])

# %%
print(movies1927Cleaned[:,4].sum())
groupedMoviesNumRatings = np.array([movies1927Cleaned[:,4].sum(),movies1937Cleaned[:,4].sum(),
                             movies1947Cleaned[:,4].sum(),movies1957Cleaned[:,4].sum(),
                             movies1967Cleaned[:,4].sum(),movies1977Cleaned[:,4].sum(),
                             movies1987Cleaned[:,4].sum(),movies1997Cleaned[:,4].sum(),
                             movies2007Cleaned[:,4].sum(),movies2017Cleaned[:,4].sum()])

# %%
plt.figure(figsize=(12,12))

fig, ax = plt.subplots()
for side in ['top','right','bottom','left']:
    ax.spines[side].set_visible(False)

plt.scatter(dates_array,groupedMoviesAverage,s=groupedMoviesLength, c=groupedMoviesNumRatings,cmap="Wistia")

frame = plt.gca();

plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)

for dates_array, groupedMoviesAverage in zip(dates_array,groupedMoviesAverage):

    label = dates_array

    plt.annotate(label, # this is the text
                 (dates_array,groupedMoviesAverage), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center



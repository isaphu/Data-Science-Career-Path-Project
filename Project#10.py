#FoodWheel

#What cuisines does FoodWheel offer?
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)

import codecademylib3
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values


plt.pie(counts,
        labels=cuisines,
       autopct='%d%%')
plt.title('FoodWheel')
plt.axis('equal')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
from ucimlrepo import fetch_ucirepo   
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

# first five rows
# print(iris.variables.head(5))
# iris.variables.dropna(inplace = True)

# print(iris.variables.info())

# print(iris.variables.describe())

# descr= iris.variables.groupby('description')
# descr.first()
# print(descr)
# # print(description)

# import pandas as pd
# import matplotlib.pyplot as plt



# # Step 3: Sort the dataset by Date
# iris = iris.variables.sort_values('Date')
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the dataset (replace 'your_dataset.csv' with the actual file)
# # The dataset should have columns like 'Date' and 'Sales'
# data = pd.read_csv('your_dataset.csv')

# # Ensure the 'Date' column is in datetime format
# data['Date'] = pd.to_datetime(data['Date'])

# # Sort the dataset by the 'Date' column
# data = data.sort_values('Date')

# # Plotting the line chart
# plt.figure(figsize=(10, 6))  # Set the figure size
# plt.plot(data['Date'], data['Sales'], marker='o', label='Sales Over Time')

# # Customizing the plot
# plt.title('Sales Trends Over Time', fontsize=16)  # Add a title
# plt.xlabel('Date', fontsize=14)  # Label the x-axis
# plt.ylabel('Sales', fontsize=14)  # Label the y-axis
# plt.grid(True)  # Add gridlines
# plt.legend()  # Add a legend
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# # Show the plot
# plt.tight_layout()  # Adjust layout to prevent label cutoff
# plt.show()

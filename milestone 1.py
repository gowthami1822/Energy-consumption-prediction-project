!pip install gdown
!gdown --fuzzy "https://drive.google.com/file/d/1bvaXJJqNObOCkX-i475BNxpidk024pyx/viewimport pandas as pd

# Load the dataset
df = pd.read_csv('household_power_consumption.txt', sep=";")

# Display basic information
print(df.head())
print(df.info())
print(df.shape)
print(df.describe(include='object'))"# Check for any missing values
print(df.isnull().any())

# Count total missing values per column
print(df.isnull().sum())

# Calculate percentage of missing values in 'Sub_metering_3'
missing_percentage = (df['Sub_metering_3'].isnull().sum() / len(df)) * 100
print("Percentage of missing values in 'Sub_metering_3':", missing_percentage)# Fill missing values with zero
df = df.fillna(0)

# Fill missing values in 'Sub_metering_3' with its mean
df['Sub_metering_3'] = df['Sub_metering_3'].fillna(df['Sub_metering_3'].mean())

# Fill missing values with median
df['Sub_metering_3'] = df['Sub_metering_3'].fillna(df['Sub_metering_3'].median())

# Drop rows with any missing values
df = df.dropna()
print(df.shape)import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Example scatter plot with sample arrays
d1 = np.array([3, 6, -8])
d2 = np.array([-7, 1, 5])
plt.plot(d1, d2, 'ro', markersize=12)
plt.show()

# Histogram of 'Global_active_power' if it exists in the dataset
if 'Global_active_power' in df.columns:
    sns.histplot(df['Global_active_power'].astype(float), kde=True)
    plt.xlabel('Global Active Power')
    plt.title('Distribution of Global Active Power')
    plt.show()

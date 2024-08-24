import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Set the number of rows
num_rows = 200

# Create sample data
data = {
    'date': pd.date_range(start='2024-01-01', periods=num_rows, freq='D'),
    'time_of_day': np.random.randint(0, 24, size=num_rows),  # Random hours of the day
    'weather_condition': np.random.choice(['Clear', 'Rain', 'Fog', 'Snow'], size=num_rows),
    'road_condition': np.random.choice(['Dry', 'Wet', 'Icy'], size=num_rows),
    'latitude': np.random.uniform(low=34.0, high=37.0, size=num_rows),
    'longitude': np.random.uniform(low=-118.0, high=-115.0, size=num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df.head())

# Data Cleaning
df.dropna(inplace=True)  # Remove missing values (though not needed for this synthetic data)
# 'time_of_day' is already in integer format

# Time of Day Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['time_of_day'], bins=24, kde=False)
plt.title('Accidents by Time of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()

# Weather Conditions Analysis
plt.figure(figsize=(12, 8))
sns.countplot(x='weather_condition', data=df)
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Road Conditions Analysis
plt.figure(figsize=(12, 8))
sns.countplot(x='road_condition', data=df)
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Hotspots Analysis
map_center = [df['latitude'].mean(), df['longitude'].mean()]
accident_map = folium.Map(location=map_center, zoom_start=12)

for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='red',
        fill=True
    ).add_to(accident_map)

accident_map.save('accident_hotspots.html')

import pandas as pd
import numpy as np

class DataAnalysisProject:
    """
    Professional data manipulation toolbox using Pandas and NumPy.
    """
    
    def __init__(self):
        print("--- Data Analysis Project Initialized ---")

    def student_analysis(self):
        """1. Basic Student Data Management"""
        print("\n[Step 1] Student Performance Data:")
        data = {
            'Student': ['Bob', 'Mark', 'Anna', 'David', 'Sam'],
            'Math_Grade': [85, 90, 78, 92, 88],
            'English_Grade': [80, 85, 92, 88, 90],
            'Hours_Studied': [250, 500, 355, 245, 199] 
        }
        df = pd.DataFrame(data)
        print(df)
        return df

    def clean_restaurant_data(self):
        """2. String Manipulation & Cleaning"""
        print("\n[Step 2] Cleaning Restaurant Categories:")
        data = {
            'food': ['Pasta', 'Burger', 'Ice Cream', 'Salad'],
            'category': ['Italian|Fine dining', 'American|Fast Food', 'Dessert', 'Healthy']
        }
        df = pd.DataFrame(data)
        # Extracting the primary category
        df['primary_category'] = df['category'].str.split('|').str[0]
        print(df)

    def generate_housing_data(self, size=500):
        """3. Synthetic Real Estate Data Generation"""
        print(f"\n[Step 3] Generating {size} Real Estate Records:")
        np.random.seed(42)
        data = {
            'Size_sqft': np.random.randint(1000, 4001, size) // 10 * 10,
            'Bedrooms': np.random.choice([1, 2, 3, 4], size),
            'Year_Built': np.random.randint(1980, 2024, size),
            'Price_USD': np.random.normal(150000, 30000, size).round(2),
            'Type': np.random.choice(['Single Family', 'Townhouse', 'Condo', 'Duplex'], size)
        }
        df = pd.DataFrame(data)
        print(df.head())
        return df

if __name__ == "__main__":
    app = DataAnalysisProject()
    app.student_analysis()
    app.clean_restaurant_data()
    app.generate_housing_data()

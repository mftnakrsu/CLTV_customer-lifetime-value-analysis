"""
created by : MEF

Customer Lifetime Value (CLTV) Calculation Script

This script calculates Customer Lifetime Value (CLTV) using an Object-Oriented Programming (OOP) approach.
It defines a class, CustomerLifetimeValue, that encapsulates the CLTV calculation process.
The main function demonstrates how to use the class to calculate CLTV for your sales data.

Note: Replace 'your_data.csv' with the actual path to your data file.
"""

import pandas as pd

class CustomerLifetimeValue:
    def __init__(self, dataframe, profit_margin=0.10):
        
        """
        Initialize the CLTV calculator.

        Args:
            dataframe (pd.DataFrame): Input dataframe containing sales data.
            profit_margin (float, optional): The profit margin to be used for calculations. Default is 0.10.
        """
        
        self.dataframe = dataframe
        self.profit_margin = profit_margin


    def preprocess_data(self):

        """
        Preprocess the input data to prepare it for CLTV calculation.
        """

        self.dataframe = self.dataframe[~self.dataframe["Invoice"].str.contains("C", na=False)]
        self.dataframe = self.dataframe[self.dataframe['Quantity'] > 0]
        self.dataframe.dropna(inplace=True)
        self.dataframe["TotalPrice"] = self.dataframe["Quantity"] * self.dataframe["Price"]

    def calculate_metrics(self):
        
        """
        Calculate CLTV metrics for each customer.

        Returns:
            pd.DataFrame: A dataframe with CLTV metrics and customer segments.
        """
        
        cltv_c = self.dataframe.groupby('Customer ID').agg({
            'Invoice': 'nunique',
            'Quantity': 'sum',
            'TotalPrice': 'sum'
        })
        cltv_c.columns = ['total_transaction', 'total_unit', 'total_price']

        cltv_c['avg_order_value'] = cltv_c['total_price'] / cltv_c['total_transaction']
        cltv_c["purchase_frequency"] = cltv_c['total_transaction'] / cltv_c.shape[0]

        repeat_rate = cltv_c[cltv_c.total_transaction > 1].shape[0] / cltv_c.shape[0]
        churn_rate = 1 - repeat_rate

        cltv_c['profit_margin'] = cltv_c['total_price'] * self.profit_margin
        cltv_c['customer_value'] = (cltv_c['avg_order_value'] * cltv_c["purchase_frequency"])
        cltv_c['cltv'] = (cltv_c['customer_value'] / churn_rate) * cltv_c['profit_margin']

        cltv_c["segment"] = pd.qcut(cltv_c["cltv"], 4, labels=["D", "C", "B", "A"])

        return cltv_c

def main():
    
    # Example usage
    df = pd.read_csv('your_data.csv')  # Load your data from a CSV file
    clv_calculator = CustomerLifetimeValue(df)
    clv_calculator.preprocess_data()
    clv_result = clv_calculator.calculate_metrics()
    print(clv_result)

if __name__ == "__main__":
    main()

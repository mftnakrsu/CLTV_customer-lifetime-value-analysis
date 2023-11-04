
# Customer Lifetime Value (CLTV) Calculation Guide

This guide provides step-by-step instructions for calculating Customer Lifetime Value (CLTV) using the provided formulas.

<p align="center">
  <img width="900" src="https://github.com/mftnakrsu/CLTV_customer-lifetime-value-analysis/assets/57320216/8e65826b-4c9b-42c4-8b97-0ba024694dff" alt="Resim Açıklaması">
</p>


## Step 1: Data Collection

To calculate CLTV, you will need the following data:

- Total Price: The sum of all transaction values.
- Total Transaction: The total number of transactions.
- Total Number of Customers: The total number of customers.

## Step 2: Calculating Customer Value

-  Customer Value is calculated using the following formula:

```
Customer Value = Average Order Value x Purchase Frequency
```

- Average Order Value: Calculated by dividing the sum of all transaction values by the total number of transactions.

```
Average Order Value = Total Price / Total Transaction
```

- Purchase Frequency: Calculated by dividing the total number of transactions by the total number of customers.

```
Purchase Frequency = Total Transaction / Total Number of Customers
```

## Step 3: Calculating Repeat Rate and Churn Rate

Repeat Rate is the ratio of customers who make multiple purchases to all customers:

```
Repeat Rate = Number of Customers Making Multiple Purchases / Total Number of Customers
```

Churn Rate is the complement of Repeat Rate:

```
Churn Rate = 1 - Repeat Rate
```

## Step 4: Determining Profit Margin

Profit Margin is defined as 10% of the Total Price:

```
Profit Margin = Total Price x 0.10
```

## Step 5: Calculating CLTV

Finally, CLTV is calculated using the following formula:

```
CLTV = (Customer Value / Churn Rate) x Profit Margin
```

## Usage

Follow these steps to calculate CLTV for your sales data:

1. **Clone the Repository:**
   Clone this GitHub repository to your local machine by running the following command:

   ```bash
   git clone https://github.com/mftnakrsu/CLTV_customer-lifetime-value-analysis.git
   ```

2. **Install Dependencies:**
   Navigate to the repository's directory and install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Your Data:**
   Replace 'your_data.csv' in the script with the path to your data file.

4. **Run the Script:**
   Execute the script to calculate CLTV and segment your customers:

   ```bash
   python cltv_main.py
   ```

5. **View Results:**
   The CLTV metrics and customer segments will be displayed in the console. You can also modify the script to save or visualize the results as needed.

Please make sure to customize the `your_data.csv` path and any other parameters in the script according to your data and requirements.

For more details on the script and its functionalities, refer to the [script file](cltv_main.py) in the repository.

Enjoy using CLTV calculations to gain insights into your customer base!

## Data Set

You can use the provided sample data set for testing and exploration. The data set is based on sales transactions from an online retail store in the UK between 01/12/2009 and 09/12/2011. It includes various variables such as `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, and `Country`.

For additional information on the data set, you can refer to the [Online Retail II Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


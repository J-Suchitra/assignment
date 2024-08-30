import pandas as pd  
  
# Load the dataset  
df = pd.read_csv('C:/Users/suchi/OneDrive/Desktop/New folder/apna/Dataset -  Assignment 1 - Sheet1.csv')  
  
# Handle missing values in Product Name column  
df['product_name'] = df['product_name'].fillna('Unknown')  
  
# Standardize date format in Order Date column  
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')  
  
# Remove non-numeric values from final_ak_price and Units Sold columns  
df['final_ak_price'] = pd.to_numeric(df['final_ak_price'], errors='coerce')  
df['units_sold'] = pd.to_numeric(df['units_sold'], errors='coerce')  
  
# Standardize quantity units in Quantity column  
df['quantity'] = df['quantity'].str.replace(' units', '').astype(int)  
  
# Calculate Placed GMV  
df['placed_gmv'] = df['final_ak_price'] * df['units_sold'] * df['quantity']  
  
# Save the cleaned dataset  
df.to_csv('cleaned_dataset.csv', index=False)


Question 1: SQL Query

To find the Average order value, total number of orders, first order date, last order date, first order value, and last order value of a customer, I would use the following SQL query:

SELECT  
  Customer_id,  
  AVG(Placed_GMV) AS Average_Order_Value,  
  COUNT(Order_ID) AS Total_Orders,  
  MIN(Order_Date) AS First_Order_Date,  
  MAX(Order_Date) AS Last_Order_Date,  
  MIN(Placed_GMV) AS First_Order_Value,  
  MAX(Placed_GMV) AS Last_Order_Value  
FROM  
  cleaned_dataset  
GROUP BY  
  Customer_id


Question 2: Top 20 Products

# Calculate total Placed GMV for each product  
product_gmv = df.groupby('Product Name')['Placed_GMV'].sum().reset_index()  
  
# Rank products by total Placed GMV  
product_gmv = product_gmv.sort_values('Placed_GMV', ascending=False)  
  
# Select top 20 products  
top_20_products = product_gmv.head(20)  
  
print(top_20_products)


Question 3: SQL Query

To find the top 3 articles for each customer in terms of Placed GMV, I would use the following SQL query:
    
SELECT  
  Customer_id,  
  Product_Name,  
  Placed_GMV  
FROM  
  cleaned_dataset  
WHERE  
  Customer_id IN (  
   SELECT  
    Customer_id  
   FROM  
    cleaned_dataset  
   GROUP BY  
    Customer_id  
   HAVING  
    COUNT(DISTINCT Product_Name) >= 3  
  )  
ORDER BY  
  Customer_id, Placed_GMV DESC  
LIMIT 3
    
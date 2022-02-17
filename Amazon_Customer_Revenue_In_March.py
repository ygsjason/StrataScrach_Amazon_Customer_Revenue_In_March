# Import your libraries
import pandas as pd

# Start writing code
df1 = orders.drop_duplicates()

# filter out customers who were active in March 2019
df2 = df1[(df1.order_date >= '2019-03-01') & (df1.order_date <= '2019-03-31')]
df2 = df1[df1.order_date.between('2019-03-01', '2019-03-31')]
df2 = df1[df1.order_date.dt.strftime("%Y-%b") == "2019-Mar"]
df2 = df1[df1.order_date.dt.strftime("%Y-%m") == "2019-03"]
# if you don't know how many days in March
df2 = df1[(df1.order_date > '2019-03') & (df1.order_date < '2019-04')]

# groupby cust_id to calculate the total cost
df2.groupby('cust_id')['total_order_cost'].sum().reset_index(name = "revenue").sort_values('revenue', ascending = [False])

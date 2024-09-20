import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Title of application
st.title('E-Commerce Data Analyst')

# Functions to load data
@st.cache_data
def load_data():
    base_path = './data/'  # Path relatif ke folder "data"
    customers = pd.read_csv(os.path.join(base_path, 'customers_dataset.csv'))
    geolocation = pd.read_csv(os.path.join(base_path, 'geolocation_dataset.csv'))
    order_items = pd.read_csv(os.path.join(base_path, 'order_items_dataset.csv'))
    order_payments = pd.read_csv(os.path.join(base_path, 'order_payments_dataset.csv'))
    order_reviews = pd.read_csv(os.path.join(base_path, 'order_reviews_dataset.csv'))
    orders = pd.read_csv(os.path.join(base_path, 'orders_dataset.csv'))
    product_category_name_translation = pd.read_csv(os.path.join(base_path, 'product_category_name_translation.csv'))
    products = pd.read_csv(os.path.join(base_path, 'products_dataset.csv'))
    sellers = pd.read_csv(os.path.join(base_path, 'sellers_dataset.csv'))
    return customers, geolocation, order_items, order_payments, order_reviews, orders, product_category_name_translation, products, sellers

# Load data
customers, geolocation, order_items, order_payments, order_reviews, orders, product_category_name_translation, products, sellers = load_data()

# Function to display sample data
def display_sample_data(dataset_name):
    datasets = {
        'Customers': customers,
        'Geolocation': geolocation,
        'Order Items': order_items,
        'Order Payments': order_payments,
        'Order Reviews': order_reviews,
        'Orders': orders,
        'Product Category Translation': product_category_name_translation,
        'Products': products,
        'Sellers': sellers
    }
    
    df = datasets.get(dataset_name)
    if df is not None:
        st.write(df.head())
    else:
        st.write("Dataset not found")

# Create a dropdown widget for selecting dataset
dataset_name = st.selectbox(
    'Select Dataset to Display Sample Data',
    ['Customers', 'Geolocation', 'Order Items', 'Order Payments', 'Order Reviews', 'Orders', 'Product Category Translation', 'Products', 'Sellers']
)
display_sample_data(dataset_name)

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# Description of General Statistics
st.subheader('Description of General Statistics')

# Select a dataset for EDA
dataset_name_eda = st.selectbox('Select Dataset for EDA', ['Customers', 'Order Items', 'Order Payments', 'Order Reviews'])

if dataset_name_eda == 'Customers':
    st.write(customers.describe())
elif dataset_name_eda == 'Order Items':
    st.write(order_items.describe())
elif dataset_name_eda == 'Order Payments':
    st.write(order_payments.describe())
elif dataset_name_eda == 'Order Reviews':
    st.write(order_reviews.describe())

# Univariate Analysis: Distribution of Payment Values
st.subheader('Distribution of Payment Values')

# Plot distribution using seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(order_payments['payment_value'], bins=30, kde=True, ax=ax)
plt.title('Distribution of Payment Values')
plt.xlabel('Payment Value')
plt.ylabel('Frequency')
st.pyplot(fig)

# Multivariate Analysis: Correlation Heatmap
st.subheader('Correlation Heatmap')

# Prepare orders and order_payments for correlation analysis
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Merge orders with order_payments to include 'payment_value'
merged_data = pd.merge(orders, order_payments, on='order_id')

# Calculate Recency
last_purchase_date = merged_data['order_purchase_timestamp'].max()
merged_data['Recency'] = (last_purchase_date - merged_data['order_purchase_timestamp']).dt.days

# Perform RFM Analysis
rfm_df = merged_data.groupby('customer_id').agg({
    'Recency': 'min',
    'order_id': 'count',
    'payment_value': 'sum'
}).rename(columns={'order_id': 'Frequency', 'payment_value': 'Monetary'})

# Correlation analysis
numeric_columns = rfm_df[['Recency', 'Frequency', 'Monetary']]
correlation_matrix = numeric_columns.corr()

# Plot the heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Product Rating by Category
st.subheader('Product Rating by Category')

# Merge order_items, products, and order_reviews
merged_data = pd.merge(order_items, products, on='product_id')
merged_data = pd.merge(merged_data, order_reviews, on='order_id')

# Group by product category and calculate mean review score
rating_by_category = merged_data.groupby('product_category_name')['review_score'].mean().sort_values()

# Visualization
fig, ax = plt.subplots(figsize=(12, 8))
rating_by_category.plot(kind='bar', ax=ax, color='skyblue')
plt.title('Average Product Rating by Category')
plt.xlabel('Product Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
st.pyplot(fig)

# Sales Visualization by Product Category
st.subheader('Sales by Product Category')

# Merge order_items and products
merged_data = pd.merge(order_items, products, on='product_id')
sales_per_category = merged_data.groupby('product_category_name').size()

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
sales_per_category.plot(kind='bar', ax=ax)
plt.title('Total Sales per Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
st.pyplot(fig)

# Visualisation of Product Rating Distribution
st.subheader('Product Rating Distribution')

# Visualisation of ratings from order_reviews
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='review_score', data=order_reviews, ax=ax)
plt.title('Product Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Total Reviews')
st.pyplot(fig)

# Conclusion
st.header('Conclusion')
st.write('1. Univariate analysis reveals the distribution of payment values, showing how most customers fall into a certain price range.')
st.write('2. The correlation heatmap shows a strong relationship between frequency of orders and monetary value, indicating that frequent buyers tend to spend more.')
st.write('3. Product rating analysis reveals that some categories consistently perform better in customer satisfaction, which can inform future business decisions.')

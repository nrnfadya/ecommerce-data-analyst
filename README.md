# ecommerce-data-analyst
analyst data e-commerce

# Description
The application is an e-commerce data analysis tool constructed using Streamlit. It permits users to examine data and execute customer clustering analysis, in addition to visualising assorted metrics and product ratings derived from an e-commerce dataset.

# Key Features
- Display Data: Select a dataset to view sample data.
- Exploratory Data Analysis (EDA): Perform basic statistical descriptions of the selected dataset.
- RFM Analysis and Clustering: The RFM metrics may be employed for the purpose of clustering customers via the K-Means clustering algorithm.
- Visualizations:
  - The mean recency, frequency, and monetary values for each customer cluster are presented.
  - The mean product rating by category is presented herewith.
  - The total sales figures for each product category are presented herewith.
  - The distribution of product ratings.

# Installation
- Clone Repository
  Using git clone https://github.com/nrnfadya/ecommerce-data-analyst
- Install Dependencies
  Using pip for install the required libraries

# Dependencies
In order to run the application, the following libraries are required:
- streamlit
- pandas
- seaborn
- matplotlib
- scikit-learn
- os

# Running the Application
- running application with streamlit in the terminal app.py
  streamlit run app.py

# Code Explanation
- The load_data() function is initiated. The program loads data from comma-separated value files located in the data/ folder.
- To display a sample of the data, enter the name of the dataset in the command line. This function displays a sample of the data from the selected dataset.
- Electrodermal Activity (EDA) Analysis: Displays statistical descriptions for the selected dataset.
- RFM Analysis and Clustering:
  - The recency metric is calculated by merging order data with payment data.
  - The K-Means algorithm is employed for the purpose of clustering customers based on RFM metrics.
  - The software displays visual representations of the mean recency, frequency, and monetary values for each customer cluster.
- The product rating visualization presents a graphical representation of the ratings assigned to products. It displays the mean ratings and total sales figures for each product category, together with the distribution of product ratings.




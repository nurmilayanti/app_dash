import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.header('Product Analyst for Top 3 E-commerce in Indonesia')

df = pd.read_excel('top_3_ecommerce_edited10.0.xlsx')

# Menghitung total penjualan setiap e-commerce
produk_terjual_per_ecommerce = df.groupby('e_commerce')['prd_sales_1'].sum()

# Menghitung jumlah produk terjual per e-commerce
produk_per_ecommerce = df['e_commerce'].value_counts()

# Memulai layout dengan 2 kolom
col1, col2 = st.columns(2)

# Menampilkan grafik pertama di kolom pertama
with col2:
    st.write('Jumlah Produk Terjual per E-commerce') 
    st.bar_chart(produk_terjual_per_ecommerce)
  
    

# Menampilkan grafik kedua di kolom kedua
with col1:
    st.write('Jumlah Produk per per E-commerce') 
    st.bar_chart(produk_per_ecommerce,  use_container_width=True)
    
    
   

st.set_option('deprecation.showPyplotGlobalUse', False)

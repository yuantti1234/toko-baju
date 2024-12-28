import streamlit as st

# Data Produk
products = {
    "Kaos": 50000,
    "Kemeja": 100000,
    "Jaket": 150000,
    "Sweater": 125000,
}
# Header aplikasi
st.title("Penjualan Baju di Toko Arfabi")
st.subheader("Silakan pilih produk yang ingin dibeli:")

# Pilihan Produk
product = st.selectbox("Pilih produk:", list(products.keys()))

# Harga Produk
price = products[product]
st.write(f"Harga per item: Rp {price:,}")

# Jumlah Pembelian
quantity = st.number_input("Jumlah pembelian:", min_value=1, max_value=100, value=1)

# Total Harga
total_price = price * quantity
st.write(f"Total harga: Rp {total_price:,}")

# pilih ukuran 
size = st.selectbox("pilih ukuran baju:", ["S", "M", "L", "XL" ])


# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product}(s) dengan total Rp {total_price:,}.")
    st.write("Terima kasih telah berbelanja!")

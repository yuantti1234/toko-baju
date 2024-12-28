import streamlit as st

# Data produk
products = {
    "Kaos":50000,
    "Kemeja":100000,
    "Jaket":150000,
    "Sweater":125000,
}

# Header aplikasi
st.title("Penjualan Baju di Toko Arfabi")
st.subheader("Silakan pilih produk yang ingin dibeli:")

# Pilihan Produk
product = st.selectbox("Pilih produk:", list(products.keys()))

# Harga Produk
products = {
    "kaos":{"harga": 50000},
    "Kemeja":{"harga": 100000},
    "Jaket":{"harga":150000},
    "Sweater":{"harga":125000},
}
product = "kaos"
price = products[product]["harga"]

# Pilihan Ukuran
size = st.selectbox("Pilih ukuran:", ["S", "M", "L", "XL"])
st.write(f"Ukuran yang dipilih: {size}")

# Jumlah Pembelian
quantity = st.number_input("Jumlah pembelian", min_value=1, max_value=100, value=1)

# Total Harga
total_price = price * quantity
st.write(f"Total harga: Rp {total_price:,}")

# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product}(s) ukuran {size} dengan total Rp {total_price:,}.")

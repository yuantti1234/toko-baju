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

# Pilihan Produk
selected_products = st.multiselect("Pilih produk:", list(products.keys()))

# Menyimpan total harga
total_price = 0

# Memproses setiap produk yang dipilih
for product in selected_products:
    st.write(f"### {product}")

# Pilihan Ukuran
size = st.selectbox( f"Pilih ukuran {product}:", ["S", "M", "L", "XL"],
                   key=f"size_{product}"
                   )
st.write(f"ukuran yang dipilih untuk {product}: {size}")
st.write(f"Ukuran yang dipilih: {size}")

# Jumlah Pembelian
quantity = st.number_input("Jumlah pembelian", min_value=1, max_value=100, value=1)

# Menampilkan total harga keseluruhan
st.write("## Total Harga")
st.write(f"Rp {total_price:,}"
        )
        
# Total Harga
total_price = price * quantity
st.write(f"Total harga: Rp {total_price:,}")

# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product}(s) ukuran {size} dengan total Rp {total_price:,}.")

import streamlit as st

# Data produk
products = {
    "Kaos": {"harga": {"S": 50000, "M": 60000, "L": 70000, "XL": 80000}},
    "Sweater": {"harga": {"S": 120000, "M": 130000, "L": 140000, "XL": 150000}},
}

# Pilih produk
st.title("Penjualan Baju di Toko Arfabi")
st.write("Silakan pilih produk yang ingin dibeli:")

selected_products = st.multiselect("Pilih produk:", list(products.keys()))

total_price = 0

for product in selected_products:
    st.write(f"### {product}")
    
    # Pilih ukuran untuk produk
    size = st.selectbox(
        f"Pilih ukuran untuk {product}:",
        list(products[product]["harga"].keys()),
        key=f"size_{product}"
    )
    st.write(f"Ukuran yang dipilih untuk {product}: {size}")
    
    # Jumlah pembelian untuk produk
    quantity = st.number_input(
        f"Jumlah {product} (Ukuran {size}):",
        min_value=1,
        max_value=100,
        value=1,
        key=f"quantity_{product}"
    )
    
    # Hitung harga untuk produk ini
    price_per_item = products[product]["harga"][size]
    price_for_product = price_per_item * quantity
    total_price += price_for_product
    
    st.write(f"Harga untuk {product} (Ukuran {size}, {quantity} pcs): Rp {price_for_product:,}")

# Menampilkan total harga keseluruhan
st.write("## Total Harga Keseluruhan")
st.write(f"Rp {total_price:,}")
# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product}(s) ukuran {size} dengan total Rp {total_price:,}.")

import streamlit as st

# Data produk
products = {
    "Kaos": {"harga": 50000},
    "Sweater": {"harga": 125000},
}

# Pilihan Produk
selected_products = st.multiselect("Pilih produk:", list(products.keys()))

# Menyimpan total harga
total_price = 0

# Memproses setiap produk yang dipilih
for product in selected_products:
    st.write(f"### {product}")
    
    # Pilih ukuran untuk produk
    size = st.selectbox(
        f"Pilih ukuran untuk {product}:",
        ["S", "M", "L", "XL"],
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
    
    # Hitung harga total untuk produk ini
    price_per_item = products[product]["harga"]
    price_for_product = price_per_item * quantity
    total_price += price_for_product
    
    st.write(f"Harga untuk {product} ({size}, {quantity} pcs): Rp {price_for_product:,}")

# Menampilkan total harga keseluruhan
st.write("## Total Harga Keseluruhan")
st.write(f"Rp {total_price:,}")


# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product}(s) ukuran {size} dengan total Rp {total_price:,}.")

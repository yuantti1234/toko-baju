import streamlit as st

# Data produk
products = {
    "Kaos": {"harga": 50000, "ukuran": ["S", "M", "L", "XL"]},
    "Kemeja": {"harga": 100000, "ukuran": ["S", "M", "L", "XL"]},
    "Jaket": {"harga": 150000, "ukuran": ["M", "L", "XL"]},
    "Sweater": {"harga": 125000, "ukuran": ["M", "L", "XL"]},
    "Celana": {"harga": 75000, "ukuran": ["M", "L", "XL"]},
}

# Judul aplikasi
st.title("Tokoh Arfabi")
st.subheader("Penjualan Pakaian")

# Input belanjaan
st.write("### Pilih produk dan jumlah")
selected_products = {}
for product, details in products.items():
    st.write(f"{product}** - Rp{details['harga']}")
    ukuran = st.selectbox(f"Pilih ukuran untuk {product}", options=details["ukuran"], key=f"size_{product}")
    jumlah = st.number_input(f"Masukkan jumlah untuk {product}", min_value=0, step=1, key=f"qty_{product}")
    if jumlah > 0:
        selected_products[product] = {"harga": details["harga"], "ukuran": ukuran, "jumlah": jumlah}

# Total belanja
if st.button("Hitung Total"):
    total = 0
    st.write("### Rincian Belanja")
    for product, details in selected_products.items():
        subtotal = details["harga"] * details["jumlah"]
        total += subtotal
        st.write(f"{product} ({details['ukuran']}) x {details['jumlah']} = Rp{subtotal}")
    st.write(f"*Total Belanja: Rp{total}*")

# Footer
st.write("Terima kasih telah berbelanja di Tokoh Arfabi!")

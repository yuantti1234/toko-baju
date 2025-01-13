import streamlit as st
import pandas as pd
import plotly.express as px

# Data produk
products = {
    "Kaos": {"harga": 50000, "ukuran": ["S", "M", "L", "XL"], "gambar": "https://via.placeholder.com/150?text=Kaos"},
    "Kemeja": {"harga": 100000, "ukuran": ["S", "M", "L", "XL"], "gambar": "https://via.placeholder.com/150?text=Kemeja"},
    "Jaket": {"harga": 150000, "ukuran": ["M", "L", "XL"], "gambar": "https://via.placeholder.com/150?text=Jaket"},
    "Sweater": {"harga": 125000, "ukuran": ["M", "L", "XL"], "gambar": "https://via.placeholder.com/150?text=Sweater"},
    "Celana": {"harga": 75000, "ukuran": ["M", "L", "XL"], "gambar": "https://via.placeholder.com/150?text=Celana"},
}

# Judul aplikasi
st.title("Tokoh Arfabi")
st.subheader("Penjualan Pakaian")
st.image("https://via.placeholder.com/600x150?text=Selamat+Datang+di+Tokoh+Arfabi", use_column_width=True)

# Input belanjaan
st.write("### Pilih produk dan jumlah")
selected_products = {}
for product, details in products.items():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(details["gambar"], caption=product, use_column_width=True)
    with col2:
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
    if total >= 500000:
        diskon = 0.1 * total
        total -= diskon
        st.write(f"*Diskon 10%: Rp{diskon}*")
    st.write(f"*Total Belanja: Rp{total}*")

# Data pembeli
st.write("### Data Pembeli")
nama = st.text_input("Nama")
alamat = st.text_area("Alamat")
no_telepon = st.text_input("Nomor Telepon")

# Checkout
if st.button("Checkout"):
    if nama and alamat and no_telepon:
        st.success("Pesanan Anda berhasil dibuat! Terima kasih telah berbelanja.")
        st.write(f"*Nama:* {nama: tokoh_arfabi}")
        st.write(f"*Alamat:* {alamat: jln.serdang raya}")
        st.write(f"*Nomor Telepon:* {no_telepon: 082168656921}")
    else:
        st.error("Mohon lengkapi data pembeli!")

# Statistik penjualan (contoh data)
st.write("### Statistik Penjualan")
data = {"Produk": ["Kaos", "Kemeja", "Jaket", "Sweater", "Celana"], "Penjualan": [20, 15, 10, 12, 8]}
df = pd.DataFrame(data)
fig = px.bar(df, x="Produk", y="Penjualan", title="Statistik Penjualan")
st.plotly_chart(fig)

# Footer
st.write("---")
st.write("Terima kasih telah berbelanja di *Tokoh Arfabi*! Semoga harimu menyenangkan!")

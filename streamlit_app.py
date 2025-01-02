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

# Menyimpan total harga
total_price = 0

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

import streamlit as st

products = {
    "Kaos": 50000,
    "Kemeja": 100000,
    "Jaket": 150000,
    "Sweater": 125000
}

keranjang = []

# ... (sisanya kode yang sudah ada)

# Tambah tombol "Tambah ke Keranjang"
st.button("Tambah ke Keranjang", on_click=lambda: keranjang.append(product))

# Tampilkan isi keranjang
st.write("Keranjang Belanja:")
for item in items [50000, 1000000, 150000, 125000]:
for item in items :
    print(item) # cetak setiap nilai dalam list
foer item in items: # mulai perulangan untuk setiap item dalam list
total_harga = 0
for item  in items:
    print(f"harga  barang: Rp {item}")
    total_harga += item
print(f"Total harga semua barang:") Rp 
print(f"Total harga: {total_harga}")
#Tambahkan blok kode dibawah ini
    
# Total Harga
total_price = price * quantity
st.write(f"Total harga: Rp {total_price:,}")

# Tombol Konfirmasi Pembelian
if st.button("Konfirmasi Pembelian"):
    st.success(f"Pembelian berhasil! Anda membeli {quantity} {product} ukuran {size} dengan total Rp {total_price:,}.")


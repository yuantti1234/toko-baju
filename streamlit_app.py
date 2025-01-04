# Data produk baju Arfabi
products = [
    {
        'name': 'Baju Arfabi',
        'type': 'Baju',
        'sizes': ['S', 'M', 'L', 'XL'],
        'price': 150000
    },
    {
        'name': 'Celana Arfabi',
        'type': 'Celana',
        'sizes': ['S', 'M', 'L', 'XL'],
        'price': 200000
    },
    {
        'name': 'Sweater Arfabi',
        'type': 'Sweater',
        'sizes': ['S', 'M', 'L', 'XL'],
        'price': 250000
    },
    {
        'name': 'Kemeja Arfabi',
        'type': 'Kemeja',
        'sizes': ['S', 'M', 'L', 'XL'],
        'price': 180000
    }
]

# Fungsi untuk menampilkan produk
def display_products(products):
    print("Daftar Produk Baju Arfabi:")
    print("{:<20} {:<10} {:<20} {:<10}".format('Nama Produk', 'Jenis', 'Ukuran', 'Harga (IDR)'))
    print("-" * 60)
    for product in products:
        print("{:<20} {:<10} {:<20} {:<10}".format(
            product['name'],
            product['type'],
            ', '.join(product['sizes']),
            product['price']
        ))

# Menampilkan produk
display_products(products)

transactions = []

def create_transaction():
    print("=== Aplikasi PustakaOne ===")
    customer = input("Masukkan Nama Customer: ").strip()
    if not customer:
        print("Nama customer tidak boleh kosong.")
        return

    filename = f"nota_{customer.replace(' ', '_')}.txt"
    nota = open(filename, 'w')

    print("=" * 60, file=nota)
    print(f"{'NOTA PEMBELIAN':^60}", file=nota)
    print(f"Nama Customer: {customer}", file=nota)
    print("=" * 60, file=nota)
    print(f"{'Qty':<5}{'Produk':<20}{'Harga':>10}{'Total':>15}", file=nota)
    print("-" * 60, file=nota)

    total_payment = 0
    cart = []

    from buku import books
    print("\nDaftar Buku:")
    for book in books:
        print(f"ID: {book['id']}, Judul: {book['title']}, Harga: Rp.{book['price']:,.0f}")

    while True:
        book_id = input("Masukkan ID Buku (Enter untuk selesai): ").strip()
        if book_id == "":
            break

        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            print("ID Buku tidak ditemukan.")
            continue

        try:
            jumlah = int(input("Masukkan Jumlah Buku: "))
        except ValueError:
            print("Jumlah harus angka!")
            continue

        total = book['price'] * jumlah
        total_payment += total
        cart.append({"id": book['id'], "title": book['title'], "price": book['price'], "qty": jumlah})

        print(f"{jumlah:<5}{book['title']:<20}Rp{book['price']:>8,}Rp{total:>12,}", file=nota)

    if not cart:
        print("Tidak ada item di transaksi.")
        nota.close()
        return

    print("=" * 60, file=nota)
    print(f"{'TOTAL PEMBAYARAN:':>45} Rp{total_payment:>12,}", file=nota)
    print("=" * 60, file=nota)

    while True:
        try:
            bayar = int(input(f"Total: Rp{total_payment:,.0f}. Masukkan uang pembeli: Rp"))
        except ValueError:
            print("Masukkan angka!")
            continue

        if bayar < total_payment:
            print("Uang tidak cukup!")
        else:
            kembalian = bayar - total_payment
            print(f"Transaksi berhasil. Kembalian: Rp{kembalian:,.0f}")
            print(f"{'Dibayar:':>45} Rp{bayar:>12,}", file=nota)
            print(f"{'Kembalian:':>45} Rp{kembalian:>12,}", file=nota)
            break

    nota.close()
    print(f"Nota telah disimpan sebagai {filename}")

    transactions.append({"customer": customer, "items": cart, "total": total_payment})

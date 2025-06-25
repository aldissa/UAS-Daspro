books = [
    {"id": "B001", "title": "Justice League: The Flashpoint Paradox", "price": 25000},
    {"id": "B002", "title": "Secret Wars", "price": 30000}
]

def list_books():
    print("\nDaftar Buku:")
    if not books:
        print("Tidak ada buku.")
    for book in books:
        print(f"ID: {book['id']}, Judul: {book['title']}, Harga: Rp.{book['price']:,.0f}")

def add_book():
    print("\nDaftar buku sebelum ditambah:")
    list_books()

    book_id = input("Masukkan ID Buku: ")
    title = input("Masukkan Judul Buku: ")
    try:
        price = float(input("Masukkan Harga Buku: "))
    except ValueError:
        print("Harga harus berupa angka!")
        return
    books.append({"id": book_id, "title": title, "price": price})
    print("Buku berhasil ditambahkan.")

    print("\nDaftar buku terbaru:")
    list_books()
    
def edit_book():
    print("\nDaftar buku sebelum diedit:")
    list_books()

    book_id = input("Masukkan ID Buku yang akan diedit: ")
    for book in books:
        if book['id'] == book_id:
            print(f"Edit Buku ID {book_id} - Judul lama: {book['title']}, Harga lama: Rp.{book['price']:,.0f}")
            
            new_title = input("Masukkan Judul Baru (tekan Enter untuk tidak mengubah): ")
            if new_title.strip():
                book['title'] = new_title

            new_price_input = input("Masukkan Harga Baru (tekan Enter untuk tidak mengubah): ")
            if new_price_input.strip():
                try:
                    new_price = float(new_price_input)
                    book['price'] = new_price
                except ValueError:
                    print("Harga harus berupa angka! Edit dibatalkan.")
                    return

            print("Buku berhasil diedit.")

            print("\nDaftar buku terbaru:")
            list_books()
            return
    print("Buku tidak ditemukan.")

def delete_book():
    print("\nDaftar buku sebelum dihapus:")
    list_books()

    book_id = input("Masukkan ID Buku yang akan dihapus: ")
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print("Buku berhasil dihapus.")
            
            print("\nDaftar buku terbaru:")
            list_books()
            return
    print("Buku tidak ditemukan.")
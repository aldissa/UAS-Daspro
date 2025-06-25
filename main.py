from buku import list_books, add_book, delete_book, edit_book
from transaksi import create_transaction, transactions

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("Login berhasil sebagai admin.")
        return "admin"
    elif username == "kasir" and password == "kasir123":
        print("Login berhasil sebagai kasir.")
        return "kasir"
    elif username == "owner" and password == "owner123":
        print("Login berhasil sebagai owner.")
        return "owner"
    else:
        print("Login gagal.")
        return None

def main_menu(role):
    while True:
        if role == "admin":
            print("\n1. Lihat Buku\n2. Tambah Buku\n3. Hapus Buku\n4. Edit Buku\n5. Logout")
            choice = input("Pilih menu: ")
            if choice == "1":
                list_books()
            elif choice == "2":
                add_book()
            elif choice == "3":
                delete_book()
            elif choice == "4":
                edit_book()
            elif choice == "5":
                print("Logout...\n")
                break
            else:
                print("Menu tidak valid.")
        elif role == "kasir":
            print("\n1. Buat Transaksi\n2. Logout")
            choice = input("Pilih menu: ")
            if choice == "1":
                create_transaction()
            elif choice == "2":
                print("Logout...\n")
                break
            else:
                print("Menu tidak valid.")
        elif role == "owner":
            print("\n1. Lihat Total Pendapatan\n2. Logout")
            choice = input("Pilih menu: ")
            if choice == "1":
                total_income = sum(t['total'] for t in transactions)
                print(f"Total pendapatan: Rp.{total_income:,.0f}")
            elif choice == "2":
                print("Logout...\n")
                break
            else:
                print("Menu tidak valid.")

def main():
    while True:
        print("\n=== SELAMAT DATANG DI PUSTAKAONE ===")
        print("1. Login")
        print("2. Keluar")
        main_choice = input("Pilih menu: ")
        if main_choice == "1":
            role = login()
            if role:
                main_menu(role)
            else:
                print("Silakan coba login lagi.\n")
        elif main_choice == "2":
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break
        else:
            print("Menu tidak valid, silakan pilih 1 atau 2.")

main()
from collections import deque
import time

class PrinterQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_document(self, document):
        self.queue.append(document)
        print(f"Dokumen '{document}' telah ditambahkan ke antrian.")
    
    def print_documents(self):
        print("\nMulai mencetak dokumen...\n")
        while self.queue:
            current_document = self.queue.popleft()
            print(f"Mencetak '{current_document}'...")
            time.sleep(1)  # Simulasi waktu mencetak 1 detik
        print("\nSemua dokumen telah dicetak.")

def main():
    printer = PrinterQueue()
    
    while True:
        print("\nMenu:")
        print("1. Tambahkan Dokumen")
        print("2. Cetak Semua Dokumen")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ")
        
        if choice == '1':
            document_name = input("Masukkan nama dokumen: ")
            printer.add_document(document_name)
        elif choice == '2':
            printer.print_documents()
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()

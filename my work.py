import streamlit as st
import time

def main():
    st.title("Contoh Animasi Streamlit")

    # Menampilkan pesan selamat datang
    st.write("Selamat datang!")

    # Menampilkan animasi loading
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        # Memperbarui nilai animasi dan teks status
        progress_bar.progress(i + 1)
        status_text.text(f"Proses {i + 1}% selesai")

        # Menambahkan jeda waktu untuk simulasi animasi
        time.sleep(0.1)

    # Menampilkan pesan setelah animasi selesai
    st.write("Animasi selesai!")

if __name__ == "__main__":
    main()

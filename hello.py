import streamlit as st

def main():
    st.sidebar.header(":green[Web Apps Aplikasi Perhitungan COD]")
    task = st.sidebar.selectbox("Pilih Menu", ("Home", "Materi", "Rumus", "Kalkulator Perhitungan COD"))

    if task == "Home":
        Welcome_to_webapps()
    elif task == "Materi":
        penjelasan_materi()
    elif task == "Rumus":
        penjelasan_Rumus()
    elif task == "Kalkulator Perhitungan COD":
        hitung_cod()

def Welcome_to_webapps():
    st.title("Selamat Datang di Website Kami")
    st.header("KELOMPOK 5")
    daftar_nama = [
        "Agnia Zahara (2230424)",
        "Arya Dhemas Pambudhi (2230435)",
        "Ghaniyyu Halmar Indrahani (2230442)",
        "Karira Anindya (2230447)",
        "Sekar Laras (2230470)",
    ]
    cols = st.columns(len(daftar_nama))
    for i, col in enumerate(cols):
        col.write(daftar_nama[i])

def penjelasan_Rumus():
    st.title("Rumus Mencari Kadar COD Dalam Sampel")
    st.write("Berdasarkan kalkulator yang kami buat, berikut adalah rumus dari hasil yang didapat :")
    st.write("rumus kadar COD= (A-B)*N*F/V)")
    st.write("Keterangan:")
    st.write("1. A adalah volume blanko (mL)")
    st.write("2. B adalah volume pereaksi (mL)")
    st.write("3. N adalah normalitas (grek/mL)")
    st.write("4. F adalah berat ekivalen menggunakan tetapan SNI yaitu 8000 grek")
    st.write("5. V adalah volume sampel (mL)")

def hitung_cod():
    st.title("Kalkulator Kadar COD")
    st.write("Masukkan nilai untuk menghitung Kadar COD")

    volume_blanko = st.number_input("Masukkan volume blanko (mL)", 0.0)
    volume_pereaksi = st.number_input("Masukkan volume pereaksi (mL)", 0.0)
    normalitas = st.number_input("Masukkan nilai normalitas (grek/mL)", 0.0)
    berat_ekivalen_oksigen = st.number_input(
        "Masukkan berat ekivalen oksigen (grek) (Tetapan dalam SNI 8000 grek)", 8000.0)
    volume_sampel = st.number_input("Masukkan nilai volume sampel (mL)", 0.0)

    if st.button("HITUNG"):
        if volume_sampel != 0:
            cod = (volume_blanko - volume_pereaksi) * normalitas * berat_ekivalen_oksigen / volume_sampel
            st.success(f"Kadar COD adalah {cod:.2f} mg/L")

def penjelasan_materi():
    st.title("Pengertian COD")
    st.header("Apa itu COD?")
    st.write("COD (Chemical Oxygen Demand) adalah ukuran oksigen yang dikonsumsi selama dekomposisi bahan organik dan oksidasi bahan kimia anorganik seperti amonia dan nitrit. COD merupakan parameter kualitas air yang penting karena dapat menilai dampak effluen air limbah yang akan dibuang pada lingkungan penerima (badan air). Tingkat COD tinggi menandakan banyaknya jumlah bahan organik yang teroksidasi pada sampel, yang akan mengurangi tingkat oksigen terlarut (DO). Penurunan DO dapat menyebabkan kondisi anaerob, yang dapat merusak kehidupan air. Tes COD sering digunakan sebagai alternatif untuk BOD karena waktu analisa yang lebih singkat.")
    st.header("Sampel Apa Saja yang Biasa diuji Kadar COD-nya?")
    st.write("1. Influen air limbah di unit pengolahan (untuk mengetahui nilai COD awal)")
    st.write("2. Effluen air limbah di unit pengolahan (untuk mengetahui nilai COD akhir, dan untuk mengetahui efisiensi pengolahan suatu unit)")
    st.write("3. Effluen air limbah ke badan air (untuk kesesuaian terhadap baku mutu)")
    st.write("4. Badan air (untuk mengetahui nilai COD dan dapat memperkirakan dampak yang ditimbulkan)")

if __name__ == "__main__":
    main()

import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))

favImage = Image.open("favicon.png")
st.set_page_config(
    page_icon=favImage,
    page_title="Persetujuan Peminjaman Bank | IF20D"
)


def run():
    logo = Image.open('bi.png')
    logo = logo.resize((400, 125))
    st.image(logo, use_column_width=False)
    st.subheader("Persetujuan Peminjaman Bank | IF20D")

    col1, col2 = st.columns(2)

    with col1:
        # Nama Lengkap
        nm_lengkap = st.text_input('Nama Lengkap')

        # Nomor Rekening
        no_rekening = st.text_input('Nomor Rekening')

        # Jenis Kelamin
        gen_display = ('Perempuan', 'Laki-Laki')
        gen_options = list(range(len(gen_display)))
        jen_kelamin = st.selectbox("Jenis Kelamin", gen_options,
                                   format_func=lambda x: gen_display[x])

        # Status Perkawinan
        mar_display = ('Belum Menikah', 'Menikah')
        mar_options = list(range(len(mar_display)))
        stat_perkawinan = st.selectbox("Status Pernikahan", mar_options,
                                       format_func=lambda x: mar_display[x])

        # Status Pendidikan
        edu_display = ('Belum Lulus', 'Lulus')
        edu_options = list(range(len(edu_display)))
        stat_pendidikan = st.selectbox("Status Pendidikan", edu_options,
                                       format_func=lambda x: edu_display[x])

        # Status Pekerjaan
        emp_display = ('Pekerja', 'Pebisnis')
        emp_options = list(range(len(emp_display)))
        stat_pekerjaan = st.selectbox("Status Pekerjaan", emp_options,
                                      format_func=lambda x: emp_display[x])

    with col2:
        # Tanggungan
        dep_display = ('Tidak Ada', 'Satu', 'Dua', 'Lebih dari dua')
        dep_options = list(range(len(dep_display)))
        jml_tanggungan = st.selectbox("Jumlah Tanggungan",  dep_options,
                                      format_func=lambda x: dep_display[x])

        # Wilayah Tempat Tinggal
        prop_display = ('Pedesaan', 'Semi Perkotaan', 'Kota')
        prop_options = list(range(len(prop_display)))
        wil_tinggal = st.selectbox("Wilayah Tempat Tinggal", prop_options,
                                   format_func=lambda x: prop_display[x])

        # Pendapatan Bulanan Pemohon
        bln_pendapatan = st.number_input(
            "Pendapatan Bulanan Pemohon ($)", value=0)

        # Pendapatan Bulanan Pasangan Pemohon
        bln_pendapatan2 = st.number_input(
            "Pendapatan Bulanan Pasangan Pemohon ($)", value=0)

        # Jumlah Peminjaman
        jml_peminjaman = st.number_input("Jumlah Peminjaman", value=0)

        # Lama Peminjaman
        dur_display = ['2 Bulan', '6 Bulan', '8 Bulan', '12 Bulan', '16 Bulan']
        dur_options = range(len(dur_display))
        lm_peminjaman = st.selectbox("Lama Peminjaman", dur_options,
                                     format_func=lambda x: dur_display[x])

    if st.button("Proses"):
        duration = 0
        if lm_peminjaman == 0:
            duration = 60
        if lm_peminjaman == 1:
            duration = 180
        if lm_peminjaman == 2:
            duration = 240
        if lm_peminjaman == 3:
            duration = 360
        if lm_peminjaman == 4:
            duration = 480
        features = [[jen_kelamin, stat_perkawinan, jml_tanggungan, stat_pendidikan, stat_pekerjaan, bln_pendapatan,
                     bln_pendapatan2, jml_peminjaman, duration, 1, wil_tinggal]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Nama Lengkap   : " + nm_lengkap + '  \n'
                "Nomor Rekening : "+no_rekening + '  \n\n'
                "Maaf...  \nBerdasarkan hasil perhitungan kami, Anda **tidak mendapatkan persetujuan peminjaman uang** di bank kami."
            )
        else:
            st.success(
                "Nama Lengkap   : " + nm_lengkap + '  \n'
                "Nomor Rekening : "+no_rekening + '  \n\n'
                "Selamat!!!  \nBerdasarkan hasil perhitungan kami, Anda **dapat melakukan peminjaman** di bank kami."
            )


run()

import pickle
import streamlit as st

# load save model
model = pickle.load(open('voice-model.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Jenis Kelamin Berdasarkan Suara')
st.text('Nama : Muhamad Rizal Rivai')
st.text('Nim : 191351173')
st.text('Matkul : Business Intelligence')

# Form Input
meanfreq = st.text_input('Masukan Gelombang (meanfreq)')

sd = st.text_input('Masukan Gelombang (sd)')

median = st.text_input('Masukan Gelombang (median)')

Q25 = st.text_input('Masukan Gelombang (Q25)')

Q75 = st.text_input('Masukan Gelombang (Q75)')

IQR = st.text_input('Masukan Gelombang (IQR)')

skew = st.text_input('Masukan Gelombang (skew)')

kurt = st.text_input('Masukan Gelombang (kurt)')

spent = st.text_input('Masukan Gelombang (spent)')

sfm = st.text_input('Masukan Gelombang (sfm)')

mode = st.text_input('Masukan Gelombang (mode)')

centroid = st.text_input('Masukan Gelombang (centroid)')

meanfun = st.text_input('Masukan Gelombang (meanfun)')

minfun = st.text_input('Masukan Gelombang (minfun)')

maxfun = st.text_input('Masukan Gelombang(maxfun)')

meandom = st.text_input('Masukan Gelombang(meandom)')

mindom = st.text_input('Masukan Gelombang(mindom)')

maxdom = st.text_input('Masukan Gelombang (maxdom)')

dfrange = st.text_input('Masukan Gelombang (dfrange)')

modindx = st.text_input('Masukan Gelombang (modindx)')
# kode Prediksi
voice_diagnosis =''

#Button Prediksi
if st.button('Prediksi Jenis Kelamin Berdasarkan Suara'):
    voice_prediction = model.predict([[meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, spent, sfm, mode, centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx]])

    if(voice_prediction[0]== 1 ):
        voice_diagnosis = 'Perempuan'
    else:
        voice_diagnosis = 'Laki - Laki'
st.success(voice_diagnosis)
import streamlit as st

# タイトルを設定
st.title('My First Streamlit App')

# テキストを追加
st.write('Welcome to my Streamlit application!')

# サイドバーにスライダーを追加
number = st.sidebar.slider('Select a number:', 0, 100, 50)
st.write(f'Selected number: {number}')

# データフレームの表示例
import pandas as pd
import numpy as np

# サンプルデータの作成
data = pd.DataFrame({
    'Column 1': list(range(1, 11)),
    'Column 2': np.arange(10, 101, 10)
})

# データフレームを表示
st.subheader('Sample DataFrame:')
st.dataframe(data)

# チャートの表示例
st.subheader('Sample Chart:')
st.line_chart(data)

# 画像アップロード機能
st.subheader('Upload an Image:')
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
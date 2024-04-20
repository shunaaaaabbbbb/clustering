import streamlit as st
import pandas as pd

def input_csv():
    # ファイルをアップロードする
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=['csv'])
    return uploaded_file

def input_n():
    n = st.number_input("クラスタ数を入力してください", min_value=1)
    return n

def show_csv(uploaded_file):
    # ファイルがアップロードされた場合
    if uploaded_file is not None:
        # PandasのDataFrameに読み込む
        df = pd.read_csv(uploaded_file)
        #DataFrameを表示する
        return df
    
    
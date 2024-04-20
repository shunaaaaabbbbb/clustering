import streamlit as st
import pandas as pd

def download_csv():
    df_base = pd.DataFrame({"Feature_1":[],"Feature_2":[]})
    csv_base = df_base.to_csv(index=False,encoding="shift-jis")
    st.download_button("テンプレートcsvファイルをダウンロード",data = csv_base,file_name="クラスタリング_テンプレート.csv")
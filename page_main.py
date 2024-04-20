import streamlit as st
import matplotlib.pyplot as plt
from clustering import clustering
from input_show import input_csv
from input_show import input_n
from input_show import show_csv
from download import download_csv
from plot import plot_graph
from plot import plot_result


def page_main():
    st.title("このサイトはデータをクラスタリングしてくれるwebサイトです。")
    st.write("")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ボタンをクリックしてテンプレートcsvファイルをダウンロード")
        download_csv()

        st.write("")
        st.write("")

        st.subheader("クラスタ数を入力")
        n = input_n()

        st.write("")
        st.write("")

        st.subheader("データを入力したcsvファイルをアップロード")
        uploaded_file = input_csv()
        df = show_csv(uploaded_file)
        col1_1,col1_2 = st.columns(2)
        with col1_1:
            if df is not None:
                st.write(df)
                if col1_2.button("グラフを表示"):
                    with col2:
                        plot_graph(df)
                if col1_2.button("クラスタリングを実行"):
                    if n <= len(df):
                        result = clustering(df,n)
                        with col2:
                            plot_result(df,result,n)
                    else:
                        with col2:
                            st.subheader(f"クラスタ数を{len(df)}個以下に設定してください。")



  
        
        
    



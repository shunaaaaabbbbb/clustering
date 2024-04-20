import streamlit as st

def page_howto():


    st.title("このサイトの使い方")
    st.write("")
    st.subheader("「テンプレートcsvファイルをダウンロード」ボタンを押してテンプレートcsvファイルをダウンロードします。")
    st.image("image/download.png")
    st.title("\u2193")
    st.subheader("csvファイルは下図のようになっています。")
    st.image("image/csv.png")
    st.title("\u2193")
    st.subheader("ダウンロードしたcsvファイルの「Feature_1」、「Feature_2」の列にデータを入力します。")
    st.image("image/input.png")
    st.title("\u2193")
    st.subheader("データを入力し終えたらcsvファイルをアップロードしてクラスタ数を設定します。")
    st.image("image/upload.png")
    st.title("\u2193")
    st.subheader("csvファイルをアップロードすると下図のようにデータが表示され、「グラフを表示」ボタンと「クラスタリングを実行」ボタンが現れます。")
    st.image("image/upload_2.png")
    st.title("\u2193")
    st.subheader("「グラフを表示」ボタンを押すと右側にグラフが表示されます。")
    st.image("image/graph.png")
    st.title("\u2193")
    st.subheader("「クラスタリングを実行」ボタンを押すとクラスタリングされたグラフが表示されます。")
    st.image("image/clustering.png")
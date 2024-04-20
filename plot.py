import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



def plot_graph(df):
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x, y=y,  color="black", ax=ax, s=200, alpha = 0.5)
    plt.title("Graph")
    st.pyplot(fig)



def plot_result(df,result,n):
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # クラスタリング結果を可視化
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x, y=y, hue=result, palette='pastel', ax=ax, s=200, alpha = 1.0, legend=False)
    # ラベルの名前を設定
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[:], labels=[f"Cluster_{i+1}" for i in range(n)], loc='upper right')  # ラベルの名前を指定
    plt.title("Clustering Result")
    st.pyplot(fig)

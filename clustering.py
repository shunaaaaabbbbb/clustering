import streamlit as st
from sklearn.cluster import KMeans

def clustering(df,n):
    kmeans = KMeans(n_clusters=n)  # クラスタ数を適宜変更してください
    kmeans.fit(df)

    return(kmeans.labels_)
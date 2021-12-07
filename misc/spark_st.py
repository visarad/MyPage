from os import truncate
from pyspark.sql import SparkSession
import streamlit as st

spark = SparkSession.builder.appName('app').getOrCreate()

movies = spark.read.csv('movies.csv',header=True,inferSchema=True)
ratings = spark.read.csv('ratings.csv',header=True,inferSchema=True)

st.dataframe(movies.collect())
st.dataframe(ratings.collect())




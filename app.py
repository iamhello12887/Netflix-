import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.title("Netflix Data Analytics Dashboard")

# Load dataset
df = pd.read_csv("Project number 1.csv")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Dataset shape
st.subheader("Dataset Shape")
st.write(df.shape)

# Dataset columns
st.subheader("Columns")
st.write(df.columns)

# Missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Numerical columns
numeric_df = df.select_dtypes(include=np.number)

# Statistical summary
st.subheader("Statistical Summary")
st.write(numeric_df.describe())

# Correlation heatmap
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)

# Histogram
st.subheader("Histogram")

if len(numeric_df.columns) > 0:
    selected_col = st.selectbox(
        "Select Column",
        numeric_df.columns
    )

    fig2, ax2 = plt.subplots()

    ax2.hist(df[selected_col].dropna(), bins=20)

    ax2.set_title(selected_col)

    st.pyplot(fig2)

st.success("Dashboard Loaded Successfully")
import pandas as pd
import streamlit as st
from typing import Any, List, Tuple
from wordcloud import WordCloud


def df_describe(
    df: pd.DataFrame,
) -> None:
    """
    Purpose:
        Render Pandas Describe
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    st.markdown(
        """Displays basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values.
        """
    )

    st.write(df.describe())


def show_metrics(df: pd.DataFrame) -> None:
    """
    Purpose:
        Render mean,max,min,std,count metrics of numeric fields
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """

    # List of all numeric fields of given dataframe
    columns = df.select_dtypes(include='number').columns
    # selected column
    column = st.selectbox('Column', options=columns)
    column = df[column]
    # Rendering metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Mean", column.mean())
    col2.metric("Max", column.max())
    col3.metric("Min", column.min())
    col4.metric("Std", column.std())
    col5.metric("Count", int(column.count()))


def gen_wordcloud(df: pd.DataFrame) -> None:
    """
    Purpose:
        Generate Word Cloud from Column
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """

    # List of all non-numeric fields of given dataframe
    non_num_cols = df.select_dtypes(include=object).columns
    # selected column
    column = st.selectbox("Column", non_num_cols)
    column = df[column]
    # generate word cloud image from unique values of selected non-numeric field
    wc = WordCloud(
        max_font_size=25, background_color="white", repeat=True, height=500, width=800
    ).generate(
        ' '.join(column.unique())
    )
    # Display the generated image:
    st.image(wc.to_image())

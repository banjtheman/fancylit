import pandas as pd
import streamlit as st
from typing import Any, List, Tuple


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
    columns = df.select_dtypes(include='number').columns
    column = st.selectbox('Column', options=columns)
    column = df[column]
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Mean", column.mean())
    col2.metric("Max", column.max())
    col3.metric("Min", column.min())
    col4.metric("Std", column.std())
    col5.metric("Count", int(column.count()))

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

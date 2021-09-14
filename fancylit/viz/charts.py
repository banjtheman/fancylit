import pandas as pd
import altair as alt
import streamlit as st


def bar_chart(
    df: pd.DataFrame,
):
    """
    Purpose:
        Renders bar chart
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """

    x_col = st.selectbox("Select x axis for bar chart", df.columns)
    xcol_string = x_col + ":O"
    if st.checkbox("Show as continuous?", key="bar_chart_x_is_cont"):
        xcol_string = x_col + ":Q"
    y_col = st.selectbox("Select y axis for bar chart", df.columns)
    z_col = st.selectbox("Select z axis for bar chart", df.columns)

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(x=xcol_string, y=y_col, color=z_col, tooltip=list(df.columns))
        .interactive()
        .properties(title="Bar Chart for " + x_col + "," + y_col)
        .configure_title(
            fontSize=20,
        )
        .configure_axis(labelFontSize=20, titleFontSize=20)
        .configure_legend(labelFontSize=20, titleFontSize=20)
    )

    st.altair_chart(chart, use_container_width=True)

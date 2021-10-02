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


def scatter_plot(df: pd.DataFrame) -> None:
    """
    Purpose:
        Renders scatter plot
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    if isinstance(df, pd.DataFrame):
        # Column identification
        numeric_data_types = ['number', 'bool', 'float', 'int']
        categorical_data_types = ['object', 'category']
        numeric_cols = df.select_dtypes(include=numeric_data_types).columns
        categorical_cols = df.select_dtypes(
            include=categorical_data_types).columns

        # Column selection
        x_col_selection = st.selectbox(
            "Select X axis for scatter plot", numeric_cols)
        y_col_selection = st.selectbox(
            "Select Y axis for scatter plot", numeric_cols)
        z_col_selection = st.selectbox(
            "Select Category for scatter plot", categorical_cols)

        # Scatter Plot rendering
        chart = (
            alt
            .Chart(df)
            .mark_circle(size=60)
            .encode(
                x=x_col_selection,
                y=y_col_selection,
                color=z_col_selection,
                tooltip=list(df.columns),
            )
            .interactive()
        )
        st.altair_chart(chart, use_container_width=True)

    return None

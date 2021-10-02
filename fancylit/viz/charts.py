import pandas as pd
import altair as alt
import plotly.express as px
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
  
  
def chart_3d(df: pd.DataFrame):
    """
    Receives a dataframe and renders a 3D scatter plot
    
    Args:
        df(pd.DataFrame)
    Returns:
        N/A
    """
    
    if len(df.columns) < 3:
        st.warning("You need to provide a Dataframe with, at least, three columns.")
    else:
        x_col = st.selectbox("Select x axis for 3D chart", df.columns, 0)
        y_col = st.selectbox("Select y axis for 3D chart", df.columns, 1)
        z_col = st.selectbox("Select z axis for 3D chart", df.columns, 2)
        hue = None
        if st.checkbox("Do you want use different colors for groups?"):
            hue = st.selectbox("Select the column of the grouping variable", df.columns, 0)
        fig = px.scatter_3d(df, x=x_col, y=y_col, z=z_col, color=hue)
        st.plotly_chart(fig, use_container_width=True)
        
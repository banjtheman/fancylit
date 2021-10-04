import pandas as pd
import altair as alt
import plotly.express as px
import streamlit as st
import seaborn as sns

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
        st.warning(
            "You need to provide a Dataframe with, at least, three columns.")
    else:
        x_col = st.selectbox("Select x axis for 3D chart", df.columns, 0)
        y_col = st.selectbox("Select y axis for 3D chart", df.columns, 1)
        z_col = st.selectbox("Select z axis for 3D chart", df.columns, 2)
        hue = None
        if st.checkbox("Do you want use different colors for groups?"):
            hue = st.selectbox(
                "Select the column of the grouping variable", df.columns, 0)
        fig = px.scatter_3d(df, x=x_col, y=y_col, z=z_col, color=hue)
        st.plotly_chart(fig, use_container_width=True)


def pair_plot(df: pd.DataFrame) -> None:
    """
    Purpose:
        Renders pair plot
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    if len(df.columns) < 2:
        st.warning(
            "You need to provide a Dataframe with, at least, two columns.")
    else:
        x_vars = st.multiselect(
            "Select x axis for pair plot",  df.columns
        )
        y_vars = st.multiselect(
            "Select y axis for pair plot",  df.columns
        )
        # List of all non-numeric fields of given dataframe
        non_num_cols = list(df.select_dtypes(include=object).columns)
        hue = None
        # Ask for hue only if atleast 1 non-numeric column is present
        if non_num_cols and st.checkbox("Do you want use different colors for groups?", key="pair_plot"):
            hue = st.selectbox(
                "Select the column of the grouping variable", non_num_cols
            )
        # Wait until user select atleast 1 column for both x and y axes
        try:
            fig = sns.pairplot(df, x_vars=x_vars, y_vars=y_vars, hue=hue)
            st.pyplot(fig)
        except ValueError:
            pass


def line_chart(df: pd.DataFrame) -> None:
    """
    Purpose:
        Renders line chart
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    if (isinstance(df, pd.DataFrame)):
        # Column identification
        numeric_data_types = ['number', 'bool', 'float', 'int']
        numeric_cols = list(df.select_dtypes(
            include=numeric_data_types).columns)

        if len(numeric_cols) < 2:
            st.warning(
                'You need to provide a Dataframe with, at least, two columns.')
            return None

        # Column selection
        x_col_selection = st.selectbox(
            'Select X axis for line chart', numeric_cols)
        y_col_selection = st.selectbox(
            'Select Y axis for line chart', numeric_cols)

        # Line Chart rendering
        chart = (
            alt
            .Chart(df)
            .mark_line()
            .encode(
                x=x_col_selection,
                y=y_col_selection,
            )
            .interactive()
        )
        st.altair_chart(chart, use_container_width=True)

    return None

def heatmap(
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

    x_col = st.selectbox("Select x axis for the heat map", df.columns)
    xcol_string = x_col + ":O"
    if st.checkbox("Show as continuous?", key="heatmap_x_is_cont"):
        xcol_string = x_col + ":Q"
    y_col = st.selectbox("Select y axis for the heat map", df.columns)
    z_col = st.selectbox("Select z axis for the heat map", df.columns)

    source = pd.DataFrame({'x': df[x_col].ravel(),
                     'y': df[y_col].ravel(),
                     'z': df[z_col].ravel()})

    chart = (
        alt.Chart(source)
        .mark_rect()
        .encode(x='x:O', y='y:O', color='z:Q', tooltip=list(source.columns))
        .interactive()
        .properties(title="Heatmap for " + x_col + ", " + y_col)
        .configure_title(
            fontSize=20,
        )
        .configure_axis(labelFontSize=20, titleFontSize=20)
        .configure_legend(labelFontSize=20, titleFontSize=20)
    )

    st.altair_chart(chart, use_container_width=True)
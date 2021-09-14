import streamlit as st
import fancylit
import pandas as pd

###
# Streamlit Main Functionality
###


def modeling_viz_examples(df: pd.DataFrame) -> None:
    """
    Purpose:
        Shows examples for modeling
    Args:
        N/A
    Returns:
        N/A
    """

    # classification_report example
    st.write("Classification Report Example")
    fancylit.yellowbrick_funcs.show_classification_report(df)


def viz_examples(df: pd.DataFrame) -> None:
    """
    Purpose:
        Shows examples for viz
    Args:
        N/A
    Returns:
        N/A
    """

    # Start bar chart example
    st.write("Bar Chart Example")
    fancylit.viz.charts.bar_chart(df)


def sidebar() -> None:
    """
    Purpose:
        Shows the side bar
    Args:
        N/A
    Returns:
        N/A
    """

    st.sidebar.header(f"Fancylit Example")


def app() -> None:
    """
    Purpose:
        Controls the app flow
    Args:
        N/A
    Returns:
        N/A
    """

    # Spin up the sidebar
    sidebar()

    # load example csv
    df = pd.read_csv("datasets/iris.csv")

    st.write("Iris CSV data")
    st.write(df)

    # Start examples
    st.header("Viz Examples")
    viz_examples(df)

    st.header("Modeling Examples")
    modeling_viz_examples(df)


def main() -> None:
    """
    Purpose:
        Controls the flow of the streamlit app
    Args:
        N/A
    Returns:
        N/A
    """

    # Start the streamlit app
    app()


if __name__ == "__main__":
    main()

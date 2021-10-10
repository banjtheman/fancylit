import random
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import classification_report
from yellowbrick.target import FeatureCorrelation
from yellowbrick.target import ClassBalance
from streamlit_yellowbrick import st_yellowbrick
from typing import Any, List, Tuple
import plotly.express as px

def data_prep(df: pd.DataFrame) -> Tuple[List, List, List, List]:
    """
    Purpose:
        Prep data for modeling
    Args:
        df - Pandas dataframe
    Returns:
        test_features - test set features
        train_features - train set feautres
        test_target -  test set target
        train_target - train set target
    """

    # Specify the target classes
    target_string = st.selectbox("Select Target Column", df.columns)
    target = np.array(df[target_string])

    # Select Features you want
    feature_cols = st.multiselect("Select Modeling Features", df.columns)

    # Get all features
    features = df[feature_cols]
    featurestmp = np.array(features)
    feats = []
    # find all bad rows
    for index, featarr in enumerate(featurestmp):
        try:
            featarr = featarr.astype(float)
            feats.append(featarr)
        except Exception as error:

            st.error(error)
            st.error(featarr)
            st.stop()

    featuresarr = np.array(feats)

    # Split Data
    randInt = random.randint(1, 200)

    (
        test_features,
        train_features,
        test_target,
        train_target,
    ) = train_test_split(featuresarr, target, test_size=0.75, random_state=randInt)

    return (
        test_features,
        train_features,
        test_target,
        train_target,
    )


def show_classification_report(
    df: pd.DataFrame,
) -> None:
    """
    Purpose:
        Renders a classification_report
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """

    # Prep data for model training
    (
        test_features,
        train_features,
        test_target,
        train_target,
    ) = data_prep(df)

    if st.button("Train Model"):

        st.header("Classification Report")

        st.markdown(
            "The classification report visualizer displays the precision, recall, F1, and support scores for the model. In order to support easier interpretation and problem detection, the report integrates numerical scores with a color-coded heatmap. All heatmaps are in the range (0.0, 1.0) to facilitate easy comparison of classification models across different classification reports."
        )

        # Instantiate the visualizer
        visualizer = classification_report(
            GaussianNB(),
            train_features,
            train_target,
            test_features,
            test_target,
            support=True,
        )

        # Get the viz
        fig = visualizer.fig
        ax = visualizer.show()
        fig.axes.append(ax)

        # show the viz
        st.write(fig)

        # TODO download model, Download report
        # TODO live predictions

def feature_correlation(df: pd.DataFrame) -> None:
    """
    Purpose:
        Renders a feature correlation graph
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    target_string = st.selectbox("Select Target Column", df.columns,
                                 key="selectbox-feature-correlation")
    residual_cols = [col for col in df.columns if col != target_string and df[col].dtype != "object"]
    feature_cols = st.multiselect("Select Modeling Features", residual_cols,
                                  key="multiselect-feature-correlation",
                                  default=residual_cols[:5])
    
    if str(df[target_string].dtype) == "object":
        method = 'mutual_info-classification'
    else:
        type_problem = st.selectbox("Select the type of problem",
                                     ['classification', 'regression'])
        
        if type_problem == 'classification':
            method = st.selectbox("Select the correlation method",
                              ['mutual_info-classification', 'pearson'])
        else:
            method = st.selectbox("Select the correlation method",
                                ['mutual_info-regression', 'pearson'])
    try:
        viz = FeatureCorrelation(method=method,
                                feature_names=feature_cols,
                                sort=True)
        viz.fit(df[feature_cols], df[target_string])
        fig = px.bar(x=viz.scores_, y=viz.features_, title="Feature Correlation")
        st.plotly_chart(fig)
        
    except :
        st.warning("Verify the type of problem that you select")

def class_balance(df: pd.DataFrame) -> None:
    """
    Purpose:
        Renders a class balance graph
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    
    classes = st.selectbox("Select Class Column", df.columns, index = len(df.columns) - 1)
    visualizer = ClassBalance(labels = df[classes].unique())
    visualizer.fit(df[classes])
    st_yellowbrick(visualizer) 
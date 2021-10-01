# Fancylit
Fancylit is a python module that contains pre-packaged Streamlit code to render fancy visualizations, run modeling tasks, and data exploration  


## Installation
```
pip install fancylit
```

## Quick Start

Fancylit makes it incredibly easy to build fancy interactive apps:

```python
import streamlit as st
import fancylit

df = pd.read_csv("datasets/iris.csv")
st.write("Bar Chart Example")
fancylit.viz.charts.bar_chart(df)
```

![image](https://user-images.githubusercontent.com/696254/133178407-c4778344-a6c5-4db1-9402-d2c0873e3921.png)


See more examples here: https://share.streamlit.io/banjtheman/fancylit/main/example_app.py



## Hacktoberfest 2021

![Hacktoberfest](https://hacktoberfest.digitalocean.com/_nuxt/img/logo-hacktoberfest-full.f42e3b1.svg)

There are plenty of modules to create, or update all detailed in the [issues page](https://github.com/banjtheman/fancylit/issues). Complete 4 PRs during October to win a free t-shirt.

To learn more, check out their [FAQ](https://hacktoberfest.digitalocean.com/resources/participation)


If you want to build right away you can use [Gitpod](https://gitpod.io/) which provides a developer environment ready to begin coding. Simply click the button below to begin building.  

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/banjtheman/fancylit/)



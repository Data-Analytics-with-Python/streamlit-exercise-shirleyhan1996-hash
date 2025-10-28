

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Medals Visualization",
                   layout="wide")
st.title("Medals Visualization")

#下拉菜单
medal=st.selectbox("Medal Type",['gold','silver','bronze'])

#勾选
show_bar = st.checkbox("Show Bar Chart",value=True)
show_pie= st.checkbox("Show Pie Chart",value=True)

#2-col structure
col1,col2 = st.columns(2)

#load rge model wide dataset
df=px.data.medals_wide()
if show_bar:
  fig_bar=px.bar(
      df,
      x='nation',
      y=f"{medal}'
      title= "Medals count({medal})"
  )
  
  fig_bar.update_layout(
      title_x=0.5,
      xaxis_title="Country",
      yaxis_title="Count",
      width=500,
      height=500
  )
  col1.plotly_chart(fig_bar,use_container_width=True)
  
if show_pie:
  fig_pie=px.pie(
      df,
      names="Country",
      values=f"{medal}",
      title=f"Medals count({medal})"
  
  fig_pie.update_layout(
      title_x=0.5,
      width=500,
      height=500
  )
  col2.plotly_chart(fig_pie,use_container_width=True)

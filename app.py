import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Drawing Board")

with st.sidebar: 
  st.subheader("Board Properties")
  drawing_mode = st.sidebar.selectbox(
    "Drawing Tool:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )
  
  stroke_width = st.slider("Select your line width", 1, 30, 15)
  stroke_color = st.color_picker("Stroke color", "#FFFFFF", key="stroke")
  bg_color = st.color_picker("Canvas color", "#000000", key = "background")

# Create a canvas component
canvas_result = st_canvas(
  fill_color = "rgba(255, 165, 0, 0.3)", #Fixed fill color with some opacity
  stroke_width = stroke_width,
  stroke_color = stroke_color,
  background_color = bg_color,
  height = 300,
  width = 500,
  drawing_mode = drawing_mode,
  key = "canvas",
)


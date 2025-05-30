import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Drawing Board")
image = Image.open('Smeargle.png')
st.image(image, width=350)

with st.sidebar: 
  st.subheader("Board Properties")
  drawing_mode = st.sidebar.selectbox(
    "Drawing Tool:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )
  stroke_width = st.slider("Select your line width", 1, 30, 15, key = "stroke size")
  stroke_color = st.color_picker("Stroke color", "#FFFFFF", key="stroke")
  bg_color = st.color_picker("Canvas color", "#000000", key = "background")
  bg_size = st.slider("Board Size", 1,  200, 100, key = "bg size")

# Create a canvas component
canvas_result = st_canvas(
  fill_color = "rgba(255, 165, 0, 0.3)", #Fixed fill color with some opacity
  stroke_width = stroke_width,
  stroke_color = stroke_color,
  background_color = bg_color,
  height = 3*bg_size,
  width = 5*bg_size,
  drawing_mode = drawing_mode,
  key = "canvas",
)


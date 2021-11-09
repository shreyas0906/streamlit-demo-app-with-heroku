import streamlit as st
# import pandas as pd
from PIL import Image
import plotly.express as px
from memory_profiler import profile


#@profile
def main():

    # icon_image = Image.open("icon.png")
    # This should always be on the top
    PAGE_CONFIG = {"page_title" : "hello",
                   "page_icon" : '🔥️',
                   "layout" : "centered",
                   "initial_sidebar_state" : "auto"}
    st.set_page_config(**PAGE_CONFIG)
    # st.set_page_config(page_title='Hello',
    #                    page_icon='🔥️',
    #                    layout='centered',
    #                    initial_sidebar_state='auto') # can add image her  e as well. just pass the icon_image here
    st.sidebar.success("Menu")

    name = 'Shreyas'
    # Title of the page
    st.title("Hello Streamlit")

    # Header of the page
    st.header("This is a header")

    # subheader
    st.subheader("This is a sub-header")
    # text to be displayed
    st.text("Hello world this is test")
    st.text(f"This is so cool {name}")

    # Makrkdown
    st.markdown("## this is markdown")

    # displaying color text
    st.success("Successful")

    # displaying warning
    st.warning("This is danger")

    # displaying information
    st.info("This is information")

    # displaying error
    st.error("This is error")

    # displaying exception
    # st.exception("This is exception")

    # Super function
    st.write("This is a text super function ")
    st.write(1+2)

    # help info
    st.help(range)

    # This is to display dynamic pandas dataframe
    # df = pd.read_csv('iris.csv')
    # How to modify this to highlight particular cells..?
    # st.dataframe(df.style.highlight_max(axis=0))

    # This is to display static dataframes.
    # st.table(df)

    # using st.write to display table
    # st.write(df.head(5))

    # using json file
    st.json({'hi': "name"})

    # display code
    my_code = """def print_hello():
    print("hello")"""
    st.code(my_code, language='python')

    # Working with widgets

    # Working with buttons
    if st.button("submit"):
        st.text("button pressed")

    if st.button("submit", key='new_key'):
        st.text("button2 pressed")

    # working with radio buttons
    status = st.radio("what's your status", ("active", 'inactive'))
    if status == 'active':
        st.text("button is active")
    elif status == 'inactive':
        st.text("button is inactive")

    # Working with checkbox
    if st.checkbox("show/hide"):
        st.text("showing something")

    # Working with beta expander
    with st.beta_expander("Python"):
        st.text("hello python")

    # single selection selectbox
    my_languages = ["python", "java", "Go"]
    choice = st.selectbox("langues", my_languages)
    st.write(f"you selected {choice}")

    # multiple selections
    spoken_languages = ["English", "hindi", "kannada", "Tamil"]
    my_spoken_languages = st.multiselect("Spoken languages", spoken_languages)

    # sliders (only for numerical values) (int/float/dates)
    age = st.slider("Age", 1, 100, 5) # just like the range function in python

    # select slider
    colors = st.select_slider("choose color",
                              options=["yellow", "red", "black","white"],
                              value=("yellow", "red"))

    # working with media files. (videos, images, audio)
    image = Image.open("data/image_01.jpg")
    st.image(image) # use_column_width=True,

    #images from url
    # st.image("https://en.wikipedia.org/wiki/David_Goggins#/media/File:DavidGogginsMay08.jpg")

    # display videos
    video_file = open("data/secret_of_success.mp4", "rb").read()
    st.video(video_file, start_time=0)

    # working with audio files
    audio_file = open("data/song.mp3", "rb")
    st.audio(audio_file.read())

    # getting text input
    fname = st.text_input("Enter first name", max_chars=32)
    st.text(f"entered text: {fname}")

    # Text area
    message = st.text_area("Enter messagae", height=100) #  max_chars=
    st.text(f"message: {message}")

    numbers = st.number_input("Enter the number", 1.0, 25.0)
    st.text(f"numbers: {numbers}")

    #  data input
    my_appointment = st.date_input("Appointment")

    # time input
    my_time = st.time_input("Time input")

    # password
    password = st.text_input("Enter password",type='password')

    # Color input
    color = st.color_picker("Select color")

    # df_1 = pd.read_csv('data/lang_data.csv')
    # st.dataframe(df_1)

    # fig = px.pie(df_1, values='Sum', names='lang', title='pie chart')
    #
    # st.plotly_chart(fig)

    # fig2 = px.bar(df_1, x='lang', y='sum')
    # st.plotly_chart(fig2)




if __name__ == '__main__':
    main()

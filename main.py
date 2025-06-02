import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz

st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")

with st.container():
    st.write("This is inside the container")
    st.write("Hello, let's learn how to build a streamlit app together.")
    st.title("This is the app title")
    st.header("This is the header")
    st.markdown("This is the markdown")
    st.subheader("This is the subheader")
    st.caption("This is the caption")
    st.code("x = 2021")
    st.latex(r''' a+a r^1+a r^2+a r^3 ''')


    # Widget
    st.checkbox('Yes')
    st.button('Click Me')
    st.radio('Pick your gender', ['Male', 'Female'])
    st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
    st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0, 50)

    st.number_input('Pick a number', 0, 10)
    st.text_input('Email address')
    st.date_input('Traveling date')
    st.time_input('School time')
    st.text_area('Description')
    st.file_uploader('Upload a photo')
    st.color_picker('Choose your favorite color')

    # Celebration balloons
    st.balloons()

    # Progress barwith
    st.subheader('Progress bar')
    st.progress(10)

    st.subheader('Wait the execution')
    # Simulating a process delay
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success("You did it!")
    st.error("Error occurred")
    st.warning("This is a warning")
    st.info("It's easy to build a Streamlit app")
    st.exception(RuntimeError("RuntimeError exception"))

    st.subheader('A pyplot:')
    rand = np.random.normal(1, 2, size=20)
    fig, ax = plt.subplots()
    ax.hist(rand, bins=15)
    st.pyplot(fig)

    st.subheader('A line chart:')
    df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
    st.line_chart(df)

    st.subheader('A bar chart:')
    df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
    st.bar_chart(df)

    st.subheader('An area chart:')
    df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
    st.area_chart(df)

    st.subheader('An altair chart:')
    df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
    chart = alt.Chart(df).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
    st.altair_chart(chart, use_container_width=True)

    st.subheader('To display graph objects:')
    st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

    st.subheader('Display maps')
    df = pd.DataFrame(    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(df)


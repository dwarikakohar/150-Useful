import streamlit as st
st.title("Dwarika Kohar")
def sidebar():
    if st.button("About Me", icon="👋" , type="secondary"):
        st.write("## About Me")
        st.write("""
I am a passionate learner exploring the world of programming.
This is my first Streamlit website!

* 🎓 Currently learning Python and AI development
* 💻 Building projects to improve my skills
* 🌱 Always eager to learn new technologies
""")
        st.image("1.jpg", caption="Dwarika Kohar")
            
    if st.sidebar.button("My Skills", icon="💻" , type="secondary"):
        st.session_state.page = "skills"
        st.write("## My Skills")
        st.write("""
        - Python
        - HTML
        - CSS
        - Streamlit
        """)

    if st.sidebar.button("Connect With Me", icon="🤝" , type="secondary"):
        st.session_state.page = "contact"
        st.write("## Connect With Me")
        st.markdown("I am on LinkedIn at")
        st.button("LinkedIn", on_click=lambda: st.write("[LinkedIn](https://www.linkedin.com/in/dwarika-kohar-7a2aa7328/)") , icon="🔗" , type="primary")
        st.markdown("I am on GitHub at")
        st.button("GitHub", on_click=lambda: st.write("[GitHub](https://github.com/dwarikakohar)"), icon="🐱" , type="primary")
        st.markdown("I am on Twitter at")
        st.button("Twitter", on_click=lambda: st.write("[Twitter](https://x.com/DwarikaKoh33958)"), icon="🐦" , type="primary")
        st.markdown("I am on YouTube at")
        st.button("YouTube", icon="📹", on_click=lambda: st.write("[YouTube](https://www.youtube.com/@dwarika-kohar)"), type="primary")

    if st.sidebar.button("Home", icon="🏠" , type="secondary"):
        st.session_state.page = "home"
        st.write("## Home")
        st.write("Welcome to my personal website!")
        st.write("Feel free to explore the different sections using the sidebar.")

    if st.sidebar.button("Education", icon="🎓" , type="secondary"):
        st.session_state.page = "education"
        st.write("## Education")
        st.write("""
        - Completed my 10th grade from Sun Saraswati English Boarding School
        - Currently pursuing my +2 from Shanti Model Secondary School (sns.edu.np) with PCM + CS
        """)


def main():
    sidebar()
main()

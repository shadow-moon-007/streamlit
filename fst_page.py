import streamlit as st


def page():
    st.title("scraper")
    st.write("""### Enter the site you want to scrape ###""")

    iemail = st.text_input("enter email")
    ipassword = st.text_input("enter password", type="password")

    isite = st.text_input("enter site")
    ilimit = st.number_input("enter limit multiple of 50", 50)
    iok = st.button("scrape")
    if iok:
        st.write("working")
    print(iemail, ipassword, ilimit, isite)

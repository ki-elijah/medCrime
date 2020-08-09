import streamlit as st
#db
import sqlite3

conn = sqlite3.connect(data.db)
c = conn.cursor()

#fuction
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS reporttable(reporter TEXT, crime TEXT, crime_place TEXT, crime_date DATE, victim TEXT, crime_description TEXT)')

def add_data(reporter, crime, crime_place, crime_date, victim, crime_description):
    c.execute('INSERT INTO reporttable(reporter, crime, crime_place, crime_date, victim, crime_description) VALUES (?,?,?,?,?,?)',(reporter, crime, crime_place, crime_date, victim, crime_description))
    conn.commit()

def view_all():
    c.execute('SECLET * FROM reporttable')
    data = c.fetchall()
    return data


def main():

    st.title("Medical Crime")

    menu = ["Home", "View Reports", "Add Report", "Search", "Manage Reports"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        result = view_all()
        st.write(result)

    elif choice == "View Reports":
        st.subheader("View Reports")

    elif choice == "Add Report":
        st.subheader("Add Reports")
        create_table()
        reporter = st.text_input("Enter your full name")
        crime = st.text_input("Enter the crime commited")
        crime_place = st.text_input("Where did the crime happen?")
        crime_date = st.date_input("When did the crime happen?")
        victim = st.text_input("Enter victim's name")
        crime_description = st.text_area("Enter the crime commited in details",height=200)
        if st.button("Add"):
            add_data(reporter, crime, crime_place, crime_date, victim, crime_description)
            st.success("Post:{} saved".format(crime))


    elif choice == "Search":
        st.subheader("Search Reports")

    elif choice == "Manage Reports":
        st.subheader("Manage Reports")

if __name__ == "__main__":
    main()
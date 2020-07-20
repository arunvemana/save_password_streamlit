import streamlit as st
import pandas as pd
# database connection
import sqlite3
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
# create a database table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS users(user TEXT,password TEXT)')
    # HAVE TO WRITE A SCRIPT TO DELETE THE PASSWORD TABLE
    c.execute('CREATE TABLE IF NOT EXISTS Passwords1(user TEXT,site TEXT,username TEXT,password TEXT)')

def SingUp_user(username,password):
    c.execute('INSERT INTO users(user,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM  users WHERE user=? AND password=?',(username,password))
    data = c.fetchall()
    return data

def insert_password(user,site,username,password):
    try:
        c.execute('INSERT INTO passwords1(user,site,username,password) VALUES (?,?,?,?)',(user,site,username,password))
        conn.commit()
        return True
    except Exception as e:
        return False
    

def all_password(username):
    c.execute('SELECT site,username,password FROM passwords1 WHERE user =?',(username,))
    data = c.fetchall()
    return data

def main():
    """ main function"""
    
    st.title("Save your passwords")
    menu = ["Home","Login","SingUp"]
    choice = st.sidebar.selectbox("Menu",menu)
    # choice logic
    if choice == "Home":
        st.subheader("Home page")
        st.write("write now only saving of your passowrd is done")
        text = ("Future develop to share password between users").upper()
        text
        text = ("Deletion of the saved passwords").upper()
        text
        text = ("Adding of the profile page").upper()
        text
    elif choice == "Login":
        st.subheader("This is login screen")
        # login menu
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type="password")
        if st.sidebar.checkbox("Login"):
            # if password == "1234":
            create_table()
            result = login_user(username,password)
            if result:
                st.success(f"Logges in as {username}")
                user_menu = st.selectbox("Navigation",["Profile","Stored Passwords","Add Password"])
                if user_menu == "Profile":
                    st.subheader("user Profile")
                    st.text("yet to develop")
                    st.success("remaining menu is working")
                elif user_menu == "Stored Passwords":
                    st.subheader("List of the passwords")
                    password_data = all_password(username)
                    clean_db = pd.DataFrame(password_data,columns=["site","username","password"])
                    st.dataframe(clean_db)
                elif user_menu == "Add Password":
                    try:
                        st.subheader("Enter your creditionals")
                        user = username
                        site = st.text_input("site name")
                        site_username = st.text_input("username/email")
                        site_password = st.text_input("password")
                        print(user,site,site_username,site_password)
                        if st.button("Add"):
                            result = insert_password(user,site,site_username,site_password)
                            if result:
                                st.success("Data was added")
                            else:
                                st.error("Error while insert")
                    except Exception as e:
                        st.error(f"Try again,Error:{e}")
            else:
                st.warning("Incorrect Password")
        else:
            text = ("Enter your username and password in the left side menu").upper()
            text

                    
    elif choice == "SingUp":
        st.subheader("this is singup screen")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type="password")
        if st.button("Sign Up"):
            create_table()
            SingUp_user(new_user,new_password)
            st.success("You have sucessfully created a valid Account")
            st.info("Go to Login")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


if __name__== '__main__':
    main()
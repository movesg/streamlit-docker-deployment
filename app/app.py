import streamlit as st
import pandas as pd
from io import BytesIO
import csv
import streamlit.components.v1 as components
import random
import time

#Setup page
st.set_page_config(page_title = "Lucky Draw", page_icon=":confetti_ball:")

st.title("Hidden Singapore 🐈‍⬛")
st.title("🎉Lucky Draw App🎉")
st.subheader('**How it works**')

st.markdown('**Step 1**')
st.markdown('Upload spreadsheet of all players and the number of chances they have, using the template provided.')
st.markdown('**Step 2**')
st.markdown('The app will generate a list of all chances with serial numbers, assigned to each player. Download the list of chances by pressing the download button.')
st.markdown('**Step 3**')
st.markdown('Use the random number generator to generate a random winner, or you can use any random number generator.')

st.subheader('**Upload player and chances file**')
#Create winner list
def create_winner_list(col_name):
    dfdf = []
    id_index = 0
    for i in ID:
        index = 0
        while index < Points[id_index]:
            dfdf.append(col_name[id_index])
            index += 1
        id_index += 1
    return dfdf
###

#file uploader
uploaded_file = False
uploaded_file = st.file_uploader(label='Upload', type=['xlsx'])

if uploaded_file:
    st.markdown("""---""")
    st.markdown("File upload successful, displaying uploaded file.")
    df = pd.read_excel(uploaded_file, index_col=None)
    ID_Points = pd.DataFrame(df, columns=['ID', 'Phone', 'Email', 'Points'])
    st.dataframe(ID_Points)
    
    Email = (ID_Points["Email"].values)
    ID=(ID_Points["ID"].values)
    Points = (ID_Points["Points"].values)
    Phone = (ID_Points["Phone"].values)

    chances_list_phone = create_winner_list(Phone)
    chances_list_email = create_winner_list(Email)
    ""
    

    # if create button is pressed, display list of chances
    st.markdown("""---""")
    st.subheader("List of chances and serial numbers") 
    #st.dataframe(chances_list)

    #Create df for excel conversion
    chances_df = pd.DataFrame(columns=['Serial Number'])

    i=1
    #i2 = 'a'
    for email in enumerate(chances_list_email):
        #st.write('C'+str(i).zfill(4))
        chances_df.loc[i] = ['C'+str(i).zfill(4)]

        #i2 = chr(ord(i2) + 1)
        i+=1

    

    chances_df = chances_df.rename(columns = {0: "Serial Number", 1:"Phone", 2:"Email"})
    chances_df['Phone'] = chances_list_phone
    chances_df['Email'] = chances_list_email
    chances_df


    ### MAKE EXCEL FILE
    #download button
    st.download_button(
        label = "Download Chances List 📤", 
        data = chances_df.to_csv(index=False),
        file_name = "Full List of Chances and Serial Numbers.csv"
        )

    min_chance = 1
    max_chance = i-1

    st.header("Min Chance: "+ str(min_chance))
    st.header("Max Chance: "+ str(max_chance))

    #generate number button
    st.markdown("""---""")
    st.subheader('Ready to choose your winner? 😏')
    generate_button = st.button(
        label = "Generate a random number 🎲"
    )
    if generate_button:
        generated_number = random.randint(min_chance, max_chance)
        st.subheader("The lucky winner is...")

        t = st.empty()
        text = 'C'+str(generated_number).zfill(4)+"🎉"
        index = 0
        for i in range(len(text) + 1):
            time.sleep(1)
            t.markdown("## %s" % text[0:i])
            
            if index == len(text):
                st.balloons()
            index += 1
            

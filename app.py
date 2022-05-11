import streamlit as st
import random
import main
import Email
import re


st.title(" Welcome to the Question Generator ")

text = st.text_area("Enter the text here",height=500)

button1 = st.button('Submit')

if st.session_state.get('button1') != True:

    st.session_state['button1'] = button1
    
if st.session_state['button1'] == True:
    
    sentences,noun_pro,keyword_sentence_mapping,keywords_distractors_list,keyword_sentence_list = main.main(text)

    index=1

    for key in keywords_distractors_list:
        sentence = keyword_sentence_list[key][0]
        pattern = re.compile(key, re.IGNORECASE)
        output = pattern.sub( " _______ ", sentence)    
        choices = [key.capitalize()] + keywords_distractors_list[key]
        top4choices = choices[:4]
        random.shuffle(top4choices)
        st.radio(str(index) + ") " + output,top4choices)
        index = index + 1
    
    st.write("Do you want to get these into your mail ??")
    
    if st.button('Yes'):
        email = st.text_input("Enter your mail here?")
        Email.send_email(keyword_sentence_list,keywords_distractors_list,email)
        st.session_state['button1'] = False
        st.write("Thank you for using our Question Generator")
    if st.button('No'):
        st.session_state['button1'] = False
        st.write("Thank you for using our Question Generator")
else:
    st.write("Enter the text and submit")
    

    

















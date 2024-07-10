import random
import streamlit as st

st.title("Syafiq's Magic 8 Ball")
st.title("_This_ is :blue[cool] :sunglasses:")

name = st.text_input("Enter a name 👇")
question = st.text_input("Enter a question 👇")
answer = ""
random_number = random.randint(1, 11)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "NOPE!!"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Computer says: No"
elif random_number == 5:
  answer = "Dunno lah"
elif random_number == 6:
  answer = "Yes, I think"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Jein"
elif random_number == 9:
  answer = "Resounding YES"
elif random_number == 10:
  answer = "Self belief is all you need"
elif random_number == 11:
  answer = "YESSIR JAWOHL"
else:
  answer = "Error"
if name and question:
    st.subheader(name + " asks:")
    st.subheader(question, divider='rainbow')
    st.subheader("Magic 8-Ball's answer:")
    st.subheader(answer,divider='rainbow')

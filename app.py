import streamlit as st

st.set_page_config(page_title="Claude Nonprofit Assistant")

st.title("Claude Nonprofit Assistant")
st.write("Helping nonprofit organizations answer common questions.")

# Load nonprofit information

with open("nonprofit_info.txt", "r") as file:
nonprofit_info = file.read()

st.subheader("Organization Information")
st.text(nonprofit_info)

question = st.text_input("Ask a question about the nonprofit:")

if question:
question = question.lower()

```
if "volunteer" in question:
    st.success("You can volunteer by contacting help@example.org.")
elif "donate" in question:
    st.success("Donations are accepted during business hours.")
elif "hours" in question:
    st.success("Our operating hours are Monday-Friday, 9 AM to 5 PM.")
elif "services" in question:
    st.success("We provide food distribution and volunteer opportunities.")
else:
    st.info("Thank you for your question. Please contact help@example.org for additional information.")
```

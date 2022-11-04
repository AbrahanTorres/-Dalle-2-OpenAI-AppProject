import streamlit as st
#from config import *
import openai 
#import webbrowser

st.set_page_config(layout="centered", page_icon="👨‍🎨", page_title="DALL·E 2")
st.title("👨‍🎨 DALL·E 2 | GENERATOR")

# Creating the generator
message = st.text_input("Type your request for Dall·e in english  |  example: The end of the universe, digital art") 
st.write("Your request: ", message)

#openai.api_key = config["key"]

openai.api_key = st.secrets["key"]

response = openai.Image.create(
  prompt=f"{message} " ,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)


st.image(
            f"{image_url}",
            width=700, 
        )

st.markdown("### Click here to open in a new window: ")

st.write(image_url)

# Read section
field = ''' 

    ### How to use.\n

    This app use the OpenAI API to create images through a requests.
    
    The more detailed the description, the more likely you are to get the result that you want. 

    For example, try the next request:

    **a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears**

    ### Generations using python.\n

    The image generations endpoint allows you to create an original imagen given a text request..\n

    To run it in python it is important to install openai using the next command: ``` pip install openai``` \n

    ```python  

    #Create your own api key in: https://beta.openai.com/

    import openai
    openai.api_key = ' paste your api_key here'  

    response = openai.Image.create(
        prompt="The end of the universe, digital art",
        n=1,
        size="1024x1024"
            )
    image_url = response['data'][0]['url']

    ``` 
    \n

'''

st.markdown(field)

# Contact area

#def web(name, link):
#    if st.button(name):
#        webbrowser.open_new_tab(link)
#    else:
#        pass

#linkedin = web('👔 LinkedIn','https://www.linkedin.com/in/abrahan-torres/') 
#notion = web('📊 Notion','https://exultant-top-534.notion.site/Abrahan-Torres-Resume-cdc3c61b650a4fb9a225d58d0a3c47a4') 
#github = web('🎪 GitHub','https://github.com/AbrahanTorres') 
#email = web('📪 email','mailto:abrahamtorres2021@gmail.com') 
#twitter = web('👔 Twitter','https://twitter.com/AbrahamTorres_') 

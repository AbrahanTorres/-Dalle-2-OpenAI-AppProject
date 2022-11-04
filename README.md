
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://abrahantorres--dalle-2-openai-appproject-dalle-h668si.streamlit.app/)

This app use the OpenAI API to create images through a requests.

## How to use

The more detailed the description, the more likely you are to get the result that you want. 

You can visit on website to check it out: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://abrahantorres--dalle-2-openai-appproject-dalle-h668si.streamlit.app/)

For example, try the next request:


**"a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears"**

## Generations using python

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





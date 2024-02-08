import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # clear the above screen
    clear()
    put_html('<p align="left"><h2><img src="https:// media.geeksforgeeks.org/wp-content/uploads/ 20210720224119/MessagingHappyicon.png" width="7%">Fun Fact Generator</h2></p>')

    # url from where we will fetch the data
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'

    # use get request
    response = requests.request('GET',url)
    
    # load the request in json file
    data = json.loads(response.text)
    
    # we will need text from the list, so pass text in the list
    useless_fact = data['text']

    # put the facts in blue colour and put the click me button
    style(put_text(useless_fact),'color:blue;font-size:30px')
    put_buttons(
        [dict(label='Click me', value='outline-success',color='outline-success')],onclick=get_fun_fact
    )

# driver function
if __name__ == '__main__':

    # put a heading "fun fact generator"
    put_html('<p align="left"><h2><img src="https:// media.geeksforgeeks.org/wp-content/uploads/ 20210720224119/MessagingHappyicon.png" width="7%">Fun Fact Generator</h2></p>')

    # hold the session for a long time and put a click me button
    put_buttons(
        [dict(label='Click me', value='outline-success',color='outline-success')],onclick=get_fun_fact
    )
hold()
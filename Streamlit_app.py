#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.environ['NUMEXPR_MAX_THREADS'] = '4'
os.environ['NUMEXPR_NUM_THREADS'] = '2'
import numexpr as ne


# In[ ]:


import requests
import json
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets7.lottiefiles.com/packages/lf20_i9mxcD.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json)


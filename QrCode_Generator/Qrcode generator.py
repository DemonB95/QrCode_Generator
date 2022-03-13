#!/usr/bin/env python
# coding: utf-8

# In[16]:


import qrcode
import image


# In[17]:


qr=qrcode.QRCode(
version=1,box_size=15,border=5
)


# In[18]:


data="https://github.com/DemonB95?tab=repositories"


# In[19]:


qr.add_data(data)
qr.make(fit=True)


# In[22]:


img=qr.make_image(fill="black",back_color="white")


# In[23]:


img.save("qr.png")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[13]:


from flask import Flask, send_from_directory
import pymysql
import pandas as pd

app = Flask(__name__)


# In[18]:


@app.route("/download")
def index():
    connection = pymysql.connect(host='localhost',user='root',password='12345678yY',db='weather')
    # cursor = connection.cursor()
    # cursor.execute("select * from wea_data")
    sql = "select now_time,tmp,hum,cond_txt,wind_deg,wind_dir,wind_sc,pres from wea_data"
    data = pd.read_sql(sql=sql,con=connection)
    data.to_csv('/Users/ycc/Downloads/data.csv',encoding='utf-8_sig')
    return send_from_directory(r"/Users/ycc/Downloads",filename="data.csv",as_attachment=True)


# In[19]:


app.run(host="127.0.0.1", port=5000)


# In[14]:





# In[15]:





# In[17]:





# In[ ]:





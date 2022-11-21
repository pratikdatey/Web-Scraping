from flask import Flask,request,render_template,url_for
import pandas as pd
import numpy as np
from autoscraper import AutoScraper


app=Flask(__name__)

scraper=AutoScraper()
scraper.load('flipkart_watch')

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/watch', methods=['POST'])



def watch():
    price=[]
    names=[]
    image=[]
    data=pd.DataFrame(columns=['Price','Brand','Image'])
    if request.method=="POST":
        name=request.form['name']
        for i in range(0,5):
            result=scraper.get_result_similar('https://www.flipkart.com/search?q={}&page='.format(name)+str(i),group_by_alias=True)
            price.append(result['Price'])
            names.append(result['Brand'])
            image.append(result['Images'])
            df1=pd.DataFrame({'Price':price[0],'Brand':names[0],'Image':image[0]})
            data=pd.concat([df1,data])
            data=data.reset_index()
            data=data.drop(['index'],axis=1)

    if (data['Price'].empty)==True:
        return render_template('index3.html')
    else:
        return render_template('index1.html',result=data,search=name)


if __name__=='__main__':
    app.run(debug=True)


  


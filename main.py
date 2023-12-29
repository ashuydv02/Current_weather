import requests
from flask import *

ob=Flask(__name__)
@ob.route('/')
def home():
    return render_template("weather.html")

@ob.route('/show_weather',methods=['POST'])
def show():
    location=request.form.get("location")
    try:
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":location}
        headers = {
            "X-RapidAPI-Key": "c6887d588cmsh6c5cbb5a3cc763ap19cc14jsn8075fd0c0f28",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data=response.json()
        img=data['current']['condition']['icon']
        if data['current']['is_day']:
                day='Day'
                return render_template("weather.html",data=data['current'],show=1,day=day,img=img)
        else:
                day='Night'
                return render_template("weather.html",data=data['current'],show=1,day=day,img=img)
    except Exception as e:
         return str(e)

if __name__=='__main__':
    ob.run(debug=True,port=5000)

from builtins import Exception, zip

from django.shortcuts import render
from django.http import HttpResponse
#from past.builtins import raw_input

from user.models import *
from user.forms import *
from django.contrib import messages
from user.models import *
from admin1.models import *


from bs4 import BeautifulSoup
import requests
import json
from .jp import job_data
import pandas as pd


def index(request):
    return render(request,'index.html')


def userlogin(request):
    return render(request,'user/userlogin.html')

def userpage(request):
    return render(request,'user/userpage.html')

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})


def userlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        print(sname)
        spasswd = request.POST.get('spasswd')
        print(spasswd)
        try:
            check = usermodel.objects.get(email=sname, passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'user/userpage.html')
            else:
                messages.success(request, 'user  is not activated')
                return render(request, 'user/userlogin.html')
        except Exception as e:
            print('Exception is ',str(e))

        messages.success(request,'Invalid name and password')
        return render(request,'user/userlogin.html')








def search(request):
    return render(request,'user/search.html')


def searchresult(request):
    if request.method == 'POST':
        name=request.POST.get('t1')
        qs=csvdatamodel.objects.filter(name=name)
        return render(request,'user/searchresult.html',{"qs":qs})



def wbscrapp(request):
    return render(request,'user/wbscrapp.html')



def fpkart(request):
    url = 'https://www.flipkart.com/search?q=mobiles'

    res = requests.get(url).content
    soup = BeautifulSoup(res, 'html.parser')
    titles = soup.find_all('div', class_='_3wU53n')
    ratings = soup.find_all('div', class_='hGSR34')
    reviews = soup.find_all('span', class_='_38sUEc')
    prices = soup.find_all('div', class_='_1vC4OE')

    mobiles = []
    m_ratings = []
    m_reviews = []
    m_prices = []

    for title, rating, review, price in zip(titles, ratings, reviews, prices):
        # print(c, title.text,rating.text,review.text,price.text)
        mobiles.append(title.text)
        m_ratings.append(rating.text)
        m_reviews.append(review.text)
        m_prices.append(price.text)

    # Exporting to CSV files

    data = {'mobiles': mobiles, 'ratings': m_ratings, 'reviews': m_reviews, 'prices': m_prices}

    df = pd.DataFrame(data=data)

    print(df.head())

    df.to_csv('mobile_data.csv', index=False)
    print('Success..!')
    return render(request, "user/userpage.html")



def jobsearch(request):
    if request.method == 'POST':
        job = request.POST['title']
        location = request.POST['location']

        job = job.strip()
        j = job.title().strip()
        items = j.split(' ')
        location = location.strip()
        job = job.replace(' ', '+')

        url = 'https://www.indeed.co.in/jobs?q=' + job + '&amp;l=' + location + '&amp;sort=date'

        x, y, z, a, b = job_data(url, items)

        data = zip(x, y, z, a, b)

        if len(x) > 0:

            context = {
                'data': data,

            }
        else:
            context = {
                'message': 'No Jobs Found..!',

            }

        return render(request, 'user/jobsearch.html', context)

    return render(request,'user/jobsearch.html')





























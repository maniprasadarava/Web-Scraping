from builtins import next

from django.shortcuts import render
from django.http import HttpResponse
from user.models import *
from admin1.models import *
from django.contrib import messages
import csv
import io
from io import TextIOWrapper


from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup





def adminlogin(request):
    print("hello gudmng")
    return render(request, "admin1/adminlogin.html")

def logout(request):
    return render(request, "index.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname == 'admin' and  passwd == 'admin':
            return render(request,"admin1/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin1/adminloginentered.html")

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        usermodel.objects.filter(id=uname).update(status=status)
        qs=usermodel.objects.all()
        return render(request,"admin1/userdetails.html",{"qs":qs})


def userdetails(request):
    qs=usermodel.objects.all()
    return render(request,'admin1/userdetails.html',{"qs":qs})

def storecsvdata(request):
    if request.method == 'POST':
        # if request.method == "GET":
        # return render(request, template, prompt)
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = csvdatamodel.objects.update_or_create(
                name=column[0],
                rating=column[1],
                reviews=column[2],
                type=column[3],
                hq=column[4],
                employees=column[5],


            )
        context = {}

        '''
        name = request.POST.get('name')
        csvfile = TextIOWrapper(request.FILES['file'])
        # columns = defaultdict(list)
        storecsvdata=csv.DictReader(csvfile)

        for row1 in storecsvdata:
            Date = row1["Date"]
            Day = row1["Day"]
            CodedDay = row1["CodedDay"]
            Zone = row1["Zone"]
            Weather = row1["Weather"]
            Temperature = row1["Temperature"]
            Traffic = row1["Traffic"]


            storetrafficdata.objects.create(Date=Date, Day=Day, CodedDay=CodedDay,
                                          Zone=Zone, Weather=Weather, Temperature=Temperature,
                                          Traffic=Traffic)

        print("Name is ", csvfile)
        return HttpResponse('CSV file successful uploaded')
    else:
'''
    return render(request, 'admin1/storecsvdata.html', {})


def storecsvdata1(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        csvfile = TextIOWrapper(request.FILES['file'])
        # columns = defaultdict(list)
        storecsvdata = csv.DictReader(csvfile)

        for row1 in storecsvdata:
            name = row1["name"]
            rating = row1["rating"]
            reviews = row1["reviews"]
            type = row1["type"]
            hq = row1["hq"]
            employees = row1["employees"]

            csvdatamodel.objects.create(name=name, rating=rating, reviews=reviews,
                                             type=type, hq=hq, employees=employees)

        print("Name is ", csvfile)
        return HttpResponse('CSV file successful uploaded')


    else:
        return render(request, 'admin1/storecsvdata.html', {})
   



def scrapping(request):
    qs=csvdatamodel.objects.all()
    return render(request,'admin1/scrappindetails.html',{"qs":qs})

















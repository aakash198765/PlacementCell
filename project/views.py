from django.shortcuts import render
import mysql.connector

mydatabase = mysql.connector.connect(host="localhost", port=3304, user="root", passwd="", database="akash",
                                     buffered=True);
data = mydatabase.cursor()


def login(request):
    return render(request, 'login.html')


def Criteria(request):
    return render(request, 'criteria.html')


def About(request):
    return render(request, 'about.html')


def login1(request):
    val1 = request.GET['username']
    val2 = request.GET['password']
    data.execute('select * from SignInn;')
    for i in data:
        a = []
        for j in i:
            a.append(j)
        if (val1 == a[0] and val2 == a[1]):
            return render(request, 'index.html')
    return render(request, 'login.html')


def SignUp(request):
    form = request.POST
    val1 = form.get('username')
    val2 = form.get('password')
    sql = "INSERT INTO SignInn (username,password) VALUES (%s, %s)"
    val = (val1, val2)
    data.execute(sql, val)
    return render(request, 'login.html')


def stdreg(request):
    return render(request, 'studentregistration.html')


def crt(request):
    return render(request, 'criteria.html')


def placementcell(request):
    return render(request, 'placementcell.html')


def Register(request):
    if request.method == "POST":
        form = request.POST
        val1 = form.get('RegisterId')
        val2 = form.get('Studentname')
        val3 = form.get('DateOfBirth')
        val4 = form.get('City')
        val5 = form.get('MobileNumber')
        val6 = form.get('Email')
        val7 = form.get('Specification')
        sql = "INSERT INTO registration (registerid,studentname,dob,city,mob_no,email,specification) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        val = (val1, val2, val3, val4, val5, val6, val7)
        print(val)
        data.execute(sql, val)
    return render(request, 'studentregistration.html')

def placedstudents(request):
    data.execute('SELECT * FROM registration')
    records = data.fetchall()
    return render(request,'registeredstudents.html',{'data1': records})



def placed(request):
    data.execute('SELECT * FROM placementssss')
    records = data.fetchall()
    return render(request,'placedstudents.html',{'data3': records})


def high(request):
    data.execute('SELECT * from placementssss where Salary=(select MAX(Salary) from placementssss) ')
    records = data.fetchall()
    data4 = []
    for row in records:
        data4 = ({

            'StudentId': row[0],
            'RegisterId': row[1],
            'CompanyName': row[2],
            'Salary': row[3]
         })
    return render(request, 'highest.html', {'data4': data4})

def low(request):
    data.execute(' SELECT * from placementssss where Salary=(select Min(Salary) from placementssss) ')
    records = data.fetchall()
    return render(request,'placedstudents.html',{'data3': records})












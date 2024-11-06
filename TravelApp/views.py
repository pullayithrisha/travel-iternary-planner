from django.shortcuts import render
import pymysql
from datetime import datetime
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os

global username

def CancelBookingAction(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "delete from BookItinerary where booking_id='"+pid+"'"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Selected Booking Deleted : "+pid
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        else:
            data = "Error in cancelling booking"
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        

def CancelBookings(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Booking ID</font></th>'
        output+='<th><font size=3 color=black>Username</font></th>'
        output+='<th><font size=3 color=black>Package ID</font></th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Travel Date/Hotel Occupying Date</th>'
        output+='<th><font size=3 color=black>Card No</th>'
        output+='<th><font size=3 color=black>CVV No</th>'
        output+='<th><font size=3 color=black>Booking Date</th>'
        output+='<th><font size=3 color=black>Booking Type</th>'
        output+='<th><font size=3 color=black>Cancel Booking</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from BookItinerary")
            lists = result.fetchall()
            for ls in lists:
                if ls[1] == username:
                    output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[5]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[6]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[7]+'</font></td>'
                    output+='<td><font size=3 color=black>'+ls[8]+'</font></td>'
                    output+='<td><a href=\'CancelBookingAction?pid='+str(ls[0])+'\'><font size=3 color=black>Click Here to Cancel</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'UserScreen.html', context)

def ViewBookings(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Booking ID</font></th>'
        output+='<th><font size=3 color=black>Username</font></th>'
        output+='<th><font size=3 color=black>Package ID</font></th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Travel Date/Hotel Occupying Date</th>'
        output+='<th><font size=3 color=black>Card No</th>'
        output+='<th><font size=3 color=black>CVV No</th>'
        output+='<th><font size=3 color=black>Booking Date</th>'
        output+='<th><font size=3 color=black>Booking Type</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from BookItinerary")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[5]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[6]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[7]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[8]+'</font></td>'
        context= {'data':output}        
        return render(request,'EmployeeScreen.html', context)

def ViewFeedback(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Username</font></th>'
        output+='<th><font size=3 color=black>Feedback</font></th>'
        output+='<th><font size=3 color=black>Ratings</font></th>'
        output+='<th><font size=3 color=black>Feedback Date</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from feedback")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td></tr>'
        context= {'data':output}        
        return render(request,'EmployeeScreen.html', context)

def Feedbacks(request):
    if request.method == 'GET':
        return render(request,'Feedbacks.html', {})

def FeedbacksAction(request):
    if request.method == 'POST':
        global username
        feedback = request.POST.get('t1', False)
        rating = request.POST.get('t2', False)
        today = str(datetime.now())
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO feedback(username,feedback,ratings,feedback_date) VALUES('"+str(username)+"','"+feedback+"','"+rating+"','"+today+"')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Your feedback Accepted! Our employees will work on it"
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        else:
            data = "Error in adding your feedback details"
            context= {'data':data}
            return render(request,'UserScreen.html', context)

def BookHotelAction(request):
    if request.method == 'POST':
        global username
        pid = request.POST.get('t1', False)
        price = request.POST.get('t2', False)
        traveldate = request.POST.get('t3', False)
        card = request.POST.get('t4', False)
        cvv = request.POST.get('t5', False)
        arr = traveldate.split("-")
        traveldate = arr[2]+"-"+arr[1]+"-"+arr[0]
        today = str(datetime.now())
        bid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(booking_id) from BookItinerary")
            lists = result.fetchall()
            for ls in lists:
                bid = ls[0]
        if bid is not None:
            bid += 1
        else:
            bid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO BookItinerary(booking_id,username,package_id,price,travel_date,card_no,cvv_no,booking_date,booking_type) VALUES('"+str(bid)+"','"+username+"','"+pid+"','"+price+"','"+traveldate+"','"+card+"','"+cvv+"','"+today+"','Hotel')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Hotel booking details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        else:
            data = "Error in adding Hotel booking details"
            context= {'data':data}
            return render(request,'UserScreen.html', context)

def BookHotel(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        price  = request.GET['price']
        output = '<tr><td><font size="3" color="black">Transport&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Price</td><td><input type="text" name="t2" size="25" value="'+price+'" readonly/></td></tr>'
        context= {'data1':output}        
        return render(request,'BookHotel.html', context)  

def SearchHotels(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Hotel ID</font></th>'
        output+='<th><font size=3 color=black>Hotel Name</font></th>'
        output+='<th><font size=3 color=black>Room Price</font></th>'
        output+='<th><font size=3 color=black>Hotel Location</th>'
        output+='<th><font size=3 color=black>Description</th>'
        output+='<th><font size=3 color=black>Book Hotel</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from hotel")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                output+='<td><a href=\'BookHotel?pid='+str(ls[0])+'&price='+ls[2]+'\'><font size=3 color=black>Click Here to Book</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'UserScreen.html', context)

def BookTransportAction(request):
    if request.method == 'POST':
        global username
        pid = request.POST.get('t1', False)
        price = request.POST.get('t2', False)
        traveldate = request.POST.get('t3', False)
        card = request.POST.get('t4', False)
        cvv = request.POST.get('t5', False)
        arr = traveldate.split("-")
        traveldate = arr[2]+"-"+arr[1]+"-"+arr[0]
        today = str(datetime.now())
        bid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(booking_id) from BookItinerary")
            lists = result.fetchall()
            for ls in lists:
                bid = ls[0]
        if bid is not None:
            bid += 1
        else:
            bid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO BookItinerary(booking_id,username,package_id,price,travel_date,card_no,cvv_no,booking_date,booking_type) VALUES('"+str(bid)+"','"+username+"','"+pid+"','"+price+"','"+traveldate+"','"+card+"','"+cvv+"','"+today+"','Transport')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Transport booking details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        else:
            data = "Error in adding Transport booking details"
            context= {'data':data}
            return render(request,'UserScreen.html', context)

def BookTransport(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        price  = request.GET['price']
        output = '<tr><td><font size="3" color="black">Transport&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Price</td><td><input type="text" name="t2" size="25" value="'+price+'" readonly/></td></tr>'
        context= {'data1':output}        
        return render(request,'BookTransport.html', context)  

def SearchTransport(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Transport ID</font></th>'
        output+='<th><font size=3 color=black>Transport Name</font></th>'
        output+='<th><font size=3 color=black>Source Location</font></th>'
        output+='<th><font size=3 color=black>Destination Location</th>'
        output+='<th><font size=3 color=black>Departure Time</th>'
        output+='<th><font size=3 color=black>Expected Arrival Time</th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Book Transport</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from transport")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[5]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[6]+'</font></td>'
                output+='<td><a href=\'BookTransport?pid='+str(ls[0])+'&price='+str(ls[6])+'\'><font size=3 color=black>Click Here to Book Transport</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'UserScreen.html', context)

def BookItineraryAction(request):
    if request.method == 'POST':
        global username
        pid = request.POST.get('t1', False)
        price = request.POST.get('t2', False)
        traveldate = request.POST.get('t3', False)
        card = request.POST.get('t4', False)
        cvv = request.POST.get('t5', False)
        arr = traveldate.split("-")
        traveldate = arr[2]+"-"+arr[1]+"-"+arr[0]
        today = str(datetime.now())
        bid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(booking_id) from BookItinerary")
            lists = result.fetchall()
            for ls in lists:
                bid = ls[0]
        if bid is not None:
            bid += 1
        else:
            bid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO BookItinerary(booking_id,username,package_id,price,travel_date,card_no,cvv_no,booking_date,booking_type) VALUES('"+str(bid)+"','"+username+"','"+pid+"','"+price+"','"+traveldate+"','"+card+"','"+cvv+"','"+today+"','Itinerary')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Itinerary booking details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'UserScreen.html', context)
        else:
            data = "Error in adding Itinerary booking details"
            context= {'data':data}
            return render(request,'UserScreen.html', context) 

def BookItinerary(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        price  = request.GET['price']
        output = '<tr><td><font size="3" color="black">Package&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Price</td><td><input type="text" name="t2" size="25" value="'+price+'" readonly/></td></tr>'
        context= {'data1':output}        
        return render(request,'BookItinerary.html', context)  

def SearchItinerary(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Itinerary ID</font></th>'
        output+='<th><font size=3 color=black>Itinerary Package Name</font></th>'
        output+='<th><font size=3 color=black>Package Description</font></th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Book Itinerary</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from Itinerary")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><a href=\'BookItinerary?pid='+str(ls[0])+'&price='+ls[3]+'\'><font size=3 color=black>Click Here to Book</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'UserScreen.html', context) 

#============================================================================user functions above

def ModifyHotelAction(request):
    if request.method == 'POST':
        pid = request.POST.get('t1', False)
        name = request.POST.get('t2', False)
        price = request.POST.get('t3', False)
        location = request.POST.get('t4', False)
        desc = request.POST.get('t5', False)
        
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "update hotel set hotel_name='"+name+"', room_price='"+price+"', location='"+location+"', service_description='"+desc+"' where hotel_id='"+pid+"'"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Hotel details modified with ID : "+str(pid)
            context= {'data':data}
            return render(request,'Hotels.html', context)
        else:
            data = "Error in modifying Hotel details"
            context= {'data':data}
            return render(request,'Hotels.html', context)

def ModifyHotel(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from hotel where hotel_id='"+pid+"'")
            lists = result.fetchall()
            for ls in lists:
                name = ls[1]
                price = ls[2]
                location = ls[3]
                desc = ls[4]                
                break
        output = '<tr><td><font size="3" color="black">Hotel&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Hotel&nbsp;Name</td><td><input type="text" name="t2" size="25" value="'+name+'"/></td></tr>'
        output += '<tr><td><font size="3" color="black">Price</td><td><input type="text" name="t3" size="50" value="'+price+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Hotel&nbsp;Location</td><td><input type="text" name="t4" size="15" value="'+location+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Description</td><td><input type="text" name="t5" size="15" value="'+desc+'"/> </td></tr>'
        context= {'data1':output}        
        return render(request,'ModifyHotel.html', context)  


def ViewHotel(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Hotel ID</font></th>'
        output+='<th><font size=3 color=black>Hotel Name</font></th>'
        output+='<th><font size=3 color=black>Room Price</font></th>'
        output+='<th><font size=3 color=black>Hotel Location</th>'
        output+='<th><font size=3 color=black>Description</th>'
        output+='<th><font size=3 color=black>Modify</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from hotel")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                output+='<td><a href=\'ModifyHotel?pid='+str(ls[0])+'\'><font size=3 color=black>Click Here to Modify</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'Hotels.html', context)

def AddHotelAction(request):
    if request.method == 'POST':
        name = request.POST.get('t1', False)
        price = request.POST.get('t2', False)
        location = request.POST.get('t3', False)
        desc = request.POST.get('t4', False)
        
        pid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(hotel_id) from hotel")
            lists = result.fetchall()
            for ls in lists:
                pid = ls[0]
        if pid is not None:
            pid += 1
        else:
            pid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO hotel(hotel_id,hotel_name,room_price,location,service_description) VALUES('"+str(pid)+"','"+name+"','"+price+"','"+location+"','"+desc+"')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Hotel details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'AddHotel.html', context)
        else:
            data = "Error in adding hotel details"
            context= {'data':data}
            return render(request,'AddHotel.html', context)   

def AddHotel(request):
    if request.method == 'GET':
        return render(request,'AddHotel.html', {})

def Hotels(request):
    if request.method == 'GET':
        return render(request,'Hotels.html', {})

def ModifyTransportAction(request):
    if request.method == 'POST':
        pid = request.POST.get('t1', False)
        name = request.POST.get('t2', False)
        source = request.POST.get('t3', False)
        dest = request.POST.get('t4', False)
        depart = request.POST.get('t5', False)
        arrival = request.POST.get('t6', False)
        price = request.POST.get('t7', False)
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "update transport set service_name='"+name+"', source_location='"+source+"', destination_location='"+dest+"', departure_time='"+depart+"', expected_reached_time='"+arrival+"', price='"+price+"' where transport_id='"+pid+"'"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Transport details modified with ID : "+str(pid)
            context= {'data':data}
            return render(request,'Transport.html', context)
        else:
            data = "Error in modifying Transport details"
            context= {'data':data}
            return render(request,'Transport.html', context)

def ModifyTransport(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from transport where transport_id='"+pid+"'")
            lists = result.fetchall()
            for ls in lists:
                name = ls[1]
                source = ls[2]
                dest = ls[3]
                depart = ls[4]
                arrival = ls[5]
                price = ls[6]
                break
        output = '<tr><td><font size="3" color="black">Transport&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Transport&nbsp;Name</td><td><input type="text" name="t2" size="25" value="'+name+'"/></td></tr>'
        output += '<tr><td><font size="3" color="black">Source&nbsp;Location</td><td><input type="text" name="t3" size="50" value="'+source+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Destination&nbsp;Location</td><td><input type="text" name="t4" size="15" value="'+dest+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Departure&nbsp;Time</td><td><input type="text" name="t5" size="15" value="'+depart+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Arrival&nbsp;Time</td><td><input type="text" name="t6" size="15" value="'+arrival+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Price</td><td><input type="text" name="t7" size="15" value="'+price+'"/> </td></tr>'
        context= {'data1':output}        
        return render(request,'ModifyTransport.html', context)  

def ViewTransport(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Transport ID</font></th>'
        output+='<th><font size=3 color=black>Transport Name</font></th>'
        output+='<th><font size=3 color=black>Source Location</font></th>'
        output+='<th><font size=3 color=black>Destination Location</th>'
        output+='<th><font size=3 color=black>Departure Time</th>'
        output+='<th><font size=3 color=black>Expected Arrival Time</th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Modify</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from transport")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[5]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[6]+'</font></td>'
                output+='<td><a href=\'ModifyTransport?pid='+str(ls[0])+'\'><font size=3 color=black>Click Here to Modify</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'Transport.html', context)

def AddTransportAction(request):
    if request.method == 'POST':
        name = request.POST.get('t1', False)
        source = request.POST.get('t2', False)
        dest = request.POST.get('t3', False)
        depart = request.POST.get('t4', False)
        arrival = request.POST.get('t5', False)
        price = request.POST.get('t6', False)
        pid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(transport_id) from transport")
            lists = result.fetchall()
            for ls in lists:
                pid = ls[0]
        if pid is not None:
            pid += 1
        else:
            pid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO transport(transport_id,service_name,source_location,destination_location,departure_time,expected_reached_time,price) VALUES('"+str(pid)+"','"+name+"','"+source+"','"+dest+"','"+depart+"','"+arrival+"','"+price+"')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Transport details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'AddTransport.html', context)
        else:
            data = "Error in adding Transport details"
            context= {'data':data}
            return render(request,'AddTransport.html', context)   

def AddTransport(request):
    if request.method == 'GET':
        return render(request,'AddTransport.html', {})

def Transport(request):
    if request.method == 'GET':
        return render(request,'Transport.html', {})

def ModifyItineraryAction(request):
    if request.method == 'POST':
        pid = request.POST.get('t1', False)
        name = request.POST.get('t2', False)
        desc = request.POST.get('t3', False)
        price = request.POST.get('t4', False)
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "update Itinerary set package_name='"+name+"', package_description='"+desc+"',price='"+price+"' where package_id='"+pid+"'"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Itinerary details modified with ID : "+str(pid)
            context= {'data':data}
            return render(request,'Itinerary.html', context)
        else:
            data = "Error in modifying Itinerary details"
            context= {'data':data}
            return render(request,'Itinerary.html', context) 
        
def ModifyItinerary(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from Itinerary where package_id='"+pid+"'")
            lists = result.fetchall()
            for ls in lists:
                name = ls[1]
                desc = ls[2]
                price = ls[3]
                break
        output = '<tr><td><font size="3" color="black">Itinerary&nbsp;ID</td><td><input type="text" name="t1" size="25" value="'+pid+'" readonly/></td></tr>'
        output += '<tr><td><font size="3" color="black">Itinerary&nbsp;Name</td><td><input type="text" name="t2" size="25" value="'+name+'"/></td></tr>'
        output += '<tr><td><font size="3" color="black">Attraction&nbsp;Description</td><td><input type="text" name="t3" size="50" value="'+desc+'"/> </td></tr>'
        output += '<tr><td><font size="3" color="black">Package&nbsp;Price</td><td><input type="text" name="t4" size="15" value="'+price+'"/> </td></tr>'
        context= {'data1':output}        
        return render(request,'ModifyItinerary.html', context)         

def ViewItinerary(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Itinerary ID</font></th>'
        output+='<th><font size=3 color=black>Itinerary Package Name</font></th>'
        output+='<th><font size=3 color=black>Package Description</font></th>'
        output+='<th><font size=3 color=black>Price</th>'
        output+='<th><font size=3 color=black>Modify</th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from Itinerary")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><a href=\'ModifyItinerary?pid='+str(ls[0])+'\'><font size=3 color=black>Click Here to Modify</font></a></td></tr>'
        context= {'data':output}        
        return render(request,'Itinerary.html', context) 

def CreateItineraryAction(request):
    if request.method == 'POST':
        name = request.POST.get('t1', False)
        desc = request.POST.get('t2', False)
        price = request.POST.get('t3', False)
        pid = 0
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select max(package_id) from Itinerary")
            lists = result.fetchall()
            for ls in lists:
                pid = ls[0]
        if pid is not None:
            pid += 1
        else:
            pid = 1
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO Itinerary(package_id,package_name,package_description,price) VALUES('"+str(pid)+"','"+name+"','"+desc+"','"+price+"')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Itinerary details added with ID : "+str(pid)
            context= {'data':data}
            return render(request,'CreateItinerary.html', context)
        else:
            data = "Error in adding Itinerary details"
            context= {'data':data}
            return render(request,'CreateItinerary.html', context)    
            

def CreateItinerary(request):
    if request.method == 'GET':
        return render(request,'CreateItinerary.html', {})

def Itinerary(request):
    if request.method == 'GET':
        return render(request,'Itinerary.html', {})

def ViewAuthEmployee(request):
    if request.method == 'GET':
        return render(request,'ViewAuthEmployee.html', {})

def ViewAuthEmployeeAction(request):
    if request.method == 'POST':
        from_date = request.POST.get('t1', False)
        to_date = request.POST.get('t2', False)
        arr = from_date.split("-")
        if int(arr[0]) <= 9:
            arr[0] = "0"+arr[0]
        if int(arr[1]) <= 9:
            arr[1] = "0"+arr[1]
        from_date = arr[2]+"-"+arr[1]+"-"+arr[0]
        arr = to_date.split("-")
        if int(arr[0]) <= 9:
            arr[0] = "0"+arr[0]
        if int(arr[1]) <= 9:
            arr[1] = "0"+arr[1]
        to_date = arr[2]+"-"+arr[1]+"-"+arr[0]
        print(from_date+" "+to_date)
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Employee Name</font></th>'
        output+='<th><font size=3 color=black>Login Date</font></th>'
        output+='<th><font size=3 color=black>Login Status</font></th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from notification where login_date between '"+from_date+"' and '"+to_date+"'")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td></tr>'
        context= {'data':output}        
        return render(request,'AdminScreen.html', context) 


def ViewEmployee(request):
    if request.method == 'GET':
        global username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Employee Name</font></th>'
        output+='<th><font size=3 color=black>Password</font></th>'
        output+='<th><font size=3 color=black>Contact No</font></th>'
        output+='<th><font size=3 color=black>Email ID</font></th>'
        output+='<th><font size=3 color=black>Address</font></th></tr>'
        mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        with mysqlConnect:
            result = mysqlConnect.cursor()
            result.execute("select * from employee")
            lists = result.fetchall()
            for ls in lists:
                output+='<tr><td><font size=3 color=black>'+str(ls[0])+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[3]+'</font></td>'
                output+='<td><font size=3 color=black>'+ls[4]+'</font></td></tr>'
        context= {'data':output}        
        return render(request,'AdminScreen.html', context) 

def AddEmployeeAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        address = request.POST.get('t5', False)
        page = None
        dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
        dbcursor = dbconnection.cursor()
        qry = "INSERT INTO employee(username,password,phone_no,email,address) VALUES('"+str(username)+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
        dbcursor.execute(qry)
        dbconnection.commit()
        if dbcursor.rowcount == 1:
            data = "Employee details added"
            context= {'data':data}
            return render(request,'AddEmployee.html', context)
        else:
            data = "Error in adding employee details"
            context= {'data':data}
            return render(request,'AddEmployee.html', context)
        
def EmployeeScreen(request):
    if request.method == 'GET':
        return render(request,'EmployeeScreen.html', {})
        
def AddEmployee(request):
    if request.method == 'GET':
        return render(request,'AddEmployee.html', {})

def index(request):
    if request.method == 'GET':
        return render(request,'index.html', {})

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})        

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})
    
def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def EmployeeLogin(request):
    if request.method == 'GET':
       return render(request, 'EmployeeLogin.html', {})

def FAQ(request):
    if request.method == 'GET':
       return render(request, 'FAQ.html', {})    

def isUserExists(username):
    is_user_exists = False
    global details
    mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
    with mysqlConnect:
        result = mysqlConnect.cursor()
        result.execute("select * from user_signup where username='"+username+"'")
        lists = result.fetchall()
        for ls in lists:
            is_user_exists = True
    return is_user_exists    

def RegisterAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        address = request.POST.get('t5', False)
        record = isUserExists(username)
        page = None
        if record == False:
            dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
            dbcursor = dbconnection.cursor()
            qry = "INSERT INTO user_signup(username,password,phone_no,email,address) VALUES('"+str(username)+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            dbcursor.execute(qry)
            dbconnection.commit()
            if dbcursor.rowcount == 1:
                data = "Signup Done! You can login now"
                context= {'data':data}
                return render(request,'Register.html', context)
            else:
                data = "Error in signup process"
                context= {'data':data}
                return render(request,'Register.html', context) 
        else:
            data = "Given "+username+" already exists"
            context= {'data':data}
            return render(request,'Register.html', context)


def checkUser(uname, password, utype):
    global username
    msg = "Invalid Login Details"
    mysqlConnect = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
    with mysqlConnect:
        result = mysqlConnect.cursor()
        result.execute("select * from "+utype+" where username='"+uname+"' and password='"+password+"'")
        lists = result.fetchall()
        for ls in lists:
            msg = "success"
            username = uname
            break
    return msg

def UserLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        msg = checkUser(username, password, "user_signup")
        if msg == "success":
            context= {'data':"Welcome "+username}
            return render(request,'UserScreen.html', context)
        else:
            context= {'data':msg}
            return render(request,'UserLogin.html', context)
        
def EmployeeLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        msg = checkUser(username, password, "employee")
        if msg == "success":
            today = str(datetime.now())
            dbconnection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Travel',charset='utf8')
            dbcursor = dbconnection.cursor()
            qry = "INSERT INTO notification(employee_name,login_date,login_status) VALUES('"+str(username)+"','"+today+"','Successful')"
            dbcursor.execute(qry)
            dbconnection.commit()
            context= {'data':"Welcome "+username}
            return render(request,'EmployeeScreen.html', context)
        else:
            context= {'data':msg}
            return render(request,'EmployeeLogin.html', context)


def AdminLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if username == 'admin' and password == 'admin':
            context= {'data':"Welcome "+username}
            return render(request,'AdminScreen.html', context)
        else:
            context= {'data':msg}
            return render(request,'AdminLogin.html', context)
            







        


        

from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('AdminLogin.html', views.AdminLogin, name="AdminLogin"), 
	       path('EmployeeLogin.html', views.EmployeeLogin, name="EmployeeLogin"), 
	       path('UserLogin.html', views.UserLogin, name="UserLogin"), 
	       path('FAQ.html', views.FAQ, name="FAQ"), 
	       path('Register.html', views.Register, name="Register"),
	       path('RegisterAction', views.RegisterAction, name="RegisterAction"),	
	       path('UserLoginAction', views.UserLoginAction, name="UserLoginAction"),	
	       path('EmployeeLoginAction', views.EmployeeLoginAction, name="EmployeeLoginAction"),	
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('AddEmployee.html', views.AddEmployee, name="AddEmployee"), 
	       path('AddEmployeeAction', views.AddEmployeeAction, name="AddEmployeeAction"),
	       path('ViewEmployee', views.ViewEmployee, name="ViewEmployee"),	
	       path('ViewAuthEmployee.html', views.ViewAuthEmployee, name="ViewAuthEmployee"), 
	       path('ViewAuthEmployeeAction', views.ViewAuthEmployeeAction, name="ViewAuthEmployeeAction"),
	       path('Itinerary.html', views.Itinerary, name="Itinerary"), 
	       path('CreateItinerary.html', views.CreateItinerary, name="CreateItinerary"), 
	       path('CreateItineraryAction', views.CreateItineraryAction, name="CreateItineraryAction"),
	       path('ViewItinerary', views.ViewItinerary, name="ViewItinerary"),
	       path('ModifyItinerary', views.ModifyItinerary, name="ModifyItinerary"),
	       path('ModifyItineraryAction', views.ModifyItineraryAction, name="ModifyItineraryAction"),
	       path('Transport.html', views.Transport, name="Transport"), 
	       path('AddTransport.html', views.AddTransport, name="AddTransport"), 
	       path('AddTransportAction', views.AddTransportAction, name="AddTransportAction"),
	       path('ViewTransport', views.ViewTransport, name="ViewTransport"),
	       path('ModifyTransport', views.ModifyTransport, name="ModifyTransport"),
	       path('ModifyTransportAction', views.ModifyTransportAction, name="ModifyTransportAction"),
	       path('Hotels.html', views.Hotels, name="Hotels"), 
	       path('AddHotel.html', views.AddHotel, name="AddHotel"), 
	       path('AddHotelAction', views.AddHotelAction, name="AddHotelAction"),
	       path('ViewHotel', views.ViewHotel, name="ViewHotel"),
	       path('ModifyHotel', views.ModifyHotel, name="ModifyHotel"),
	       path('ModifyHotelAction', views.ModifyHotelAction, name="ModifyHotelAction"),
	       path('EmployeeScreen', views.EmployeeScreen, name="EmployeeScreen"),
	       path('SearchItinerary', views.SearchItinerary, name="SearchItinerary"),
	       path('BookItinerary', views.BookItinerary, name="BookItinerary"),
	       path('BookItineraryAction', views.BookItineraryAction, name="BookItineraryAction"),
	       path('SearchTransport', views.SearchTransport, name="SearchTransport"),
	       path('BookTransport', views.BookTransport, name="BookTransport"),
	       path('BookTransportAction', views.BookTransportAction, name="BookTransportAction"),
	       path('SearchHotels', views.SearchHotels, name="SearchHotels"),
	       path('BookHotel', views.BookHotel, name="BookHotel"),
	       path('BookHotelAction', views.BookHotelAction, name="BookHotelAction"),
	       path('Feedbacks.html', views.Feedbacks, name="Feedbacks"), 
	       path('FeedbacksAction', views.FeedbacksAction, name="FeedbacksAction"),
	       path('ViewFeedback', views.ViewFeedback, name="ViewFeedback"),
	       path('ViewBookings', views.ViewBookings, name="ViewBookings"),
	       path('CancelBookings', views.CancelBookings, name="CancelBookings"),
	       path('CancelBookingAction', views.CancelBookingAction, name="CancelBookingAction"),
]

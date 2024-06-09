from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Product
import mysql.connector
import smtplib

# Create your views here.

def login(request):
    template = "login.html"
    return render(request,template)
def index(request):
    template = "index.html"
    return render(request,template)

def home(request):
    template = 'home.html'
    return render(request,template)

def contact(request):
    if request.method == 'POST':
        print('in register post event')
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="name"
        )
        mycursor = conn.cursor()

        # Retrieve post details
        email = request.POST['email']
        pwd = request.POST['pwd']
        cp=request.POST['cpwd']

        # Execute the SQL query with proper syntax
        mycursor.execute("INSERT INTO regestration (email, password,conform_password) VALUES (%s, %s,%s)", (email, pwd,cp))
        
        conn.commit()
        
        return redirect('index')
    else:
        return render(request, 'contact.html')  
def products(request):
    template = "products.html"
    return render(request,template)
def about(request):
    template = "about.html"
    return render(request,template)

def email_send(request, mailss):
    my_acc = "isolatedman100@gmail.com"
    passs = "ijzz bmdr wyyn przh"

    if request.method == 'POST':
        # Use SMTP_SSL for a secure connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connect:
            try:
                connect.login(user=my_acc, password=passs)

                # Create the email message
                subject = "E-HUB"
                body = "congratulations YOU HAVE BEEN SUCCESFULLY REGISTERD FOR THE EVENT "
                message = f"Subject: {subject}\n\n{body}"

                # Send the email
                connect.sendmail(from_addr=my_acc, to_addrs=mailss, msg=message)

                print("Email sent successfully!")

            except smtplib.SMTPAuthenticationError as e:
                print(f"Authentication failed: {e}")
            except Exception as e:
                print(f"Error: {e}")

            return render(request,'index.html')

    # Handle GET requests or any other logic if needed
    return HttpResponse("Invalid request")
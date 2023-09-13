from django.shortcuts import redirect, render
from Blog_App.models import Blog_A,Contactus
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# for email 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# end email


@login_required(login_url='login')
def home(request):
        blog = Blog_A.objects.all()
        return render(request,'home.html',{'blog':blog})

@login_required(login_url='login')
def more_detail(request,id):
        blog = Blog_A.objects.get(id=id)
        context = {
            'blog':blog,
        }
        return render(request,'more_detail.html',context)


def register(request):
    if request.method=='POST':
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       password1=request.POST['password1']
       if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,('username Taken'))
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,('email Taken')) 
                return redirect('register')
            else: 
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                return redirect('login')
       else:
            messages.info(request,('password not valid..'))
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,('invlid username/password'))    
        
    else:    
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')    

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contactus = Contactus.objects.create(name=name,email=email,subject=subject,message=message)
        contactus.save()

        # email

        fromaddr = "ayushisharma0059@gmail.com"
        toaddr = email
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = subject
        
        # string to store the body of the mail
        body = 'thanks for contacting us we can get to you soon' + message
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "sapna@1234")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()

        return redirect('contactus')
    else:
        return render(request,'contactus.html')

   

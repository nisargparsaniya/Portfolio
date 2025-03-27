from django.core.mail import send_mail   # here we import send_mail function which is used to send mail 
from django.shortcuts import render
from django.http import HttpResponse

def smtp(request):
    if request.method == 'POST':    # here we check if the request method is POST or not

        # alert_message = "Form submitted successfully!"


        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        msg = request.POST.get('msg')

        # user/developer name
        user = "Nisarg Parsaniya"

        # Email content

        # we can change the view of mail accoording to our need
        # we can also use html tags in the email_message

        subject = f"Hello {user} you got a message from {name}"
        email_message = (
            f"hey Mr {user} You've Got A Mail From {name}\n"
            "-----------------------------------------\n\n"
            "Details of the sender :\n\n"
            "-----------------------------------------\n"
            f"--> Name : {name}\n"
            f"--> Phone Number : {phone}\n"
            f"--> Email ID : {mail}\n"
            f"--> Message : {msg}\n"
            "-----------------------------------------\n\n"
        )
        # recipient email   # here we can add multiple email id's   # your email id where you want to send the mail
        recipient_email = 'nisargparsaniya@gmail.com'

        # we call here send mail function which is inbuilt function in django
        send_mail(subject, email_message, mail,[recipient_email])

        # after sending the mail we return a message to the user
        # we can also redirect to another page NOTE : we can change return page as per our need
        # return HttpResponse("Thank you,for contact us, Your message has been sent.(we will contact you soon)")
                # return render(request,'HOME.html')
    return render(request, 'nisarg.html') 
    # return render(request, 'nisarg.html', {'alert_message': alert_message}) 
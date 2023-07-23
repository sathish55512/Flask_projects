from flask import Flask, render_template, request, url_for,redirect
from email.message import EmailMessage
import ssl,smtplib,random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mail = request.form['mail']
        email_sender = 'sathishreigns428@gmail.com'
        email_password = 'ssbxvufiqmkvdbvj'
        email_receiver = mail
        n = random.randint(1,8)

        subject = "0"
        body = "0"

        if email_receiver == 'sssk3037@gmail.com' or email_receiver == 'sureshkumar.s@nandhatech.org':
            subject = "HI Suresh Iam Sathish"
            body = """
You are the kind and Humble person i Ever met 
Then you are so smart
One day you'll be a Greatest Enterpruner like Elon Musk
We came a long day, From where we begin . it will continue till the end
Today is your lucky day, Do what ever you Want Today 
                   """
        elif n == 1:
            subject = "This is Sathish Wants To Tell You"
            body = """
Veerame jeyam
                   """
        elif n == 2:
            subject = "This is Sathish Wants To Tell You"
            body = """
Ulagin Thalai Sirantha soll "Seyal"
                   """
        elif n == 3:
            subject = "This is Sathish Wants To Tell You"
            body = """
Unnala Mudiyathunu Yarrchum Unkita Sonna 
Nee Namba Vendiyathu Avungala Illa Unna 
                   """
        elif n == 4:
            subject = "This is Sathish Wants To Tell You"
            body = """
Intha ulagam jeychiduvenu sonna kekathu
ana Jeyichavan sonna kekum
                   """   
        elif n == 5:
            subject = "This is Sathish Wants To Tell You"
            body = """
Muyalum jeykum Aamaiyum jeukum
Ana Muyalamai jeykathu
                   """ 
        elif n == 6:
            subject = "This is Sathish Wants To Tell You"
            body = """
Unthan valvum oru olymphics ai pole veyarvai vetri tharum
                   """ 
        elif n == 7:
            subject = "This is Sathish Wants To Tell You"
            body = """
Inna seitharai oruthal avarnaana 
nanaiyum seithu vidal
                   """    
        elif n == 8:
            subject = "This is Sathish Wants To Tell You"
            body = """
Mudiyumnu nambuna yarru venunmnalum enna venunalum agalam sir
                   """                 

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return redirect(url_for("endex"))
    return render_template('index.html')

@app.route('/endex')
def endex():
     return render_template('endex.html')

if __name__ == '__main__':
    app.run(debug=True)






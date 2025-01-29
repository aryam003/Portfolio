from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aryamarya537@gmail.com'
app.config['MAIL_PASSWORD'] = 'mggb ctmh vpmb azcq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_mail',methods=['POST'])
def send_message():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    message=request.form['message']
    msg = Message(subject='Hello', sender=email, recipients=['aryamarya537@gmail.com'])
    # msg.body = f"From: {name}\n {email}\n phone: \n{phone} \n Message:\n{message}"
    # mail.send(msg)
    msg = Message(subject='Hello', sender=email, recipients=['aryamarya537@gmail.com'])
    msg.body = f"From: {name}\n{email}\nPhone: {phone}\nMessage:\n{message}"  # Plain text version (for email clients that don't support HTML)
    msg.html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <h3 style="color: #4CAF50;">New Message from {name}</h3>
            <p><strong>From:</strong> {name} ({email})</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Message:</strong></p>
            <p style="border: 1px solid #ddd; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">
                {message}
            </p>
        </body>
    </html>
    """
    mail.send(msg)
    return render_template('index.html', success=True)


app.run()
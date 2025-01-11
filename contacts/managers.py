from django.db import models
from bands.models import Band
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ContactManager(models.Manager):

  @staticmethod
  def forward_to_band(form):
    band = Band.objects.get(id=form.data['band_id'])
    
    if form.data['add_to_mailer']:
      band.contact_set.create(name=form.data['name'],email=form.data['email'],phone=form.data['phone'])
      
    port = band.smtp_port
    smtp_server = band.smtp_server
    sender_email = band.email
    receiver_email = band.email
    password = band.email_password
    message = MIMEMultipart("alternative")
    message["Subject"] = form.data['message_subject']
    message["From"] = sender_email
    message["To"] = receiver_email
    
    text = """\
      New Contact Form Submission:
      Name: """ + form.data['name'] + """
      Reply to: """ + form.data['email'] + """
      Phone: """ + form.data['phone'] + """
      
      Message:
      """ + form.data['message_body'] + """
      
      """ + ("Added to mailing list!" if form.data['add_to_mailer'] else "") + """
      """
      
    html = """\
    <html>
      <body>
        <h2>New Contact Form Submission</h2>
        <p>
          <b>Name:</b> """ + form.data['name'] + """<br>
          <b>Reply to:</b> """ + form.data['email'] + """<br>
          <b>Phone:</b> """ + form.data['phone'] + """<br>
        </p>
        <h3>Message:</h3>
        <p>""" + form.data['message_body'] + """</p>
        """ + ("<p><i>Added to mailing list!</i></p>" if form.data['add_to_mailer'] else "") + """
      </body>
    </html>
    """       
      
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)
    message.attach(part2)
    
    try:
        # Create connection with server and send email
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
        raise
    finally:
        server.quit()

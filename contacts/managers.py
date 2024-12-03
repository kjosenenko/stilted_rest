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
      
    port = band.smtp_port  # For SSL
    smtp_server = band.smtp_server
    sender_email = band.email  # Enter your address
    receiver_email = band.email  # Enter receiver address
    password = band.email_password # Enter password
    message = MIMEMultipart("alternative")
    message["Subject"] = form.data['message_subject']
    message["From"] = sender_email
    message["To"] = receiver_email
    
    text = """\
      New Reservation generated for:
      Name: """ + form.data['name'] + """"
      Reply to: """ + form.data['email'] + """"
      Phone: """ + form.data['phone'] + """"

      """ + form.data['message_body']
      
    html = """\
    <html>
      <body>
        <p>
          <b>Name:</b> """ + form.data['name'] + """<br>
          <b>Reply to:</b> """ + form.data['email'] + """<br>
          <b>Phone:</b> """ + form.data['phone'] + """<br><br>
          """ + form.data['message_body'] + """<br>
        </p>
      </body>
    </html>
    """       
      
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )

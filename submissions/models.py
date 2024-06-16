from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import smtplib, ssl

class Submission(models.Model):
  contact_name = models.CharField(max_length=128, blank=True, null=True)
  contact_email = models.CharField(max_length=128, blank=True, null=True)
  contact_phone = models.CharField(max_length=128, blank=True, null=True)
  message_subject = models.CharField(max_length=128, blank=True, null=True)
  message_body = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
@receiver(post_save, sender=Submission)
def send_email(sender, instance, **kwargs):
  print(instance.contact_name)
  print(instance.contact_email)
  print(instance.contact_phone)
  print(instance.message_subject)
  print(instance.message_body)
  
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "stilted.band@gmail.com"  # Enter your address
  receiver_email = "stilted.band@gmail.com"  # Enter receiver address
  password = "" # Enter password
  message = MIMEMultipart("alternative")
  message["Subject"] = instance.message_subject
  message["From"] = sender_email
  message["To"] = receiver_email
  
  text = """\
    New Reservation generated for:
    Name: """ + instance.contact_name + """"
    Reply to: """ + instance.contact_email + """"
    Phone: """ + instance.contact_phone + """"

    """ + instance.message_body
    
  html = """\
  <html>
    <body>
      <p>
        <b>Name:</b> """ + instance.contact_name + """<br>
        <b>Reply to:</b> """ + instance.contact_email + """<br>
        <b>Phone:</b> """ + instance.contact_phone + """<br><br>
        """ + instance.message_body + """<br>
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
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )

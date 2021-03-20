#!/usr/bin/env python3
import emails
import reports
import os
imoirt sys

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = 'Upload Completed - Online Fruit Stroe'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
message = emails.generate_email(sender, receiver, 

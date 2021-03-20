#!/usr/bin/env python3
import emails
import reports
import os
imoirt sys

report_path = '/home/username'
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = 'Upload Completed - Online Fruit Stroe'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
table_data = 
reports.generate_report(report_path, 'Processed Update on ' + os.getdate(), table_data)
message = emails.generate_email(sender, receiver, subject, body, report_path)
email.send(message)

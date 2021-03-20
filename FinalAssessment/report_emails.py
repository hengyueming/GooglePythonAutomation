#!/usr/bin/env python3
import emails
import reports
import os
import sys
import datetime

path = 'supplier-data/descriptions/'
files = os.listdir(path)
date = datetime.datetime.now().strftime('%m-%d-%Y')

def get_data(files):
  data = ""
  for file in files:
    if file.endswith('.txt'):
      with open(path + file, 'r') as f:
        line = f.readlines()
        name = line[0].strip()
        weight = line[1].strip()
        data += 'name: ' + name + '<br/>' + 'weight: ' + weight + '<br/><br/>'
  return data

if __name__ == "__main__":
  table_data = get_data(files)
  report_path = '/tmp/processed.pdf'
  reports.generate_report(report_path, 'Processed Update on ' + date, table_data)
  
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = 'Upload Completed - Online Fruit Stroe'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
  attachment = '/tmp/processed.pdf'
  message = emails.generate_email(sender, receiver, subject, body, report_path)
  
  emails.send_email(message)

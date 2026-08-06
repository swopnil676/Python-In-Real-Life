import webbrowser
import urllib.parse

email = "innovatetechlearning@gmail.com"
subject = "Test Email"
body = "This email was sent using Python automation!"

# Encode text for URL
subject_encoded = urllib.parse.quote(subject)
body_encoded = urllib.parse.quote(body)

# Gmail compose URL
url = (
    f"https://mail.google.com/mail/?view=cm&fs=1"
    f"&to={email}"
    f"&su={subject_encoded}"
    f"&body={body_encoded}"
)

webbrowser.open(url)
print("Email window opened")
import webbrowser
import urllib.parse

email = "innovatetechlearning@gmail.com"
subject = urllib.parse.quote("Test Email")
body = urllib.parse.quote("This email was sent using Python automation!")

webbrowser.open(
    f"mailto:{email}?subject={subject}&body={body}"
)
print("open window")
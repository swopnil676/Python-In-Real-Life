links =[
    "www.b001.io",
    "www.youtube.com",
    "www.google.com",
    "www.wikipidia.org"
]
    # Method 1 :-
for link in links:
    print(link.lstrip("www.")) 
# Output =>
#         b001.io
#         youtube.com
#         google.com
#         ikipidia.org

    # Method 2 :-
for link in links:
    print(link.removeprefix("www.")) 
# Output =>
#         b001.io
#         youtube.com
#         google.com
#         wikipidia.org


student_list = ("CSE.Prakash","CSE.Rahul","CSE.Vishal","CSE.Ehatha","CSE.Emily","CSE.Anil")

for name in student_list: 
    # print(name.lstrip('CSE.')) # lstrip() does NOT remove the exact string "CSE."
    print(name.removeprefix('CSE.')) # This removes the exact prefix only.

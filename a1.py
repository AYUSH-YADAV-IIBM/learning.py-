student={
"aniket kumar yadav":{"roll":157,"marks":480,"collage-name":"indian institute of business management",
                      "course":"BCA","semester":"secound semester","year":"1st year"},

"bobby kumar":{"roll":148,"marks":500,"collage-name":"indian institute of business management",
               "course":"BCA","semester":"secound semester","year":"1st year"}

}

name=input("ENTER STUDENT NAME!:")

if name in student:
    print("roll",student[name]["roll"])
    print("marks",student[name]["marks"])
    print("collage-name",student[name]["collage-name"])
    print("course",student[name]["course"])
    print("semester",student[name]["semester"])
    print("year",student[name]["year"])

else:
    print("student name not found")
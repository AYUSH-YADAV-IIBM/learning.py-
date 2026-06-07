student={
    "ayush yadav":{
        "name":"ayush yadav",
        "roll":157,
        "marks":400,
        "course":"bca",
        "collage":"iibm",
        "semester":"first",
        "year":"first"
        

    },
         "bobby kumar":{
         "name":"bobby kumar",
        "roll":148,
        "marks":400,
        "course":"bca",
        "collage":"iibm",
        "semester":"first",
        "year":"first"
        

    }
  
}

name=input("ENTER STUENT NAME:")

if name in student:
    print("name",student[name]["name"])
    print("roll",student[name]["roll"])
    print("marks",student[name]["marks"])
    print("course",student[name]["course"])
    print("collage",student[name]["collage"])
    print("semester",student[name]["semester"])
    print("year",student[name]["year"])

else:
    print("student not found")
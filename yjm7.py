Staff = {"name" : "Yash" , "age" : "25", "designation" : "HOD"}
print("key And Values Are :- ",Staff)

Staff["pincode"]=360005
print("name:- ",Staff.get("name"))

print("Remove Pincode:- ",Staff.pop("age"),Staff)
print("check designation in Staff:- ","designation" in Staff)

print("KEYs:-")
for staff in Staff:
    print(staff)

print("VALUES:-")
for staff1 in Staff:
    print(staff1)

print("KEYs And VALUEs:-")
for key,values in Staff.items():
    print(f"{key}={values}")

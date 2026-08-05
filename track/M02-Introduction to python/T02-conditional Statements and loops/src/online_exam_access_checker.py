registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()
if registered != "Yes":
    print("Access Denied: Registration Incomplete")
elif system_check != "Pass":
    print("Access Denied: System Check Failed")
elif fee_paid != "Yes" or identity_verified != "Yes":
    print("Access Denied: Verification Pending")
else:
    print("Access Granted")
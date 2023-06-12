token = "bearer fd6524b01178e47c96671ced0b739108487b7237"

if token:
    if "Bearer" in token:
        print({"Authorization": "%s" % token})
    else:
        print({"Authorization": "Token %s" % token})
    
    
    
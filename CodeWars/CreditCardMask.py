def maskify(cc):
    if len(cc) >= 4:
        tt = len(cc)-4
        return print(str('#'*tt + cc[-4:len(cc)]))
    else:
        return print(str(cc))



maskify("")
maskify("123")  
maskify("SF$SDfgsd2eA")

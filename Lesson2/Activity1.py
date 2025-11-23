def total(ba, tp):
    tl = ba*(1 + 0.01*tp)
    tl = round(tl,2)
    print(f"Please pay $",{tl})
total(150, 20)
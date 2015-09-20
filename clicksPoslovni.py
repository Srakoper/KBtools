# manko klikov

print("IZRAČUN KLIKOV ZA PAKETE POSLOVNI, ver. 1.0, @Damjan Mihelič ;)")

while True:

    packages = {
        49: 200,
        99: 400,
        199: 800,
        399: 1600
        }

    months = {
        1: ("JANUAR", 31),
        2: ("FEBRUAR", 28),
        3: ("MAREC", 31),
        4: ("APRIL", 30),
        5: ("MAJ", 31),
        6: ("JUNIJ", 30),
        7: ("JULIJ", 31),
        8: ("AVGUST", 31),
        9: ("SEPTEMBER", 30),
        10: ("OKTOBER", 31),
        11: ("NOVEMBER", 30),
        12: ("DECEMBER", 31),
        13: ("FEBRUAR PRESTOPNO", 29)
        }

    print("\n--------------------------------------------------------------------\n--------------------------------------------------------------------\n")

    month = 0
    while True:
        try:
            month = int(input("Mesec (1-12): "))
            if month in range(1, 14):
                break
        except ValueError:
            pass

    startDay = 0
    while True:
        try:
            startDay = int(input("Dan začetka akcije: "))
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if startDay in range(1, 32):
                    break
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if startDay in range(1, 31):
                                break
            elif month == 2:
                if startDay in range(1, 29):
                    break
            else:
                if startDay in range(1, 30):
                    break
        except ValueError:
            pass

    currentDay = 0
    while True:
        try:
            currentDay = int(input("Današnji dan: "))
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if currentDay in range(1, 32) and currentDay >= startDay:
                    break
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if currentDay in range(1, 31) and currentDay >= startDay:
                    break
            elif month == 2:
                if currentDay in range(1, 29) and currentDay >= startDay:
                    break
            else:
                if currentDay in range(1, 30) and currentDay >= startDay:
                    break
        except ValueError:
            pass

    package = 0
    while True:
        try:
            package = int(input("Paket (49, 99, 199, 399): "))
            if package == 49 or package == 99 or package == 199 or package == 399:
                break
        except ValueError:
            pass
        
    GAdW = None
    while True:
        GAdW = input("Google AdWords? (D/N) ").upper()
        if GAdW == "D" or GAdW == "N":
            break

    clicksGAdW = 0
    clicksTSmedia = 0
    clicksGeneratedGAdW = 0
    clicksGeneratedTSmedia = 0
    clicksTSmediaAvg = 0
    clicksGAdWNow = 0
    clicksTSmediaNow = 0

    if GAdW == "D":

        clicksGAdW = packages[package] * 1/5
        clicksTSmedia = packages[package] * 4/5
        clicksGAdWMonth = round((clicksGAdW / (months[month][1])) * ((months[month][1]) - (startDay)), 2)
        clicksTSmediaMonth = round((clicksTSmedia / (months[month][1])) * ((months[month][1]) - (startDay)), 2)
        
        clicksGeneratedGAdW = 0
        while True:
            try:
                clicksGeneratedGAdW = int(eval(input("Število generiranih klikov v omrežju GAdW: ")))
                break
            except NameError:
                pass
            except SyntaxError:
                pass
            
        clicksGeneratedTSmedia = 0
        while True:
            try:
                clicksGeneratedTSmedia = int(eval(input("Število generiranih klikov v omrežju TSmedia: ")))
                break
            except NameError:
                pass
            except SyntaxError:
                pass

        clicksGAdWAvg = round(clicksGAdW / (months[month][1]), 2)
        clicksTSmediaAvg = round(clicksTSmedia / (months[month][1]), 2)
        try:
            clicksGAdWNow = round((clicksGeneratedGAdW / (currentDay - startDay)), 2)
            clicksTSmediaNow = round((clicksGeneratedTSmedia / (currentDay - startDay)), 2)
        except ZeroDivisionError:
            clicksGAdWNow = round((clicksGeneratedGAdW / (currentDay - (startDay - 1))), 2)
            clicksTSmediaNow = round((clicksGeneratedTSmedia / (currentDay - (startDay - 1))), 2)
        try:
            clicksGAdWFuture = round((clicksGAdWMonth - clicksGeneratedGAdW) / ((months[month][1] - currentDay)), 2)
            clicksTSmediaFuture = round((clicksTSmediaMonth - clicksGeneratedTSmedia) / ((months[month][1] - currentDay)), 2)
        except ZeroDivisionError:
            clicksGAdWFuture = round((clicksGAdWMonth - clicksGeneratedGAdW), 2)
            clicksTSmediaFuture = round((clicksTSmediaMonth - clicksGeneratedTSmedia), 2)

        print("\n--------------------------------------------------------------------\n--------------------------------------------------------------------")

        print("\nSPLOŠNO")
        
        print("\nŠtevilo mesečnih klikov v omrežju GAdW pri paketu Poslovni %s: " % str(package) + str(clicksGAdW))
        print("Število mesečnih klikov v omrežju TSmedia pri paketu Poslovni %s: " % str(package) + str(clicksTSmedia))

        print("\nBudget v omrežju GAdW: " + str(round((package * 1/5), 2)) + " EUR (na dan: " + str(round((package * 1/5 / months[month][1]), 2)) + " EUR)")
        print("Budget v omrežju TSmedia: " + str(round((package * 4/5), 2)) + " EUR")

        print("\nZačetek akcije v tekočem mesecu: " + str(startDay) + ". " + str(months[month][0]))
        print("Trajanje akcije v dnevih: " + str(currentDay - startDay))

        print("\n--------------------------------------------------------------------")

        print("\nCILJI")
        
        print("\nSkupni cilj: " + str(clicksGAdWMonth) + " klikov v omrežju GAdW v mesecu %s." % (months[month][0]))
        print("Skupni cilj: " + str(clicksTSmediaMonth) + " klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\nDnevni cilj: " + str(round((clicksGAdW / (months[month][1])), 2)) + " klikov na dan v omrežju GAdW v mesecu %s." % (months[month][0]))
        print("Dnevni cilj: " + str(round((clicksTSmedia / (months[month][1])), 2)) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\n--------------------------------------------------------------------")

        print("\nIZRAČUNI")

        print("\nGeneriranih klikov v omrežju GAdW v mesecu %s: " % (months[month][0]) +str(clicksGeneratedGAdW))
        print("Generiranih klikov v omrežju TSmedia v mesecu %s: " % (months[month][0]) + str(clicksGeneratedTSmedia))

        if clicksGeneratedGAdW <= clicksGAdWMonth:
            print("\nOstanek: " + str(round((clicksGAdWMonth - clicksGeneratedGAdW), 2)) + " klikov v omrežju GAdW v mesecu %s." % (months[month][0]))
        else:
            print("\nOstanek: 0.0 klikov v omrežju GAdW v mesecu %s." % (months[month][0]))
        if clicksGeneratedTSmedia <= clicksTSmediaMonth:
            print("Ostanek: " + str(round((clicksTSmediaMonth - clicksGeneratedTSmedia), 2)) + " klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))
        else:
            print("Ostanek: 0.0 klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\nDo današnjega dne: " + str(clicksGAdWNow) + " klikov na dan v omrežju GAdW v mesecu %s." % (months[month][0]))
        print("Do današnjega dne: " + str(clicksTSmediaNow) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        if clicksGAdWFuture >= 0:
            print("\nOd današnjega dne: " + str(clicksGAdWFuture) + " klikov na dan v omrežju GAdW v mesecu %s." % (months[month][0]))
        else:
            print("\nOd današnjega dne: 0.0 klikov na dan v omrežju GAdW v mesecu %s." % (months[month][0]))
        if clicksTSmediaFuture >= 0:
            print("Od današnjega dne: " + str(clicksTSmediaFuture) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))
        else:
            print("Od današnjega dne: 0.0 klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        if clicksGeneratedGAdW <= clicksGAdWMonth:
            try:
                print("\nStanje klikov trenutno/prihodnje v omrežju GAdW: " + str(round((clicksGAdWNow - clicksGAdWFuture), 2)) + " (" + str(round((100 / clicksGAdWFuture * clicksGAdWNow), 2)) + "% realizacija)")
            except ZeroDivisionError:
                print("\nCilj klikov v omrežju GAdW v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedGAdW)) + " od " + str(clicksGAdWMonth) + " klikov. (100%)")
        else:
            print("\nCilj klikov v omrežju GAdW v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedGAdW)) + " od " + str(clicksGAdWMonth) + " klikov. (" + str(round((clicksGeneratedGAdW / clicksGAdWMonth * 100), 2)) + "%)")
        if clicksGeneratedTSmedia <= clicksTSmediaMonth:
            try:
                print("Stanje klikov trenutno/prihodnje v omrežju TSmedia: " + str(round((clicksTSmediaNow - clicksTSmediaFuture), 2)) + " (" + str(round((100 / clicksTSmediaFuture * clicksTSmediaNow), 2)) + "% realizacija)")
            except ZeroDivisionError:
                print("Cilj klikov v omrežju TSmedia v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedTSmedia)) + " od " + str(clicksTSmediaMonth) + " klikov. (100%)")
        else:
            print("Cilj klikov v omrežju TSmedia v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedTSmedia)) + " od " + str(clicksTSmediaMonth) + " klikov. (" + str(round((clicksGeneratedTSmedia / clicksTSmediaMonth * 100), 2)) + "%)")

    else:

        clicksTSmedia = packages[package]
        clicksTSmediaMonth = round((clicksTSmedia / (months[month][1])) * ((months[month][1]) - (startDay)), 2)
        
        clicksGeneratedTSmedia = 0
        while True:
            try:
                clicksGeneratedTSmedia = int(eval(input("Število generiranih klikov v omrežju TSmedia: ")))
                break
            except NameError:
                pass
            except SyntaxError:
                pass

        clicksTSmediaAvg = round(clicksTSmedia / (months[month][1]), 2)
        try:
            clicksTSmediaNow = round((clicksGeneratedTSmedia / (currentDay - startDay)), 2)
        except ZeroDivisionError:
            clicksTSmediaNow = round((clicksGeneratedTSmedia / (currentDay - (startDay - 1))), 2)
        clicksTSmediaFuture = round((clicksTSmediaMonth - clicksGeneratedTSmedia) / ((months[month][1] - currentDay)), 2)

        print("\n--------------------------------------------------------------------\n--------------------------------------------------------------------")

        print("\nSPLOŠNO")

        print("\nŠtevilo mesečnih klikov v omrežju TSmedia pri paketu Poslovni %s: " % str(package) + str(clicksTSmedia))

        print("\nBudget v omrežju TSmedia: " + str(round(package, 2)) + " EUR")

        print("\nZačetek akcije v tekočem mesecu: " + str(startDay) + ". " + str(months[month][0]))
        print("Trajanje akcije v dnevih: " + str(currentDay - startDay))

        print("\n--------------------------------------------------------------------")

        print("\nCILJI")

        print("\nSkupni cilj: " + str(clicksTSmediaMonth) + " klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\nDnevni cilj: " + str(round((clicksTSmedia / (months[month][1])), 2)) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\n--------------------------------------------------------------------")

        print("\nIZRAČUNI")

        print("\nGeneriranih klikov v omrežju TSmedia v mesecu %s: " % (months[month][0]) + str(clicksGeneratedTSmedia))

        if clicksGeneratedTSmedia <= clicksTSmediaMonth:
            print("\nOstanek: " + str(round((clicksTSmediaMonth - clicksGeneratedTSmedia), 2)) + " klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))
        else:
            print("\nOstanek: 0.0 klikov v omrežju TSmedia v mesecu %s." % (months[month][0]))

        print("\nDo današnjega dne: " + str(clicksTSmediaNow) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        if clicksTSmediaFuture >= 0:
            print("\nOd današnjega dne: " + str(clicksTSmediaFuture) + " klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))
        else:
            print("\nOd današnjega dne: 0.0 klikov na dan v omrežju TSmedia v mesecu %s." % (months[month][0]))

        if clicksGeneratedTSmedia <= clicksTSmediaMonth:
            try:
                print("\nStanje klikov trenutno/prihodnje v omrežju TSmedia: " + str(round((clicksTSmediaNow - clicksTSmediaFuture), 2)) + " (" + str(round((100 / clicksTSmediaFuture * clicksTSmediaNow), 2)) + "% realizacija)")
            except ZeroDivisionError:
                print("\nCilj klikov v omrežju TSmedia v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedTSmedia)) + " od " + str(clicksTSmediaMonth) + " klikov. (100%)")
        else:
            print("\nCilj klikov v omrežju TSmedia v mesecu %s dosežen: " % (months[month][0]) + str(float(clicksGeneratedTSmedia)) + " od " + str(clicksTSmediaMonth) + " klikov. (" + str(round((clicksGeneratedTSmedia / clicksTSmediaMonth * 100), 2)) + "%)")

    print("\n--------------------------------------------------------------------\n--------------------------------------------------------------------")

    while True:
        again = input("\nNov izračun? (D/N) ").upper()
        if again == "D" or again == "N":
            break

    if again == "D":
        pass
    else:
        break

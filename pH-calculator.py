import math
import sys

n = 1

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def limitConc(conc):
    if conc > 1 or conc < 1e-14:
        return False
    else:
        return True

def errorLeaveProgram():
    sys.exit("Error: Entered value isn't valid!")

inp = input("Input charge of electrolyte :")
if not isInt(inp):
    errorLeaveProgram()
    
el = int(inp)

inp = input("Input concentration of electrolyte :")
if not isFloat(inp):
    errorLeaveProgram()

conc = float(inp)

if not limitConc(conc):
    sys.exit("It isn't possible to calculate pH value for this concentration.")

else:
    PEl = input("Input whether electrolyte is weak or strong.")

    if PEl == 'strong':
        if abs(el) > 1:
            if el<0:
                constants = {}
                while (abs(el) - (n+1)) >= 0:
                    constant_num = f"K{n+1}"
                    inp = input(f"Input {n+1}. acid/base dissociation constant.")

                    if not isFloat(inp):
                            errorLeaveProgram()
                    else:
                            constants[constant_num] = float(inp)
                            n += 1  
                results = {}

                previous_results = [conc]

                for num, value in constants.items():
                                
                    result = (-value + (((value**2) + (4*value*(min(previous_results))))**0.5)) / 2
                                
                    results[num] = result

                    previous_results.append(result)

                cH = sum(results.values()) + conc
                pH = str(round((-(math.log10(cH))),3))
                cH = str(round((cH),4))
                print("pH value is :",pH)
                print("Concentration of H+ cations is :", cH,"M")

            else:
                constants = {}
                while (abs(el) - (n+1)) >= 0:
                    constant_num = f"K{n+1}"
                    inp = input(f"Input {n+1}. acid/base dissociation constant.")

                    if not isFloat(inp):
                            errorLeaveProgram()
                    else:
                            constants[constant_num] = float(inp)
                            n += 1  
                results = {}

                previous_results = [conc]

                for num, value in constants.items():
                                
                    result = (-value + (((value**2) + (4*value*(min(previous_results))))**0.5)) / 2
                                
                    results[num] = result

                    previous_results.append(result)
                
                cOH = sum(results.values()) + conc
                cH = (1e-14)/cOH
                pH = str(round((-(math.log10(cH))),3))
                cOH = str(round((cOH),4))
                print("pH value is :",pH)
                print("Concentration of OH- anions is :", cOH,"M")

        else:
            if el<0:
                cH = conc
                pH = str(round((-(math.log10(cH))),3))
                cH = str(round((cH),4))
                print("pH value is :",pH)
                print("Concentration of H+ cations is :", cH,"M")
            else:
                cOH = conc
                cH = (1e-14)/cOH
                pH = str(round((-(math.log10(cH))),3))
                cOH = str(round((cOH),4))
                print("pH value is :",pH)
                print("Concentration of OH- anions is :", cOH,"M")

    elif PEl == 'slab':
        if abs(el) > 1:
            if el<0:
                constants = {}
                while (abs(el) - (n)) >= 0:
                    constant_num = f"K{n}"
                    inp = input(f"Input {n+1}. acid/base dissociation constant.")

                    if not isFloat(inp):
                            errorLeaveProgram()
                    else:
                            constants[constant_num] = float(inp)
                            n += 1  
                results = {}

                previous_results = [conc]

                for num, value in constants.items():
                                
                    result = (-value + (((value**2) + (4*value*(min(previous_results))))**0.5)) / 2
                                
                    results[num] = result

                    previous_results.append(result)
                    
                cH = sum(results.values())
                pH = str(round((-(math.log10(cH))),3))
                cH = str(round((cH),4))
                print("pH value is :",pH)
                print("Concentration of H+ cations is :", cH,"M")
            else:
                constants = {}
                while (abs(el) - (n)) >= 0:
                    constant_num = f"K{n}"
                    inp = input(f"Input {n+1}. acid/base dissociation constant.")

                    if not isFloat(inp):
                            errorLeaveProgram()
                    else:
                            constants[constant_num] = float(inp)
                            n += 1  
                results = {}

                previous_results = [conc]

                for num, value in constants.items():
                                
                    result = (-value + (((value**2) + (4*value*(min(previous_results))))**0.5)) / 2
                                
                    results[num] = result

                    previous_results.append(result)
                    
                cOH = sum(results.values())
                cH = (1e-14)/cOH
                pH = str(round((-(math.log10(cH))),3))
                cOH = str(round((cOH),4))
                print("pH value is :",pH)
                print("Koncentracija OH- katjona je ", cOH,"M")
        else:
             
            inp = input("Input acid/base dissociation constant :")
            if isFloat(inp) == False:
                errorLeaveProgram()
            else:
                K = float(inp)  
                if el<0:
                    cH = (-K+(((K**2)+(4*K*conc))**0.5))/2
                    pH = str(round((-(math.log10(cH))),2))
                    cH = str(round((cH),4))                    
                    print("pH value is :",pH)
                    print("Concentration of H+ cations is :", cH,"M")
                
                else:
                    cOH = (-K+(((K**2)+(4*K*conc))**0.5))/2
                    cH = (1e-14)/cOH
                    pH = str(round((-(math.log10(cH))),2))
                    cOH = str(round((cOH),4))                    
                    print("pH value is :",pH)
                    print("Concentration of OH- anions is :", cOH,"M")
                     
	
    else:
        print("Input exactly whether electrolyte is 'weak' or 'strong'." )


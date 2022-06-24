import math

#SIMPLE CALCULATOR
def summation():
    while True:
        x=0
        i = 0
        iteration = int(input("Enter How many Numbers you want to add:"))
        if iteration < 0:
            print("Please Enter A Positive Number")
            continue
        else:
            while i != iteration:
                n = eval(input())
                x+=n
                i+=1
        print("THE SUM IS {}".format(x))    
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def subtraction():
    while True:
        lis = []
        i = 0
        iteration = int(input("Enter how many Numbers you want to subtract:"))
        if iteration < 0:
            print("Please Enter A Positive Number")
            continue
        else:
            while i != iteration:
                n = eval(input())
                lis.append(n)
                i+=1
            key = lis[0]
            for i in range(1,len(lis)):
                key= key - lis[i]
        print("THE answer is {}".format(key))    
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break
    
def multiplication():
    while True:
        lis = []
        i = 0
        iteration = int(input("Enter how many Numbers you want to Multiply:"))
        if iteration < 0:
            print("Please Enter A Positive Number")
            continue
        else:
            while i != iteration:
                n = eval(input())
                lis.append(n)
                i+=1
            key = lis[0]
            for i in range(1,len(lis)):
                key= key * lis[i]
        print("THE answer is {}".format(key))    
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def division():
    while True:
        lis = []
        i = 0
        iteration = int(input("Enter how many Numbers you want to Divide:"))
        if iteration < 0:
            print("Please Enter A Positive Number")
            continue
        else:
            while i != iteration:
                n = eval(input())
                lis.append(n)
                i+=1
            key = lis[0]
            for i in range(1,len(lis)):
                key= key/lis[i]
        print("THE answer IS {}".format(key))    
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def log():
    while True:
        opt = input("Do you want to use base e or other base\n Enter Y for e and N for other:")
        if opt == "Y":
            num1=eval(input('Enter the number: '))
            print("ln({}) = {}".format(num1,math.log(num1)))
        else:
            num1=eval(input('Enter the number: '))
            base=int(input('Enter the base number: '))
            print("lg({}) = {}".format(num1,round(math.log(num1,base), 3)))
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def squareroot():
    while True:
        n = eval(input("Enter a number:"))
        if n<0:
            print("Cannot Find Square Root Of Negative Number:")
            continue
        else:
            result = n**(1/2)
        print("The Square Root Of {} = {}".format(n,result))
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def power():
    while True:
        num1 = eval(input("Enter A Number:"))
        powr = eval(input("Enter the Power:"))
        if num1<0 and type(powr) == float:
            print("Not Possible Enter Again")
            continue
        else:
            result = num1**(powr)
            print("{} to the power of {} = {}".format(num1,powr,result))
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def sin():
    while True:
        opt = input("Radians(R) or Degree(D):")
        if opt == "D":
            deg=eval(input('Enter the value of angle in degrees :'))
            angle=math.radians(deg)
            common_val=math.sin(angle)
            print("sin({}) = {}".format(deg,round(common_val,3)))
        elif opt == "R":
            rad = eval(input("Enter the value of angle in radians :"))
            common_val = math.sin(rad)
            print("sin({}) = {}".format(rad,round(common_val,3)))
        else:
            print("Invalid Option\n")
            continue
        
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def cos():
    while True:
        opt = input("Radians(R) or Degree(D):")
        if opt == "D":
            deg=eval(input('Enter the value of angle in degrees :'))
            angle=math.radians(deg)
            common_val=math.cos(angle)
            print("cos({}) = {}".format(deg,round(common_val,3)))
        elif opt == "R":
            rad = eval(input("Enter the value of angle in radians :"))
            common_val = math.cos(rad)
            print("cos({}) = {}".format(rad,round(common_val,3)))
        else:
            print("Invalid Option\n")
            continue
        
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break

def tan():
    while True:
        opt = input("Radians(R) or Degree(D):")
        if opt == "D":
            deg=eval(input('Enter the value of angle in degrees :'))
            if deg == 90:
                print("Not defined")
                continue
            else:
                angle=math.radians(deg)
                common_val=math.tan(angle)
                print("tan({}) = {}".format(deg,round(common_val,3)))
        elif opt == "R":
        
            rad = eval(input("Enter the value of angle in radians :"))
            common_val = math.tan(rad)
            print("tan({}) = {}".format(rad,round(common_val,3)))
        else:
            print("Invalid Option\n")
            continue
        inp = input("Do you want to continue Y/N:")
        if inp == "Y":
            pass
        else:
            break   
# ---------------------------------------------END----------------------------------------------------#
#CONVERSION CALCULATOR

def meter_to_kilometer():
    while True:
        inp = int(input("Select One:\n 1.Meter -> Kilometer\n 2.Kilometer -> Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in meters:"))
            if x>=0:
                kilometer=x/1000
                print("Value in kilometers is = {}km".format(kilometer))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in kilometer:"))
            if x>=0:
                meter=x*1000
                print("Value in meter is = {}m".format(meter))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break 

def meter_to_centimeter():
    while True:
        inp = int(input("Select One:\n 1.Meter -> Centimeter\n 2.Centimeter -> Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in meters:"))
            if x>=0:
                centimeter=x*100
                print("Value in kilometers is = {}cm".format(centimeter))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Centimeter:"))
            if x>=0:
                meter=x/100
                print("Value in meter is = {}m".format(meter))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break 

def centimeter_to_kilometer():
    while True:
        inp = int(input("Select One:\n 1.Centimeter -> Kilometer\n 2.Kilometer -> Centimeter\n"))
        if inp == 1:
            x=eval(input("Enter value in Centimeters:"))
            if x>=0:
                kilometer=x/100000
                print("Value in kilometers is = {}km".format(kilometer))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Kilometer:"))
            if x>=0:
                centimeter=x*100000
                print("Value in meter is = {}cm".format(centimeter))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break 

def liter_milliliter():
    while True:
        inp = int(input("Select One:\n 1.Liter -> Milliliter\n 2.Milliliter -> Liter\n"))
        if inp == 1:
            x=eval(input("Enter value in Liter:"))
            if x>=0:
                milliliter=x*1000
                print("Value in Milliliter is = {} ml".format(milliliter))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in milliliter:"))
            if x>=0:
                liter=x/1000
                print("Value in Liter is = {}L".format(liter))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break 

def liter_cubicmeter():
    while True:
        inp = int(input("Select One:\n 1.Liter -> Cubic Meter\n 2.Cubic Meter -> Liter\n"))
        if inp == 1:
            x=eval(input("Enter value in Liter:"))
            if x>=0:
                cubicmeter=x/1000
                print("Value in Cubic Meter is = {} cubicmeter".format(cubicmeter))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Cubic Meter:"))
            if x>=0:
                liter=x*1000
                print("Value in Liter is = {}L".format(liter))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break

def cubicm_cubiccm():
    while True:
        inp = int(input("Select One:\n 1.Cubic Meter -> Cubic Centimeter\n 2.Cubic Centimeter -> Cubic Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in Cubic Meter:"))
            if x>=0:
                cubiccm=x*1000000
                print("Value in Cubic Centimeter is = {} cubic centimeter".format(cubiccm))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Cubic Centimeter:"))
            if x>=0:
                cubicm=x/1000000
                print("Value in Cubic Meter is = {} Cubicmeter".format(cubicm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def sqm_sqcm():
    while True:
        inp = int(input("Select One:\n 1.Square Meter -> Square Centimeter\n 2.Square Centimeter -> Square Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in Square Meter:"))
            if x>=0:
                sqcm=x*10000
                print("Value in Square Centimeter is = {} square centimeter".format(sqcm))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Square Centimeter:"))
            if x>=0:
                sqm=x/10000
                print("Value in Square Meter is = {} sq m ".format(sqm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def sqm_sqkm():
    while True:
        inp = int(input("Select One:\n 1.Square Meter -> Square Kilometer\n 2.Square Kilometer -> Square Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in Square Meter:"))
            if x>=0:
                sqkm=x/1000000
                print("Value in Square Kilometer is = {} sq km".format(sqkm))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Square Kilometer:"))
            if x>=0:
                sqm=x*1000000
                print("Value in Square Meter is = {} sq m".format(sqm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def sqm_acre():
    while True:
        inp = int(input("Select One:\n 1.Square Meter -> Acre\n 2.Acre -> Square Meter\n"))
        if inp == 1:
            x=eval(input("Enter value in Square Meter:"))
            if x>=0:
                acre=x/4046.86
                print("Value in Acre is = {} acre".format(acre))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Acre:"))
            if x>=0:
                sqm=x*4046.86
                print("Value in Square Meter is = {} sq m".format(sqm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def gm_kg():
    while True:
        inp = int(input("Select One:\n 1.Gram -> Kilogram\n 2.Kilogram -> Gram\n"))
        if inp == 1:
            x=eval(input("Enter value in Gram:"))
            if x>=0:
                kg=x/1000
                print("Value in Kilogram is = {} kg".format(kg))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Kilogram:"))
            if x>=0:
                gm=x*1000
                print("Value in Gram is = {} g".format(gm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def gm_mg():
    while True:
        inp = int(input("Select One:\n 1.Gram-> Milligram\n 2.Milligram -> Gram\n"))
        if inp == 1:
            x=eval(input("Enter value in Gram:"))
            if x>=0:
                mg=x*1000
                print("Value in Milligram is = {} mg".format(mg))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Milligram:"))
            if x>=0:
                gm=x/1000
                print("Value in Gram is = {} g".format(gm))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  
    
def kg_ton():
    while True:
        inp = int(input("Select One:\n 1.Kilogram -> Tonne\n 2.Tonne -> Kilogram\n"))
        if inp == 1:
            x=eval(input("Enter value in Kilogram:"))
            if x>=0:
                ton=x/1000
                print("Value in Tonne is = {} t".format(ton))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Tonne:"))
            if x>=0:
                kg=x*1000
                print("Value in Kilogram is = {} kg".format(kg))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def cel_kel():
    while True:
        inp = int(input("Select One:\n 1.Celsius -> Kelvin\n 2.Kelvin -> Celsius\n"))
        if inp == 1:
            x=eval(input("Enter value in Celsius:"))
            kel=x+273.15
            print("Value in Kelvin is = {} degree kelvin".format(kel))
        elif inp == 2:
            x=eval(input("Enter value in Kelvin:"))
            cel=x-273.15
            print("Value in Celsius is = {} degree celsius".format(cel))
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def cel_far():
    while True:
        inp = int(input("Select One:\n 1.Celsius -> Fahrenheit\n 2.Fahrenheit -> Celsius\n"))
        if inp == 1:
            x=eval(input("Enter value in Celsius:"))
            far=(x*(9/5)) + 32
            print("Value in Fahrenheit  is = {} degree fahrenheit ".format(far))
        elif inp == 2:
            x=eval(input("Enter value in Fahrenheit :"))
            far=(x-32)*(5/9)
            print("Value in Celsius is = {} degree celsius".format(far))
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def far_kel():
    while True:
        inp = int(input("Select One:\n 1.Fahrenheit -> Kelvin\n 2.Kelvin -> Fahrenheit\n"))
        if inp == 1:
            x=eval(input("Enter value in Fahrenheit:"))
            kel=((x-32)*(5/9))+273.15
            print("Value in Kelvin is = {} degree kelvin".format(kel))
        elif inp == 2:
            x=eval(input("Enter value in Kelvin:"))
            far=((x-273.15)* (9/5)) + 32
            print("Value in Fahrenheit is = {} degree fahrenheit".format(far))
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def mps_kms():
    while True:
        inp = int(input("Select One:\n 1.Meter/s -> Kilometer/s\n 2.Kilometer/s-> Meter/s\n"))
        if inp == 1:
            x=eval(input("Enter value in Meter/s:"))
            if x>=0:
                kms=x/1000
                print("Value in Kilometer/s is = {} km/s".format(kms))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Kilometer/s:"))
            if x>=0:
                mps=x*1000
                print("Value in Meter/s is = {} m/s".format(mps))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def mps_kmh():
    while True:
        inp = int(input("Select One:\n 1.Meter/s -> Kilometer/h\n 2.Kilometer/h-> Meter/s\n"))
        if inp == 1:
            x=eval(input("Enter value in Meter/s:"))
            if x>=0:
                kmh=x*3.6
                print("Value in Kilometer/h is = {} km/h".format(kmh))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Kilometer/h:"))
            if x>=0:
                mps=x/3.6
                print("Value in Meter/s is = {} m/s".format(mps))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break  

def mileph_mps():
    while True:
        inp = int(input("Select One:\n 1.Meter/s -> Miles/h\n 2.Miles/h-> Meter/s\n"))
        if inp == 1:
            x=eval(input("Enter value in Meter/s:"))
            if x>=0:
                mileph=x*2.237
                print("Value in Miles/h is = {} miles/h".format(mileph))
            else:
                print("Please enter positive value")
        elif inp == 2:
            x=eval(input("Enter value in Miles/h:"))
            if x>=0:
                mps=x/2.237
                print("Value in Meter/s is = {} m/s".format(mps))
            else:
                print("Please enter positive value")
        else:
            print("Option Not Available")
        inpt = input("Do you want to continue Y/N:")
        if inpt == "Y":
            pass
        else:
            break 

def quadratic():
    while True:
        print("\nQuadratic Equation Format --> ax\u00b2+bx+c=0\n") 
        a = eval(input("Enter the value of a:"))
        b = eval(input("Enter the value of b:"))
        c = eval(input("Enter the value of c:"))

        d=((b**2)-(4*a*c))
        if d<0:
            print("Roots are not real\n")
            inpt = input("Do you want to continue Y/N:")
            if inpt == "Y":
                pass
            else:
                break  
        if d>=0:
            d = d**(1/2)
            root1 = ((-b)+d)/(2*a)
            root2 = ((-b)-d)/(2*a)
            print("The root of equation {}x\u00b2+({})x+({})=0 are\n Root 1 ={} and Root 2={}".format(a,b,c,root1,root2))
            inpt = input("Do you want to continue Y/N:")
            if inpt == "Y":
                pass
            else:
                break 

def palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False


def armstrong():
    while True:
        num = int(input("Enter a number: \n"))
        if num < 0 :
            print("Please enter again\n")
            continue
        else:
            sum = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if num == sum:
                print(num,"is an Armstrong number\n")
            else:
                print(num,"is not an Armstrong number\n")
            break



def prime(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number is not prime\n")
            return False
        else:
            return prime(n, div-1)
    else:
        print("Number is prime\n")
        return 'True'

def fibonacci():
    while True:
        nterms = int(input("How many terms? "))
        n1, n2 = 0, 1
        count = 0
        if nterms <= 0:
            print("Please enter a positive integer")
            continue
        elif nterms == 1:
            print("Fibonacci sequence upto",nterms,":")
            print(n1)
            break
        else:
            print("Fibonacci sequence:")
            while count < nterms:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
            break

    



#drivers code
print("                          SCIENTIFIC CALCULATOR")
while True:
    selection = eval(input("Choose what you would like to do:\n 1.Simple Calculation\n 2.Conversion Calculation\n 3.Complex Calculation\n 4.Quadratic Equation Solver\n 5.Quit\n"))
    assert type(selection) == int  , "Selection Number can only be a positive Integer"
    if selection == 1:
        while True:
            selection_one = int(input("Choose any one operation::\n 1.Summation(+)\n 2.Subtraction(-)\n 3.Multiplication(x)\n 4.Division(/)\n 5.Log\n 6.Square Root\n 7.Power(^)\n 8.Sin()\n 9.Cos()\n 10.Tan()\n 11.Return to Main Page\n"))
            if selection_one == 1:
                summation()
            elif selection_one == 2:
                subtraction()
            elif selection_one == 3:
                multiplication()
            elif selection_one == 4:
                division()
            elif selection_one == 5:
                log()
            elif selection_one == 6:
                squareroot()
            elif selection_one == 7:
                power()
            elif selection_one == 8:
                sin()
            elif selection_one == 9:
                cos()
            elif selection_one == 10:
                tan()
            elif selection_one == 11:
                break
            else:
                print("Wrong selection")
    elif selection == 2:
        while True:
            selection_two = int(input("Choose any one of the following:\n 1.Length Conversion\n 2.Volume Conversion\n 3.Mass Conversion\n 4.Area Conversion\n 5.Temparature Conversion\n 6.Speed Conversion\n 7.Return to Main Page\n"))
            if selection_two == 1:
                lc = int(input("Choose any one of the following:\n 1.Meter<->Kilometer\n 2.Meter<->Centimeter\n 3.Centimeter<->Kilometer\n"))
                if lc == 1:
                    meter_to_kilometer()
                elif lc == 2:
                    meter_to_centimeter()
                elif lc == 3:
                    centimeter_to_kilometer()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 2:
                vc = int(input("Choose any one of the following:\n 1.Liter<->Milliliter\n 2.Cubic meter<-> Cubic centimeter\n 3.Liter<->Cubicmeter\n"))
                if vc == 1:
                    liter_milliliter()
                elif vc == 2:
                    cubicm_cubiccm()
                elif vc == 3:
                    liter_cubicmeter()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 3:
                mc = int(input("Choose any one of the following:\n 1.Gram<->Kilogram\n 2.Gram<->Milligram\n 3.Kilogram<->Tonne\n"))
                if mc == 1:
                    gm_kg()
                elif mc == 2:
                    gm_mg()
                elif mc == 3:
                    kg_ton()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 4:
                ac = int(input("Choose any one of the following:\n 1.Square Meter<->Square Centimeter\n 2.Square Meter<-> Square Kilometer\n 3.Square Meter<->Acre\n"))
                if ac == 1:
                    sqm_sqcm()
                elif ac == 2:
                    sqm_sqkm()
                elif ac == 3:
                    sqm_acre()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 5:
                tc = int(input("Choose any one of the following:\n 1.Celsius<->Kelvin\n 2.Celsius<-> Fahrenheit\n 3.Fahrenheit<->Kelvin\n"))
                if tc == 1:
                    cel_kel()
                elif tc == 2:
                    cel_far()
                elif tc == 3:
                    far_kel()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 6:
                sc = int(input("Choose any one of the following:\n 1.Meter/s<->Kilometer/s\n 2.Meter/s<-> Kilometer/h\n 3.Miles/h<->Meter/s\n"))
                if sc == 1:
                    mps_kms()
                elif sc == 2:
                    mps_kmh()
                elif sc == 3:
                    mileph_mps()
                else:
                    print("OPTION NOT AVAILABLE")
            elif selection_two == 7:
                break
            else:
                print("INVALID OPTION")
    elif selection == 3:
        while True:
            selection_three = int(input("Choose any one of the following:\n 1.Prime Number\n 2.Palindrome Number\n 3.Armstrong Number\n 4.Fibonacci Series\n 5.Return to Main Page\n"))
            if selection_three == 1:
                while True:
                    n = int(input("Enter a number:\n"))
                    if n < 0:
                        print("Enter again-")
                        continue
                    else:
                        prime(n)
                        break
            elif selection_three == 2:
                s = str(input("Enter a number:\n"))
                palindrome(s)
                if palindrome(s)==True:
                    print("String is a palindrome!\n")
                else:
                    print("String isn't a palindrome!\n")
            elif selection_three == 3:
                armstrong()
            elif selection_three == 4:
                fibonacci()
            elif selection_three == 5:
                break
            else:
                print("OPTION NOT AVAILABLE")
    elif selection == 4:
        quadratic()
        
    elif selection == 5:
        print("Thank You!")
        break
    else:
        print("The selection you entered does not exist, Please select again or Quit.")
        print()
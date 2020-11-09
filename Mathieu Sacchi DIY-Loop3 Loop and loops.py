

def patern(symbol,height,width,centered):

   for i in range(1,height+1):
       if height == width and centered == False :
           print(symbol*i)

       if height > width and centered == False : # Symmetrical pattern like patern 1
            if i <= width :
                print (symbol*i)

            else:
                print (symbol*(width+(width-i)))

       if centered == True:  # Mirror pattern like patern 3
           print(" " * (height-i+1) + symbol * (i*2-1))



print("Patern 1 : ")
patern("*",10,5,False)

print("Patern 2 : ")
patern("*",10,10,False)

print("Patern 3 : ")
patern("^",12,23,True)
def captura_div_cero():
    
    try: 
        num = input("Ingresa el número: ")
        
        if num.isdigit():
            num = int(num)
        
        result = 10/num
        print(result)
        
        
        
    except ZeroDivisionError as e:
        print("Error",e)
        
captura_div_cero()
print("Este programa dirá se você pode rodar")
placa = input("final de placa entre 00 a 09: ")
 
match placa:
    case '01' | '02':
        print("Na segunda-feira você pode rodar")
    case '03' | '04':
        print("Na terça-feira você pode rodar")
    case '05' | '06' :
        print("Na quarta-feira você pode rodar")
    case '07' | '08' :
       print("Na quinta-feira você pode rodar")
    case '09' | '00' :
        print("Na sexta-feira você pode rodar")
    case '_':
        print("Sem placas com esse final. Tente novamente")
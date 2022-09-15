def suhu(x):
    reamur = x * 4/5
    fahrenheit = (x * 9/5)+32
    kelvin = x + 273
    print("suhu dalam Reamur : " + str(reamur))
    print("suhu dalam fahrenheit : " + str(fahrenheit))
    print("suhu dalam kelvin : " + str(kelvin))

a = int(input("Masukan Suhu Dalam Celcius : "))
suhu(a)

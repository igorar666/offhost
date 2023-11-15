import requests

a = int(input("1 Перезагрузить компьютеры\n2 Выключить компьютеры\n3 Перезагрузить доску\n4 Выключить доску\n5 Перезагрузить всё\n6 Выключить всё\n7 Перезакгрузить устройство по номеру\n8 Выключить устройство по номеру\n\nВведите свой выбор: "))

        
if a == 1:
        for i in range(1,17):
                requests.get(f"https://1862-3inf-{i}.serveo.net/reboot")
elif a == 2:
        for i in range(1,17):
                requests.get(f"https://1862-3inf-{i}.serveo.net/shutdown")
elif a == 3:
        requests.get(f"https://1862-3inf-0.serveo.net/reboot")
elif a == 4:
        requests.get(f"https://1862-3inf-0.serveo.net/shutdown")
elif a == 5:
        for i in range(17):
                requests.get(f"https://1862-3inf-{f}.serveo.net/reboot")
elif a == 6:
        for i in range(17):
                requests.get(f"https://1862-3inf-{i}.serveo.net/shutdown")
elif a == 7:
        requests.get(f"https://1862-3inf-{int(input("Введите номер устройства: "))}.serveo.net/reboot")
elif a == 8:
        requests.get(f"https://1862-3inf-{int(input("Введите номер устройства: "))}.serveo.net/shutdown")
else: print("Нету такого")
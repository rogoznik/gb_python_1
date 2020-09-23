input_time = int(input('Введите время в секндах: '))

hours = input_time // 3600
minutes = input_time % 3600 // 60
seconds = input_time % 3600 % 60

num_days = hours // 24
if num_days > 0:
    hours = hours % 24

str_hours = str(hours)
str_minutes = str(minutes)
str_second = str(seconds)

if hours < 10:
    str_hours = '0' + str(hours)

if minutes < 10:
    str_minutes = '0' + str(minutes)

if seconds < 10:
    str_second = '0' + str(seconds)

str_num_days = str(num_days)
last_symbol = int(str_num_days[-1])

str_day = ''

if (num_days >= 11) and (num_days <= 14):
    str_day = 'дней'
elif (last_symbol == 0) or (last_symbol >= 5):
    str_day = 'дней'
elif last_symbol == 1:
    str_day = 'день'
elif (last_symbol >= 2) and (last_symbol <= 4):
    str_day = 'дня'
if (num_days > 100) and ((int(str_num_days[-2:]) >= 11) and (int(str_num_days[-2:]) <= 14)):
    str_day = 'дней'

days = str_num_days + ' ' + str_day

print(f'Введенное время: {days} {str_hours}:{str_minutes}:{str_second}')

# возможно можно было проще, но это первое решение, которое выдал мой "воспаленный" мозг :)

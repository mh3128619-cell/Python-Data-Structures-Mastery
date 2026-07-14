worked_minutes = [45, 150, 90, 200, 300, 110]

result = [minutes / 60 for minutes in worked_minutes if minutes >= 120]
print(result)

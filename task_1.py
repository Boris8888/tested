duration = int(input('В ведите продолжительность:'))
print("До секунды: ", duration, "сек")
print("До минуты: ", duration//60, "мин, ", duration % 60, "сек, ")
print("До часа: ", duration//3600, "ч, ", (duration // 60) % 60, "мин, ", duration % 60, "сек.")
print("До дня: ", duration//86400, "дн, ", (duration // 3600) % 24, "ч, ",
      (duration // 60) % 60, "мин, ", duration % 60, "сек.")

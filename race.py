# Импортируем данные из файла import_this.py
from import_this import RACE_DATA

def print_race_results(results):
    # Находим победителя (гонщика с минимальным временем)
    winner = min(results.values(), key=lambda x: x['FinishedTimeSeconds'])

    # Выводим сообщение о победителе
    winner_message = f"Выиграл - {winner['RacerName']}!!! Поздравляем!!"
    print(winner_message)
    print("_" * len(winner_message))
    
    # Сортируем результаты гонки по времени
    sorted_results = sorted(results.values(), key=lambda x: x['FinishedTimeSeconds'])

    # Выводим первые три места
    print("\nПервые три места:\n")
    for i, racer in enumerate(sorted_results[:3], start=1):
        print(f"Гонщик на {i} месте:\n")
        print(f"Имя: {racer['RacerName']}\n")
        print(f"Команда: {racer['RacerTeam']}\n")
        time_seconds = racer['FinishedTimeSeconds']
        hours, remainder = divmod(time_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"Время: {time_str} (H:M:S)\n")
        print("\n")

if __name__ == "__main__":
    print_race_results(RACE_DATA)
# Импортируем данные из файла import_this.py
from started.import_this import RACE_DATA

def print_race_results(results):
    # Находим победителя (гонщика с минимальным временем)
    winner: dict = min(results.values(), key=lambda x: x['FinishedTimeSeconds'])

    # Выводим сообщение о победителе
    winner_message: str = f"Выиграл - {winner['RacerName'].upper()}!!! Поздравляем!!"
    print(winner_message + '\n')
    print("_" * len(winner_message))
    print("\n")
    
    # Сортируем результаты гонки по времени
    sorted_results: list = sorted(results.values(), key=lambda x: x['FinishedTimeSeconds'])

    # Выводим первые три места
    print("\nПервые три места:\n\n\n")
    for i, racer in enumerate(sorted_results[:3], start=1):
        print(f"Гонщик на {i} месте:\n")
        print(f"   Имя: {racer['RacerName']}\n")
        print(f"   Команда: {racer['RacerTeam']}\n")
        time_seconds: int = racer['FinishedTimeSeconds']
        hours: int
        remainder: int
        minutes: int
        seconds: int
        hours, remainder = divmod(time_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str: str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"   Время: {time_str} (H:M:S)\n")
        print("\n")

if __name__ == "__main__":
    print_race_results(RACE_DATA)
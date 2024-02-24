def main():
  n, m = map(int, input().split())
  
  # Создание кругового массива
  circular_array = list(range(1, n + 1))
  
  # Путь
  path = []
  
  # Индекс начала текущего интервала
  start_index = 0
  while True:
    # Добавление начального элемента интервала в путь
    path.append(circular_array[start_index])
    
    # Вычисление индекса конца текущего интервала
    end_index = (start_index + m - 1) % n
    
    # Проверка, является ли конец интервала первым элементом
    if end_index == 0:
      break
    
    # Начало следующего интервала
    start_index = end_index
  
  # Вывод пути
  print(*path)

if __name__ == "__main__":
  main()

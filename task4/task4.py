import sys

def min_moves(nums):
  mean = sum(nums) / len(nums)
  moves = [abs(num - mean) for num in nums]
  return sum(moves)


if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    nums = [int(line) for line in f]

  min_moves = min_moves(nums)
  print("Минимальное количество ходов:", min_moves)

# запуск : python3 task4.py numbers.txt
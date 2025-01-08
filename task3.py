def hanoi_tower(n, source, target, auxiliary, state):
    if n == 1:
        # Переміщення диску
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Перемістити n-1 дисків з source на auxiliary
        hanoi_tower(n - 1, source, auxiliary, target, state)
        # Перемістити найбільший диск з source на target
        hanoi_tower(1, source, target, auxiliary, state)
        # Перемістити n-1 дисків з auxiliary на target
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main():
    n = int(input("Введіть кількість дисків: "))
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi_tower(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
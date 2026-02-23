def total_salary(path: str) -> tuple[int, float]:
    
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    
                    _, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1

        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return 0, 0


if __name__ == "__main__":
    
    path_to_file = "Task_01/salary_file.txt"
    
    total, average = total_salary(path_to_file)
    
    if total > 0 or average > 0:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
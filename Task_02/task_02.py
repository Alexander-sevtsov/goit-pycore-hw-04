def get_cats_info(path: str) -> list[dict[str, str]]:
    
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                   
                    cat_id, name, age = line.split(',')
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
        
        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return []


if __name__ == "__main__":
   
    path_to_cats = "Task_02/cats_file.txt"
    cats = get_cats_info(path_to_cats)
    
    print(cats)
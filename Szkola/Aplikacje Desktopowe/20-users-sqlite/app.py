import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("400x400")
        
        #center window
        self.center_window()

        #main container
        self.main_frame = tk.Frame(self.root, padx = 20, pady = 20)
        self.main_frame.pack(expand=True, fill='both')
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        self.clear_frame()

        title = tk.Label(self.main_frame, text="Logowanie", font=("Arial", 20, 'bold'))
        title.pack(pady=20)

        tk.Label(self.main_frame, text="Email:", font=("Arial", 14)).pack(pady=5)
        self.login_email = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        self.login_email.pack(pady=10)
        
        tk.Label(self.main_frame, text="Hasło:", font=("Arial", 14)).pack(pady=5)
        self.login_password = tk.Entry(self.main_frame, width=30, font=("Arial", 14), show='*')
        self.login_password.pack(pady=10)
        
        btn_frame = ttk.Frame(self.main_frame)
        login_button = tk.Button(btn_frame, text="Zaloguj się", font=("Arial", 14), command=self.login)
        register_button = tk.Button(btn_frame, text="Zarejestruj się", font=("Arial", 14), command=self.show_register_screen)

        login_button.pack(pady=10)
        register_button.pack(pady=10)
        btn_frame.pack()

    def show_register_screen(self):
        self.clear_frame()

        title = tk.Label(self.main_frame, text="Rejestracja", font=("Arial", 20, 'bold'))
        title.pack(pady=20)

        tk.Label(self.main_frame, text="Email:", font=("Arial", 14)).pack(pady=5)
        self.reg_email = tk.Entry(self.main_frame, width=30, font=("Arial", 14))
        self.reg_email.pack(pady=10)
        
        tk.Label(self.main_frame, text="Hasło:", font=("Arial", 14)).pack(pady=5)
        self.reg_password = tk.Entry(self.main_frame, width=30, font=("Arial", 14), show='*')
        self.reg_password.pack(pady=10)

        tk.Label(self.main_frame, text="Potwierdź hasło:", font=("Arial", 14)).pack(pady=5)
        self.reg_password_confirm = tk.Entry(self.main_frame, width=30, font=("Arial", 14), show='*')
        self.reg_password_confirm.pack(pady=10)
        
        btn_frame = ttk.Frame(self.main_frame)
        register_button = tk.Button(btn_frame, text="Zarejestruj się", font=("Arial", 14), command=self.register)
        back_button = tk.Button(btn_frame, text="Wróć do logowania", font=("Arial", 14), command=self.show_login_screen)

        register_button.pack(pady=10)
        back_button.pack(pady=10)
        btn_frame.pack()

    def show_dashboard(self):
        self.clear_frame()

        title = tk.Label(self.main_frame, text="Panel użytkownika", font=("Arial", 14))
        title.pack(pady=20)

        welcome_label = tk.Label(self.main_frame, text="Witamy w panelu użytkownika!", font=("Arial", 14))
        welcome_label.pack(pady=10)

        info = tk.Label(self.main_frame, text="To jest przykładowy panel użytkownika po zalogowaniu.", font=("Arial", 12))
        info.pack(pady=10)

        tk.Button(self.main_frame, text="Wyloguj się", font=("Arial", 14), command=self.show_login_screen).pack(pady=20)

    def register(self):
        email = self.reg_email.get().strip()
        password = self.reg_password.get()
        password_confirm = self.reg_password_confirm.get()


        if not email or not password:
            messagebox.showerror("Błąd", "Proszę wypełnić wszystkie pola.")
            return
        
        if '@' not in email:
            messagebox.showerror("Błąd", "Brak '@' w emailu")
            return
        
        if password != password_confirm:
            messagebox.showerror("Błąd", "Hasła różnią się od siebie!")
            return
        
        session = Session()
        
        if session.query(Users).filter_by(email=email).first():
            messagebox.showerror("Błąd", "Użytkownik o podanym emailu już istnieje.")
            session.close()
            return
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = Users(email=email, password=hashed_password)
        session.add(new_user)
        session.commit()
        session.close()

        messagebox.showinfo("Sukces", "Rejestracja zakończona pomyślnie!")
        self.show_login_screen()

    def login(self):
        email = self.login_email.get().strip()
        password = self.login_password.get()

        if not email or not password:
            messagebox.showerror("Błąd", "Proszę wypełnić wszystkie pola.")
            return
        
        session = Session()
        user = session.query(Users).filter_by(email=email).first()
        if not user:
            messagebox.showerror("Błąd", "Nieprawidłowy email!")
            session.close()
            return
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user.password != hashed_password:
            messagebox.showerror("Błąd", "Nieprawidłowe hasło.")
            session.close()
            return
        
        self.show_dashboard()
        session.close()
        messagebox.showinfo("Sukces", "Zalogowano pomyślnie!")

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    app.show_login_screen()
    root.mainloop()
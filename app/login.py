from tkinter.constants import *
import ttkbootstrap as tb


class LoginWindow:
    def __init__(self, master) -> None:
        self.master = master
        self.is_logged = False

    def show(self):
        left_frame = tb.Frame(self.master, bootstyle="dark", border=True, borderwidth=5)
        right_frame = tb.Frame(self.master, bootstyle="dark", style="bg.TFrame")

        # Pack the frames horizontally to create the split layout
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Left frame - Large App Name
        app_name_label = tb.Label(
            left_frame,
            text="PEDKAI KRUSHI\nSEVA KENDRA",
            font=("Halvetica", 38, "bold"),
        )
        app_name_label.pack(pady=200)  # Add padding for spacing

        # Right frame - Login View
        username_label = tb.Label(right_frame, text="Username:")
        username_label.pack(pady=5)
        username_entry = tb.Entry(right_frame)
        username_entry.pack(padx=5)

        password_label = tb.Label(right_frame, text="Password:")
        password_label.pack(pady=5)
        password_entry = tb.Entry(right_frame, show="*")
        password_entry.pack(padx=5)

        login_button = tb.Button(
            right_frame,
            text="Login",
            command=lambda: self.handle_login(
                username_entry.get(), password_entry.get()
            ),
        )
        login_button.pack(pady=10, padx=5)

        cancel_button = tb.Button(right_frame, text="Quit", command=self.close_window)
        cancel_button.pack(pady=10, padx=5)

    def handle_login(self, username: str, password: str) -> None:
        print(f"{username=}:{password=}")
        self.is_logged = True

    def close_window(self) -> None:
        self.master.destroy()
        self.master.master.destroy()

    def is_logged_in(self) -> bool:
        return is_logged

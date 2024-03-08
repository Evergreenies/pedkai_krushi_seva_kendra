from tkinter.constants import *
import ttkbootstrap as tb

from login import LoginWindow


def set_layout(_app: tb.Window) -> None:
    _app.geometry(get_geometry(_app))
    PedkaiKrushiSevaKendra(_app)


def get_geometry(_app: tb.Window) -> str:
    return f"{_app.winfo_screenwidth()}x{_app.winfo_screenheight()}"


class PedkaiKrushiSevaKendra(tb.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        login = LoginWindow(self)
        login.show()
        if login.is_logged_in():
            pass


if __name__ == "__main__":
    app = tb.Window(
        "Pedkai Krushi Seva Kendra",
        themename="superhero",
    )
    set_layout(app)
    app.mainloop()

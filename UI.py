import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Complex Calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, padx=24)


    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame



    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calculator = GUI()
    calculator.run()

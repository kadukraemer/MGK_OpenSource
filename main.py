import tkinter as tk
from tkinter import ttk

# Sample configuration for UI elements
ui_config = [
    {"type": "label", "text": "Hello, World!", "row": 0, "column": 0, "font": ("Helvetica", 12)},
    {"type": "button", "text": "Click Me", "row": 1, "column": 0, "width": 15, "command": lambda: button_click()},
    {"type": "entry", "placeholder": "Enter Text", "row": 2, "column": 0, "width": 20},
    {"type": "checkbox", "text": "Check Me", "row": 3, "column": 0, "bg": "lightblue"},
    {"type": "frame", "row": 4, "column": 0, "bg": "lightgray", "height": 50},
    {"type": "menu", "menu_items": [
        {"type": "command", "label": "File", "command": lambda: menu_click("File")},
        {"type": "command", "label": "Edit", "command": lambda: menu_click("Edit")},
        {"type": "separator"},
        {"type": "command", "label": "Help", "command": lambda: menu_click("Help")}
    ], "row": 5, "column": 0},
    {"type": "combobox", "values": ["Option 1", "Option 2", "Option 3"], "row": 6, "column": 0, "width": 15, "event_handler": lambda event: combobox_select(event)}
]

class DynamicUIGenerator:
    def __init__(self, app, ui_config):
        self.app = app
        self.ui_config = ui_config
        self.create_ui()

    def create_ui(self):
        widget_types = {
            "label": self.create_label,
            "button": self.create_button,
            "entry": self.create_entry,
            "checkbox": self.create_checkbox,
            "frame": self.create_frame,
            "menu": self.create_menu,
            "combobox": self.create_combobox,
        }

        for item in self.ui_config:
            widget_type = item.get("type")
            create_widget = widget_types.get(widget_type)
            if create_widget:
                create_widget(item)

    def create_label(self, item):
        label = tk.Label(self.app, text=item["text"], font=item.get("font"))
        label.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)

    def create_button(self, item):
        command = item.get("command", None)  # Default command if not specified
        button = tk.Button(self.app, text=item["text"], width=item.get("width"), command=command)
        button.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)

    def create_entry(self, item):
        entry_text = tk.StringVar()
        entry_text.set(item.get("placeholder", ""))
        entry = tk.Entry(self.app, width=item.get("width"), textvariable=entry_text)
        entry.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)

    def create_checkbox(self, item):
        checkbox = tk.Checkbutton(self.app, text=item["text"], bg=item.get("bg"))
        checkbox.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)

    def create_frame(self, item):
        frame = tk.Frame(self.app, bg=item.get("bg"), height=item.get("height"))
        frame.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)

    def create_menu(self, item):
        menu = tk.Menu(self.app)
        for menu_item in item["menu_items"]:
            menu_type = menu_item.get("type")
            if menu_type == "command":
                menu.add_command(label=menu_item["label"], command=menu_item["command"])
            elif menu_type == "separator":
                menu.add_separator()
        self.app.config(menu=menu)

    def create_combobox(self, item):
        combobox = ttk.Combobox(self.app, values=item["values"], width=item.get("width"))
        combobox.grid_configure(row=item["row"], column=item["column"], padx=5, pady=5)
        event_handler = item.get("event_handler")
        if event_handler:
            combobox.bindtags((combobox, self.app, "all"))
            combobox.bind("<<ComboboxSelected>>", event_handler)

# Sample function
def button_click():
    print("Button Clicked!")

def menu_click(item):
    print(f"Menu Clicked: {item}")

def combobox_select(event):
    selected_value = event.widget.get()
    print(f"Combobox Selected: {selected_value}")

# Main App
app = tk.Tk()
app.title("Dynamic UI Generator")

ui_generator = DynamicUIGenerator(app, ui_config)
app.mainloop()

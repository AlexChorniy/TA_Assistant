import tkinter as tk
from tkinter import filedialog

# Main function to create the GUI application
# This application creates a window with a size of 400x800 pixels,
def setup_ui(root, logicResult):
    print(logicResult)  # Print the result of the logic to console

    root.title("400x800 Interface")

    # Set window size
    width = 400
    height = 800

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position for centering the window
    x = (screen_width - width ) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    # Label to display a message    
    label = tk.Label(root, text="Hello, world!", font=("Arial", 12))
    label.pack(pady=20)

    # Frame to hold buttons
    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    tk.Button(root, text="Select File", command=select_file).pack(pady=40)

    # Exit button
    exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
    exit_button.pack(side="left", padx=20)

    # Close button (same behavior here, but can be customized)
    close_button = tk.Button(button_frame, text="Close", command=root.destroy)
    close_button.pack(side="right", padx=60)

def perform_logic():
    # Placeholder for any logic you want to perform

    return "Logic performed successfully"

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("All files", "*.*"), 
            ("Text files", "*.txt"),
            ("Python files", "*.py"), 
            ("pdf files", "*.pdf")],
    )
    if file_path:
        print("User selected:", file_path)
        # You can now open, read, or process the file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("File content:")
            print(content)   

# 🔹 This launches the app
def main():
    root = tk.Tk()
    logicResult = perform_logic()
    setup_ui(root, logicResult)
    
    root.mainloop()

if __name__ == "__main__":
    main()

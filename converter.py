# converter.py
import argparse
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def terminal_mode(input_path, output_path):
    im = Image.open(input_path)
    im.save(output_path)
    print(f"Converted '{input_path}' to '{output_path}'")

def gui_mode():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    import_file_path = filedialog.askopenfilename(title="Select JPEG")
    if not import_file_path:
        return
    im = Image.open(import_file_path)
    export_file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if export_file_path:
        im.save(export_file_path)
        messagebox.showinfo("Success", f"Saved to {export_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true", help="Use GUI mode")
    parser.add_argument("--input", help="Input JPEG path (terminal mode)")
    parser.add_argument("--output", help="Output PNG path (terminal mode)")
    args = parser.parse_args()

    if args.gui:
        gui_mode()
    elif args.input and args.output:
        terminal_mode(args.input, args.output)
    else:
        print("Usage:")
        print("  GUI mode:     python converter.py --gui")
        print("  Terminal mode: python converter.py --input input.jpeg --output output.png")

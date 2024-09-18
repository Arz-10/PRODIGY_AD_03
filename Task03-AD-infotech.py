import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("500x250")  # Increase window size
        
        # Initialize time variables
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        
        # Set colors and fonts
        bg_color = "#2b2b2b"
        fg_color = "#ffffff"
        button_color = "#4caf50"
        button_font = ("Helvetica", 14, "bold")
        label_font = ("Helvetica", 64, "bold")
        
        # Configure window background color
        self.root.configure(bg=bg_color)
        
        # Create and place labels and buttons with updated styles
        self.label = tk.Label(root, text="00:00:00", font=label_font, fg=fg_color, bg=bg_color)
        self.label.pack(pady=20)  # Add padding around label
        
        # Create a frame to hold the buttons
        button_frame = tk.Frame(root, bg=bg_color)
        button_frame.pack(pady=10)
        
        # Button style with rounded corners
        style = {
            "bg": button_color,
            "fg": fg_color,
            "font": button_font,
            "width": 12,  # Increased button width for better fit
            "height": 2,
            "relief": "solid",
            "bd": 0,
            "highlightthickness": 0,
            "activebackground": "#388e3c",  # Darker shade on hover
            "borderwidth": 1,
        }

        # Create buttons with rounded corners and equal size using a canvas
        self.start_button = tk.Button(button_frame, text="Start", command=self.start, **style)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause, **style)
        self.pause_button.grid(row=0, column=1, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, **style)
        self.reset_button.grid(row=0, column=2, padx=10)
        
        # Add padding between buttons
        self.update_display()
        
    def update_display(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 100)
        
        self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
        
        self.root.after(10, self.update_display)
    
    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
    
    def pause(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
    
    def reset(self):
        self.elapsed_time = 0
        self.running = False
        self.update_display()

# Create the main window and start the application
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()

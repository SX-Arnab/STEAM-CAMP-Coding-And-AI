# import schedule
# import time

# def job():


# schedule.every().day.at("10:30").do(job)

# while True:
#     # Check if any scheduled task is ready to run
#     schedule.run_pending()
#     time.sleep(1)

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First App")
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pack=20) # 'pack' places it in the window with some padding

# Start the application
root.mainloop()


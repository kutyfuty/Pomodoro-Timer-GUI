# 🍅 Custom Pomodoro Timer with Settings

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge)

A customized version of the classic Pomodoro Timer. Unlike the standard implementation, this project features a **Dynamic Settings Menu** allowing users to modify Work/Break durations without restarting the code.

![WhatsApp Image 2026-01-26 at 22 15 24](https://github.com/user-attachments/assets/aaae6eee-c471-4872-894a-22f5631f6d16)

## ✨ Key Features (Added by Me)
* **⚙️ Dynamic Settings:** Includes a pop-up settings window (`Toplevel` widget) to customize timer durations.
* **💾 Live Updates:** Updates global variables dynamically based on user input.
* **🔊 Audio Feedback:** Uses `winsound` for auditory alerts when the timer ends.
* **Wait Mechanism:** Prevents button spamming using `after_cancel`.

## ⚠️ Compatibility Note
This project uses the `winsound` library for audio alerts, which is **Windows-exclusive**.
* **Windows Users:** Works out of the box.
* **Mac/Linux Users:** The code may crash on the beep function. Please remove `import winsound` and the `play_alarm()` function to run it.

## 🚀 How to Run
Since this project uses only Python's standard libraries, no external installation is required.

1. Clone the repository:
   ```bash
   git clone [https://github.com/kutyfuty/Pomodoro-Custom-App.git](https://github.com/kutyfuty/Pomodoro-Custom-App.git)

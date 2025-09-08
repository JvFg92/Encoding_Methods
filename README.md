# 📡 Signal Encoding Simulator  

A fun and interactive Python project to encode short text messages into digital line coding schemes such as:  
- 🔹 **2B1Q**: Maps pairs of binary bits (dibits) to four signal levels.  
- 🔹 **8B6T**: Maps groups of 6 binary bits (sextets) to a set of 8 signal levels.
- 🔹 **4DPAM5**: Maps dibits to four signal levels.
- 🔹 **MLT-3**:  A three-level line code that uses three voltage levels.

Each encoding scheme generates a plot of the signal waveform for visualization.

📂 Signal-Encoding-Simulator

 ┣ 📜 Codify.py          # Contains encoding functions and plotting utilities
 
 ┣ 📜 main.py            # Entry point for the program
 
 ┗ 📜 README.md          # Project documentation

---

## Requirements
- 🔹 **Python 3.12** (🐍)
- 🔹 **matplotlib** (🖼)

This project requires the `matplotlib` library to create and save the signal plots. You can install it using `pip`:
```bash
   pip install matplolib
```

---

## 🛠️ Installation  

1. Create a new folder:
```bash
   mkdir Encoding_Methods
   cd Encoding_Methods
 ```

2. Clone the repository:  
```bash
   git clone https://github.com/JvFg92/Encoding_Methods/
```

---

## ▶️ Usage

Run the main script:
```bash
   python main.py
```

You’ll be prompted to:

- 🔹 ✍️ Enter a message (up to 4 characters).

- 🔹 📊 Choose the encoding scheme.

- 🔹 🖼️ The program will generate and save a PNG image of the encoded signal.

⚠️The image files will be saved in the folder you created.⚠️


## 🎯 Example (Hi -> 2B1Q)
<img width="1000" height="400" alt="2B1Q_Encoding" src="https://github.com/user-attachments/assets/76f044ee-912a-41a1-b410-b1893e9fd40c" />

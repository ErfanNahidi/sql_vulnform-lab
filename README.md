# vulnform-lab

⚠️ **Educational Security Lab - Use Responsibly**

This is a deliberately insecure web form built with [Streamlit](https://streamlit.io) and raw SQLite. It is designed for training and practicing basic web security vulnerabilities such as:

- SQL Injection
- Cross-Site Scripting (XSS)
- Input validation bypasses

> ✅ Intended for educational and ethical testing **in isolated lab environments only**.

---

## 🧩 Features

- Simple GUI for inputting:
  - First name, last name, job
  - Country, province, and city (Iran)
  - Free-form text explanation (e.g. used for XSS training)
- Backend stores data with **raw SQL** (vulnerable by design)
- Easy to run, lightweight, no dependencies beyond `streamlit` and `sqlite3`

---

## 🚀 How to Run

1. **Install requirements** (only Streamlit is needed):
    ```bash
    pip install streamlit
    ```

2. **Run the app**:
    ```bash
    streamlit run gui.py
    ```

3. **Visit in your browser**:
    ```
    http://localhost:8501
    ```

---

## 📂 File Structure

.
├── gui.py # Streamlit GUI frontend
├── backend.py # Logic to save form data
└── db.py # SQLite DB and schema setup


---

## ⚠️ Warning

This app is **intentionally vulnerable**.

- Do **NOT** deploy it to public servers.
- Use only in controlled environments (e.g. local VMs, CTFs, isolated labs).
- Do **NOT** submit real or sensitive data.

This project is for **education**, **red team training**, and **research** purposes **only**.

---

## 📜 License

MIT License – feel free to use, fork, and modify, but **you are responsible** for all consequences of misuse.

---

## 🙋 Who is this for?

- Students learning ethical hacking
- Security researchers
- CTF competitors
- Developers learning secure coding via insecure examples

---

## ✍️ Author

Developed by a security enthusiast for training and awareness.

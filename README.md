# Astra - Smart Password Wordlist Generator

Astra is a lightweight and powerful terminal-based password wordlist generator for cybersecurity and penetration testing. Inspired by tools like `cupp` and `crunch`, Astra allows you to craft personalized password dictionaries using user details and smart combinations.

---

## 🔧 Features

- Easy-to-use CLI interface
- Combine names, DOBs, cities, symbols, years, and custom keywords
- Generate wordlists for offline attacks (WPA/WPA2, Hashcat, Hydra, etc.)
- Length filters (min/max)
- Verbose mode to see generated entries live
- Save output to `.txt` file

---

## 📦 Installation

Astra runs on Python 3.

```bash
# Clone the repository
git clone https://github.com/your-username/astra.git
cd astra

# Run it with Python
python3 astra.py --help
```

---

## 🚀 Usage Examples

```bash
python3 astra.py \
  --name Ram --dob 2000 --city Ajmer \
  --symbols @ # _ --years 2024 2025 \
  --custom NSS Cyber Sharma \
  --min-length 6 --max-length 16 \
  --output ram_passwords.txt --verbose
```

---

## 📂 Output

- Wordlist is saved to a `.txt` file of your choice (default: `astra_wordlist.txt`)
- Can be directly used with tools like:
  - `hydra -L usernames.txt -P astra_wordlist.txt ...`
  - `aircrack-ng -w astra_wordlist.txt ...`

---

## 📜 License

MIT License - Free for personal and educational use. See `LICENSE` for details.

---

## 🤝 Contribute

Feel free to fork, enhance, and contribute. You can suggest new pattern strategies or help improve performance.

---

## 👨‍💻 Author

Developed by Parth (aka `sentinel`) for the cyber community.

> *"Astra is not just a tool, it's a digital shastra—crafted for warriors in the world of 1s and 0s."*

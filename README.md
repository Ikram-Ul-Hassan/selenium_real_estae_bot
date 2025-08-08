# 🏘️ Selenium Real Estate Data Scraper - 99acres.com

A professional web scraping project built with **Python** and **Selenium** that automates the extraction of verified property listings from [99acres.com](https://www.99acres.com). This scraper applies smart filters, navigates paginated listings, and exports clean, analysis-ready data to Excel.

---

## 📌 Features

- 🔍 Automatically searches for properties in a given city (e.g. Chennai)
- 🧮 Adjusts budget filter via slider for refined results
- ✅ Applies filters like: Verified Listings, Ready to Move, With Photos, With Videos
- 📄 Extracts:
  - Property Name
  - Location (Cleaned)
  - Price (Converted to Lacs)
  - Area (in sqft)
  - BHK Count
- 📤 Exports clean data to `.xlsx` format (via Pandas)
- 🔁 Navigates through all result pages using `Next Page` button
- 🧠 Applies string cleaning and data transformation using Pandas

---

## 🛠️ Tech Stack Used

| Tool        | Purpose                            |
|-------------|------------------------------------|
| `Python`    | Programming Language               |
| `Selenium`  | Browser Automation (Web Scraping)  |
| `Pandas`    | DataFrame creation & Excel export  |
| `NumPy`     | Handling missing data              |
| `OpenPyXL`  | Write `.xlsx` files                |

---

## 📁 File Structure

```
├── 99_acres_project.py         # Main Scraper Script  
├── requirements.txt            # Dependencies  
├── sample_data.xlsx            # Cleaned Sample Output  
├── .gitignore                  # Ignoring unnecessary files
```

---

## 🔧 How to Run

### 📥 Clone the Repository

```
git clone https://github.com/IkramDev512/selenium-real-estate-data-scraper.git
cd selenium-real-estate-data-scraper
```

### 📦 Install Dependencies
  ```
  pip install -r requirements.txt
```
### ▶️ Run the Scraper
```
  python 99_acres_project.py
```
### 📊 Sample Output Format
| name                 | location | price\_in\_lac | area\_in\_sqft | bhk |
| -------------------- | -------- | -------------- | -------------- | --- |
| Prestige Bella Vista | Porur    | 88.0           | 1250           | 3   |
| DLF Commanders Court | Egmore   | 145.0          | 1700           | 3   |


### 🧑‍💻 About the Developer
Hi, I'm Ikram, a Python developer having expertise in browser automation, data extraction, and real-world data projects.
I’ve completed multiple scraping projects successfully.

---

## 📬 Let's Connect

Looking for a custom scraper or automation help? Feel free to contact me for freelance or collaboration!

- 📧 Email: [shahikram295@gmail.com](mailto:shahikram295@gmail.com)
- 💻 GitHub: [github.com/IkramDev512](https://github.com/IkramDev512)


📄 License
This project is open source and available under the MIT License.                 

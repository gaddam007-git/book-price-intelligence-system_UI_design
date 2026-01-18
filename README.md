
# 📘 Book Price Intelligence System – UI Design

This project is the **UI and deployment module** of the Book Price Intelligence System.  
It presents final price comparison results using a **Streamlit web application**, applying a **smart 5% discount rule** and showing the cheapest platform for each book.

This module is mainly used for:

- Final result visualization  
- Demonstration and presentation  
- Rule-based price adjustment display  

---

## 📂 Project Structure

```text
book-price-intelligence-system_UI_design/
├── app.py                     # Streamlit UI application
├── task3_price_comparison.csv # Input data
├── requirements.txt           # Dependencies
├── LICENSE                    # MIT License
└── README.md                  # This file
```
---

## 🚩 Module – UI Design & Deployment

**File:** `app.py`  
**Framework:** Streamlit


### Purpose:

* Display book prices from our website and competitor website
* Clean and standardize price values
* Apply smart discount logic
* Compare final prices
* Show cheapest website

---

## 📊 Input File

**File Name:**

```
task3_price_comparison.csv
```

### Required Columns:

| Column Name             | Description              |
| ----------------------- | ------------------------ |
| Book_Title              | Name of the book         |
| Our_Price               | Price on our website     |
| Lowest_Competitor_Price | Competitor website price |

Example:

```
Book_Title,Our_Price,Lowest_Competitor_Price
Book A,₹500,₹480
Book B,₹300,₹350
```

---

## ⚙️ Logic Implemented

1. Load data from CSV
2. Remove currency symbols
3. Convert prices to numeric values
4. If:

```
Our_Price > Competitor_Price
```

Then:

```
Apply 5% discount on Our_Price
```

5. Compare final prices
6. Decide cheapest website

---

## ▶ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This UI is deployed using:

* Streamlit Community Cloud (Free Tier)

Steps:

1. Push code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy `app.py`

A public link is generated for presentation and demo.

---

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas

---

## 🎯 Final Outcome

This UI:

* Shows final price comparison results
* Applies smart discount logic
* Identifies cheapest website
* Helps in decision making
* Used for live demo and presentation

---

## 👨‍💻 Author

**Gaddam Sathvik Reddy**
UI Module of Book Price Intelligence System
Developed using Python and Streamlit

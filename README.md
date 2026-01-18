```md
# 📘 Book Price Intelligence System – UI Design

This project is the **UI and deployment layer** of the Book Price Intelligence System.  
It presents final price comparison results using a **Streamlit web application**, applying a **smart 5% discount rule** and showing the cheapest platform for each book.

---

## 🎯 Project Purpose

This module focuses on:

- Displaying book prices from our website and competitor website  
- Cleaning and standardizing price values  
- Applying rule-based discount logic  
- Comparing final prices  
- Showing results in a clean web UI  

This is used mainly for:

- Demonstration  
- Presentation  
- Final output visualization  

---

## 📂 Project Structure

```

book-price-intelligence-system_UI_design/
│
├── app.py                     # Streamlit UI application
├── task3_price_comparison.csv # Input data
├── requirements.txt           # Dependencies
├── LICENSE                    # MIT License
└── README.md                  # Project documentation

```

---

## 📊 Input File

### File Name

```

task3_price_comparison.csv

```

### Required Columns

| Column Name | Description |
|-------------|-------------|
| Book_Title | Name of the book |
| Our_Price | Price on our website |
| Lowest_Competitor_Price | Competitor website price |

---

## ⚙️ Logic Implemented

1. Load data from CSV  
2. Remove currency symbols  
3. Convert prices to numbers  
4. If:

```

Our_Price > Competitor_Price

```

Then:

```

Apply 5% discount on Our_Price

````

5. Compare final prices  
6. Decide cheapest website  

---

## ▶ How to Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
````

2. Run the app:

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This UI is deployed using:

* Streamlit Community Cloud (Free)

Steps:

1. Push code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy `app.py`

A public link is generated for presentation.

---

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas

---

## 🎯 Final Outcome

This UI:

* Shows price comparison results
* Applies smart discount logic
* Helps decide cheapest platform
* Is used for live demo and presentation

---

## 👨‍💻 Author

**Gaddam Sathvik Reddy**
UI Module of Book Price Intelligence System
Developed using Python and Streamlit

import streamlit as st              # Streamlit for building web UI
import pandas as pd                # Pandas for data handling

st.set_page_config(layout="wide")   # Makes the app use full browser width
st.title("Price Comparison App")   # App title

# -----------------------
# URLs (Display only)
# -----------------------
c1, c2 = st.columns(2)              # Create two columns side by side
with c1:
    st.subheader("Our Website")     # Left column heading
    st.info("https://books.toscrape.com/")  # Display our website URL
with c2:
    st.subheader("Competitor Website")      # Right column heading
    st.info("https://booksrun.com")         # Display competitor URL

# -----------------------
# Load data
# -----------------------
df = pd.read_csv("task3_price_comparison.csv")   # Load CSV file into DataFrame

# Clean prices
# Convert price columns to string and remove symbols like ₹, $, etc.
df["Our_Price"] = df["Our_Price"].astype(str).str.replace(r"[^0-9.]", "", regex=True)
df["Lowest_Competitor_Price"] = df["Lowest_Competitor_Price"].astype(str).str.replace(r"[^0-9.]", "", regex=True)

# Convert cleaned strings to numeric values
df["Our_Price"] = pd.to_numeric(df["Our_Price"], errors="coerce")
df["Lowest_Competitor_Price"] = pd.to_numeric(df["Lowest_Competitor_Price"], errors="coerce")

# -----------------------
# Discount: 5% if Our_Price > Competitor_Price
# -----------------------
def calculate_discount(row):
    our = row["Our_Price"]              # Get our price
    comp = row["Lowest_Competitor_Price"]  # Get competitor price

    # If any value is missing, return 0 discount and original price
    if pd.isna(our) or pd.isna(comp):
        return 0, our

    # If our price is higher, apply 5% discount
    if our > comp:
        discount = our * 0.05
        final_price = our - discount
    else:
        discount = 0
        final_price = our

    # Return rounded values
    return round(discount, 2), round(final_price, 2)

# Apply discount function row-wise and create two new columns
df[["Discount_Given", "Discounted_Our_Price"]] = df.apply(
    lambda row: pd.Series(calculate_discount(row)), axis=1
)

# -----------------------
# Cheapest Website After Discount
# -----------------------
def get_cheapest_website(row):
    our = row["Discounted_Our_Price"]
    comp = row["Lowest_Competitor_Price"]

    # Handle missing values
    if pd.isna(our) and pd.isna(comp):
        return "Unknown"
    if pd.isna(our):
        return "Competitor"
    if pd.isna(comp):
        return "Our Website"

    # Compare prices
    if our < comp:
        return "Our Website"
    elif our > comp:
        return "Competitor"
    else:
        return "Both"

# Apply comparison function to each row
df["Cheapest_Website"] = df.apply(get_cheapest_website, axis=1)

# -----------------------
# Prepare Tables
# -----------------------
our_prices = df[["Book_Title", "Our_Price"]]     # Our website table
competitor_prices = df[["Book_Title", "Lowest_Competitor_Price"]]  # Competitor table

# Final result table with renamed column
result_df = df[[
    "Book_Title",
    "Our_Price",
    "Discount_Given",
    "Discounted_Our_Price",
    "Lowest_Competitor_Price",
    "Cheapest_Website"
]].rename(columns={"Lowest_Competitor_Price": "Competitor_Price"})

# -----------------------
# Tables + Compare Button
# -----------------------
t1, mid, t2 = st.columns([4,1,4])   # Create 3 columns (left, center, right)

with t1:
    st.subheader("Our Website Prices")
    st.dataframe(our_prices, height=250)   # Show our prices table

with mid:
    st.markdown("<br><br>", unsafe_allow_html=True)  # Add spacing
    compare = st.button("Compare")        # Button to trigger comparison

with t2:
    st.subheader("Competitor Prices")
    st.dataframe(competitor_prices, height=250)   # Show competitor prices

# -----------------------
# Result Section
# -----------------------
if compare:                             # When Compare button is clicked
    st.markdown("## Results After 5% Discount")
    st.dataframe(result_df, height=250)   # Show final comparison table
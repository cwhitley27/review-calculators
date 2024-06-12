#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit


# In[2]:


import streamlit as st

# Custom CSS to enhance aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: #31333f;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #00509e;
        color: white;
    }
    .stSelectbox, .stNumberInput {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Function definitions
def calculate_new_rating(current_rating, total_reviews, new_review):
    total_rating = current_rating * total_reviews
    total_rating += new_review
    return total_rating / (total_reviews + 1)

def reviews_needed_to_reach_target(current_rating, total_reviews, target_rating):
    additional_reviews = 0
    while current_rating < target_rating:
        total_reviews += 1
        additional_reviews += 1
        current_rating = ((current_rating * (total_reviews - 1)) + 5) / total_reviews
        if additional_reviews > 1000:  # Safety check
            return -1
    return additional_reviews

def reviews_needed_to_lower_rating(current_rating, total_reviews, target_rating, low_review_rating):
    additional_reviews = 0
    while current_rating > target_rating:
        total_reviews += 1
        additional_reviews += 1
        current_rating = ((current_rating * (total_reviews - 1)) + low_review_rating) / total_reviews
        if additional_reviews > 1000:  # Safety check
            return -1
    return additional_reviews

# Streamlit application
def main():
    st.title("🔢 Rating Calculator")
    st.write("### Choose a calculation type:")

    choice = st.selectbox("Select Calculation", ["New Rating", "Reviews Needed to Reach Target", "Reviews Needed to Lower Rating"])

    if choice == "New Rating":
        current_rating = st.number_input("Enter current rating:", min_value=0.0, max_value=5.0, step=0.1)
        total_reviews = st.number_input("Enter total number of reviews:", min_value=0, step=1)
        new_review = st.number_input("Enter new review rating:", min_value=0.0, max_value=5.0, step=0.1)
        if st.button("Calculate New Rating"):
            new_rating = calculate_new_rating(current_rating, total_reviews, new_review)
            st.write(f"### New average rating after receiving a {new_review}-star review: {new_rating:.2f}")

    elif choice == "Reviews Needed to Reach Target":
        current_rating = st.number_input("Enter current rating:", min_value=0.0, max_value=5.0, step=0.1)
        total_reviews = st.number_input("Enter total number of reviews:", min_value=0, step=1)
        target_rating = st.number_input("Enter target rating:", min_value=0.0, max_value=5.0, step=0.1)
        if st.button("Calculate Reviews Needed"):
            reviews_needed = reviews_needed_to_reach_target(current_rating, total_reviews, target_rating)
            if reviews_needed == -1:
                st.write("### More than 1000 reviews needed, calculation aborted for safety.")
            else:
                st.write(f"### Number of 5-star reviews needed to reach a {target_rating} rating: {reviews_needed}")

    elif choice == "Reviews Needed to Lower Rating":
        current_rating = st.number_input("Enter current rating:", min_value=0.0, max_value=5.0, step=0.1)
        total_reviews = st.number_input("Enter total number of reviews:", min_value=0, step=1)
        target_rating = st.number_input("Enter target rating:", min_value=0.0, max_value=5.0, step=0.1)
        low_review_rating = st.number_input("Enter low review rating (1-3 stars):", min_value=1.0, max_value=3.0, step=0.1)
        if st.button("Calculate Reviews Needed to Lower Rating"):
            reviews_needed_lower = reviews_needed_to_lower_rating(current_rating, total_reviews, target_rating, low_review_rating)
            if reviews_needed_lower == -1:
                st.write("### More than 1000 reviews needed, calculation aborted for safety.")
            else:
                st.write(f"### Number of {low_review_rating}-star reviews needed to decrease to a {target_rating} rating: {reviews_needed_lower}")

if __name__ == "__main__":
    main()


# In[ ]:





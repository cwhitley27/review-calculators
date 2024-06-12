import streamlit as st

# Custom CSS to enhance aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        color: #31333f;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    .stNumberInput>div>input {
        border-radius: 5px;
        border: 2px solid #4CAF50;
    }
    .stMarkdown {
        font-size: 16px;
    }
    .section {
        margin-bottom: 40px;
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
    st.write("Use these calculators to understand how ratings will affect your overall rating and other related scenarios.")

    # New Rating Calculator
    st.markdown("## 📈 New Rating Calculator")
    st.write("Calculate the new average rating after receiving a new review. For example, if your current rating is 4.2 with 50 reviews and you receive a new 5-star review, this calculator will show your new average rating.")
    
    current_rating_new = st.number_input("Enter current rating for New Rating Calculator:", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_new")
    total_reviews_new = st.number_input("Enter total number of reviews for New Rating Calculator:", min_value=0, step=1, key="total_reviews_new")
    new_review = st.number_input("Enter new review rating:", min_value=0.0, max_value=5.0, step=0.1, key="new_review")
    
    if st.button("Calculate New Rating", key="calc_new_rating"):
        new_rating = calculate_new_rating(current_rating_new, total_reviews_new, new_review)
        st.write(f"### New average rating after receiving a {new_review}-star review: {new_rating:.2f}")

    st.markdown("---")

    # Reviews Needed to Reach Target Rating
    st.markdown("## 🎯 Reviews Needed to Reach Target Rating")
    st.write("Calculate the number of 5-star reviews needed to reach a target rating. For example, if your current rating is 4.2 with 50 reviews and you want to reach a 4.5 rating, this calculator will show the number of additional 5-star reviews needed.")
    
    current_rating_target = st.number_input("Enter current rating for Target Rating Calculator:", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_target")
    total_reviews_target = st.number_input("Enter total number of reviews for Target Rating Calculator:", min_value=0, step=1, key="total_reviews_target")
    target_rating = st.number_input("Enter target rating:", min_value=0.0, max_value=5.0, step=0.1, key="target_rating")
    
    if st.button("Calculate Reviews Needed to Reach Target Rating", key="calc_target_rating"):
        reviews_needed = reviews_needed_to_reach_target(current_rating_target, total_reviews_target, target_rating)
        if reviews_needed == -1:
            st.write("### More than 1000 reviews needed, calculation aborted for safety.")
        else:
            st.write(f"### Number of 5-star reviews needed to reach a {target_rating} rating: {reviews_needed}")

    st.markdown("---")

    # Reviews Needed to Lower Rating
    st.markdown("## 📉 Reviews Needed to Lower Rating")
    st.write("Calculate the number of low-star reviews needed to decrease your rating to a target rating. For example, if your current rating is 4.2 with 50 reviews and you want to decrease it to a 3.8 rating with 1-star reviews, this calculator will show the number of additional 1-star reviews needed.")
    
    current_rating_lower = st.number_input("Enter current rating for Lower Rating Calculator:", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_lower")
    total_reviews_lower = st.number_input("Enter total number of reviews for Lower Rating Calculator:", min_value=0, step=1, key="total_reviews_lower")
    target_rating_lower = st.number_input("Enter target rating for Lower Rating Calculator:", min_value=0.0, max_value=5.0, step=0.1, key="target_rating_lower")
    low_review_rating = st.number_input("Enter low review rating (1-3 stars):", min_value=1.0, max_value=3.0, step=0.1, key="low_review_rating")
    
    if st.button("Calculate Reviews Needed to Lower Rating", key="calc_lower_rating"):
        reviews_needed_lower = reviews_needed_to_lower_rating(current_rating_lower, total_reviews_lower, target_rating_lower, low_review_rating)
        if reviews_needed_lower == -1:
            st.write("### More than 1000 reviews needed, calculation aborted for safety.")
        else:
            st.write(f"### Number of {low_review_rating}-star reviews needed to decrease to a {target_rating_lower} rating: {reviews_needed_lower}")

if __name__ == "__main__":
    main()

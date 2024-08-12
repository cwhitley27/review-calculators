import streamlit as st

# Custom CSS to enhance aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: #31333f;
    }
    .stButton>button {
        background-color: #0F2866;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #0C1F4A;
        color: white;
    }
    .stNumberInput>div>input {
        background-color: #ffffff;
        color: #31333f;
        border-radius: 5px;
        border: 2px solid #000000;
        width: 200px; /* Set input field width */
    }
    .stSelectbox>div>div {
        background-color: #ffffff;
        color: #31333f;
        border-radius: 5px;
        border: 2px solid #000000;
        width: 200px; /* Set input field width */
    }
    .stMarkdown {
        font-size: 16px;
        color: #31333f;
    }
    .stMarkdown strong {
        font-weight: bold;
    }
    .section {
        margin-bottom: 40px;
    }
    .error {
        color: red;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

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
    st.title("🔢 Short Term Rental Rating Calculator")
    st.write("As Air BnB and other platforms become more saturated and competitive, it's important to ensure as a host we are receiving 5-star reviews and maintaining a high overall rating. Use any of the three calculators to better understand how your properties overall rating will be impacted by various scenarios.")

    # Reviews Needed to Reach Target Rating (Moved to First Position)
    st.markdown("## 🎯 Reviews Needed to Reach Target Rating")
    st.write("**Calculate the number of 5-star reviews needed to reach a target rating. For example, if your current rating is 4.2 with 50 reviews and you want to reach a 4.5 rating, this calculator will show the number of additional 5-star reviews needed.**")
    
    current_rating_target = st.number_input("**Enter your properties current rating:**", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_target")
    total_reviews_target = st.number_input("**Enter how many total reviews your property has:**", min_value=0, step=1, key="total_reviews_target")
    target_rating = st.number_input("**Enter the rating you want to achieve:**", min_value=0.0, max_value=5.0, step=0.1, key="target_rating")
    
    if st.button("Calculate Reviews Needed to Reach Target Rating", key="calc_target_rating"):
        if current_rating_target is not None and total_reviews_target is not None and target_rating is not None:
            reviews_needed = reviews_needed_to_reach_target(current_rating_target, total_reviews_target, target_rating)
            if reviews_needed == -1:
                st.write("### More than 1000 reviews needed, calculation aborted for safety.")
            else:
                st.write(f"### You need {reviews_needed} 5-star reviews to reach a {target_rating} rating")
        else:
            st.markdown("<div class='error'>Please fill out all fields.</div>", unsafe_allow_html=True)

    st.markdown("---")

    # New Rating Calculator (Moved to Second Position)
    st.markdown("## 📈 New Rating Calculator")
    st.write("**Calculate what your new overall rating will be after receiving a new review. For example, if your current rating is 4.2 with 50 reviews and you receive a new 5-star review, this calculator will show your new average rating.**")
    
    current_rating_new = st.number_input("**Enter your properties current rating:**", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_new")
    total_reviews_new = st.number_input("**Enter how many total reviews your property has:**", min_value=0, step=1, key="total_reviews_new")
    new_review = st.number_input("**Enter the new rating:**", min_value=0, max_value=5, step=1, key="new_review")
    
    if st.button("Calculate New Rating", key="calc_new_rating"):
        if current_rating_new is not None and total_reviews_new is not None and new_review is not None:
            new_rating = calculate_new_rating(current_rating_new, total_reviews_new, new_review)
            st.write(f"### Your new average rating after receiving the latest {new_review}-star review: {new_rating:.2f}")
        else:
            st.markdown("<div class='error'>Please fill out all fields.</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Reviews Needed to Lower Rating
    st.markdown("## 📉 How will my rating drop?")
    st.write("**Calculate the number of low-star reviews needed to decrease your rating to a target rating. For example, if your current rating is 4.2 with 50 reviews and you want to decrease it to a 3.8 rating with 1-star reviews, this calculator will show the number of additional 1-star reviews needed.**")
    
    current_rating_lower = st.number_input("**Enter your properties current rating:**", min_value=0.0, max_value=5.0, step=0.1, key="current_rating_lower")
    total_reviews_lower = st.number_input("**Enter how many total reviews your property has:**", min_value=0, step=1, key="total_reviews_lower")
    target_rating_lower = st.number_input("**Enter target rating:**", min_value=0.0, max_value=5.0, step=0.1, key="target_rating_lower")
    low_review_rating = st.number_input("**Enter low review rating (1-3 stars):**", min_value=1.0, max_value=3.0, step=0.1, key="low_review_rating")
    
    if st.button("Calculate Reviews Needed to Lower Rating", key="calc_lower_rating"):
        if current_rating_lower is not None and total_reviews_lower is not None and target_rating_lower is not None and low_review_rating is not None:
            reviews_needed_lower = reviews_needed_to_lower_rating(current_rating_lower, total_reviews_lower, target_rating_lower, low_review_rating)
            if reviews_needed_lower == -1:
                st.write("### More than 1000 reviews needed, calculation aborted for safety.")
            else:
                st.write(f"### Number of {low_review_rating}-star reviews needed to decrease to a {target_rating_lower} rating: {reviews_needed_lower}")
        else:
            st.markdown("<div class='error'>Please fill out all fields.</div>", unsafe_allow_html=True)

if __name__ == "__main

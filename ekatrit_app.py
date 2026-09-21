import streamlit as st
import pandas as pd
import os
import hashlib
from datetime import datetime, date

# ============================================================
# EKATRIT - SOCIAL IMPACT & FUNDRAISING PLATFORM
# ============================================================

st.set_page_config(
    page_title="Ekatrit",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# FILE PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.csv")
CAMPAIGNS_FILE = os.path.join(DATA_DIR, "campaigns.csv")
DONATIONS_FILE = os.path.join(DATA_DIR, "donations.csv")
CREATED_CAMPAIGNS_FILE = os.path.join(DATA_DIR, "campaigns_created.csv")
REWARDS_FILE = os.path.join(DATA_DIR, "rewards.csv")
REDEMPTIONS_FILE = os.path.join(DATA_DIR, "redemptions.csv")
UPDATES_FILE = os.path.join(DATA_DIR, "updates.csv")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.csv")

os.makedirs(DATA_DIR, exist_ok=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_data(file, columns):
    """Load CSV safely. Create it if it doesn't exist."""
    if os.path.exists(file):
        try:
            df = pd.read_csv(file)
            for column in columns:
                if column not in df.columns:
                    df[column] = ""
            return df[columns] if not df.empty else df
        except Exception:
            pass

    df = pd.DataFrame(columns=columns)
    df.to_csv(file, index=False)
    return df


def save_data(df, file):
    """Save dataframe to CSV."""
    df.to_csv(file, index=False)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def next_id(df, column, prefix):
    if df.empty:
        return f"{prefix}001"

    numbers = []
    for value in df[column].astype(str):
        digits = "".join(filter(str.isdigit, value))
        if digits:
            numbers.append(int(digits))

    number = max(numbers) + 1 if numbers else 1
    return f"{prefix}{number:03d}"


def to_float(value, default=0.0):
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def to_int(value, default=0):
    return int(to_float(value, default))


# ============================================================
# DATA LOADING
# ============================================================

USER_COLUMNS = [
    "user_id", "name", "email", "phone", "age", "city",
    "password", "points", "total_donation",
    "campaigns_supported", "created_at"
]

CAMPAIGN_COLUMNS = [
    "campaign_id", "campaign_name", "category",
    "description", "location", "goal_amount",
    "raised_amount", "donors", "status",
    "start_date", "end_date"
]

DONATION_COLUMNS = [
    "donation_id", "user_id", "campaign_id",
    "amount", "points_earned", "donation_date"
]

CREATED_CAMPAIGN_COLUMNS = [
    "campaign_id", "creator_user_id", "campaign_name",
    "category", "description", "goal_amount",
    "raised_amount", "donors", "location",
    "start_date", "end_date", "status"
]

REWARD_COLUMNS = [
    "reward_id", "reward_name", "points_required",
    "description", "status"
]

REDEMPTION_COLUMNS = [
    "redemption_id", "user_id", "reward_id",
    "points_used", "redemption_date"
]

UPDATE_COLUMNS = [
    "update_id", "campaign_id", "title",
    "update_text", "update_date"
]

FEEDBACK_COLUMNS = [
    "feedback_id", "user_id", "rating",
    "feedback", "suggestion", "submitted_at"
]

users = load_data(USERS_FILE, USER_COLUMNS)
campaigns = load_data(CAMPAIGNS_FILE, CAMPAIGN_COLUMNS)
donations = load_data(DONATIONS_FILE, DONATION_COLUMNS)
created_campaigns = load_data(CREATED_CAMPAIGNS_FILE, CREATED_CAMPAIGN_COLUMNS)
rewards = load_data(REWARDS_FILE, REWARD_COLUMNS)
redemptions = load_data(REDEMPTIONS_FILE, REDEMPTION_COLUMNS)
updates = load_data(UPDATES_FILE, UPDATE_COLUMNS)
feedback = load_data(FEEDBACK_FILE, FEEDBACK_COLUMNS)

# Seed a few default rewards the first time the app runs
if rewards.empty:
    rewards = pd.DataFrame([
        {"reward_id": "R001", "reward_name": "Bronze Supporter Badge",
         "points_required": 100, "description": "A digital badge for your profile.", "status": "Active"},
        {"reward_id": "R002", "reward_name": "Silver Supporter Badge",
         "points_required": 500, "description": "Show off your growing impact.", "status": "Active"},
        {"reward_id": "R003", "reward_name": "Ekatrit E-Certificate",
         "points_required": 1000, "description": "An official certificate of appreciation.", "status": "Active"},
        {"reward_id": "R004", "reward_name": "Gold Supporter Badge",
         "points_required": 2000, "description": "For our most dedicated changemakers.", "status": "Active"},
        {"reward_id": "R005", "reward_name": "Ekatrit Merch Voucher",
         "points_required": 5000, "description": "Redeemable for Ekatrit branded merchandise.", "status": "Active"},
    ])
    save_data(rewards, REWARDS_FILE)


# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
:root {
    --ek-primary: #ff6b35;
    --ek-primary-dark: #e0511e;
    --ek-secondary: #2b2d42;
    --ek-bg-soft: rgba(255, 107, 53, 0.06);
}

.main-title {
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 0px;
    background: linear-gradient(90deg, var(--ek-primary), #f7931e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

.subtitle {
    font-size: 17px;
    color: #8a8a8a;
    margin-top: -6px;
    margin-bottom: 10px;
}

.ek-card {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid rgba(128,128,128,0.18);
    margin-bottom: 16px;
    background: var(--ek-bg-soft);
}

.ek-stat {
    padding: 14px 18px;
    border-radius: 14px;
    border: 1px solid rgba(128,128,128,0.18);
    text-align: center;
}

.ek-badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 999px;
    background: var(--ek-primary);
    color: white;
    font-size: 12px;
    font-weight: 600;
}

.stButton>button[kind="primary"] {
    background-color: var(--ek-primary);
    border-color: var(--ek-primary);
}

.stButton>button[kind="primary"]:hover {
    background-color: var(--ek-primary-dark);
    border-color: var(--ek-primary-dark);
}

hr {
    margin: 0.6rem 0 1.2rem 0;
}
</style>
""", unsafe_allow_html=True)


def app_header(subtitle="Together, we create an impact."):
    st.markdown('<div class="main-title">🤝 Ekatrit</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{subtitle}</div>', unsafe_allow_html=True)


# ============================================================
# AUTH SCREEN (LOGIN / SIGN UP)
# ============================================================

if not st.session_state.logged_in:

    app_header()
    st.divider()

    login_tab, signup_tab = st.tabs(["🔐 Log In", "✨ Create Account"])

    # ---------------- LOGIN ----------------
    with login_tab:
        st.subheader("Welcome back")

        with st.form("login_form"):
            login_email = st.text_input("Email Address")
            login_password = st.text_input("Password", type="password")
            login_submitted = st.form_submit_button(
                "Log In", use_container_width=True, type="primary"
            )

        if login_submitted:
            if not login_email.strip() or not login_password:
                st.error("Please enter both your email and password.")
            else:
                match = users[
                    (users["email"].astype(str).str.lower() == login_email.strip().lower())
                    & (users["password"].astype(str) == hash_password(login_password))
                ]
                if match.empty:
                    st.error("Incorrect email or password.")
                else:
                    st.session_state.user_id = str(match.iloc[0]["user_id"])
                    st.session_state.logged_in = True
                    st.rerun()

    # ---------------- SIGN UP ----------------
    with signup_tab:
        st.subheader("Create Your Ekatrit Account")
        st.write("Enter your details below to create your Ekatrit profile.")

        with st.form("signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")

            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age", min_value=1, max_value=120, value=18)
            with col2:
                city = st.text_input("City")

            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

            submitted = st.form_submit_button(
                "Create My Ekatrit Account", use_container_width=True, type="primary"
            )

        if submitted:
            if not name.strip():
                st.error("Please enter your name.")
            elif not email.strip():
                st.error("Please enter your email.")
            elif not phone.strip():
                st.error("Please enter your phone number.")
            elif not city.strip():
                st.error("Please enter your city.")
            elif not password:
                st.error("Please create a password.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif email.lower().strip() in users["email"].astype(str).str.lower().values:
                st.error("An account with this email already exists. Please log in instead.")
            else:
                new_user_id = next_id(users, "user_id", "U")

                new_user = pd.DataFrame([{
                    "user_id": new_user_id,
                    "name": name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                    "age": int(age),
                    "city": city.strip(),
                    "password": hash_password(password),
                    "points": 0,
                    "total_donation": 0,
                    "campaigns_supported": 0,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }])

                users = pd.concat([users, new_user], ignore_index=True)
                save_data(users, USERS_FILE)

                st.session_state.user_id = new_user_id
                st.session_state.logged_in = True

                st.success(f"Welcome to Ekatrit, {name}! Your account has been created.")
                st.rerun()

    st.info(
        "This is a prototype. Create a new account, or log in with an "
        "account you created earlier in this session."
    )
    st.stop()


# ============================================================
# CURRENT USER
# ============================================================

users = load_data(USERS_FILE, USER_COLUMNS)

current_user_rows = users[users["user_id"].astype(str) == str(st.session_state.user_id)]

if current_user_rows.empty:
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.rerun()

current_user = current_user_rows.iloc[0]
user_id = str(current_user["user_id"])
user_name = str(current_user["name"])

points = to_int(current_user["points"])
total_donation = to_float(current_user["total_donation"])
campaigns_supported = to_int(current_user["campaigns_supported"])


# ============================================================
# HEADER
# ============================================================

header_col, logout_col = st.columns([6, 1])
with header_col:
    app_header()
    st.write(f"Welcome, **{user_name}** 👋")
with logout_col:
    st.write("")
    if st.button("Log Out", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.rerun()

stat1, stat2, stat3 = st.columns(3)
with stat1:
    st.markdown(
        f'<div class="ek-stat"><div class="big-number">⭐ {points}</div>'
        f'<div>Ekatrit Points</div></div>',
        unsafe_allow_html=True,
    )
with stat2:
    st.markdown(
        f'<div class="ek-stat"><div class="big-number">₹{total_donation:,.0f}</div>'
        f'<div>Total Donated</div></div>',
        unsafe_allow_html=True,
    )
with stat3:
    st.markdown(
        f'<div class="ek-stat"><div class="big-number">{campaigns_supported}</div>'
        f'<div>Campaigns Supported</div></div>',
        unsafe_allow_html=True,
    )

st.divider()


# ============================================================
# SIDEBAR MAIN MENU
# ============================================================

st.sidebar.title("🤝 MAIN MENU")

menu_options = [
    "🌍 Explore Campaigns",
    "🔎 Search Campaigns",
    "💝 Donate",
    "📢 Create Campaign",
    "👤 My Profile",
    "🧾 Donation History",
    "🎁 Redeem Points",
    "📰 Campaign Updates",
    "📊 Ekatrit Impact",
    "🚪 Exit",
]

selected_menu = st.sidebar.radio("Choose an option:", menu_options)

st.sidebar.divider()
st.sidebar.metric("Your Points", points)
st.sidebar.metric("Total Donated", f"₹{total_donation:,.0f}")


# ============================================================
# 1. EXPLORE CAMPAIGNS
# ============================================================

if selected_menu == "🌍 Explore Campaigns":

    st.header("🌍 Explore Campaigns")
    st.write("Discover verified social-impact campaigns and choose a cause you would like to support.")

    if campaigns.empty:
        st.warning("No campaigns are currently available. Be the first to create one!")
    else:
        categories = ["All"] + sorted(campaigns["category"].dropna().astype(str).unique().tolist())
        category = st.selectbox("Filter by Category", categories)

        display_campaigns = campaigns.copy()
        if category != "All":
            display_campaigns = display_campaigns[display_campaigns["category"] == category]

        if display_campaigns.empty:
            st.info("No campaigns match this filter yet.")

        for _, campaign in display_campaigns.iterrows():
            goal = to_float(campaign["goal_amount"])
            raised = to_float(campaign["raised_amount"])
            progress = min(raised / goal, 1) if goal > 0 else 0

            with st.container(border=True):
                st.subheader(str(campaign["campaign_name"]))
                st.write(str(campaign["description"]))

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Category:** {campaign['category']}")
                with col2:
                    st.write(f"**Location:** {campaign['location']}")
                with col3:
                    st.markdown(f'<span class="ek-badge">{campaign["status"]}</span>', unsafe_allow_html=True)

                st.progress(progress)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Raised", f"₹{raised:,.0f}")
                with col2:
                    st.metric("Goal", f"₹{goal:,.0f}")
                with col3:
                    st.metric("Donors", to_int(campaign["donors"]))


# ============================================================
# 2. SEARCH CAMPAIGNS
# ============================================================

elif selected_menu == "🔎 Search Campaigns":

    st.header("🔎 Search Campaigns")
    search = st.text_input("Search by campaign name, category or location")

    if search:
        term = search.lower()
        results = campaigns[
            campaigns.apply(
                lambda row:
                    term in str(row["campaign_name"]).lower()
                    or term in str(row["category"]).lower()
                    or term in str(row["location"]).lower()
                    or term in str(row["description"]).lower(),
                axis=1
            )
        ] if not campaigns.empty else campaigns

        if results.empty:
            st.warning("No campaigns found.")
        else:
            st.success(f"{len(results)} campaign(s) found.")
            for _, campaign in results.iterrows():
                with st.container(border=True):
                    st.subheader(str(campaign["campaign_name"]))
                    st.write(str(campaign["description"]))
                    st.write(
                        f"📍 {campaign['location']}  |  "
                        f"🏷️ {campaign['category']}  |  "
                        f"Status: {campaign['status']}"
                    )
    else:
        st.info("Enter something to search.")


# ============================================================
# 3. DONATE
# ============================================================

elif selected_menu == "💝 Donate":

    st.header("💝 Make a Donation")

    if campaigns.empty:
        st.warning("No campaigns are available yet.")
    else:
        campaign_names = campaigns["campaign_name"].astype(str).tolist()
        selected_campaign_name = st.selectbox("Choose a campaign", campaign_names)
        selected_campaign = campaigns[campaigns["campaign_name"] == selected_campaign_name].iloc[0]

        st.info(f"**{selected_campaign_name}** — {selected_campaign['description']}")

        amount = st.number_input(
            "Enter donation amount (₹)",
            min_value=1.0,
            max_value=100000000.0,
            value=500.0,
            step=1.0,
        )

        points_earned = int(amount // 10)
        st.write(f"⭐ You will earn **{points_earned} Ekatrit Points**")

        if st.button("Donate Now", type="primary", use_container_width=True):
            donation_id = next_id(donations, "donation_id", "D")
            campaign_id = selected_campaign["campaign_id"]

            new_donation = pd.DataFrame([{
                "donation_id": donation_id,
                "user_id": user_id,
                "campaign_id": campaign_id,
                "amount": amount,
                "points_earned": points_earned,
                "donation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }])
            donations = pd.concat([donations, new_donation], ignore_index=True)
            save_data(donations, DONATIONS_FILE)

            mask = campaigns["campaign_id"].astype(str) == str(campaign_id)
            campaigns.loc[mask, "raised_amount"] = campaigns.loc[mask, "raised_amount"].apply(to_float) + amount
            campaigns.loc[mask, "donors"] = campaigns.loc[mask, "donors"].apply(to_int) + 1
            save_data(campaigns, CAMPAIGNS_FILE)

            # Keep the created_campaigns mirror table in sync, if applicable
            if not created_campaigns.empty:
                cmask = created_campaigns["campaign_id"].astype(str) == str(campaign_id)
                if cmask.any():
                    created_campaigns.loc[cmask, "raised_amount"] = (
                        created_campaigns.loc[cmask, "raised_amount"].apply(to_float) + amount
                    )
                    created_campaigns.loc[cmask, "donors"] = (
                        created_campaigns.loc[cmask, "donors"].apply(to_int) + 1
                    )
                    save_data(created_campaigns, CREATED_CAMPAIGNS_FILE)

            user_index = users[users["user_id"].astype(str) == user_id].index[0]
            users.loc[user_index, "points"] = points + points_earned
            users.loc[user_index, "total_donation"] = total_donation + amount
            users.loc[user_index, "campaigns_supported"] = campaigns_supported + 1
            save_data(users, USERS_FILE)

            st.success(f"Donation of ₹{amount:,.2f} completed successfully!")
            st.balloons()
            st.info(f"You earned **{points_earned} points**. Your new balance is **{points + points_earned} points**.")
            st.rerun()


# ============================================================
# 4. CREATE CAMPAIGN
# ============================================================

elif selected_menu == "📢 Create Campaign":

    st.header("📢 Create a Campaign")
    st.write("Create your own social-impact campaign and start raising support.")

    with st.form("campaign_form"):
        campaign_name = st.text_input("Campaign Name")

        category = st.selectbox(
            "Category",
            [
                "Education", "Medical", "Food", "Environment",
                "Disaster Relief", "Animal Welfare",
                "Community Development", "Skill Development",
                "Youth", "Other",
            ],
        )

        description = st.text_area("Campaign Description")
        goal_amount = st.number_input("Fundraising Goal (₹)", min_value=1.0, value=10000.0, step=100.0)
        location = st.text_input("Location")

        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=date.today())
        with col2:
            end_date = st.date_input("End Date")

        submitted = st.form_submit_button("Submit Campaign", use_container_width=True, type="primary")

    if submitted:
        if not campaign_name.strip():
            st.error("Please enter a campaign name.")
        elif not description.strip():
            st.error("Please enter a description.")
        elif not location.strip():
            st.error("Please enter the campaign location.")
        elif end_date < start_date:
            st.error("End date cannot be before start date.")
        else:
            campaign_id = next_id(campaigns, "campaign_id", "C")
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")

            new_campaign = pd.DataFrame([{
                "campaign_id": campaign_id,
                "campaign_name": campaign_name.strip(),
                "category": category,
                "description": description.strip(),
                "location": location.strip(),
                "goal_amount": goal_amount,
                "raised_amount": 0,
                "donors": 0,
                "status": "Active",
                "start_date": start_str,
                "end_date": end_str,
            }])
            campaigns = pd.concat([campaigns, new_campaign], ignore_index=True)
            save_data(campaigns, CAMPAIGNS_FILE)

            new_created = pd.DataFrame([{
                "campaign_id": campaign_id,
                "creator_user_id": user_id,
                "campaign_name": campaign_name.strip(),
                "category": category,
                "description": description.strip(),
                "goal_amount": goal_amount,
                "raised_amount": 0,
                "donors": 0,
                "location": location.strip(),
                "start_date": start_str,
                "end_date": end_str,
                "status": "Active",
            }])
            created_campaigns = pd.concat([created_campaigns, new_created], ignore_index=True)
            save_data(created_campaigns, CREATED_CAMPAIGNS_FILE)

            st.success(f"🎉 Campaign **{campaign_name}** has been created and is now live!")
            st.balloons()


# ============================================================
# 5. MY PROFILE
# ============================================================

elif selected_menu == "👤 My Profile":

    st.header("👤 My Profile")

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Name:** {current_user['name']}")
            st.write(f"**Email:** {current_user['email']}")
            st.write(f"**Phone:** {current_user['phone']}")
        with col2:
            st.write(f"**Age:** {to_int(current_user['age'])}")
            st.write(f"**City:** {current_user['city']}")
            st.write(f"**Member Since:** {current_user['created_at']}")

    st.subheader("Your Impact")
    col1, col2, col3 = st.columns(3)
    col1.metric("Ekatrit Points", points)
    col2.metric("Total Donated", f"₹{total_donation:,.0f}")
    col3.metric("Campaigns Supported", campaigns_supported)

    my_campaigns = created_campaigns[created_campaigns["creator_user_id"].astype(str) == user_id]
    if not my_campaigns.empty:
        st.subheader("Campaigns You Created")
        for _, c in my_campaigns.iterrows():
            with st.container(border=True):
                st.write(f"**{c['campaign_name']}** — {c['status']}")
                st.write(f"Raised ₹{to_float(c['raised_amount']):,.0f} of ₹{to_float(c['goal_amount']):,.0f}")


# ============================================================
# 6. DONATION HISTORY
# ============================================================

elif selected_menu == "🧾 Donation History":

    st.header("🧾 Donation History")

    my_donations = donations[donations["user_id"].astype(str) == user_id].copy()

    if my_donations.empty:
        st.info("You haven't made any donations yet. Head over to the Donate page!")
    else:
        my_donations = my_donations.merge(
            campaigns[["campaign_id", "campaign_name"]],
            on="campaign_id",
            how="left",
        )
        my_donations["amount"] = my_donations["amount"].apply(to_float)
        my_donations["points_earned"] = my_donations["points_earned"].apply(to_int)

        my_donations = my_donations.sort_values("donation_date", ascending=False)

        st.dataframe(
            my_donations[["donation_date", "campaign_name", "amount", "points_earned"]].rename(
                columns={
                    "donation_date": "Date",
                    "campaign_name": "Campaign",
                    "amount": "Amount (₹)",
                    "points_earned": "Points Earned",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.metric("Total Donated (all time)", f"₹{my_donations['amount'].sum():,.0f}")


# ============================================================
# 7. REDEEM POINTS
# ============================================================

elif selected_menu == "🎁 Redeem Points":

    st.header("🎁 Redeem Your Points")
    st.write(f"You currently have **⭐ {points} points**.")

    active_rewards = rewards[rewards["status"].astype(str) == "Active"]

    if active_rewards.empty:
        st.info("No rewards are available right now.")
    else:
        for _, reward in active_rewards.iterrows():
            req_points = to_int(reward["points_required"])
            with st.container(border=True):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{reward['reward_name']}** — {req_points} points")
                    st.write(reward["description"])
                with col2:
                    disabled = points < req_points
                    if st.button(
                        "Redeem",
                        key=f"redeem_{reward['reward_id']}",
                        disabled=disabled,
                        use_container_width=True,
                    ):
                        redemption_id = next_id(redemptions, "redemption_id", "RD")
                        new_redemption = pd.DataFrame([{
                            "redemption_id": redemption_id,
                            "user_id": user_id,
                            "reward_id": reward["reward_id"],
                            "points_used": req_points,
                            "redemption_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }])
                        redemptions = pd.concat([redemptions, new_redemption], ignore_index=True)
                        save_data(redemptions, REDEMPTIONS_FILE)

                        user_index = users[users["user_id"].astype(str) == user_id].index[0]
                        users.loc[user_index, "points"] = points - req_points
                        save_data(users, USERS_FILE)

                        st.success(f"You redeemed **{reward['reward_name']}**!")
                        st.rerun()

    my_redemptions = redemptions[redemptions["user_id"].astype(str) == user_id]
    if not my_redemptions.empty:
        st.subheader("Your Redemption History")
        merged = my_redemptions.merge(rewards[["reward_id", "reward_name"]], on="reward_id", how="left")
        st.dataframe(
            merged[["redemption_date", "reward_name", "points_used"]].rename(
                columns={"redemption_date": "Date", "reward_name": "Reward", "points_used": "Points Used"}
            ),
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# 8. CAMPAIGN UPDATES
# ============================================================

elif selected_menu == "📰 Campaign Updates":

    st.header("📰 Campaign Updates")

    post_tab, feed_tab = st.tabs(["📝 Post an Update", "📢 Latest Updates"])

    with post_tab:
        my_campaigns = created_campaigns[created_campaigns["creator_user_id"].astype(str) == user_id]

        if my_campaigns.empty:
            st.info("You need to create a campaign before you can post updates.")
        else:
            with st.form("update_form"):
                campaign_choice = st.selectbox(
                    "Choose your campaign",
                    my_campaigns["campaign_name"].astype(str).tolist(),
                )
                title = st.text_input("Update Title")
                update_text = st.text_area("Update Details")
                post_submitted = st.form_submit_button("Post Update", type="primary")

            if post_submitted:
                if not title.strip() or not update_text.strip():
                    st.error("Please fill in both the title and the update details.")
                else:
                    chosen_campaign = my_campaigns[my_campaigns["campaign_name"] == campaign_choice].iloc[0]
                    update_id = next_id(updates, "update_id", "UP")
                    new_update = pd.DataFrame([{
                        "update_id": update_id,
                        "campaign_id": chosen_campaign["campaign_id"],
                        "title": title.strip(),
                        "update_text": update_text.strip(),
                        "update_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }])
                    updates = pd.concat([updates, new_update], ignore_index=True)
                    save_data(updates, UPDATES_FILE)
                    st.success("Update posted!")
                    st.rerun()

    with feed_tab:
        if updates.empty:
            st.info("No updates have been posted yet.")
        else:
            merged = updates.merge(
                campaigns[["campaign_id", "campaign_name"]], on="campaign_id", how="left"
            ).sort_values("update_date", ascending=False)

            for _, u in merged.iterrows():
                with st.container(border=True):
                    st.write(f"**{u['title']}** — *{u['campaign_name']}*")
                    st.write(u["update_text"])
                    st.caption(u["update_date"])


# ============================================================
# 9. EKATRIT IMPACT
# ============================================================

elif selected_menu == "📊 Ekatrit Impact":

    st.header("📊 Ekatrit Impact")
    st.write("See the collective difference the Ekatrit community is making.")

    total_raised = campaigns["raised_amount"].apply(to_float).sum() if not campaigns.empty else 0
    total_donors = donations["user_id"].nunique() if not donations.empty else 0
    total_campaigns = len(campaigns)
    total_users = len(users)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Raised", f"₹{total_raised:,.0f}")
    col2.metric("Total Campaigns", total_campaigns)
    col3.metric("Unique Donors", total_donors)
    col4.metric("Community Members", total_users)

    if not donations.empty:
        st.subheader("🏆 Top Supporters")
        leaderboard = (
            users.assign(total_donation=users["total_donation"].apply(to_float))
            .sort_values("total_donation", ascending=False)
            .head(5)
        )
        st.dataframe(
            leaderboard[["name", "city", "total_donation", "points"]].rename(
                columns={
                    "name": "Name",
                    "city": "City",
                    "total_donation": "Total Donated (₹)",
                    "points": "Points",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    st.subheader("💬 Share Your Feedback")
    with st.form("feedback_form"):
        rating = st.slider("How would you rate your Ekatrit experience?", 1, 5, 5)
        feedback_text = st.text_area("Feedback")
        suggestion = st.text_area("Suggestions for improvement (optional)")
        feedback_submitted = st.form_submit_button("Submit Feedback", type="primary")

    if feedback_submitted:
        feedback_id = next_id(feedback, "feedback_id", "F")
        new_feedback = pd.DataFrame([{
            "feedback_id": feedback_id,
            "user_id": user_id,
            "rating": rating,
            "feedback": feedback_text.strip(),
            "suggestion": suggestion.strip(),
            "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }])
        feedback = pd.concat([feedback, new_feedback], ignore_index=True)
        save_data(feedback, FEEDBACK_FILE)
        st.success("Thank you for your feedback! 🙏")


# ============================================================
# 10. EXIT
# ============================================================

elif selected_menu == "🚪 Exit":

    st.header("🚪 Exit Ekatrit")
    st.write("Thank you for being part of the Ekatrit community. Together, we create an impact.")

    if st.button("Log Out Now", type="primary", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.rerun()

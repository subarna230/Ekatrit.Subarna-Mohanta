
# 🤝 EKATRIT

### Bringing People, Purpose & Impact Together

<p align="center">

**Ekatrit** is a digital fundraising and social-impact platform designed to connect people with meaningful causes, simplify donations, encourage community participation, and make social contribution more engaging.

</p>

---

## 🌟 Project Preview

Ekatrit is a **functional web-based prototype** developed using Python and Streamlit.

The platform allows users to:

- 👤 Create their own account
- 🔎 Discover fundraising campaigns
- 🔍 Search campaigns
- 💰 Donate any amount
- 📢 Create fundraising campaigns
- 📊 Track personal contributions
- 🏆 Earn impact points
- 🎁 Redeem rewards
- 📜 View donation history
- 📢 Receive campaign updates
- 🌍 View overall platform impact
- 💬 Submit feedback and suggestions

The project combines **technology, fundraising, gamification, data management, and social impact** into one simple platform.

---

# 🌍 About Ekatrit

The word **Ekatrit** represents the idea of bringing people together for a common purpose.

Many individuals want to contribute to social causes but may find it difficult to discover campaigns, track their contributions, or understand the impact of their participation.

Ekatrit attempts to address this by creating a centralized platform where users can:

> **Discover → Contribute → Participate → Earn → Track → Impact**

The platform is designed as an academic prototype demonstrating how a social-impact application can be developed using Python, Streamlit, and structured data storage.

---

# 🎯 Problem Statement

Fundraising and social-impact activities often involve several challenges:

- Difficulty discovering relevant campaigns
- Limited visibility into campaign progress
- Lack of personalized contribution tracking
- Limited engagement after making a donation
- Difficulty maintaining donation records
- Lack of simple reward mechanisms
- Limited feedback and interaction between users and the platform

Ekatrit attempts to provide a unified digital environment to address these challenges.

---

# 💡 Proposed Solution

Ekatrit provides a centralized platform where users can:

```text
        DISCOVER
           ↓
      FIND A CAUSE
           ↓
        CONTRIBUTE
           ↓
      EARN POINTS
           ↓
       TRACK IMPACT
           ↓
     REDEEM REWARDS
           ↓
      STAY ENGAGED

Users can participate according to their own interests and contribution capacity.


---

✨ Core Features

👤 1. User Registration

Users can create an account by providing:

Full Name

Email

Phone Number

Age

City

Password

Confirm Password


After registration, the system generates a unique user ID.

The user's initial profile is automatically created with:

Points              → 0
Total Donation      → ₹0
Campaigns Supported → 0


---

🔎 2. Explore Campaigns

Users can browse available campaigns and explore different social causes.

Each campaign can display:

Campaign name

Category

Description

Location

Fundraising goal

Amount raised

Number of donors

Campaign status

Start date

End date

Progress


Users can also filter campaigns by category.

Example categories include:

Education
Medical
Food
Environment
Animal Welfare
Community Development
Skill Development
Youth
Disaster Relief


---

🔍 3. Search Campaigns

Users can search for campaigns based on relevant information such as:

Campaign name

Category

Location

Description


This makes it easier to find campaigns matching the user's interests.


---

💰 4. Flexible Donation System

Ekatrit allows users to enter any donation amount.

There are no fixed donation denominations.

For example:

Donation Amount
₹4,286

The platform automatically calculates the user's impact points.

🎯 Points Rule

₹10 = 1 Impact Point

Therefore:

₹4,286 ÷ ₹10 = 428 Points

The system then updates:

User Points
      ↓
Total Donation
      ↓
Campaign Raised Amount
      ↓
Campaign Donor Count
      ↓
Donation History


---

📢 5. Create a Campaign

Registered users can create their own fundraising campaigns.

Users provide:

Campaign Name

Category

Description

Goal Amount

Location

Start Date

End Date


Newly created campaigns are stored with:

Status → Pending Verification

This represents a simplified campaign verification workflow.


---

👤 6. My Profile

Users can view their personal information and contribution statistics.

The profile includes:

User ID

Name

Email

Phone Number

Age

City

Total Donations

Impact Points

Campaigns Supported

Recognition Level



---

🏆 Recognition System

Ekatrit includes a simple recognition mechanism based on contribution.

Example levels:

Contribution	Recognition

₹0 – ₹999	New Supporter
₹1,000+	Bronze Supporter
₹5,000+	Silver Supporter
₹10,000+	Gold Supporter
₹25,000+	Community Champion


The recognition system is intended to encourage continued participation.


---

📜 7. Donation History

Every donation made through the application is recorded.

The history includes:

Donation ID

User ID

Campaign ID

Donation amount

Points earned

Donation date


This allows users to keep track of their contribution activity.


---

🎁 8. Redeem Points

Users can redeem accumulated impact points for available rewards.

Example reward system:

Reward	Required Points

🏅 Supporter Badge	100
📜 Ekatrit Certificate	200
🎓 Webinar Pass	300
🎁 Gift Voucher	500


When a reward is successfully redeemed:

Available Points
        ↓
Points Deducted
        ↓
Redemption Recorded


---

📢 9. Campaign Updates

Campaign updates allow users to stay informed about ongoing activities.

Updates can communicate information such as:

Campaign progress

Community activities

Milestones

Important announcements

Fundraising developments



---

🌍 10. Ekatrit Impact

The Impact section provides a broader overview of the platform.

It can display:

Total donations

Total campaigns

Total donors

Total impact points

Individual contribution

Platform-level statistics

Visual charts


The purpose is to show how individual contributions can contribute to a larger collective impact.


---

💬 11. Feedback System

Users can provide feedback about their experience.

The feedback system includes:

⭐ Rating
📝 Feedback
💡 Suggestions

All submitted feedback is stored for future analysis and improvement.


---

🧭 Main Application Menu

The platform provides the following main menu:

1. Explore Campaigns
2. Search Campaigns
3. Donate
4. Create Campaign
5. My Profile
6. Donation History
7. Redeem Points
8. Campaign Updates
9. Ekatrit Impact
10. Exit


---

🔄 Application Workflow

┌─────────────────┐
                     │     SIGN UP     │
                     └────────┬────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    MAIN MENU      │
                    └─────────┬─────────┘
                              │
       ┌──────────────┬───────┼───────┬──────────────┐
       │              │       │       │              │
       ▼              ▼       ▼       ▼              ▼
   Explore         Search   Donate   Create       Profile
  Campaigns       Campaigns         Campaign      & History
       │              │       │       │              │
       └──────────────┴───────┼───────┴──────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │    PROCESSING   │
                     │                 │
                     │ Validation      │
                     │ Calculations    │
                     │ Points          │
                     │ Updates         │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │  DATA STORAGE   │
                     │                 │
                     │ CSV Datasets    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │     OUTPUT      │
                     │                 │
                     │ Profiles        │
                     │ History         │
                     │ Statistics      │
                     │ Charts          │
                     └─────────────────┘


---

🏗️ System Architecture

Ekatrit follows a simple and understandable architecture:

┌───────────────────────────────────────┐
│              USER LAYER               │
│                                       │
│ Registration • Search • Donations     │
│ Campaign Creation • Feedback          │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│           APPLICATION LAYER            │
│                                       │
│ Streamlit Interface                  │
│ Input Validation                      │
│ Business Logic                        │
│ Points Calculation                    │
│ Campaign Processing                   │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│             DATA LAYER                 │
│                                       │
│ Pandas + CSV Files                    │
│                                       │
│ Users • Campaigns • Donations         │
│ Rewards • Redemptions • Feedback      │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│            OUTPUT LAYER                │
│                                       │
│ Profiles • History • Charts           │
│ Impact Statistics • Updates           │
└───────────────────────────────────────┘


---

🗂️ Project Structure

Ekatrit/
│
├── 📄 ekatrit.py
│
├── 📁 data/
│   ├── campaigns.csv
│   ├── users.csv
│   ├── donations.csv
│   ├── campaigns_created.csv
│   ├── rewards.csv
│   ├── redemptions.csv
│   ├── updates.csv
│   └── feedback.csv
│
└── 📄 README.md


---

📊 Dataset Description

The project uses CSV files as its local data-storage mechanism.

Dataset	Purpose

campaigns.csv	Stores available campaigns
users.csv	Stores registered user information
donations.csv	Stores donation transactions
campaigns_created.csv	Stores campaigns created by users
rewards.csv	Stores available rewards
redemptions.csv	Stores reward redemption records
updates.csv	Stores campaign updates
feedback.csv	Stores user feedback


This approach keeps the prototype simple and makes the underlying data easy to inspect and understand.


---

🛠️ Technology Stack

Programming Language

🐍 Python

Python is used for application logic, data processing, validation, calculations, and file management.


---

Web Framework

🌐 Streamlit

Streamlit is used to transform the Python application into an interactive web interface.


---

Data Processing

🐼 Pandas

Pandas is used for:

Reading CSV files

Updating datasets

Filtering campaigns

Processing donations

Managing user records

Generating statistics



---

Data Storage

📁 CSV

CSV files provide lightweight local storage suitable for this academic prototype.


---

Development Environment

💻 Visual Studio Code

The project was developed and tested using Visual Studio Code.


---

⚙️ Installation & Setup

Step 1 — Clone the Repository

git clone <YOUR-REPOSITORY-LINK>


---

Step 2 — Open the Project

cd Ekatrit


---

Step 3 — Create a Virtual Environment

macOS / Linux

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Windows

python -m venv .venv

Activate it:

.venv\Scripts\activate


---

Step 4 — Install Dependencies

pip install streamlit pandas


---

Step 5 — Run the Application

streamlit run ekatrit.py

The application will automatically open in a browser.


---

🔐 Security

The prototype implements basic password hashing before storing user credentials.

However, Ekatrit is currently an academic prototype, not a production financial application.

For a production deployment, additional security measures would be required, including:

Secure authentication

Multi-factor authentication

Encrypted databases

HTTPS

Secure session management

Role-based access control

Payment security

Server-side validation

Data privacy controls

Professional campaign verification



---

💳 Payment Disclaimer

Ekatrit currently does not process real financial transactions.

The donation feature is designed to demonstrate the application's workflow:

Donation Input
      ↓
Validation
      ↓
Donation Processing
      ↓
Points Calculation
      ↓
Campaign Update
      ↓
User Profile Update
      ↓
Donation History

Real payment integration can be added in future development.


---

🚀 Future Scope

Ekatrit can be expanded significantly beyond the current prototype.

💳 Real Payment Gateway

Integration with:

UPI

Credit/Debit Cards

Net Banking

Digital Wallets



---

🤖 AI-Powered Campaign Recommendations

An AI recommendation engine could suggest campaigns based on:

Previous donations

User interests

Location

Campaign category

Contribution patterns



---

🔐 Advanced Authentication

Future versions could include:

OTP verification

Email verification

Two-factor authentication

Social login

Password recovery



---

☁️ Cloud Database

The current CSV-based storage could be replaced with:

PostgreSQL

MySQL

MongoDB

Firebase


This would allow the platform to scale to a larger number of users.


---

📱 Mobile Application

Dedicated Android and iOS applications could make the platform more accessible.


---

📊 Advanced Analytics

An administrative dashboard could provide:

Donation trends

Campaign performance

User engagement

Category-wise funding

Geographic contribution analysis

Monthly and yearly statistics



---

🛡️ Campaign Verification

A dedicated verification system could be introduced to validate:

Campaign creators

Supporting documents

Fundraising objectives

Beneficiary information



---

🏆 Advanced Gamification

Future versions could introduce:

Achievement badges

Leaderboards

Donation streaks

Community challenges

Milestone rewards

Social recognition



---

🌐 Multilingual Support

The platform could support multiple Indian languages to improve accessibility and reach.


---

🎓 Academic Significance

Ekatrit demonstrates practical implementation of several software-development concepts.

Programming

Python

Functions

Conditional logic

Loops

Data structures

Exception handling


Data Management

CSV handling

Pandas DataFrames

Data filtering

Data updating

Record management


Application Development

Streamlit UI

Form handling

Session state

User navigation

Interactive components


Data Processing

Donation calculations

Points calculation

Campaign progress

User statistics

Impact analysis


Software Design

Input

Processing

Storage

Output



---

🧪 Testing

The prototype can be tested through different user scenarios.

User Registration

Input → User Details
Expected → New User Created

Donation

Input → Donation Amount
Expected → Donation + Points + Campaign Update

Campaign Creation

Input → Campaign Details
Expected → New Campaign Stored

Reward Redemption

Input → Reward Selection
Expected → Points Deducted + Redemption Stored

Feedback

Input → Rating + Feedback
Expected → Feedback Stored


---

📈 Example

Suppose a user makes a donation of:

₹4,286

The system calculates:

₹4,286 ÷ ₹10
      ↓
428 Impact Points

The user's profile then reflects:

Total Donation → ₹4,286
Points          → 428

The campaign's fundraising information is also updated.


---

🌱 Social Impact

Ekatrit is designed around a simple principle:

> Small contributions can collectively create meaningful change.



The platform encourages users to participate in social causes while providing transparency around their contribution history and engagement.

Instead of treating a donation as a one-time action, Ekatrit attempts to create a continuing participation cycle:

DISCOVER
   ↓
DONATE
   ↓
EARN
   ↓
TRACK
   ↓
REDEEM
   ↓
PARTICIPATE AGAIN


---

📌 Project Status

🟢 Functional Prototype

Current features:

✅ User Registration

✅ User Profiles

✅ Campaign Exploration

✅ Campaign Search

✅ Flexible Donations

✅ Campaign Creation

✅ Donation History

✅ Impact Points

✅ Recognition Levels

✅ Reward Redemption

✅ Campaign Updates

✅ Impact Dashboard

✅ Feedback System

✅ CSV Data Storage

✅ Streamlit Web Interface



---

🔗 Project Links

🌐 Live / Project Link

Ekatrit Project Link

> Replace <PASTE-YOUR-LINK-HERE> with your actual GitHub repository, Streamlit deployment, or project URL.



💻 Source Code

View Source Code


---

📁 Repository Information

Project Name  : Ekatrit
Project Type  : Social Impact Platform
Application   : Web Application
Framework     : Streamlit
Language      : Python
Database      : CSV
Development   : Visual Studio Code
Status        : Functional Prototype


---

⚠️ Disclaimer

Ekatrit is an academic and educational prototype developed to demonstrate the application of programming, data management, web development, and social-impact concepts.

It should not currently be used for real-money fundraising or production deployment.

Real-world deployment would require appropriate:

Financial regulations

Payment security

Campaign verification

Data protection

User authentication

Legal compliance

Infrastructure security



---

❤️ Made With Love by Subarna Mohanta♥️

This project was designed and developed with the idea of using technology to encourage meaningful participation and community impact.

Here is the link of the Ekatrit prototype app: https://ekatritsubarna-mohanta-v8fyewhkqhlfemhrazg6d5.streamlit.app/

Thank you for exploring Ekatrit! ❤️

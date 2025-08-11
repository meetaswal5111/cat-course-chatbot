import streamlit as st

st.set_page_config(page_title="CAT Course Chatbot", page_icon="🤖")

# --- Initialize State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "step" not in st.session_state:
    st.session_state.step = "menu"

# --- Helper to Add Messages ---
def add_bot_message(text):
    st.session_state.messages.append({"role": "bot", "text": text})

def add_user_message(text):
    st.session_state.messages.append({"role": "user", "text": text})

# --- Main Menu Function ---
def show_main_menu():
    add_bot_message(
        "Hi 👋! Which CAT course would you like to explore?\n\n"
        "1️⃣ CAT Full Course\n"
        "2️⃣ CAT Crash Course\n"
        "3️⃣ CAT Test Series"
    )
    st.session_state.step = "await_choice"

# --- Course Details ---
def show_course_details(choice):
    courses = {
        "1": ("📘 **CAT Full Course**", "₹15,000", "https://yourwebsite.com/cat-full-course", "https://yourwebsite.com/demo-full-course"),
        "2": ("⚡ **CAT Crash Course**", "₹8,000", "https://yourwebsite.com/cat-crash-course", "https://yourwebsite.com/demo-crash-course"),
        "3": ("📝 **CAT Test Series**", "₹3,000", "https://yourwebsite.com/cat-test-series", "https://yourwebsite.com/demo-test-series")
    }
    if choice in courses:
        title, price, buy_link, demo_link = courses[choice]
        add_bot_message(
            f"{title}\n💰 Total Fees: {price}\n"
            f"🔗 [Buy Now]({buy_link})\n"
            f"📧 Email: contact@yourwebsite.com\n"
            f"📞 Phone: +91-9876543210\n"
            f"🎥 [Upcoming Demo Session]({demo_link})"
        )
        add_bot_message("Type 1️⃣ to return to the main menu, or 2️⃣ to end the chat.")
        st.session_state.step = "menu_or_end"
    else:
        add_bot_message("❌ Invalid choice. Please type 1, 2, or 3.")

# --- If First Load, Show Menu ---
if len(st.session_state.messages) == 0:
    show_main_menu()

# --- Display All Messages in Order ---
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        st.markdown(f"<div style='background:#eef3ff;padding:10px;border-radius:10px;margin:5px 0;max-width:70%;'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background:#d1ffd6;padding:10px;border-radius:10px;margin:5px 0;max-width:70%;float:right;text-align:right;'>{msg['text']}</div><div style='clear:both;'></div>", unsafe_allow_html=True)

# --- User Input ---
user_input = st.text_input("Your response:", key=f"input_{len(st.session_state.messages)}")

if user_input:
    add_user_message(user_input.strip())

    if st.session_state.step == "await_choice":
        show_course_details(user_input.strip())

    elif st.session_state.step == "menu_or_end":
        if user_input.strip() == "1":
            show_main_menu()
        elif user_input.strip() == "2":
            add_bot_message("✅ Thank you for visiting! Have a great day! 🎯")
            st.session_state.step = "done"
        else:
            add_bot_message("❌ Please type 1 to go to menu or 2 to end chat.")

    st.rerun()

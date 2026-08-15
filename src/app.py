import streamlit as st
from Get_Review_Analysis import get_review_result




# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Review Analysis",
    page_icon="public/icon.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)




# ==========================================
# 2. ENTERPRISE CSS INJECTION (Glassmorphism)
# ==========================================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #F8FAFC;
    }

    /* Background Gradient */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1E1B4B 0%, #0F172A 50%, #020617 100%);
        background-attachment: fixed;
    }

    /* Main Container Card */
    .main-container {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 32px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }

    /* Typography */
    .app-title {
        font-size: 2.25rem;
        font-weight: 700;
        background: linear-gradient(135deg, #818CF8 0%, #C084FC 50%, #F472B6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 8px;
    }

    .app-subtitle {
        font-size: 1rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 32px;
    }

    /* Text Area Styling */
    .stTextArea textarea {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #F1F5F9 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 1rem !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #818CF8 !important;
        box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.2) !important;
    }

    /* Result Output Card */
    .result-card {
        background: rgba(15, 23, 42, 0.8);
        border-left: 4px solid #818CF8;
        border-radius: 12px;
        padding: 20px;
        margin-top: 24px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-left: 4px solid #818CF8;
    }

    .result-header {
        font-weight: 600;
        font-size: 1.1rem;
        color: #C7D2FE;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        color: gray;
        font-size: 14px;
    }

    /* Hide Streamlit Clutter */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)




# ==========================================
# 4. SESSION STATE MANAGEMENT
# ==========================================

if "active_tab" not in st.session_state:
    st.session_state.active_tab = None
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""




# ==========================================
# 5. UI LAYOUT & ROUTING
# ==========================================

st.markdown('<h1 class="app-title">Review Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="app-subtitle">Transform unstructured customer feedback into precision insights instantly.</p>', unsafe_allow_html=True)




# ==========================================
# 6. INPUT FIELD
# ==========================================

review_text = st.text_area(
    "Customer Review",
    placeholder="Paste or type customer review here...",
    height=150,
    label_visibility="collapsed"
)

st.markdown("<div style='margin-height: 20px;'></div>", unsafe_allow_html=True)




# ==========================================
# 7. BUTTONS
# ==========================================

btn1, btn2, btn3, btn4 = st.columns(4)

with btn1:
    if st.button("📝 Summary", use_container_width=True):
        if review_text.strip():
            with st.spinner("Analyzing..."):
                st.session_state.analysis_result = get_review_result("summary", review_text)
                st.session_state.active_tab = "Summary"
        else:
            st.warning("Please enter a review first.")

with btn2:
    if st.button("⚖️ Sentiment", use_container_width=True):
        if review_text.strip():
            with st.spinner("Analyzing..."):
                st.session_state.analysis_result = get_review_result("sentiment", review_text)
                st.session_state.active_tab = "Sentiment"
        else:
            st.warning("Please enter a review first.")

with btn3:
    if st.button("✨ Pros", use_container_width=True):
        if review_text.strip():
            with st.spinner("Analyzing..."):
                st.session_state.analysis_result = get_review_result("pros", review_text)
                st.session_state.active_tab = "Pros"
        else:
            st.warning("Please enter a review first.")

with btn4:
    if st.button("⚠️ Cons", use_container_width=True):
        if review_text.strip():
            with st.spinner("Analyzing..."):
                st.session_state.analysis_result = get_review_result("cons", review_text)
                st.session_state.active_tab = "Cons"
        else:
            st.warning("Please enter a review first.")




# ==========================================
# 8. RESULT CARDS
# ==========================================

if st.session_state.active_tab and review_text.strip():
    icon_map = {"Summary": "📝", "Sentiment": "⚖️", "Pros": "✨", "Cons": "⚠️"}
    icon = icon_map.get(st.session_state.active_tab, "📌")


    #---- Pros/Cons Result Card ----#
    if st.session_state.active_tab in ['Pros', 'Cons']:

        result = "".join(f"<li>{item}</li>" for item in st.session_state.analysis_result)

        result_format = f"""
        <div class="result-card">
            <div class="result-header">
                {icon} {st.session_state.active_tab} Analysis
            </div>
            <div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                <ul style="padding-left: 20px;">
                    {result}
                </ul>
            </div>
        </div>"""

        st.markdown(result_format, unsafe_allow_html=True)


    #---- Summary/Sentiment Result Card ----#
    else:
        result_format = f"""
        <div class="result-card">
            <div class="result-header">
                {icon} {st.session_state.active_tab} Analysis
            </div>
            <div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                {st.session_state.analysis_result}
            </div>
        </div>
        """
        st.markdown(result_format, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)




# ==========================================
# 9. FOOTER
# ==========================================

st.markdown('''<p class='footer'>© 2026 Jinit Limbachiya. All rights reserved.</p>''', unsafe_allow_html=True)
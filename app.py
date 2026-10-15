import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="LangMock - Tamil", page_icon="🎓", layout="centered")

# --- FULL DATABASE WITH SCRIPT & GIFS ---
tamil_vocab = [
    {"telugu": "Nenu (I)", "tamil": "Naan", "tamil_script": "நான்", "category": "Basics", "writing_gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXN6MzN6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6/placeholder/giphy.gif"},
    {"telugu": "Nuvvu (You)", "tamil": "Nee", "tamil_script": "நீ", "category": "Basics", "writing_gif": ""},
    {"telugu": "Neellu (Water)", "tamil": "Thanneer", "tamil_script": "தண்ணீர்", "category": "Food", "writing_gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXN6MzN6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6/placeholder/giphy.gif"},
    {"telugu": "Annam (Food)", "tamil": "Saapadu", "tamil_script": "சாப்பாடு", "category": "Food", "writing_gif": ""},
    {"telugu": "Ekkada (Where)", "tamil": "Enga", "tamil_script": "எங்கே", "category": "Questions", "writing_gif": ""}
]
df = pd.DataFrame(tamil_vocab)

# --- SESSION STATE INITIALIZATION ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'current_q' not in st.session_state: st.session_state.current_q = None
if 'answered' not in st.session_state: st.session_state.answered = False

def get_new_question():
    st.session_state.current_q = random.choice(tamil_vocab)
    st.session_state.answered = False

if st.session_state.current_q is None:
    get_new_question()

# --- HEADER ---
st.title("🎓 LangMock - Learn Tamil")
st.write(f"**⭐ Total XP: {st.session_state.xp}**")

# --- TABS CREATION ---
tab1, tab2, tab3 = st.tabs(["🎴 Learn & Write", "📝 Daily Mock", "📚 Vocabulary"])

# --- TAB 1: LEARN & WRITE ---
with tab1:
    st.header("Learn How to Write")
    st.markdown("Prathi word ki Telugu meaning mariyu adi ela rayalo ikkada nerchuko.")
    st.divider()
    
    selected_word = st.selectbox("Select a word to learn:", df['telugu'])
    word_data = df[df['telugu'] == selected_word].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Meaning & Pronunciation")
        st.write(f"**Telugu Meaning:** {word_data['telugu']}")
        st.write(f"**Pronunciation:** {word_data['tamil']}")
        st.markdown(f"<h1 style='text-align: center; color: #ff4b4b; font-size: 60px;'>{word_data['tamil_script']}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.info("How to Write (Stroke Order)")
        if word_data['writing_gif']:
            st.image(word_data['writing_gif'], caption=f"Writing: {word_data['tamil_script']}", use_container_width=True)
        else:
            st.write("Animation not available yet!")

# --- TAB 2: MOCK TEST ---
with tab2:
    st.header("Daily Tamil Mock")
    q = st.session_state.current_q

    st.markdown(f"### Translate this word: **{q['telugu']}**")
    st.caption(f"Category: {q['category']}")

    # Generate options
    all_tamil_words = df['tamil'].tolist()
    # Ensure we don't pick the same word twice and pick enough options
    options = random.sample([w for w in all_tamil_words if w != q['tamil']], min(2, len(all_tamil_words)-1))
    options.append(q['tamil'])
    random.shuffle(options)

    with st.form("quiz_form"):
        selected = st.radio("Choose the correct option:", options, index=None)
        submit = st.form_submit_button("Check Answer ✅")

        if submit and selected:
            st.session_state.answered = True
            if selected == q['tamil']:
                st.success(f"🎉 Super! '{q['telugu']}' in Tamil is '{q['tamil_script']}' ({q['tamil']}).")
                st.session_state.xp += 10
            else:
                st.error(f"❌ Tappu! The correct answer is '{q['tamil_script']}' ({q['tamil']}).")

    if st.session_state.answered:
        if st.button("Next Question ➡️"):
            get_new_question()
            st.rerun()

# --- TAB 3: VOCABULARY REVISION ---
with tab3:
    st.header("📚 Full Vocabulary List")
    st.markdown("Exam ki mundu quick reading kosam!")
    
    # Selecting only required columns to show in table cleanly
    display_df = df[['telugu', 'tamil', 'tamil_script', 'category']]
    display_df.columns = ["Telugu Word", "Pronunciation", "Tamil Script", "Category"]
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)

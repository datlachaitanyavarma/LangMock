import streamlit as st
import pandas as pd

st.set_page_config(page_title="LangMock - Tamil", page_icon="🎓", layout="centered")

# --- UPDATED DATABASE WITH SCRIPT & WRITING GIFS ---
tamil_vocab = [
    {
        "telugu_meaning": "Nenu (I)", 
        "tamil_pronunciation": "Naan", 
        "tamil_script": "நான்", 
        "category": "Basics",
        # Ikkada nuvvu real Tamil letter writing GIFs petkovachu. Present sample GIFs unnai.
        "writing_gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXN6MzN6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6/placeholder/giphy.gif" 
    },
    {
        "telugu_meaning": "Neellu (Water)", 
        "tamil_pronunciation": "Thanneer", 
        "tamil_script": "தண்ணீர்", 
        "category": "Food",
        "writing_gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXN6MzN6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6M3N6/placeholder/giphy.gif"
    }
]
df = pd.DataFrame(tamil_vocab)

st.title("🎓 LangMock - Learn Tamil")

# --- TABS CREATION ---
tab1, tab2, tab3 = st.tabs(["🎴 Learn & Write", "📝 Daily Mock", "📚 Vocabulary"])

# --- TAB 1: LEARN & WRITE (New Feature) ---
with tab1:
    st.header("Learn How to Write")
    st.markdown("Prathi word ki Telugu meaning mariyu adi ela rayalo ikkada nerchuko.")
    st.divider()
    
    # Word selector
    selected_word = st.selectbox("Select a word to learn:", df['telugu_meaning'])
    
    # Fetch details for the selected word
    word_data = df[df['telugu_meaning'] == selected_word].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Meaning & Pronunciation")
        st.write(f"**Telugu Meaning:** {word_data['telugu_meaning']}")
        st.write(f"**Pronunciation:** {word_data['tamil_pronunciation']}")
        # Big font for Tamil Script
        st.markdown(f"<h1 style='text-align: center; color: #ff4b4b; font-size: 60px;'>{word_data['tamil_script']}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.info("How to Write (Stroke Order)")
        # Show animated GIF of how to write the word/letter
        if word_data['writing_gif']:
            st.image(word_data['writing_gif'], caption=f"Writing: {word_data['tamil_script']}", use_container_width=True)
        else:
            st.write("Writing animation coming soon!")

# --- TAB 2 & 3: Mock Test & Vocab (Mundu rasina code ikkada continue avuthundi) ---
with tab2:
    st.write("Mock test logic ikkada add cheyyi...")

with tab3:
    st.write("Vocabulary table ikkada add cheyyi...")

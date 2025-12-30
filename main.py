import streamlit as st
from morse_covert import text_to_morse_sound, validate_morse_code, validate_text_input


def main():
    st.title("Welcome to the Morse Code Converter App!")
    tab1, tab2 = st.tabs(["Text to Morse Code", "Morse Code to Text"])
    with tab1:
        st.text_area("Enter text to convert to Morse code:", key="text_input", placeholder="Type your message here...")
        if st.button("Convert to Morse Code"):
            from morse_covert import encode
            if not validate_text_input(st.session_state.text_input):
                st.error("❌ Invalid input! Use only letters A-Z, numbers 0-9, and basic punctuation.")
            elif st.session_state.text_input.strip() == "":
                st.warning("⚠️ Please enter some text.")
            else:
                text = st.session_state.text_input
                morse_code = encode(text)
                st.code(f"Morse Code: {morse_code}")
                text_to_morse_sound(text)
                
    with tab2:
        morse_input=st.text_area("Enter Morse code to convert to text (e.g: ... --- ...):", key="morse_input", placeholder="Use . for dot, and - for dash for space between words.")
        if st.button("Convert to Text"):
            from morse_covert import decode
            # Validate morse code
            if not validate_morse_code(morse_input):
                st.error("❌ Invalid input! Use only dots (.), dashes (-), and spaces.")
            elif morse_input.strip() == "":
                st.warning("⚠️ Please enter morse code.")
            else:
                text = decode(morse_input)
                st.success(f"Decoded Text: {text}")  
    st.markdown("---")

if __name__ == "__main__":
    main()

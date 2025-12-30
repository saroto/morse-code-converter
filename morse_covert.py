import numpy as np
import streamlit as st
import time
textToMorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}
morseCodeToText = {v: k for k, v in textToMorseCode.items()}

def validate_morse_code(morse_input):
    """Validate that morse code contains only dots, dashes, and spaces."""
    allowed_chars = {'.', '-', ' ', '/'}
    return all(char in allowed_chars for char in morse_input)

def validate_text_input(text):
    """Validate that text input contains only valid characters."""
    allowed_chars = set(textToMorseCode.keys())
    return all(char.upper() in allowed_chars for char in text)

def encode(text)-> str:
    """Convert plain text to Morse code."""
    text = text.upper()
    morse_code = ' '.join(textToMorseCode.get(char, '') for char in text)
    return morse_code

def decode(morse_code: str) -> str:
    """Convert Morse code to plain text."""
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        characters = word.split()
        decoded_word = ''.join(morseCodeToText.get(char, '') for char in characters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words).lower()

def play_tone(duration, freq=600, sample_rate=44100):
    """Generates and plays a sine wave tone."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate a smooth sine wave
    tone = np.sin(freq * t * 2 * np.pi) * 0.3
    # Add fade-out to reduce clicking sound
    fade_out = np.linspace(1, 0, int(sample_rate * duration * 0.2))
    tone[-len(fade_out):] *= fade_out
    # Play the tone
    st.audio(tone, sample_rate=sample_rate)
    # st.wait()

def text_to_morse_sound(text, dot_duration=0.2, freq=600, sample_rate=44100):
    """Convert text to morse sound and play it."""
    dash_duration = dot_duration * 3
    pause_between_elements = dot_duration
    pause_between_letters = dot_duration * 3
    pause_between_words = dot_duration * 7
    
    audio_data = []
    
    for char in text.upper():
        if char == ' ':
            # Add silence for word pause
            silence = np.zeros(int(sample_rate * pause_between_words))
            audio_data.append(silence)
            continue
        
        code = textToMorseCode.get(char, '')
        
        for symbol in code:
            if symbol == '.':
                tone = generate_tone(dot_duration, freq, sample_rate)
            elif symbol == '-':
                tone = generate_tone(dash_duration, freq, sample_rate)
            else:
                continue
            
            audio_data.append(tone)
            
            # Add silence between elements
            silence = np.zeros(int(sample_rate * pause_between_elements))
            audio_data.append(silence)
        
        # Add silence between letters
        silence = np.zeros(int(sample_rate * pause_between_letters))
        audio_data.append(silence)
    
    # Combine all audio
    complete_audio = np.concatenate(audio_data)
    st.audio(complete_audio, sample_rate=sample_rate)

def generate_tone(duration, freq, sample_rate):
    """Generate a single tone."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi) * 0.3
    
    # Fade out
    fade_out = np.linspace(1, 0, int(sample_rate * duration * 0.1))
    tone[-len(fade_out):] *= fade_out
    
    return tone
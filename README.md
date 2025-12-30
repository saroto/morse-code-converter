# 🔤 Morse Code Converter

A modern web application for converting between text and Morse code with audio playback functionality. Built with Streamlit and NumPy.

## ✨ Features

- **Text to Morse Code**: Convert any text (letters A-Z, numbers 0-9) to Morse code
- **Morse Code to Text**: Decode Morse code back to readable text
- **Audio Playback**: Play Morse code as audio with customizable frequency and duration
- **Input Validation**: Validates both text and Morse code inputs
- **User-Friendly Interface**: Interactive tabs for easy navigation

## 📋 Requirements

- Python 3.8+
- NumPy
- Streamlit

## 🚀 Installation

1. Clone the repository:

```bash
git clone git@github.com:saroto/morse-code-converter.git
cd morse-code-converter
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit numpy sounddevice
```

## 💻 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### Text to Morse Code

1. Enter text in the text area
2. Click "Convert to Morse Code"
3. View the Morse code output
4. Click the play button to hear the audio

### Morse Code to Text

1. Enter Morse code (use `.` for dots, `-` for dashes, and spaces between characters)
2. Click "Convert to Text"
3. View the decoded text

## 📁 Project Structure

```
morse-code-converter/
├── main.py                 # Streamlit app entry point
├── morse_covert.py         # Core morse code functions
├── README.md              # This file
└── pyproject.toml         # Project configuration
```

## 🔧 Core Functions

### `encode(text: str) -> str`

Converts plain text to Morse code.

```python
encode("HELLO")  # Returns: ".... . .-.. .-.. ---"
```

### `decode(morse_code: str) -> str`

Converts Morse code to plain text.

```python
decode(".... . .-.. .-.. ---")  # Returns: "HELLO"
```

### `text_to_morse_sound(text: str, dot_duration: float = 0.2, freq: int = 600)`

Plays Morse code as audio.

```python
text_to_morse_sound("HELLO")  # Plays audio representation
```

### `visualize(morse_code: str) -> str`

Displays Morse code with corresponding letters.

```python
visualize(".... . .-.. .-.. ---")
# Output: .... (H) . (E) .-.. (L) .-.. (L) --- (O)
```

## 🎵 Audio Customization

Adjust audio parameters in `text_to_morse_sound()`:

- `dot_duration`: Duration of a dot in seconds (default: 0.2)
- `freq`: Frequency in Hz (default: 600 Hz) - higher = higher pitch
- `sample_rate`: Audio quality (default: 44100 Hz)

## 📊 Morse Code Reference

| Character | Code  | Character | Code  |
| --------- | ----- | --------- | ----- |
| A         | .-    | N         | -.    |
| B         | -...  | O         | ---   |
| C         | -.-.  | P         | .--.  |
| ...       | ...   | ...       | ...   |
| 0         | ----- | 9         | ----. |

## ✅ Input Validation

- **Text Input**: Accepts letters A-Z, numbers 0-9, and spaces
- **Morse Input**: Accepts only dots (.), dashes (-), and spaces

## 🛠️ Development

To run the app in development mode:

```bash
streamlit run main.py --logger.level=debug
```

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created by saroto

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

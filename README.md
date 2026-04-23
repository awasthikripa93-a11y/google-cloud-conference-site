# Google Cloud Summit 2026

A modern, responsive, 1-day technical conference informational site built with Flask (Python) and Vanilla HTML/CSS/JavaScript. It features a premium "glassmorphism" design with dark mode, vibrant neon colors, and real-time frontend search filtering.

## Features
- **Modern UI**: High-end visual aesthetic utilizing CSS grid/flexbox, blur effects, gradients, and micro-animations.
- **Dynamic Schedule**: Displays 8 conference talks and a 60-minute lunch break, fully populated with dummy data about Google Cloud Technologies.
- **Real-time Search**: Instantly filter talks by title, speaker, or category using vanilla JavaScript.
- **Responsive**: Adapts gracefully to mobile and desktop screen sizes.

## Tech Stack
- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## Setup & Installation

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd neon-snake-beats
   ```

2. **Install Requirements**
   Ensure you have Python installed. It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The only major dependency is Flask).*

3. **Run the Application**
   Start the Flask development server:
   ```bash
   python app.py
   ```

4. **Access the Site**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Customization
- **Schedule Data**: Modify the `schedule` list inside `app.py` to change the talks, speakers, descriptions, and times.
- **Theme Colors**: The Google Cloud colors are defined as CSS variables at the top of `static/css/style.css`. You can tweak these to change the overall color scheme.

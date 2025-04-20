
# 🖼️ Neural Style Transfer Web Application

This is a Flask-based web application for performing **neural style transfer**, where a content image is combined with a style image to generate a stylized output. Users can upload their own images, choose how many intermediate images they want (for visualizing progress), and view both intermediate and final results.

---

## 🚀 Features

- Upload a **content** and **style** image
- Specify the number of **intermediate outputs** (1 to 10)
- See real-time progress via **loading bar**
- View and download **stylized result**
- Frontend with **HTML, CSS (Bootstrap), and JavaScript**
- Backend with **Python Flask**
- Uses a modified version of `inetwork_tf.py` for style transfer

---

## 📁 Project Structure

```
project/
│
├── data/                 # Stores uploaded images and outputs
├── static/               # Static files like CSS, JS, intermediate outputs
├── templates/            # HTML templates (Jinja2)
│
├── app.py                # Main Flask app
├── color_transfer.py     # Color adjustment module (optional)
├── INetwork.py           # Legacy style transfer network (unused here)
├── inetwork_tf.py        # TensorFlow-based style transfer script
├── tf_bfgs.py            # Optimization utilities
├── utils.py              # Helper utilities
│
├── requirements.txt      # Requirements for app (Flask, etc.)
├── requirements_tf.txt   # Requirements for TensorFlow script
└── README.md             # Project overview
```

---

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/neural-style-webapp.git
   cd neural-style-webapp
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install TensorFlow requirements (optional if not already installed):**
   ```bash
   pip install -r requirements_tf.txt
   ```

---

## 🧠 Run the Web App

Make sure all necessary dependencies are installed, then run:

```bash
python app.py
```

- Open browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Upload content and style images.
- Select number of intermediate images (1 to 10).
- View progress and final output on the result page.

---

## 🧩 Based On

This project reuses and modifies the following:

- `inetwork_tf.py` – adapted from an earlier neural style transfer repository
- `INetwork.py` – reference only, not used in current app
- `color_transfer.py` – structure inspired by external project

---

## 📷 Sample Usage

1. Upload images:
   - `Content Image`: Photo you want to stylize
   - `Style Image`: Artwork style to apply
2. Set how many intermediate results to show (e.g., 5 = 25 min of training)
3. Watch progress and download results.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Python Flask
- **ML Engine:** TensorFlow
- **Deployment-ready:** Local development mode

---

## 📝 License

This project is for educational and experimental purposes.

---

## 👨‍💻 Author

Made by [Your Name] – 2025  
Inspired by [external repo link if needed]

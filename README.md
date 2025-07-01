# PRODIGY_GA_05: AI Neural Style Transfer Web App

This web app allows you to apply the artistic style of any image to your own photos using neural style transfer. This project was done as part of my internship at Prodigy Infotech.

---

## Features

- **AI-powered neural style transfer** using TensorFlow and TensorFlow Hub
- **Modern, responsive web UI** (Flask + HTML/CSS/JS)
- **Drag & drop image upload** with live previews
- **Displays both input and generated images**
- **Easy to run locally or deploy to the cloud**

---

## Project Structure

```
PRODIGY_GA_05/
│
├── backend/
│   ├── app.py                # Flask app
│   ├── static/               # CSS & JS
│   ├── templates/            # HTML templates
│   ├── uploads/              # Uploaded & generated images
│   └── style_transfer/
│       └── model.py          # Style transfer logic
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/PRODIGY_GA_05.git
   cd PRODIGY_GA_05
   ```
2. **(Optional) Create a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```sh
   python backend/app.py
   ```
5. **Open your browser:**
   Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Deployment

### **Local Network**

- To let others on your network try the app, run:
  ```python
  # In backend/app.py
  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000, debug=False)
  ```
- Share your local IP (e.g., http://192.168.1.10:5000/)

### **Cloud (Render.com Example)**

1. Push your code to GitHub.
2. Create a new web service on [Render.com](https://render.com/).
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python backend/app.py`
5. (Optional) Add a disk for persistent uploads.
6. Access your app via the public Render URL.

---

## How It Works

- **Upload a content image and a style image.**
- The app uses a pre-trained neural network to blend the style of one image with the content of another.
- The result is displayed alongside your input images.

---

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.
- For best performance, use a machine with a GPU and compatible TensorFlow version.

---

## Credits

- Built as part of the Prodigy Infotech Internship.
- Uses [TensorFlow Hub](https://tfhub.dev/) for neural style transfer.
- UI inspired by modern AI image generation platforms.

---

## 📄 License

This project is for educational and demonstration purposes.

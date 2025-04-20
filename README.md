
#  Neural Style Transfer Web Application

This is a Flask-based web application for performing **neural style transfer**, where a content image is combined with a style image to generate a stylized output. Users can upload their own images, choose how many intermediate images they want (for visualizing progress), and view both intermediate and final results.

---

##  Features

- Upload a **content** and **style** image
- Specify the number of **intermediate outputs** (1 to 10)
- See real-time progress via **loading bar**
- View and download **stylized result**

---

##  Project Structure

```
project/
│
├── data/                 # Stores sample data
├── static/               # Static files like CSS, JS, intermediate outputs, uploaded images
├── templates/            # HTML templates (Jinja2)
│
├── app.py                # Main Flask app
├── color_transfer.py     # Color adjustment module (optional)
├── INetwork.py           # Legacy style transfer network 
├── inetwork_tf.py        # TensorFlow-based style transfer script
├── tf_bfgs.py            # Optimization utilities
├── utils.py              # Helper utilities
│
├── requirements.txt      # Requirements for model
├── requirements_tf.txt   # Requirements for TensorFlow script
└── README.md             # Project overview
```

---

##  Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/onkarhshinde/Custom-Artistic-Neural-Style-Transfer.git
   cd neural-style-webapp
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
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

##  Run the Web App

Make sure all necessary dependencies are installed, then run:

```bash
python app.py
```

- Open browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Upload content and style images.
- Select number of intermediate images (1 to 10).
- View progress and final output on the result page.




###  Sample Usage for webpage

1. Upload images:
   - `Content Image`: Photo you want to stylize
   - `Style Image`: Artwork style to apply
2. Set how many intermediate results to show (e.g., 5 = 25 min of training)
3. Watch progress and download results.
   
###  Web Dashboard Preview

Here are some screenshots of the interface and results:

|  Upload Section |  Stylized Results + Download Option |
|-------------------|----------------------------------------|
| ![Upload](https://github.com/user-attachments/assets/799d8206-f10c-486e-ad1a-37951d21a55c) | ![Results](https://github.com/user-attachments/assets/0953be98-dbe2-4c98-b664-494f22571d21) |

---


## Usage: Neural Style Transfer (Terminal Commands)

INetwork.py
```
python inetwork_tf.py "/path/to/content image" "path/to/style image" "/path/to/result prefix"
```

To pass multiple style images, after passing the content image path, seperate each style path with a space
```
python inetwork_tf.py "/path/to/content image" "path/to/style image 1" "path/to/style image 2" ... "/path/to/result prefix" --style_weight 1.0 1.0 ... 
```

There are various parameters discussed below which can be modified to alter the output image. Note that many parameters require the command to be enclosed in double quotes ( " " ).

Example:
```
python inetwork_tf.py "/path/to/content image" "path/to/style image" "result prefix or /path/to/result prefix" --preserve_color "True" --pool_type "ave" --rescale_method "bicubic" --content_layer "conv4_2"
```


(For post processing of image )

To perform color preservation on an already generated image, use the `color_transform.py` as below. It will save the image in the same folder as the generated image with "_original_color" suffix.
```
python color_transfer.py "path/to/content/image" "path/to/generated/image"
```


---
# Examples
## Single Style Transfer
<img src="https://github.com/user-attachments/assets/bf227190-4a79-447b-bf50-5261427c9d21" width=49% height=300 alt="Golden_gate"> <img src="https://github.com/user-attachments/assets/b80887e2-45ce-4e8a-be9e-a4f34057aa0a" width=49% height=300 alt="blue_swirls">
<br><br> Results after 5 iterations using the inetwork_tf <br>
<img src="https://github.com/user-attachments/assets/f7027658-bbc6-43f1-aaec-5f2ff54b8218" width=98% height=450 alt="blue_swirls style transfer">
<br><br> Style Transfer with Color Preservation
<img src="https://github.com/user-attachments/assets/e1f65183-f80f-4c3f-98c7-6a100179283e" width=98% height=450 alt="blue_swirls style transfer">

## Neural Style Transfer Parameters

- **`--style_masks`**: Multiple style masks for specific regions. Number of style masks must match `style_weight` count.
- **`--color_mask`**: Defines region to preserve color.
- **`--image_size`**: Sets Gram Matrix size (default 400x400).
- **`--num_iter`**: Number of iterations (default 10).
- **`--init_image`**: Initial image type (`"content"`, `"noise"`, or `"gray"`).
- **`--pool_type`**: Pooling method (`max` or `ave`).
- **`--model`**: Model architecture (`vgg16` or `vgg19`).
- **`--content_loss_type`**: Loss scaling type (`0`, `1`, or `2`).
- **`--preserve_color`**: Preserves content image color.
- **`--min_improvement`**: Minimum required improvement to continue (default 0.0).
- **`--content_weight`**: Content weight (default 0.025).
- **`--style_weight`**: Style weight (default 1, space-separated for multiple styles).
- **`--style_scale`**: Scales style weight (default 1).
- **`--total_variation_weight`**: Regularization factor (default 8.5E-5).
- **`--rescale_image`**: Rescales to original size after each iteration.
- **`--rescale_method`**: Rescaling algorithm (`nearest`, `bilinear`, `bicubic`, or `cubic`).
- **`--maintain_aspect_ratio`**: Maintains aspect ratio during rescaling (default True).
- **`--content_layer`**: Content layer (`conv4_2` or `conv5_2`).


##  Tech Stack

- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Python Flask
- **ML Engine:** TensorFlow
- **Deployment-ready:** Local development mode



##  Author

Made by Onkar Shinde  


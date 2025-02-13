
🎨 Pictoon - Artistic Image Filter App

Bring life to your images with **Pictoon**, a creative web application that transforms photos with unique, artistic filters! Choose from a range of styles, including *Cartoon*, *Pencil Sketch*, *Watercolor*, *Pop Art*, and more. Whether you upload your own images or select from our built-in datasets, Pictoon helps you create eye-catching visuals with just a few clicks.


## ✨ Features

- **20+ Artistic Filters**: Convert your images to *Cartoon*, *Pencil Sketch*, *Manga*, *Cel Shading*, and more.
- **Upload or Choose**: Use your own image or select from our ready-to-use datasets.
- **Adjust Intensity & Resize**: Control the look with adjustable filter intensity and resizing options.
- **Instant Download**: Download your edited images directly from the app.

## 🚀 Getting Started

### 1. Installation

To run Pictoon locally, clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/pictoon.git
cd pictoon
pip install -r requirements.txt
```

*Requirements: Python 3.x, Streamlit, OpenCV, NumPy, and Pillow.*

### 2. Run the Application

Launch the app using Streamlit:
```bash
streamlit run main.py
```

Open your browser to the displayed URL to start using Pictoon!

## 🖼️ Using Pictoon

### Select an Image

1. **Upload an Image**: Go to the sidebar and choose "Upload Image" to import an image from your device.
2. **Select from Datasets**: Choose "Select from Datasets" and pick from categories like *Pets*, *Flowers*, *Actors*, *Cartoons*, *Cars*, and *Buildings*.

### Apply Filters

1. **Resize**: Enter the width and height values in the sidebar if you'd like to resize the image.
2. **Choose a Filter**: Select from over 20 artistic filters using the dropdown.
3. **Adjust Intensity**: Use the slider to customize the filter’s strength.
4. **Apply and Compare**: Click "Apply Filter" to see the transformed image side-by-side with the original.

![Filter Application Preview](images/filter_application_preview.png)

### Save Your Work

After applying a filter, download your final image with the **"Download Filtered Image"** button. You can also view and download previews of all filters in the **"All Filters"** section.

## 📂 Dataset Setup

To enable the dataset image selection feature, update the paths in `main.py` to your local directory structure:

python
DATASETS = {
    "Pets": "path/to/PETS",
    "Flowers": "path/to/FLOWERS_AND_NATURE",
    "Actors": "path/to/ACTORS",
    "Cartoons": "path/to/CARTOONS_AND_ANIME",
    "Cars": "path/to/CARS",
    "Buildings": "path/to/BUILDINGS"
}
```

 🎨 Filter Gallery

| Filter         | Description                           | Sample Output                        |
|----------------|---------------------------------------|--------------------------------------|
| **Cartoon**    | Adds cartoonish outlines and colors   | ![Cartoon](images/cartoon_example.png) |
| **Pencil Sketch** | Converts to black-and-white sketch | ![Pencil Sketch](images/sketch_example.png) |
| **Watercolor** | Smooth and painted look               | ![Watercolor](images/watercolor_example.png) |
| **Manga**      | Comic-style look with sharp edges     | ![Manga](images/manga_example.png) |






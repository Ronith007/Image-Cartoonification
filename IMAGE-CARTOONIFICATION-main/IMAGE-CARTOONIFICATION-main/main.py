import streamlit as st
import cv2
import numpy as np
from filters import FILTER_MAP  # Ensure this module exists
from PIL import Image
import os
import io

# Define datasets with representative icons
DATASETS = {
    "Pets": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/PETS",
    "Flowers": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/FLOWERS AND NATURE",
    "Actors": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/ACTORS",
    "Cartoons": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/CARTOONS AND ANIME",
    "Cars": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/CARS",
    "Buildings": "C:/Users/Lawrence/OneDrive/Documents/MP/code/DATASETS/BUILDINGS"
}

# Load all dataset images
DATASET_IMAGES = {}
for dataset_name, folder_path in DATASETS.items():
    images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg'))]
    DATASET_IMAGES[dataset_name] = images

st.title("PICTOON")

def apply_filter(image, filter_name, intensity):
    if filter_name in FILTER_MAP:
        filter_func = FILTER_MAP[filter_name]
        return filter_func(image, intensity)
    return image

def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# User selection: Upload image or select from datasets
st.sidebar.title("Image Source")
source_option = st.sidebar.radio("Choose an option", ("Upload Image", "Select from Datasets"))

image = None

if source_option == "Upload Image":
    uploaded_file = st.sidebar.file_uploader("Upload your own image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Selected Image", use_column_width=True)
        image = np.array(image.convert("RGB"))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

elif source_option == "Select from Datasets":
    st.sidebar.title("Select Dataset Category")
    dataset_category = st.sidebar.selectbox("Choose a category", list(DATASETS.keys()))

    if dataset_category:
        st.header(f"{dataset_category} Dataset")
        dataset_images = DATASET_IMAGES[dataset_category]

        selected_image_path = None
        num_cols = 3
        cols = st.columns(num_cols)

        for i, img_path in enumerate(dataset_images):
            col = cols[i % num_cols]
            with col:
                if st.button(f"Select {os.path.basename(img_path)}", key=img_path):
                    selected_image_path = img_path
                st.image(img_path, use_column_width=True)

        if selected_image_path:
            image = Image.open(selected_image_path)
            st.image(image, caption="Selected Image", use_column_width=True)
            image = np.array(image.convert("RGB"))
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

if image is not None:
    # Resize Options
    st.sidebar.title("Resize Image")
    width = st.sidebar.number_input("Width", min_value=1, value=image.shape[1])
    height = st.sidebar.number_input("Height", min_value=1, value=image.shape[0])

    if st.sidebar.button("Resize Image"):
        image = resize_image(image, width, height)
        st.image(image, caption="Resized Image", use_column_width=True)

    # Filter Selection
    st.sidebar.title("Filters")
    filter_name = st.sidebar.selectbox("Choose a filter", list(FILTER_MAP.keys()))
    intensity = st.sidebar.slider("Intensity", 1, 10, 5)

    if st.sidebar.button("Apply Filter"):
        filtered_image = apply_filter(image, filter_name, intensity)
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

        # Display Before and After images
        col1, col2 = st.columns(2)
        col1.header("Before")
        col1.image(image, use_column_width=True)
        col2.header("After")
        col2.image(filtered_image, use_column_width=True)

        # Download filtered image
        im_pil = Image.fromarray(filtered_image)
        img_buffer = io.BytesIO()
        im_pil.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        st.download_button(label="Download Filtered Image",
                           data=img_buffer,
                           file_name="filtered_image.png",
                           mime="image/png")

    # Display all filters with download buttons
    st.header("All Filters")
    all_filtered_images = {}
    filter_names = list(FILTER_MAP.keys())
    num_filters = len(filter_names)

    for i in range(0, num_filters, 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < num_filters:
                fname = filter_names[i + j]
                filtered_img = apply_filter(image.copy(), fname, intensity)
                filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
                all_filtered_images[fname] = filtered_img

                cols[j].subheader(fname)
                cols[j].image(filtered_img, caption=fname, use_column_width=True)

                im_pil = Image.fromarray(filtered_img)
                img_buffer = io.BytesIO()
                im_pil.save(img_buffer, format='PNG')
                img_buffer.seek(0)

                with cols[j]:
                    st.download_button(label=f"Download {fname} Image",
                                       data=img_buffer,
                                       file_name=f"{fname}.png",
                                       mime="image/png")

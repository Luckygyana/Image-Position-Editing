# Image-Position-Editing

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Common Arguments](#common-arguments)
  - [Tasks](#tasks)
    - [Task 1: Generate Red Mask on the Object](#task-1-generate-red-mask-on-the-object)
    - [Task 2: Change Position of the Segmented Object](#task-2-change-position-of-the-segmented-object)
    - [Task 3: Remove the Object](#task-3-remove-the-object)
- [Examples](#examples)
- [Directory Structure](#directory-structure)
- [Configuration Files](#configuration-files)
- [Contributing](#contributing)
- [License](#license)

## Introduction

`ImageEditor` is a versatile image processing tool that allows users to perform various tasks on images, such as generating red masks, changing the position of segmented objects, and removing objects. This tool leverages advanced segmentation models to achieve these tasks efficiently.

## Requirements

- Python 3.6+
- `src` package including `ImageEditor`
- Additional dependencies as specified in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ImageEditor.git
    cd ImageEditor
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

The `ImageEditor` script can be used from the command line to perform various image processing tasks. Below are the common arguments and task-specific arguments.

### Common Arguments

- `--image`: Path to the input image (required).
- `--class`: Class of the object to be segmented (required).
- `--output`: Path to the output image (required).

### Tasks

#### Task 1: Generate Red Mask on the Object

Generates a red mask over the specified object in the image.

```sh
python script.py --image path/to/image.jpg --class "object_class" --output path/to/output.jpg task1
```

#### Task 2: Change Position of the Segmented Object

Changes the position of the segmented object by the specified number of pixels in the x and y directions.

```sh
python script.py --image path/to/image.jpg --class "object_class" --output path/to/output.jpg task2 --x shift_x --y shift_y
```

- `--x`: Number of pixels to shift in the x direction (required).
- `--y`: Number of pixels to shift in the y direction (required).

#### Task 3: Remove the Object

Removes the specified object from the image.

```sh
python script.py --image path/to/image.jpg --class "object_class" --output path/to/output.jpg task3
```

## Examples

### Example 1: Generate Red Mask

```sh
python script.py --image sample.jpg --class "cat" --output masked_cat.jpg task1
```

### Example 2: Change Object Position

```sh
python script.py --image sample.jpg --class "cat" --output moved_cat.jpg task2 --x 50 --y 30
```

### Example 3: Remove Object

```sh
python script.py --image sample.jpg --class "cat" --output no_cat.jpg task3
```

## Directory Structure

```
ImageEditor/
├── lama/
│   ├── configs/
│   │   └── prediction/
│   │       └── default.yaml
│   └── pretrained-models/
│       └── big-lama
├── src/
│   └── ImageEditor.py
├── script.py
├── requirements.txt
└── README.md
```

## Configuration Files

The `lama` directory contains the necessary configuration files and pre-trained models for performing the image editing tasks. The default configuration file for predictions is located at `lama/configs/prediction/default.yaml`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and include relevant tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

For any further questions or support, please open an issue on the [GitHub repository](https://github.com/yourusername/ImageEditor).
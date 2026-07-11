# BMW Car Sales Price Analysis & Machine Learning Prediction System

## Project Information

**Project Title:** Web-Based Data Analysis and Prediction System

**Project Name:** BMW Car Sales Price Analysis & Machine Learning Prediction

**Developed By:** Attique ur Rehman
**Department:** Computer Science
**University:** The Islamia University of Bahawalpur (IUB)
**Session:** 2022–2026

---

## Project Description

This project is a web-based application developed using Django and Machine Learning techniques. It provides BMW car sales data analysis through various visualizations and insights, along with a car price prediction system.

The application includes:

* User authentication using Django's built-in authentication system.
* BMW car sales data analysis with graphs and visual insights.
* Car price prediction using the Random Forest Machine Learning algorithm.
* Integrated project report and documentation.

---

## Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Machine Learning (Random Forest)

---

## Project Structure

* `manage.py`
* `prediction/`
* `core/`
* `templates/`
* `db.sqlite3`
* `Last Prediction Model.ipynb`
* `requirements.txt`

---

## Model Generation

This repository does not include the trained model (`.pkl`) file because of its large size.

To generate the trained model:

1. Open the Jupyter Notebook file:

   `orgmodel.ipynb`

2. Run all notebook cells from start to finish.

3. After successful execution, the notebook will automatically generate the trained model file (`.pkl`).

4. Create a folder named:

   `model`

5. Place the generated `.pkl` file inside the `model` folder.

6. Ensure the model file path matches the path configured in the Django project.

---

## Installation

### 1. Install Python

Install Python 3.x on your system.

### 2. Clone or Download the Project

Download the project and extract it, or clone the repository.

### 3. Open Command Prompt

Open Command Prompt in the project root directory.

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Django Server

```bash
python manage.py runserver
```

### 6. Open in Browser

```text
http://127.0.0.1:8000/
```

---

## Important Notes

* This project was developed as a Final Year Project (FYP).
* The trained machine learning model (`.pkl`) file is intentionally excluded from the repository due to its large size.
* To use the prediction feature, generate the model file by running the provided Jupyter Notebook and place it inside the `model` folder.
* Make sure all required libraries are installed before running the application.

---

## Author

**Attique ur Rehman**
Department of Computer Science
The Islamia University of Bahawalpur (IUB)

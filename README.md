# Wine Quality Prediction Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a machine learning-based web application that predicts whether the wine is of good or bad quality based on 11 physicochemical features (without including 'quality'). The model is trained using a `RandomForestClassifier` and deployed using `Streamlit`.

## Features

- Predicts the quality of red wine as either **good** or **bad**.
- Takes 11 input features and provides a prediction.
- The machine learning model is built using the `RandomForestClassifier` from `scikit-learn`.
- The web interface is created using `Streamlit`.

## Dataset

The dataset used for this project is the **Wine Quality Dataset**, which contains the following features:

1. Fixed Acidity
2. Volatile Acidity
3. Citric Acid
4. Residual Sugar
5. Chlorides
6. Free Sulfur Dioxide
7. Total Sulfur Dioxide
8. Density
9. pH
10. Sulphates
11. Alcohol
12. Quality (Target variable)

The target variable (`quality`) is categorized into:

- **Good Quality**: Wine with a quality score of 7 or above.
- **Bad Quality**: Wine with a quality score of less than 7.

The model will use the other 11 features (excluding 'quality') to predict if the wine is good or bad.

## How to Use

### Prerequisites

Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

### Step 1: Clone the Repository

```bash
git clone https://github.com/FahithKRM/ML_Wine-Quality-Prediction.git
```
```bash
cd wine-quality-prediction
```

### Step 2: Create a Virtual Environment

#### On Windows : 
```bash
python -m venv env
```
```bash
.\env\Scripts\activate
```

#### On macOS/Linux : 
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
![WhatsApp Image 2024-10-10 at 22 29 16_f676e94b](https://github.com/user-attachments/assets/41090706-8d5d-402e-a4f3-48337b38eb3b)

### Step 4: Run the Web Application
```bash
streamlit run app.py
```

### Step 5: Input Features
On the web interface, you'll need to input the 11 physicochemical features (excluding 'quality') as a comma-separated string. For example:
```bash
7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4
```
### These values correspond to the following features:
1. Fixed Acidity
2. Volatile Acidity
3. Citric Acid
4. Residual Sugar
5. Chlorides
6. Free Sulfur Dioxide
7. Total Sulfur Dioxide
8. Density
9. pH
10. Sulphates
11. Alcohol
#### Once you input the features, the model will predict if the wine is of Good Quality or Bad Quality.

### Step 6: View Prediction
#### The model will output either:
  - Good Quality Wine if the wine's predicted quality is 7 or more.
  - Bad Quality Wine otherwise.

### Examples : 
##### Input : 
```bash
11.2,0.28,0.56,1.9,0.075,17.0,60.0,0.998,3.16,0.58,9.8
```
##### Output :
![image](https://github.com/user-attachments/assets/8581df71-8ada-4b9f-a90c-15511e896fcd)

##### Input : 
```bash
7.5,0.52,0.16,1.9,0.085,12.0,35.0,0.9968,3.38,0.62,9.5
```
##### Output :
![image](https://github.com/user-attachments/assets/634d8071-cc27-43d5-9e4f-f788cb9afbe0)


### Project Structure : 
![WhatsApp Image 2024-10-10 at 22 28 56_e18de4ad](https://github.com/user-attachments/assets/4d4fe191-84a4-448c-b142-9e85ac889f13)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

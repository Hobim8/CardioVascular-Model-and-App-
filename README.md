# CardioVascular Risk Prediction 

**CardioGuard** - An intelligent web application for predicting cardiovascular disease risk in patients.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cardiovascularapp.streamlit.app/)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Overview

CardioGuard is a machine learning-powered web application designed to assist healthcare professionals in assessing cardiovascular disease (CVD) risk in patients. Built with Python and Streamlit, it provides quick, accurate risk predictions through an intuitive and secure interface.

The application leverages Support Vector Machine (SVM) algorithm, selected after rigorous comparison with multiple machine learning models, to deliver reliable cardiovascular risk assessments based on the well-established Framingham Heart Study dataset.

## ✨ Key Features

- 🎯 **Accurate Risk Prediction** - SVM-based model trained on the Framingham dataset
- 📊 **Comprehensive Output** - Risk probability, risk level classification, and personalized recommendations
- 🔒 **Secure Authentication** - User authentication system to protect sensitive health data
- 💻 **User-Friendly Interface** - Intuitive Streamlit web app designed for healthcare professionals
- ⚡ **Real-Time Results** - Instant risk assessment with actionable insights
- 🌐 **Cloud Deployed** - Accessible anywhere via web browser

## 🚀 Demo

Try out CardioGuard: [Live Demo](YOUR_STREAMLIT_APP_URL)

### 🔑 Demo Credentials

For testing purposes, use the following credentials:

```
Username: demo_user
Password: demo123
```

*Note: These are demo accounts for testing only. Do not enter real patient data.*

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Framework**: Streamlit
- **Machine Learning**: Scikit-learn (SVM)
- **Data Source**: Framingham Heart Study Dataset (Kaggle)

## 📋 Input Features

The model analyzes multiple patient health indicators including:

- Age
- Blood Pressure (Systolic & Diastolic)
- Cholesterol Levels
- Smoking Status
- BMI (Body Mass Index)
- Diabetes Status
- And other relevant cardiovascular risk factors

## 📈 Model Performance

After comparing multiple machine learning algorithms, **Support Vector Machine (SVM)** was selected for its superior performance in predicting cardiovascular disease risk on the Framingham dataset.

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/CardioVascular-Risk-Prediction.git
cd CardioVascular-Risk-Prediction
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 💡 Usage

1. **Login/Register** - Authenticate to access the application
2. **Enter Patient Data** - Input relevant health metrics
3. **Get Prediction** - Receive instant risk assessment including:
   - Risk Probability (%)
   - Risk Level Classification (Low/Moderate/High)
   - Personalized Recommendations

## 📊 Output Interpretation

| Risk Level | Probability Range | Recommendation |
|------------|-------------------|----------------|
| 🟢 Low | 0-30% | Maintain healthy lifestyle |
| 🟡 Moderate | 31-60% | Monitor and lifestyle changes |
| 🔴 High | 61-100% | Immediate medical consultation |

## 🔒 Security & Privacy

CardioGuard implements authentication mechanisms to ensure patient data privacy and secure access, making it suitable for clinical healthcare environments.

## 🎯 Target Audience

This application is designed specifically for **healthcare professionals** including:
- Physicians
- Nurses
- Clinical Researchers
- Medical Practitioners

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/CardioVascular-Risk-Prediction/issues).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍⚕️ Disclaimer

⚠️ **Medical Disclaimer**: CardioGuard is a support tool for healthcare professionals and should not be used as a sole diagnostic tool. Always consult with qualified healthcare providers for medical decisions.

## 📧 Contact

For questions or feedback, please open an issue or reach out to the maintainers.

---

⭐ **Star this repo** if you find it helpful!

Built with ❤️ for better cardiovascular health outcomes

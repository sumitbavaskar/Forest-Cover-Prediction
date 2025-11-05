# Forest Cover Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://forest-cover-prediction-mgcedndthcpvedkb35mkr5.streamlit.app/)

## 🚀 Live Demo

**Try the live app here:** [Forest Cover Prediction App](https://forest-cover-prediction-mgcedndthcpvedkb35mkr5.streamlit.app/)


Forest Cover Prediction is a machine learning project aimed at predicting forest cover types using environmental data. This project uses Python and Jupyter Notebook for exploratory data analysis, feature engineering, model training, and deployment via a web application.

## Table of Contents

- Introduction
- Features
- Project Structure
- Installation
- Usage
- Dataset
- Model
- - Web Application
- Deployment
- Web Application
- Contributing
- License

## Introduction

This repository contains code and resources for a forest cover type prediction project. The objective is to classify areas of land into different forest cover types based on environmental and geographical data. The project demonstrates the full pipeline from data exploration to model deployment.

## Features

- Exploratory Data Analysis (EDA)
- Feature selection & engineering
- Machine learning model training & evaluation
- Streamlit-based web app for demo and predictions

## Project Structure



## 🚀 Deployment

This project is deployed on **Streamlit Cloud** and accessible via the link below:

**Live App:** [https://forest-cover-prediction-mgcedndthcpvedkb35mkr5.streamlit.app/](https://forest-cover-prediction-mgcedndthcpvedkb35mkr5.streamlit.app/)

### Deployment Process

1. **Push code to GitHub repository**
   ```bash
   git add .
   git commit -m "Update deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Navigate to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `sumitbavaskar/Forest-Cover-Prediction`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Automatic Redeployment**
   - Any push to the `main` branch automatically triggers a redeployment
   - The app typically redeploys within 1-2 minutes

### Requirements for Deployment

- `app.py` - Main Streamlit application file
- `requirements.txt` - Python dependencies
- `.python-version` (optional) - Specify Python version
- `packages.txt` (optional) - System-level dependencies

### Deployment Features

✅ **Automatic CI/CD** - GitHub integration enables continuous deployment  
✅ **Free Hosting** - Streamlit Community Cloud provides free hosting  
✅ **HTTPS Support** - Secure connection out of the box  
✅ **Custom Domain** - Can configure custom domain (Pro plan)  
✅ **Resource Management** - Automatic sleep after inactivity (wakes on visit)

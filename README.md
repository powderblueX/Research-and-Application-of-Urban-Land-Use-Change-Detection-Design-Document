# SEME: Urban Land Use Change Detection System

[English](README.md) | [中文](README_CN.md)

## Project Overview
SEME (Spatial and Environmental Monitoring Engine) is a comprehensive system for urban land use change detection and analysis. The project integrates multiple services including API gateway, authentication, data processing, model prediction, and result comparison to provide a complete solution for urban planning and environmental monitoring.

## Architecture
The system uses a microservice architecture with the following components:
- **Frontend**: Vue 3 + TypeScript + Element Plus
- **Backend**: FastAPI microservices
- **Database**: SQLite
- **Machine Learning**: MLP and Random Forest models
- **APIs**: RESTful API design

## Project Structure
```
SEME-main/
├── KAN-BackEnd/           # Backend microservices
│   ├── api_gateway/       # API gateway service
│   ├── auth_service/      # Authentication service
│   ├── compare_service/   # Model comparison service
│   ├── data_service/      # Data processing service
│   ├── predict_service/   # Prediction service
│   └── analyze_service/   # Data analysis service
├── KAN-FrontEnd/          # Frontend application
├── baselineModels/        # Machine learning models
├── KAN-Test/              # Test suite
└── documents/             # Project documentation
```

## Installation
### Prerequisites
- Conda
- Node.js (v14+)
- Python 3.9+

### Backend Setup
```bash
# Navigate to backend directory
cd KAN-BackEnd

# Create and activate conda environment
conda env create -f environment.yml
conda activate kan-backend

# Start all services
start_all_services.bat
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd KAN-FrontEnd

# Install dependencies
npm install

# Start development server
npm run dev
```

## Services
The backend services run on the following ports:
- API Gateway: 8000
- Authentication Service: 8001
- Comparison Service: 8002
- Data Service: 8003
- Prediction Service: 8004
- Analysis Service: 8005

## Testing
### Run Component Tests
```bash
cd KAN-Test/component_level
pytest .
```

### Run Integration Tests
```bash
cd KAN-Test/integration_level
# Run Postman collection or pytest
```

## Machine Learning Models
The system includes baseline models for prediction:
- MLP (Multi-Layer Perceptron)
- Random Forest

Model training scripts can be found in the `baselineModels` directory.

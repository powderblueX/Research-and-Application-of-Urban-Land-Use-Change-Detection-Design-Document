# SEME: 城市土地利用变化检测系统

[English](README.md) | [中文](README_CN.md)

## 项目概述
SEME（空间与环境监测引擎）是一个用于城市土地利用变化检测与分析的综合系统。该项目集成了API网关、认证、数据处理、模型预测和结果比较等多个服务，为城市规划和环境监测提供完整解决方案。

## 架构设计
该系统采用微服务架构，包含以下组件：
- **前端**：Vue 3 + TypeScript + Element Plus
- **后端**：FastAPI微服务
- **数据库**：SQLite
- **机器学习**：MLP（多层感知器）和随机森林模型
- **API**：RESTful API设计

## 项目结构
```
SEME-main/
├── KAN-BackEnd/           # 后端微服务
│   ├── api_gateway/       # API网关服务
│   ├── auth_service/      # 认证服务
│   ├── compare_service/   # 模型比较服务
│   ├── data_service/      # 数据处理服务
│   ├── predict_service/   # 预测服务
│   └── analyze_service/   # 数据分析服务
├── KAN-FrontEnd/          # 前端应用
├── baselineModels/        # 机器学习模型
├── KAN-Test/              # 测试套件
└── documents/             # 项目文档
```

## 安装指南
### 前置要求
- Conda
- Node.js (v14+)
- Python 3.9+

### 后端设置
```bash
# 进入后端目录
cd KAN-BackEnd

# 创建并激活conda环境
conda env create -f environment.yml
conda activate kan-backend

# 启动所有服务
start_all_services.bat
```

### 前端设置
```bash
# 进入前端目录
cd KAN-FrontEnd

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

## 服务端口
后端服务运行在以下端口：
- API网关：8000
- 认证服务：8001
- 比较服务：8002
- 数据服务：8003
- 预测服务：8004
- 分析服务：8005

## 测试说明
### 运行组件测试
```bash
cd KAN-Test/component_level
pytest .
```

### 运行集成测试
```bash
cd KAN-Test/integration_level
# 运行Postman集合或pytest
```

## 机器学习模型
系统包含以下预测基线模型：
- MLP（多层感知器）
- 随机森林

模型训练脚本位于`baselineModels`目录中。

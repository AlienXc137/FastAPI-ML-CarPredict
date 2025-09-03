# FastAPI ML Car Prediction API
This project is a Machine Learning-powered API built using FastAPI to predict the selling price of a used car based on its characteristics.

## Project Features
* Authentication: JWT-based token auth and API key validation
* ML Model Prediction: Trained model predicts used car prices
* Redis Caching: inputs cached in redis for 30 minutes
* Monitoring Ready: Prometheus metrics + Grafana dashboards
* Dockerized Setup: Simplified deployment with Docker Compose
* Cloud Deployment: Deployed on render : https://fastapi-ml-carpredict.onrender.com/

## Model Input Variables

The prediction model expects the following input features:

| Feature           | Description                          | Example         |
|------------------|--------------------------------------|-----------------|
| `company`         | Brand of the car                     | `"Maruti"`      |
| `year`            | Year of manufacturing                | `2015`          |
| `owner`           | Number of previous owners            | `"Second"`      |
| `fuel`            | Fuel type                            | `"Petrol"`      |
| `seller_type`     | Individual or Dealer                 | `"Individual"`  |
| `transmission`    | Transmission type                    | `"Automatic"`   |
| `km_driven`       | Kilometers driven                    | `200000`        |
| `mileage_mpg`     | Mileage in miles per gallon          | `55`            |
| `engine_cc`       | Engine capacity in cc                | `1250`          |
| `max_power_bhp`   | Maximum power in BHP                 | `80`            |
| `torque_nm`       | Torque in Newton meters              | `200`           |
| `seats`           | Number of seats                      | `5`             |

---

## Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AlienXc137/FastAPI-ML-CarPredict.git
cd fastapi-project
```

### 2. Set Environment Variables

```bash
API_KEY=demo-key
JWT_SECRET_KEY=your-secret
REDIS_URL=redis://localhost:6379
```

### 3. Build and Run via Docker

```bash
docker-compose up --build
```

### 4. Access Interfaces

- FastAPI Docs: http://localhost:8000/docs
- FastAPI Metrics: http://localhost:8000/metrics
- Prometheus UI: http://localhost:9090
- Grafana UI: http://localhost:3000

---

## Deployment on Render (API only)

1. Push code to GitHub
2. Add render.yaml to the project root
3. Create a new Web Service on Render
4. Include environment variables

---

## GI-Service

**A Backend-for-Frontend (BFF)** API that serves optimized data to the OpenGINXplore frontend.

This service acts as a Backend-for-Frontend (BFF) for the OpenGINXplore web application.
It fetches data from the OpenGIN backend, aggregates and transforms it, and exposes
frontend-friendly REST APIs to improve performance and reduce complexity on the client side.

### High Level Overview
```mermaid
     flowchart LR
         N1["Frontend (OpenGINXplore)"]
         N2["Backend (OpenGIN)"]
         N3["BFF"]
         N4["Databases"]
     
         N1 <-. API calls .-> N3
         N3 <-. API calls .-> N2
         N2 <-. DB Interaction .-> N4
```
### What the BFF calls
The BFF communicates with the OpenGIN backend services REST APIs.
It fetches raw domain data such as:
- Entities (e.g. `Ministry`, `Departments`, `Persons`, `Documents`, `Dataset`
- Time-Based Relationships between entities (e.g., `AS_PRIME_MINISTER`, `AS_MINISTER` )
- Datasets with metadata

The BFF does not store data; it acts purely as a consumer of OpenGIN APIs.

### What it returns
The BFF returns frontend-optimized JSON responses to the OpenGINXplore application.

Instead of exposing raw OpenGIN structures, it provides:
- Aggregated data from multiple OpenGIN endpoints
- Flattened and simplified JSON structures
- Only the fields required by the UI
- Data formatted to match frontend components (cards, grids, timelines, etc.)

This allows the frontend to consume ready-to-use data without additional processing.

### Why this layer exists

This BFF layer exists to:

- Improve performance by reducing multiple frontend calls into a single optimized API call
- Prevent over-fetching and under-fetching of data
- Hide OpenGIN’s internal data model from the frontend
- Centralize aggregation and transformation logic
- Allow frontend changes without impacting the OpenGIN backend

In short, it ensures the frontend gets exactly the data it needs, in the right format, with minimal latency.

### Tech Stack

- Language: Python
- Framework: FastAPI
- Communication: REST
- Auth: None
- Database: None (BFF layer only)
- Containerization: Docker

## API Documentation
Find the API contracts:

- **Organisation**: [contract](https://github.com/LDFLK/GI-SERVICE/blob/858cd41582ab9da9ad38afb5920e6e4b60a9a88a/gi_service/contract/rest/organisation_api_contract.yaml)
- **Data**: [contract](https://github.com/LDFLK/GI-SERVICE/blob/858cd41582ab9da9ad38afb5920e6e4b60a9a88a/gi_service/contract/rest/data_api_contract.yaml)

## API Endpoints

### Organisation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/v1/organisation/active-portfolio-list` | Get portfolio list |
| `POST` | `/v1/organisation/departments-by-portfolio/{portfolio_id}` | Get departments under a given portfolio |
| `POST` | `/v1/organisation/prime-minister` | Get prime minister for a given date

## Installation & Setup

### Prerequisite

- Python 3.8 to 3.13
- pip (Python package installer)
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd GI-SERVICE
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL_QUERY` | OpenGIN service URL | `http://0.0.0.0:8081` |

### 5. Run the Application

#### Using Terminal

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Using Docker
```bash
docker-compose up
```

The API will be available at: `http://localhost:8000`

## Testing the APIs

### Test Basic Connectivity

```bash
http://localhost:8000/docs
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in the uvicorn command
2. **Environment variables not loaded**: Ensure `.env` file is in the root directory
3. **Import errors**: Make sure virtual environment is activated
4. **API not responding**: Check if the OpenGIN services are running

### Debug Mode

```bash
# Run with debug logging
uvicorn main:app --reload --log-level debug
```

## How to contribute?

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team

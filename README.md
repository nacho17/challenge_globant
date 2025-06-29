# Data Engineer Challenge - Globant Interview

## Features

- Load historical data from CSV into SQL database
- Insert batch data (1-1000 rows) via API
- Designed with FastAPI + SQLAlchemy

## Endpoints

- `POST /upload/{table_name}`: Load CSV from `data/` folder
- `POST /batch/{table_name}`: Insert JSON batch data

## Setup

```bash
pip install -r requirements.txt
chmod +x run.sh
./run.sh

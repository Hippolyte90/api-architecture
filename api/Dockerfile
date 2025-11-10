# -- Using a Python 3.12 image as basic slim (legère) --
FROM python:3.12-slim

# -- Define the work repository into the container --
WORKDIR /app

# --   Copy the requirements file in the container --
COPY requirements.txt .

# -- Install the Python dependencies without cache --
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# -- Copy all .py files and .db file into the container --
COPY . .

# -- Launch the server Uvicorn to execute FastAPI API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
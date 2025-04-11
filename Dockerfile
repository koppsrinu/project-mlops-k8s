# STEP 1: Base image
FROM python:3.9-slim

# STEP 2: Set working directory
WORKDIR /app

# STEP 3: Copy files into the container
COPY train.py ./
#COPY train.csv ./
COPY requirements.txt ./

# STEP 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Run the training script
CMD ["python", "train.py"]


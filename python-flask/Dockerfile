# 基础镜像
FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    build-essential \
    libicu-dev \
    gcc \
    g++ \
    python3-numpy \
    python3-scipy \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install flask gunicorn polyglot six numpy pyicu pycld2 morfessor

COPY ./app.py /app/

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
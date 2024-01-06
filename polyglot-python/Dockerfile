# 使用官方 Python 基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 安装 Polyglot 依赖项
RUN apt-get update && apt-get install -y \
    python3-tk \
    build-essential \
    libicu-dev \
    gcc \
    g++ \
    python3-numpy \
    python3-scipy \
    && rm -rf /var/lib/apt/lists/*

# 安装 Polyglot
RUN pip install polyglot six numpy

RUN pip install pyicu pycld2 morfessor

# （可选）安装其他您可能需要的 Python 包
# RUN pip install numpy pandas ...

# 将您的应用程序代码复制到容器中
COPY . /app

# 指定命令运行您的应用
CMD ["python", "./sentenceRegment.py"]                                                                                                                                       
# 使用官方 Python 映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製應用程式文件到容器中
COPY . /app

# 安裝依賴
RUN pip install -r requirements.txt

# 開放端口
EXPOSE 5000

CMD ["sh", "-c", "cd myproject && python manage.py runserver 0.0.0.0:5000"]
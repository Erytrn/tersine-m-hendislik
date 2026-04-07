FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 git curl
WORKDIR /app
COPY . .
CMD ["python3", "src/bypass_simulasyonu.py"]

# ใช้ Python เวอร์ชัน 3.12-slim เป็นฐานของ image
FROM python:3.12-slim

# ตั้งค่า working directory ใน container
WORKDIR /usr/src/app

# คัดลอกไฟล์ requirements.txt เข้าไปใน container
COPY requirements.txt .

# ติดตั้ง dependencies จาก requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์ทั้งหมดในโปรเจ็คเข้าไปใน container
COPY . .

# เปิด port ที่ service จะใช้ (เช่น 5000)
EXPOSE 5000

# คำสั่งที่ใช้รัน service (เปลี่ยนตามโปรเจ็คของคุณ)
CMD ["python", "app.py"]


FROM python:3.10

WORKDIR /app

COPY . .

# Install dependencies including local franpos_sdk package
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    ./franpos_sdk_full_package
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# 🛠️ Telecom Data ETL Pipeline with Airflow & Docker

Pipeline ini merupakan contoh implementasi **ETL (Extract, Transform, Load)** menggunakan **Apache Airflow** yang dijalankan dalam container **Docker**. Data yang digunakan berasal dari file CSV berisi informasi pengguna layanan telekomunikasi, kemudian diolah dan dimasukkan ke database PostgreSQL.

## 🚀 Fitur

- Menggunakan Airflow sebagai orchestrator data pipeline
- Load data dari file CSV ke database PostgreSQL
- Cek koneksi database dengan BashOperator
- Eksekusi SQL query untuk transformasi data
- Struktur modular dengan PythonOperator dan SQLExecuteQueryOperator
- Dapat dijalankan lokal dengan Docker


## ⚙️ Tools & Teknologi

- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- Pandas
- SQLAlchemy
- BashOperator
- Python 3

## 📌 Cara Menjalankan (Local)

1. **Clone repo ini**:
   ```bash
   git clone https://github.com/username/airflow-docker-etl-telecom-data.git
   cd airflow-docker-etl-telecom



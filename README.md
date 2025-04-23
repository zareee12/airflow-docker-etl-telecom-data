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

2. **Atur variabel di .env (contoh: URI database):**
   ```bash
   DB_URI=postgresql+psycopg2://username:password@hostname:port/dbname
3. **Jalankan docker compose**
   ```bash
   docker-compose up -d
4. **Akses Airflow Web UI:**
   ```bash
   http://localhost:8080
   ```
   Jalankan DAG
   
## 📈 Alur DAG
start_task – Dummy task sebagai awalan >>
check_database_connection – Mengecek koneksi ke database target >>
load_csv – Membaca dan memasukkan data dari CSV ke Postgres >>
create_another_table – Membuat tabel baru jika belum ada >>
insert_filtered_data – Menjalankan query transformasi dan insert data >>
end_task – Dummy task sebagai penutup

## ✍️ Penulis
Reza Septian
An enthusiast in Data Engineering


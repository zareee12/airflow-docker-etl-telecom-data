transform_query = """
    TRUNCATE TABLE another_table;
    
    INSERT INTO another_table (id, customer_name, data_usage_gb)
    SELECT id, customer_name, data_usage_gb
    FROM telecom_users
    WHERE data_usage_gb > 10
    ON CONFLICT (id) DO NOTHING;
"""

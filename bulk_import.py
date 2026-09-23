# import pandas as pd
# from sqlalchemy import create_engine

# # 1. Baca data dari Excel/CSV
# df = pd.read_csv('data_historis_mohair.csv')

# # 2. Hubungkan ke database SQLite proyek
# engine = create_engine('sqlite:///instance/mohair.db')

# # 3. Masukkan seluruh baris data ke tabel 'leads' atau 'orders'
# df.to_sql('orders', con=engine, if_exists='append', index=False)

# print("Data historis berhasil didigitasi ke SQLite!")
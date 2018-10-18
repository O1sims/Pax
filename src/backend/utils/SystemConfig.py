import os


DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "8210"))
DB_NAME = os.environ.get("DB_NAME", "PaxDB")

import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

# Configuração do JWT
SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")
ALGORITHM = "HS256"

# Configuração do banco de dados
USER = quote_plus(os.environ.get('DATABASE_USERNAME', 'root'))
PASS = quote_plus(os.environ.get('DATABASE_PASSWORD', ''))
HOST = os.environ.get('DATABASE_HOSTNAME', 'localhost')
PORT = os.environ.get('PORT', '3306')
BASE = os.environ.get('DATABASE_BASENAME', 'builders')

# Conexão com o banco existente
DATABASE_URL = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{BASE}"

# Token de acesso a api OMDB
TOKEN_OMDB = os.environ.get('TOKEN_OMDB', None)

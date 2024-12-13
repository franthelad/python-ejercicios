import pandas as pd
from pathlib import Path

file_path = Path('data') / 'BASES DE DATOS.xlsx'
sh_name = 'FACTURACIÓN TELEFONÍA'

data = pd.read_excel(file_path, sheet_name= sh_name)

data_facturacion = pd.DataFrame(data)

print(data_facturacion.info())
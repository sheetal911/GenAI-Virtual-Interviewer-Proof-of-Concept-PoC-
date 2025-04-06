import camelot

def extract_tables_from_pdf(path):
    tables = camelot.read_pdf(path, pages='all')
    for i, table in enumerate(tables):
        table.to_csv(f'table_{i}.csv')
    return tables

import os

import pandas as pd
from mvp_scrapping.app.adapters.storage_adapter import StorageAdapter


def test_save_to_csv(tmpdir):
    storage = StorageAdapter()
    test_data = [{'Title': 'Test Post', 'Author': 'Anônimo'}]
    
    # Diretório temporário para o teste
    file_path = os.path.join(tmpdir, 'test_data.csv')
    
    storage.save_to_csv(test_data, file_path)
    
    # Verifica se o arquivo CSV foi criado e se os dados estão corretos
    df = pd.read_csv(file_path)
    assert df.iloc[0]['Title'] == 'Test Post'
    assert df.iloc[0]['Author'] == 'Anônimo'

def test_save_to_json(tmpdir):
    storage = StorageAdapter()
    test_data = [{'Title': 'Test Post', 'Author': 'Anônimo'}]
    
    file_path = os.path.join(tmpdir, 'test_data.json')
    
    storage.save_to_json(test_data, file_path)
    
    # Verifica se o arquivo JSON foi criado e se os dados estão corretos
    df = pd.read_json(file_path, lines=True)
    assert df.iloc[0]['Title'] == 'Test Post'
    assert df.iloc[0]['Author'] == 'Anônimo'

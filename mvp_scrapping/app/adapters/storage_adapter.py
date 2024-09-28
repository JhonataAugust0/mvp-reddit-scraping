import pandas as pd
from mvp_scrapping.app.domain.ports.storage_port import StoragePort


class StorageAdapter(StoragePort):
    @staticmethod
    def save_to_csv(data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    @staticmethod
    def save_to_json(data, filename):
        df = pd.DataFrame(data)
        df.to_json(filename, orient='records', lines=True)

from interfaces import InterfacePipeline
from etl import ExtractData, TransformData, LoadData, ConvertFile
import pandas as pd


# Implementação do pipeline
class Pipeline(InterfacePipeline):

    def __init__(self) -> None:
        super().__init__()

    def Extract(self, df) -> pd.DataFrame:
        data = ExtractData()
        data.Start(df)
        return data


    def Transform(self, df) -> pd.DataFrame:
        transform = TransformData()
        transform.ToString(df)
        return transform

    def Load():
        load = ConvertFile()
        return load

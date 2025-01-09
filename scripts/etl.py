import pandas as pd


# Recebe os dados e transforma em um Pandas DataFrame
class ExtractData():

    def __init__(self) -> None:
        pass

    def Start(self, df) -> pd.DataFrame:
        data = pd.DataFrame(df)
        return data


# Responsável por realizar as transformações 
class TransformData():

    def __init__(self):
        pass

    def ToString(self, df):
        dfToString = pd.DataFrame(df)
        dfToString.astype(str)
        return dfToString
    
    def RemovePointsCPF():
        return

    def JustCellNumber():
        return

    def JustNumberCoursePeriod():
        return

    def SplitAddress():
        return


# Carrega os dados
class LoadData():

    def __init__(self):
        pass

# Suporte a conversão para diferenter formatos de arquivos
class ConvertFile():

    def __init__(self):
        pass

    def ToJson(self, df):
        df = pd.DataFrame(df)
        df.to_json()
        return df

    def ToSql():
        return
    
    def ToXlsx():
        return

    def ToTxt():
        return
    
    def ToCsv():
        return
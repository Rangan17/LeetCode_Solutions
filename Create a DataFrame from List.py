import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    List = ['student_id','age']
    df = pd.DataFrame(student_data, columns = List)
    return df

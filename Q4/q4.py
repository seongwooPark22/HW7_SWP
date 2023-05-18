import pandas as pd

def main() : 
    data = pd.read_csv("gender2.csv",encoding="cp949", index_col="행정구역")
    processed_data = data.loc[:,["2022년_계_총인구수","2022년_남_총인구수", "2022년_여_총인구수"]]
    processed_data.rename(columns={"2022년_계_총인구수":'Total',"2022년_남_총인구수":"Male", "2022년_여_총인구수":"Female"}, inplace=True)
    print(processed_data)
if __name__ == "__main__" :
    main()


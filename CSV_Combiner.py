import pandas as pd
import sys
import csv


def load_csv(files):
    i = 0
    try:
        with open('combined.csv', 'a', newline = '\n') as f:
            for file in files:
                try:
                    df = pd.read_csv("./fixtures/"+f'{file}')
                    df.loc[df.index[::-1],'file_name'] = file
                    if i==0:
                        df.to_csv(f, header=True,index=False)
                        i +=1
                    else:
                        df.to_csv(f, header=False,index=False)
                except FileNotFoundError:
                    raise FileNotFoundError(f" {file}")
            f.close()
    except Exception as e:
        print("error in opening file",e)        

    print("CSV files are combined successfully")

# def load_csv(files):
#     df = pd.DataFrame()
#     for file in files:
#         try:
#             file_df = pd.read_csv("./fixtures/"+f'{file}')
#             file_df.loc[file_df.index[::-1],'file_name'] = file
#             df = df.append(file_df)
            
#         except FileNotFoundError:
#             raise FileNotFoundError(f" {file}")
#     df.to_csv("combined.csv",index=False)
#     print("CSV files are combined successfully")

if __name__ == "__main__":
    files = []
    num = len(sys.argv)
    for i in range(1,num):
        files.append(sys.argv[i])
    if len(files)<2:
        print("Please include Minimum Two Files")
    else:
        load_csv(files)



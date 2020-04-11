import pandas as pd

class NBA_Analysis:
    
    def __init__(self,path):
        self.path = path
        
    def Split(self):
        file = open(self.path,"r")
        data_all = []
        i = 0 
        for line in file:
            if(i == 0):
                line = line.strip('\n')
                name = line.split('|')
                head = []
                for i in range(1,len(name)):
                    head.append(name[i])
                i += 1
                continue
            line = line.strip('\n')
            part = line.split('|')
            dic = {}
            for index,value in enumerate(head):
                if index <= 2:
                    dic[value] = part[index+1]
                else:
                    dic[value] = int(part[index+1])
            efficiency = (dic['pts']+dic['reb']+dic['asts']+dic['stl']+dic['blk']-(dic['fga']-dic['fgm'])\
                          +dic['fta']-dic['ftm']+dic['turnover'])/float(dic['gp'])
            dic['efficiency'] = efficiency
            data_all.append(dic)
        data_all = pd.DataFrame(data_all)
        return data_all
    
    
    def ListUp(self,name):
        df = self.Split()
        df_name = df.sort_values(by=name, ascending=False)
        df_name.reset_index(drop=True, inplace=True)
        listup = []
        for i in range (df_name.shape[0]):
            firstname = df_name.loc[i,'firstname']
            lastname = df_name.loc[i,'lastname']
            value = df_name.loc[i,name]
            listup.append([firstname,lastname,value])
        return listup
            
    def PrintMost(self):
        df = self.Split()
        for i in range(3, len(df.columns)):
            ln = df[df.columns[i]].argmax()
            print("Most "+df.columns[i]+": "+df.loc[ln,df.columns[0]]+" "+df.loc[ln,df.columns[1]]+", "+str(df.loc[ln,df.columns[i]])+"\n")
        
    def Save(self,name):
        data = self.ListUp(name)
        outfile = open("top50_"+name+".txt","w")
        for i in range(50):
            outfile.write(data[i][0]+" "+data[i][1]+", "+str(data[i][2])+"\n")
        outfile.close()
        print("Save Top50 "+name+" File Finished.")       
        
if __name__ == "__main__":    
    path = "player_regular_season_career.txt"
    NBA = NBA_Analysis(path)
    NBA.PrintMost()
    NBA.Save('efficiency')


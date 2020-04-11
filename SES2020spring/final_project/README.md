#NBA历史五十大最有效率球员
##摘要
NBA拥有三十支职业队伍，在发展历史中涌现了众多优秀的运动员。本实验通过计算历史上所有球员的上场效率，得出了NBA历史五十大最有效率球员的排名。
##实现
###数据获取
我们从NBA的官方网站获取了3924名球员的数据，其中包括球员的得分、篮板、抢断等信息。出于样品容量的考虑，仅采用球员在常规赛季中的数据，汇总在txt文件中。手动获取原始数据后，将其接入到python程序中进行计算。

###球员效率
球员效率是定量评价球员表现的依据，并且认为球员价值与在场效率直接相关。NBA官方提供的计算公式为：

$$Efficiency=$$
$$\frac{pts+reb+asts+stl+blk-((fga-fgm)+(fta-ftm)+turnover)}{gp}$$

###数据输出
录入球员信息，计算每一名球员的效率，输出效率最高的50名球员的数据到txt文件中。除此之外还可以得到各项数据的排名，比如出场时间最多的球员、的分最高的球员等。

###python代码
```
import pandas as pd

class NBA_Analysis:
    
    def __init__(self,path):
        self.path = path
        
    def Split(self):
        file = open(self.path,"r")
        data_all = []
        i = 0 
        for line in file:
            #提取head数据
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
            efficiency = (dic['pts']+dic['reb']+dic['asts']+dic['stl']+dic['blk']-(dic['fga']-dic['fgm'])+dic['fta']-dic['ftm']+dic['turnover'])/float(dic['gp'])
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
```
##总结
本次实验圆满完成了目的，定量地计算了NBA历史上球员的效率，得到了50大最有效率球员的排名，以及各种单项排名。
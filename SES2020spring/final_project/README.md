# NBA历史五十大最有效率球员
## 摘要
NBA拥有三十支职业队伍，在发展历史中涌现了众多优秀的运动员。本实验通过计算历史上所有球员的上场效率，得出了NBA历史五十大最有效率球员的排名。除此之外，还会输出各项数据（如得分、篮板、抢断等）排行最高的球员。

## 实现
### 数据获取
我们从NBA的官方网站获取了3924名球员的数据，包括球员的得分、篮板、抢断等各项指标。出于样品容量的考虑，仅采用球员在常规赛季中的数据，汇总在txt文件中。对原始数据进行下载后，将其接入到python程序中进行计算。

### 球员效率
球员效率是定量评价球员表现的依据，并且认为球员价值与在场效率直接相关。NBA官方提供的计算公式为：

$$Efficiency=$$
$$\frac{pts+reb+asts+stl+blk-((fga-fgm)+(fta-ftm)+turnover)}{gp}$$

### 数据输出
录入球员信息，计算每一名球员的效率，输出效率最高的50名球员的数据到txt文件中。除此之外还可以得到各项数据的排名，比如出场时间最多的球员、的分最高的球员等。

## 运行方法

### 所需库的安装
在此主要用到的库为Pandas，可通过如下方式进行安装  
```
pip install -r requirements.txt
```
### Run
```
cd Run/
python final_project_NBA.py
```
预测结果将会保存到top50_efficiency.txt中   
运行程序的输出截图如下所示：    
  
![程序运行输出截图](https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/Run/Output.png)

### Test
```
cd Test/
python function_test.py
```
测试程序的输出截图如下所示：  
 
![程序运行输出截图](https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/Test/Output.png)

## 代码思想
将player_regular_season_career.txt中的数据进行处理，并借用Pandas库生成一个更便于处理的表格文件，其标题行由球员姓名及各项指标的名称构成。在此基础上，我们可以十分便捷地分析出我们所期望得到的信息。  
我们定义了NBA_Analysis类，并对函数功能进行了高质量的封装。  
Split函数实现了从原始文件中读取数据，并返回pandas.Dataframe格式的表格数据。  
ListUp函数实现了对特定指标进行球员排序，且会生成一个排序后的pandas.Dataframe格式的表格数据。  
PrintMost函数实现了对各项指标排名最高球员的数据输出，以Most xxx: Player Name的格式进行打印。
Save函数实现了对特定指标进行排序后，取出排名前50球员的数据,并保存至top_xxx.txt文件中。

## 总结
本次实验圆满完成了目的，定量地计算了NBA历史上球员的效率，得到了50大最有效率球员的排名，以及各种单项排名。

## 参考资料
详见该项目的说明及要求文档：https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/project_description.pdf  
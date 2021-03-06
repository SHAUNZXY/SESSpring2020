# NBA历史五十大最有效率球员
工程科学2020年春项目实践
组员：邹晓阳 王星 李想

## 摘要
NBA拥有三十支职业队伍，在发展历史中涌现了众多优秀的运动员。本实验通过分析NBA网站中的历史数据统计，计算了历史上所有球员的上场效率，得出了NBA历史五十大最有效率球员的排名。除此之外，还会输出各项数据指标（如得分、篮板、抢断等）排行最高的球员。

## 实现
### 数据获取
我们从NBA的官方网站获取了历史数据统计。其包含有3924名球员的数据，如球员的得分、篮板、抢断等各项指标。出于样品容量的考虑，仅采用球员在常规赛季中的数据，汇总在txt文件中。

### 球员效率
球员效率是定量评价球员表现的依据，并且认为球员价值与在场效率直接相关。NBA官方提供的计算公式为：  

![程序运行输出截图](https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/Formula.png)


### 数据输出
录入球员信息，计算每一名球员的效率，输出效率最高的50名球员的数据到txt文件中。除此之外还可以得到各项数据的排名，比如出场时间最多的球员、得分最高的球员等。

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

此外可以在Travis CI这一持续集成服务中，测试代码在各个版本中的运行状况，测试结果如下图所示，均能通过  

![程序运行输出截图](https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/Travis_CI_Result.png)

## 代码思想
将player_regular_season_career.txt中的数据进行处理，并借用Pandas库生成一个更便于处理的表格文件，其标题行由球员姓名及各项指标的名称构成。在此基础上，我们可以十分便捷地分析出我们所期望得到的信息。  
  
我们定义了NBA-Analysis类，并对函数功能进行了高质量的封装。  
1. Split函数实现了从原始文件中读取数据，并返回pandas.Dataframe格式的表格数据。  
2. ListUp函数实现了对特定指标进行球员排序，且会生成一个排序后的pandas.Dataframe格式的表格数据。  
3. PrintMost函数实现了对各项指标排名最高球员的数据输出，以Most xxx: Player Name的格式进行打印。
4. Save函数实现了对特定指标进行排序后，取出排名前50球员的数据,并保存至top_xxx.txt文件中。

## 总结
本次实验定量地分析了NBA历史上球员的各种技术指标，可得到任一特定技术指标排名前50的球员信息，以及各种指标排名最高的球员信息。这在圆满完成项目要求的基础上，使接口更加灵活，可以更加自由地生成目标数据。在实验过程中，对于数据获取，我们从NBA官网得到了球员的历史数据；对于数据处理，我们学习了Pandas库的使用，优化了原始数据的处理过程，合理地利用了其他数据格式；对于计算与输出，我们采取了官方提供的效率计算公式，在得到每位球员的数据基础上实现了排序和输出。通过这次实验，我们从数据获取到设计函数再到结果输出，锻炼了完整解决问题的能力、使用Python编程的能力和模块检测的能力。相信我们能够在未来的课程中会更为熟练地使用！


## 参考资料
详见该项目的说明及要求文档：https://github.com/SHAUNZXY/SESSpring2020/blob/master/SES2020spring/final_project/project_description.pdf  
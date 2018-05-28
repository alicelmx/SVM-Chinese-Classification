# SVM-Chinese-Classification
利用支持向量机实现中文文本分类

先放[GitHub代码](https://github.com/alicelmx/SVM-Chinese-Classification)，如果觉得写得不错，记得加个star哦，嘻嘻～
## 基本流程
**1、准备好数据食材、去停用词并利用**结巴**(jieba)进行分词处理**

数据食材选用参考：[NLP中必不可少的语料资源](https://blog.csdn.net/alicelmx/article/details/79083903)

jieba分词模块参考[官方文档](https://pypi.org/project/jieba/)啦～
```
# 参照代码中的cutWords.py文件
```
**2、利用*卡方检验*特征选择**

**卡方检验：**在构建每个类别的词向量后，对每一类的每一个单词进行其卡方统计值的计算。
1. **首先对卡方 检验所需的 a、b、c、d 进行计算。**
a 为在这个分类下包含这个词的文档数量;
b 为不在该分类下包含这个词的文档数量;
c 为在这个分类下不包含这个词的文档数量; 
d 为不在该分类下，且不包含这个词的文档数量。
2. **然后得到该类中该词的卡方统计值**
公式为 float(pow((a*d - b*c), 2)) /float((a+c) * (a+b) * (b+d) * (c+d))。
3. **对每一类别的所有词按卡方值进行排序，取前 k 个作为该类的特征值，这里我们取 k 为 1000**
```
# featureSelection.py
```
**3、利用*TF*IDF算法*进行特征权重计算**

**TF-IDF算法**：


- 全称叫 Term Frequency-Inverse Document Frequency **词频-逆文档频率算法**
- 主要用于关键词抽取
- 优点：每个词的权重与特征项在文档中出现的频率成正比，与在整个语料中出现该特征项的文档数成反比。
- 原理解说：
![这里写图片描述](https://img-blog.csdn.net/20180524002834406?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FsaWNlbG14/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
训练文本的特征向量表示数据在 train.svm文件中，测试文本的特征向量表示数据在test.svm 中。

```
# featureWeight.py
```
**3、基于训练文本的特征向量数据，使用*LIBSVM库*训练SVM 模型**

使用libsvm对train.svm进行模型训练，和对test.svm模型进行预测

测试命令：

```
对train.svm文件数据进行缩放到[0,1]区间
./svm-scale -l 0 -u 1 train.svm > trainscale.svm

对test.svm文件数据进行缩放到[0,1]区间
./svm-scale -l 0 -u 1 test.svm > testscale.svm

对trainscale.svm 文件进行模型训练
./svm-train -s 1 trainscale.svm trainscale.model

对testscale.svm 文件进行模型预测，得到预测结果，控制台会输出正确率
./svm-predict testscale.svm trainscale.model testscale.result
```
**4、对于测试集进行特征向量表示，代入训练得到的 SVM 模型中进行预测分类**
预测结果：92%
![这里写图片描述](https://img-blog.csdn.net/20180524111844195?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FsaWNlbG14/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

目前这个阶段，能够讲到这个程度，以后在补充吧，小明酱撤退了～

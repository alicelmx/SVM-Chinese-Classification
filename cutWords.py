# 本程序用于将搜狗语料库中的文本进行分词，并且去除停用词
# coding=utf-8
import jieba
import jieba.posseg as pseg
import time
import os
'''
训练集：1200
测试集：200
'''
# 文本分词

def cutText(dirname):
	# dirname数据目录
	for category in os.listdir(dirname):
		catdir = os.path.join(dirname,category)
		if not os.path.isdir(catdir):
			continue
		files = os.listdir(catdir)

		i = 0
		for cur_file in files:
			print("正在处理"+category+"中的第"+str(i)+"个文件.............")
			filename = os.path.join(catdir,cur_file)
			#读取文本
			with open(filename,"r",encoding='utf-8') as f:
				content = f.read()
			
			#进行分词
			words = pseg.cut(content)
			# 用于剔除停用词的列表
			finalContent = []
			# 停用词列表
			stopWords = [line.strip() for line in open('Chinesestopword.txt', 'r', encoding='utf-8').readlines()]

			for word in words:
				word = str(word.word)
				# 如果该单词非空格、换行符、不在听用词表中就将其添加进入最终分词列表中
				if len(word)  > 1 and word != '\n' and word != '\u3000' and word not in stopWords:
					finalContent.append(word)

			# 组合成最终需要的字符串
			finalStr = " ".join(finalContent)
			
			# 写入文件
			writeFileName = writeFilePathPrefix+"/"+category+"/"+str(i)+".txt"
			print(writeFileName)
			with open(writeFileName,"w",encoding = 'utf-8') as f:
				f.write(finalStr)
			i = i + 1

			print("成功处理"+category+"中的第"+str(i)+"个文件～哦耶！")

if __name__ == '__main__':
	# 记录开始时间
	t1=time.time()

	readFilePathPrefix = "SogouData/ClassFile"
	writeFilePathPrefix = "SogouDataCut"

	cutText(readFilePathPrefix)

	# 记录结束时间
	t2=time.time()
	#反馈结果
	print("您的分词终于完成，耗时："+str(t2-t1)+"秒。") 

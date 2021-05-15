import nltk
from nltk import word_tokenize,pos_tag
from nltk.corpus import stopwords
import re
#nltk抽取关键词
#去除网址，标点符号，数字等无关信息
def remove(text):
    rep= re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("",text)
    rep = re.compile(r'https://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("", text)
    remove_chars = '[0-9’!"#$%&\'()*+,./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    return re.sub(remove_chars, '', text)
paragraph = "As part of the High Velocity Testing initiative we'd like to create an experiment which will attempt to prove or disprove a causal relationship with increased retention for Multi-Accont Containers addon.There will be 4 branches for this experimentControl - No treatmentTrigger the CFR when a user visits a social media site with the shopping sites in the topFrecentSites. It will use a privacy-oriented message.Trigger the CFR when a user visits a shopping site with the social media sites in the 'topFrecentSites'. It will use a privacy-oriented message, but different than the 2. branch.Same trigger as 2., but it will use a Life-Organizing related message.The site list can be found hereThe CFR recipe can be found here. But it still subjects to change, we are still working on copies. ".lower()
paragraph = remove(paragraph)
print(paragraph)
cutwords1 = word_tokenize(paragraph)   #分词
print('【NLTK分词结果：】')
print(cutwords1)

interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']   #定义符号列表
cutwords2 = [word for word in cutwords1 if word not in interpunctuations]   #去除标点符号
print('\n【NLTK分词后去除符号结果：】')
print(cutwords2)

stops = set(stopwords.words("english"))
cutwords3 = [word for word in cutwords2 if word not in stops]
print('\n【NLTK分词后去除停用词结果：】')
cutwords3 = nltk.FreqDist(cutwords3)
print(cutwords3.most_common(5))

print('\n【NLTK分词去除停用词后进行词性标注：】')
print(pos_tag(cutwords3))

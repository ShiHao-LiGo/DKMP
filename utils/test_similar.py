from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))

def tfidf(s1):
    s8='loop code variable type bottom Junk characters Gnome shell KDE Plasma Unity core GUI Network I/O Driver'
    # 将字中间加入空格
    # 转化为TF矩阵
    def add_space(s):
        return ''.join(list(s))
    s1,s8= add_space(s1),add_space(s8)
    print(s1,s8)
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1,s8]
    vectors = cv.fit_transform(corpus).toarray()
    print("计算TF-IDF值yayaya")
    print(corpus)
    print(vectors)

def tfidf_similarity(s1, s2):
    def add_space(s):
        return ''.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    print("计算TF-IDF值")
    print(vectors)
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator


if __name__ == '__main__':

    s1 = "The downloads view in the Library is broken"
    s2 = '出现的原因是什么'
    tfidf(s1)
    s3 = 'code improve scanna'
    s4 = '优先级怎么样'
    an = {}
    i = 0
    s = {
        'bug01':'Add in a sponsored by override to collections',
        'bug02':'The downloads view in the Library is broken,Firefox',
        'bug03':'The message-group provider is causing 404 error for RemoteSettings',
        'bug04':'Add default theme as an option on theme screen in Fx 80',
        'bug05': 'Remove registration for FTP support on Windows',
        'bug06': 'Use different tippytop icons for different Yandex search shortcuts',
        'bug07': 'Show messaging-experiments messages in devtool'
    }
    # s = ['Add in a sponsored by override to collections', 'The downloads view in the Library is broken,Firefox', 'The message-group provider is causing 404 error for RemoteSettings', 'Add default theme as an option on theme screen in Fx 80', 'Remove registration for FTP support on Windows',
    #      'Use different tippytop icons for different Yandex search shortcuts', 'Show messaging-experiments messages in devtool']
    for key,value in s.items():
        sim1 = tfidf_similarity(s1, value)
        # sim2 = jaccard_similarity(s1, k)
        # sim3=tf_similarity(s3, s1)
        an[key] = sim1
        i = i + 1
    an = sorted(an.items(), key=lambda x: x[1], reverse=True)
    print(an)
    # choice = an[0][0]
    # print(choice == 3)
    # print(an[0][1])
    # print(s)
    # print(an)
    # print(an[0][0])
    # print("tf-idf计算相似度 ")
    # print(tfidf_similarity(s3, s1))
    # print(tfidf_similarity(s3, s2))
    # print(tfidf_similarity(s3, s3))
    # print(tfidf_similarity(s3, s4))
    # print("tf计算相似度 ")
    # print(tf_similarity(s3, s1))
    # print(tf_similarity(s3, s2))
    # print(tf_similarity(s3, s3))
    # print(tf_similarity(s3, s4))
    # print("jaccard计算相似度 ")
    # print(jaccard_similarity(s3, s1))
    # print(jaccard_similarity(s3, s2))
    # print(jaccard_similarity(s3, s3))
    # print(jaccard_similarity(s3, s4))

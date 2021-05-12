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


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
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
    s1 = "Bug-108746's des？"
    s2 = '出现的原因是什么'
    s3 = '严重性怎么样'
    s4 = '优先级怎么样'
    an = {}
    i = 0
    s = ['type或类型或种类', '出现的原因或症状或描述是什么怎么复现或步骤或describe', '严重性或severity怎么样', '优先级或priority怎么样', '状态或status是怎么样',
         '现在的阶段或milestone', '作用的产品或product']
    for k in s:
        sim1 = tfidf_similarity(s1, k)
        sim2 = jaccard_similarity(s1, k)
        sim3=tf_similarity(s3, s1)
        an[i] = sim2
        i = i + 1
    an = sorted(an.items(), key=lambda x: x[1], reverse=True)
    choice = an[0][0]
    print(choice == 3)
    print(an[0][1])
    print(s)
    print(an)
    print(an[0][0])
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

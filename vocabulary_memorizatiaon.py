# -*- coding: utf-8 -*-
# 项目：英语单词记忆小程序
# 编写日期：2026-09-18
# 作者：LM0510cc
# 功能：字典存储单词，查询词义、随机默写练习

vocabulary_dict = {"company":"公司，交往，陪伴","action":"行为，行动"}
vocabulary_dict["balance"] = "保持平衡，平衡，抵消"
vocabulary_dict["stretch"] = "伸展，延伸，夸大"
vocabulary_dict["diet"] = "日常饮食，节食"
vocabulary_dict["frame"] = "画框，构架，画面"



while True:
    learn_english = input("请输入您要默写的单词，并默念它的以意思（结束请说‘今天的任务已完成’）：")
    if learn_english == "今天的任务已完成":
        print("我就知道你一定能行！！！加油，明天我们不见不散")
        print("当前英语记忆代码总共收录了\033[31m" + str(len(vocabulary_dict)) + "\033[0m" + "个单词\n期待你更多的积累")
        break
    if learn_english in vocabulary_dict:
        print("您查询的英文单词释义为\033[34m" + vocabulary_dict[learn_english] + "\033[0m")
        print("非常棒，拼写的一点没错，来继续")
    else:
        print("再回去翻翻，输入错了，别气馁")

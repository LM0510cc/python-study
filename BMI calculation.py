# -*- coding: utf-8 -*-
# 项目：BMI计算器
# 编写日期：2026-09-18
# 作者：LM0510cc
# 功能：输入身高体重，计算BMI并给出健康评估

while True:
    weight_input = input("请输入您的体重 单位 kg：")

    if weight_input == "所有人已计算完毕":
        print("\33[91m" + "好的，BMI计算程序已关闭 "+ "\33[0m")
        break
    user_weight = float(weight_input)
    user_height = float(input("请输入您的身高 单位 m:"))
    BMI = user_weight / (user_height)**2
    print("您的BMI为\033[94m" + str(BMI) + "\033[0m")
    if BMI < 18.5:
        print("太瘦了，兄弟，该增肌了")
    elif BMI < 24:
        print("牛逼兄弟，身材真是完美\n同龄男生看了流泪")
    elif BMI < 28:
        print("兄弟，稍微有点胖了，晚上尽量别吃饭了！")
    else:
        print("逼自己一把，你一定会发现更好的自己，该减肥了兄弟")



weight=float(input("請輸入你的體重(單位:公斤):"))   #設定身高及體重並規定單位
height=float(input("請輸入你的身高(單位:公尺):"))

BMI=weight/height**2    #**為平方

print("BMI"+str(BMI))
"""计算加速度
位移=初速度×时间+加速度×时间的平方/2
"""
distance=float(input("请输入位移："))
start_speed=float(input("请输入初速度："))
time=float(input("请输入时间："))
eccelarate=(distance-start_speed*time)*2/time**2
print(eccelarate)

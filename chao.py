import time

name = "Bảo Ngọc"
greeting = "Xin chào"

for char in f"{greeting}, {name}!":
    print(char, end="", flush=True)
    time.sleep(0.05)

print()
time.sleep(0.5)
print("Chúc bạn luôn xinh đẹp, vui vẻ và gặp nhiều may mắn!")
print("Cảm ơn bạn đã chạy chương trình này ♥")
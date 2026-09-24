# 1.. dono me koi bhi method use kr skte hai
file=open('youtube.txt','w')

try:
    file.write('chai aur code')
finally:
    file.close()

# 2..
with open ('youtube.txt','w') as file:
    file.write('chai aur python')    
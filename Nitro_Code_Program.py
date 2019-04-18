import random, string
import webbrowser

print(">>> Discord Nitro Code Program <<< ")
print(">>> MythaTR#5274 Discord Official ; https://discord.gg/YdkYb2J <<< \n\n\n ")
webbrowser.open('')

num=input('Kac Kod Üreteyim : ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Üretiyorum...")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write(y)
   f.write("\n")

f.close()
input("\n\nFinished, Press enter to exit. Codes saved in Nitro Codes")

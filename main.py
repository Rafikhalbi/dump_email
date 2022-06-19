import os,sys,time,random
from datetime import datetime

data = []

#color
red = "\x1b[1;91m"
blue = "\x1b[1;96m"
white = "\x1b[1;97m"

#gmail/email input
GM = "@gmail.com"
YH = "@yahoo.com"

def main():
    global data 
    print("cth: rafi")
    name = input("[•] Name: ")
    print("""
    *------[LIST]-----*
    [1] Gmail 
    [2] Yahoo 
            """)
    choose = input("[•] Choose: ")
    if choose =='1' or choose == '02':
        jumlah = int(input("[•] jumalah Dump: "))
        for i in range(jumlah):
            data.append(name+str(i)+GM)
    elif choose == '2' or choose == '02':
        jumlah = int(input("[•] jumlah dump: "))
        for i in range(jumlah):
            data.append(name+str(i)+YH)
    rand = random.randint(0,999999)
    save = open(f"result/{name}{rand}.txt","w")
    save.write(str(data))
    save.close()
    print(f"[•] File save: result/{name}{rand}.txt")
    return True

def ketik(z):
    for i in z+"\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(00.1)

if __name__ == "__main__":
    os.system("clear")
    ketik("""
            *-----[DUMP EMAIL]----*
            """)
    print("* Gunakan Dengan Bijak")
    print("* Author Tidak bertanggung Jawab atas apa yang terjadi")
    a = input("[•] Next (y/n): ")
    if a in["y","Y"]:
        main()
    else:
        ketik("[•] See You:)")


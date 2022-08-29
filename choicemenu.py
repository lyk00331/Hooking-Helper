import os

def choice_menu():
	choice = int(input("해당 apk가 mono 방식인지 il2cpp 방식인지 확인하는 과정입니다.\n다음 중 해당하는 번호를 입력하세요.\n\n1. libmono 파일 존재\n2. libil2cpp 파일 존재\n3. 프로그램 종료\n\n==> "))
	print("\n=============================================================\n")

	if choice == 1:
		print("mono 방식은 지원하지 않습니다.\n프로그램을 종료합니다.")
		exit()

	elif choice == 2:
		num = int(input("il2cpp 방식을 진행하기 위해서는 'il2cppdumper'가 필요합니다.\n다음 중 해당하는 번호를 입력하세요.\n\n1. 프로그램 존재\n2. 프로그램 미존재\n\n==> "))
		print("\n=============================================================\n")

		if num == 1:
			num2 = int(input("il2cppdumper의 압축을 푼 후, 현재 스크립트가 있는 곳으로 옮겨주세요.\n되셨으면 1을 입력해 주세요.\n\n==> "))
			print("\n=============================================================\n")
			if num2 == 1:
				packname()
		elif num == 2:
			webbrowser.open("https://github.com/Perfare/Il2CppDumper/releases/download/v6.7.25/Il2CppDumper-v6.7.25.zip")
			num2 = int(input("파일 다운로드가 완료되면 압축을 푼 후, 현재 스크립트가 있는 곳으로 옮겨주세요.\n되셨으면 1을 입력해 주세요.\n\n==> "))
			print("\n=============================================================\n")
			if num2 == 1:
					packname()

	elif choice == 3:
		print("프로그램을 종료합니다.")
		exit()


def packname():
	folder = input("apktool을 이용하여 생성된 폴더 경로를 복사 및 붙여넣어주세요.\n\n=> ")
	os.chdir(folder)
	f_op = open("AndroidManifest.xml", "r")
	while 1:
		line = f_op.readline()
		if not line:
			break
		if "package" in line:
			a = list(line.split(" "))
			for b in a:
				if "package" in b:
					c = b.split('"')
					k = c[1]
	f_op.close()
	return k


def findoffset():
	ass = input("Il2CppDumper를 통해 생성된 dump.cs 파일 경로를 복사 및 붙여넣어주세요.\n\n=> ")
	os.chdir("{}",format(ass))
	ch_g = find_O()
	f = open('dump.cs','r',encoding="utf-8")
	if ch_g == 1:
		while 1:
			line = f.readline()
		if not line:
			exit()
		if "GetHPMaxBase" in line:
			a = list(line.split(" "))
			b = list()
			for i in a:
				if "0x" in i:
					b.append(i)
			print("RVA값 == ",b[0], "offset값 == ",b[1])
			OSF.append(b[0])


def hooking():
	a = str(OSF[0])
	


print("\n=============================================================\n")
choice_menu()


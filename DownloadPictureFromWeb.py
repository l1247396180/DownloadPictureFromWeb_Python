import requests


def downloadPicture(url: str, id: int):
    picture = requests.get(url)
    picture.encoding = 'utf-8'
    with open('picture'+str(id)+'.jpg', 'wb+') as f:
        f.write(picture.content)

if __name__ == '__main__':
	print(u"输入网址即可开始下载所有图片")
	cnt = 0
	response = requests.get(input())
	originCode = response.text
	idx = 0
	length = len(originCode)
	while originCode.find('<img src=\"https:', idx) != -1:
		idx = originCode.find('<img src=\"https:', idx)+1
		begin = originCode.find('\"', idx)+1
		end = originCode.find('\"', begin)
		cnt += 1
		downloadPicture(originCode[begin:end], cnt)

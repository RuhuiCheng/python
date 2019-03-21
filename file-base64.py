import base64

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

if __name__ == "__main__":
    # ToBase64("/home/crh/Documents/xmh/x.mp4",'/home/crh/Documents/xmh/base64.txt')  # 文件转换为base64
    ToFile("/home/crh/Documents/xmh/base64.txt",'/home/crh/Documents/xmh/x2.mp4')  # base64编码转换为二进制文件
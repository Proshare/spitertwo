#保存在文件当中
import os
import downloadImage

def downloadDIR(urlList,page):
    if not os.path.exists("downloads"):
        os.makedirs('downloads')
    root_path=os.getcwd();
    for i in range(page):

        img_dir="downloads/"+urlList[i][24:].replace("/",'')
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        os.chdir(img_dir)
        # 调用下载图片的文件
        print("都是那些帖子"+urlList[i])
        downloadImage.downloadImage(urlList[i])
        os.chdir(root_path)
        # 可以用来改变python当前所在的文件夹
        # 然后在下载完一个帖子后得移回当前目录
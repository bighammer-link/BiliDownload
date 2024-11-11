### 介绍：

仓库脚本只是将**Bilibili**某UP主的所有视频链接解析出来，并且存放到`txt`文件夹里面，搭配工具[**LUX**](https://github.com/iawia002/lux)使用，完成所有视频下载。

### 使用方法：

1.安装LUX：[**安装教程**](https://github.com/iawia002/lux?tab=readme-ov-file#installation)

2.安装脚本依赖：`requests`

3.在B站登陆上你的账号，获取你的Cookie填到main.py第11行字段`'Cookie':""`,的引号中。Cookie获取方法，请自行百度。

4..使用**命令行工具**运行脚本：`python mian.py {UP主ID}`

**ID获取方式：**

点击UP主页，上方地址栏数字就是ID

![](https://raw.githubusercontent.com/bighammer-link/My_Pictures/myblog/6194002f88505dedb828d5d2e99149d4.png)

**使用示例：**

![](https://raw.githubusercontent.com/bighammer-link/My_Pictures/myblog/eb03987bb910064b0859454134ecf38b.png)

5.等待所有视频URL解析完成后，会将结果保存在一个名为**UP主ID**的文件夹下面的`urls.txt`文件内，在该文件夹下打开命令行窗口，使用**LUX**的命令，进行批量下载即可。

命令：

```
lux -F urls.txt
```

![](https://raw.githubusercontent.com/bighammer-link/My_Pictures/myblog/f92e2f88e1261e15d094c0526a9af918.png)
**注意事项**
播放下载的视频的时候，可能会出现下方问题。
![](https://raw.githubusercontent.com/bighammer-link/My_Pictures/myblog/20241111221608.png)
**解决方法：**到[release](https://github.com/bighammer-link/BiliDownload/releases/tag/1.0)里面[下载)(https://objects.githubusercontent.com/github-production-release-asset-2e65be/886723004/4e551f56-95e6-44c4-82eb-4fe470546cd3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20241111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241111T142426Z&X-Amz-Expires=300&X-Amz-Signature=59612f33dee3ba3b18e1ccecc8b0f180d3198af4d43d7f9b6967d01543e3032c&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3DHEVC.ISO&response-content-type=application%2Foctet-stream)HEVC扩展，安装即可。

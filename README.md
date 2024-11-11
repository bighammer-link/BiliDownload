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
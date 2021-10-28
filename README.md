## 会议铭牌生成器

新人初到单位一般都是打打杂的嘛。一般开会准备铭牌这种没什么技术含量但是需要一定时间准备的事情肯定是归新人桑所有啦！

社畜冰冰喵之前一直是使用高级的否头少破软件来制作高精度好用的铭牌，并且很贴心的在图片铭牌的边边上只做了1px宽的切割辅助线，方便打印完后切割，直到  **怎么一场突发会议能有30个人参加！**

事情是这样的。在这一天，社畜冰冰喵早上一如既往的来摸鱼，结果没想到一早上就有调研人员在开会，本以为只要忙完这边就够了，结果在上午突然接到通知！说下午有30个人来开会！这个中午，冰冰喵没有休息。

但是！冰冰喵即便社畜化了，但作为懒冰服首席开发肯定是不能这么让休息时间这么溜走的！于是她花了两个下午的时间把自动化铭牌生成的屎山拉出来了！



## Usage：

##### ※ 使用 pipy 安装所需轮子: 

##### `pip3 install –r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

​	1. 选择底图使用什么

​	2. 输入名字

​	3. 得到图片

​	n. 如需制作其他铭牌，继续输入名字即可，将使用同一底图制作。



TIP: 程序只能处理 1~7个中国字儿，根据那天中午的经验，名字超过7个字的铭牌数量只有一小部分，给每一个字符长度匹配一组参数太累惹。（因为参数都是根据制作好的图片手写的）



## example：

![nameplateMakerExample](https://file.hk1.sinbing.com/image/github/NameplateMaker/nameplateMakerExample.png)

![nameplateMakerExample-icecat](https://file.hk1.sinbing.com/image/github/NameplateMaker/nameplateMakerExample-icecat.png)






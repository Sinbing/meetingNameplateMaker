# -*-* Coding: UTC-8 By: Sinbing *-*- #
from func_timeout import FunctionTimedOut, func_timeout
from PIL import ImageFont, ImageDraw, Image
import time
import sys



'''---------------- 可编辑变量开始 ----------------'''
Flag_enableSeletBGmode = 1      # 是否启用可切换背景模式，1 = 启用
defaule_BG = 'white_BG.png'     # 不启用切换背景模式时的默认背景
'''---------------- 可编辑变量结束 ----------------'''


def darwImgBlackText(Dx, Dy, Dtext, imgName, Tsize):
    # Set img draw type.
    draw = ImageDraw.Draw(imgName)                                        
    # Font setting.      
    font = ImageFont.truetype('./res/simhei.ttf', Tsize)
    # Add Text in image.
    draw.text((Dx, Dy),  Dtext, font = font, fill = (0, 0, 0))


# Hardcode config for white_bg
def getWhiteConfig(input):
    global Tx1, Ty1, Tx2, Ty2, Tsize
    # FontSize| 2~4: 120 | 5: 95 | 6: 78 | 7: 68 |
    if len(input) <= 4:
        Tx1, Ty1, Tx2, Ty2, Tsize = 387, 4333, 625, 4333, 1000
    elif len(input) == 5:
        Tx1, Ty1, Tx2, Ty2, Tsize = 387, 4515, 600, 4515, 792
    elif len(input) == 6:
        Tx1, Ty1, Tx2, Ty2, Tsize = 415, 4635, 630, 4638, 650
    elif len(input) == 7:
        Tx1, Ty1, Tx2, Ty2, Tsize = 392, 4560, 599, 4565, 567
    else:
        print('ERROR on get Hardcode Config.')
    if Tx1 != '':
        return Tx1, Ty1, Tx2, Ty2, Tsize
    else:
        print('ERROR on getHardCodeConfig return \'\'')


# Hardcode config for logo_bg
def getLogoConfig(input):
    global Tx1, Ty1, Tx2, Ty2, Tsize
    # FontSize| 2~4: 120 | 5: 95 | 6: 78 | 7: 68 |
    if len(input) <= 4:
        Tx1, Ty1, Tx2, Ty2, Tsize = 357, 4513, 625, 4513, 1000
    elif len(input) == 5:
        Tx1, Ty1, Tx2, Ty2, Tsize = 380, 4567, 625, 4567, 792
    elif len(input) == 6:
        Tx1, Ty1, Tx2, Ty2, Tsize = 400, 4618, 638, 4648, 650
    elif len(input) == 7:
        Tx1, Ty1, Tx2, Ty2, Tsize = 369, 4663, 593, 4627, 567
    else:
        print('ERROR on get Hardcode Config.')
    if Tx1 != '':
        return Tx1, Ty1, Tx2, Ty2, Tsize
    else:
        print('ERROR on getHardCodeConfig return \'\'')


def makeNamedImg(input_imgName:str, x1, y1, x2, y2, Tsize):
    img = Image.open('./res/' + bg_img)
    darwImgBlackText(x1, y1, input_imgName, img, Tsize)
    # rotate 180 & again.
    img180 = img.transpose(Image.ROTATE_180)
    darwImgBlackText(x2, y2, input_imgName, img180, Tsize)
    # Output ERROR info when file cant saved.
    try:
        # Save file.
        img180.save('./' + input_imgName + '.png')
        write_logFile(input_imgName, 1)
        print('''
 -----------------------------------------------
  已生成 {0} 的铭牌，文图片已保存至程序所在目录下。
 -----------------------------------------------'''.format(input_Name))
    except:
        write_logFile(input_imgName, 2)
        print('''
     ----------------------------------------
      文件保存失败，请检查是否有未关闭的重名文件。
     ----------------------------------------\n''')


# Retry when user input info wrong.
def tranceUserInputRetry(user_input):
    global jumpFlag
    jumpFlag = 0
    write_logFile(user_input, 0)
    print('''
 -------------------------------------------------------
           ERROR: 用户输入信息无法被解析
  一次请只输入 ** 一个名字 ** 且不能携带空格逗号等标点符号。
  如名字长度>=8个字，请手动处理。
 -------------------------------------------------------
\n 请在 2s 后重试。\n''')
    time.sleep(2)
    return jumpFlag


def checkUserInput(user_input):
    # retry when inputLen>7 or ''
    if user_input == '':
        tranceUserInputRetry(user_input)
    elif len(user_input) > 7:
        tranceUserInputRetry(user_input)
    elif len(user_input) < 2:
        tranceUserInputRetry(user_input)


def tranceUserInput(user_input):
    global inputName
    # inputLen limit: 1~7
    if len(user_input) == 3:
        inputName = (user_input[0]  + ' ' + user_input[1] + ' ' + user_input[2])
        # inputName = (user_input[::-1])    # ?
    elif len(user_input) == 2:
        inputName = (user_input[0] + '    ' + user_input[1])
    elif len(user_input) >= 4:
        inputName = (user_input)
    return inputName


# User input 2 selet Background img.
def seletBGimg():
    global bg_img, bg_selet
    sub_jumpFlag = 0
    while sub_jumpFlag == 0:
        bg_selet = input('''
 请输入数字选择本次需要使用的背景：
  0. 空白背景
  1. logo背景
    如输入： 1 \n''')
        sub_jumpFlag = 1
        if bg_selet == '1':
            bg_img = 'logo_BG.png'
        elif bg_selet == '0':
            bg_img = 'white_BG.png'
        else:
            sub_jumpFlag = 0
            print('''
 --------------------------------------
        无法解析输入内容
  请只输入 **  1 或 0  ** 且不能携带空格。
 --------------------------------------
\n 请在 2s 后重试。\n''')
            time.sleep(2)
    return bg_img, bg_selet


def writeFile(openFile, writeText):
    with open(openFile, 'a+') as f:
        f.write(writeText)


def write_logFile(loggerName, status: int):
    # create log File -> log_YYYYMMDD.txt
    file = ('./log_' + time.strftime("%Y-%m-%d", time.localtime()) + '.txt')
    # status == 1 -> True; ==0 -> Warn; ==2 -> ERROR.
    nowTime = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    try:
        if status == 1:
            writeFile(file, f'{nowTime}    INFO                   [{loggerName}] 的铭牌生成 成功。\n')
        elif status == 0:
            writeFile(file, f'{nowTime}    * WARN *            [{loggerName}] 的铭牌生成 失败。\n')
        elif status == 2:
            writeFile(file, f'{nowTime}    ## ERROR ##    [{loggerName}] 的铭牌生成 错误，请检查源码。\n')
    except:
        writeFile(file, f'## {nowTime} ## ERROR ##    出现错误，[log status type]异常。 ##\n')


def shutdown(shutdown_time):
    # quikc shutdown with sleep ()s.
    str_shutdown_time = str(shutdown_time)
    print ('程序将在 ' + str_shutdown_time + 's 后自动关闭。')
    time.sleep(shutdown_time)
    sys.exit(0)


if __name__ == '__main__':
    endProgame:str = 0
    # Enable Background selet mode when Flag = 1.
    if Flag_enableSeletBGmode == 1:
        seletBGimg()
        print('本次选用的是' + bg_img)
    else:
        bg_selet = '0'
        bg_img = defaule_BG
    # retry input name.
    jumpFlag = 0
    while jumpFlag == 0:
        jumpFlag = 1
        input_Name = input('\n请输入需要制作铭牌的名字，一次请输入一个名字: \n')
        checkUserInput(input_Name)
    # remake nameSign loop.
    while endProgame == 0:     
        tranceUserInput(input_Name)
        # swich config for diff BG.
        if bg_selet == '0':
            getWhiteConfig(input_Name)
        else:
            getLogoConfig(input_Name)
        makeNamedImg(inputName, Tx1, Ty1, Tx2, Ty2, Tsize)
        # start remake input loop.
        print('\n\n如需继续生成铭牌请输入下一个姓名 ，超过15s无输入程序会自动关闭。\n')
        jumpFlag = 0
        while jumpFlag == 0:
            # 15s no input -> shutdown.
            try:
                remakeText = func_timeout(15,lambda: input('''
 请输入下一个姓名：
 输入 n 会立即关闭程序\n'''))
                # input 'n' to shutdown.
                if remakeText == 'n':
                    shutdown(0)
                # input other -> check input & remake.
                else:
                    input_Name = remakeText
                    jumpFlag = 1
                    checkUserInput(input_Name)
            except FunctionTimedOut:
                sys.exit(0)
import base64


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('ImageConvertResult.py', 'a') as f:
        f.write(content)


if __name__ == '__main__':
    pic2str('./images/LoginBg.png', 'LoginBg')
    pic2str('./images/LoginPageBg.png', 'LoginPageBg')
    pic2str('./images/ObjectDetectionPageBg.png', 'ObjectDetectionBg')
    pic2str('./images/LoginFaceDetectPageBg.png', 'LoginFaceDetectPageBg')
    pic2str('./images/DonePurchasePageBg.png', 'DonePurchasePageBg')
    pic2str('./images/FinishPurchasePageBg.png', 'FinishPurchasePageBg')

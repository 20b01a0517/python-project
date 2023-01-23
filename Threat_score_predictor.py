import matplotlib.pyplot as plt
import cv2

def rgb_to_hex(rgb):
    return '#'+'%02x%02x%02x' % rgb
def threat_score(plaque):
    return plaque*2/10000

def threat_score_predictor(image):
    img1=cv2.imread(image)
    hist1 = cv2.calcHist([img1], [0], None, [256], [1, 255])
    hist2 = cv2.calcHist([img1], [1], None, [256], [1, 255])
    plt.subplot(222), plt.plot(hist1,label="Red pixel count",color='red'), plt.plot(hist2,label="Green pixel count",color='green')
    plt.legend(loc='upper right')
    plt.xlabel('Intensity of Pixel')
    plt.ylabel('Pixel Count(Density)')
    ax=plt.gca()
    line=ax.lines[1]
    arr=line.get_ydata()
    arr=list(arr[1:])
    plaque=max(arr)
    print("Plaque Area is approx. : ",plaque)
    ts=threat_score(plaque)
    print("Threat Score is : ",threat_score(plaque))
    print("Suggestions to the User: ")
    print("Nominal value for plaque percentage is 30 to 70")
    if(ts>=70):
        print("Your Condition is quite Critical. Consult nearby hospital or Doctor immediately")
    elif(ts>=30 and ts<70):
        print("It is better if you follow proper diet and medical prescription. Consult a doctor for further instructions")
    else:
        print("You are healthy. Follow the as usual diet")

    plt.show()
    
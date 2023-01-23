#import matplotlib.pyplot as plt
import extcolors
def color_extractor(image):
    colors,pixel_count=extcolors.extract_from_path(image)
    pixel_count-=colors[0][1]
    pixel_dict={}

    for i in colors[1:  ]:
        pixel_dict[i[0]]=i[1]*100/pixel_count
        print(i[0],"-->",i[1]*100/pixel_count,"%")
    print(pixel_dict)

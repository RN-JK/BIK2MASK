import os

try:
    os.mkdir("input")
    os.mkdir("output")
    input('insert bik files in input. ')
    exit()

except:
    pass

for bik in os.listdir('input'):
    filename=bik.split(".")[0]
    os.system('ffmpeg -i input/'+bik+' -vf "[in] scale=iw/2:ih/1, pad=iw:1.5*ih [top]; movie=input/'+bik+', scale=iw/2:ih/2, fade=out:9999999:9999999:alpha=0, curves=r="0.0/1.0":g="0.0/1.0":b="0.0/1.0" [bottom]; [top][bottom] overlay=main_w-main_w:main_h/1.5 [out]" -s 960x1080 -b:v 2500k output/'+filename+'.mp4')
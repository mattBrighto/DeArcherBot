from PIL import Image
import time
def blend_together(h, m):
    file1=time.strftime(f"/home/debian/DeArcher/hours/{h}.png")
    file2=time.strftime(f"/home/debian/DeArcher/minutes/{m}.png")
    file3=time.strftime(f"/var/www/html/full/{h}_{m}.png")
    im1= Image.open(file1)
    im2= Image.open(file2)
    face= Image.open('face.png')
    faceless = Image.composite(im1, im2, im1)
    merged = Image.composite(faceless, face, faceless)
    merged.save(file3)
for h in range(24):
    for m in range(60):
        if len(str(h)) < 2:
            h = "0"+str(h)
        else:
            h = str(h)
        if len(str(m)) < 2:
            m = "0"+str(m)
        else:
            m = str(m)
        blend_together(h, m)
from PIL import image
im = image.open('myfile.png',r)
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
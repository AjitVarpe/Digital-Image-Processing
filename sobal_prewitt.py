# MATLAB code for Sobel operator
k=imread("logo.png");
# edge detection
k=rgb2gray(k);
k1=double(k);
s_msk=[-1 0 1; -2 0 2; -1 0 1];
kx=conv2(k1, s_msk, 'same');
ky=conv2(k1, s_msk', 'same');
ked=sqrt(kx.^2 + ky.^2);

# #display the images.
imtool(k,[]);

# #display the edge detection along x-axis.
imtool(abs(kx), []);

# #display the edge detection along y-axis.
imtool(abs(ky),[]);

# #display the full edge detection.
imtool(abs(ked),[]);


# #Scharr operator -> edge detection
k=imread("logo.png");
k=rgb2gray(k);
k1=double(k);
s_msk=[-3 0 3; -10 0 10; -3 0 3];
kx=conv2(k1, s_msk, 'same');
ky=conv2(k1, s_msk', 'same');
ked=sqrt(kx.^2 + ky.^2);
# #display the images.
imtool(k,[]);
# #display the edge detection along x-axis.
imtool(abs(kx), []);
# #display the edge detection along y-axis.
imtool(abs(ky),[]);
# #display the full edge detection.
imtool(abs(ked),[]);


# # MATLAB code for prewitt
# # operator edge detection
k=imread("logo.png");
k=rgb2gray(k);
k1=double(k);
p_msk=[-1 0 1; -1 0 1; -1 0 1];
kx=conv2(k1, p_msk, 'same');
ky=conv2(k1, p_msk', 'same');
ked=sqrt(kx.^2 + ky.^2);
imtool(k,[]);
imtool(abs(kx), []);
imtool(abs(ky),[]);

# display the images.

# display the edge detection along x-axis.
imtool(abs(ked),[]);

# display the edge detection along y-axis.

# display the full edge detection.

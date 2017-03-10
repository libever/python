import PIL.Image  
imgNames = [((72,72),"icon-72.png"),((40,40),"icon-40.png"),((80,80),"icon-40@2x.png"),((50,50),"icon-50.png"),((100,100),"icon-50@2x.png"),((60,60),"icon-60.png"),((120,120),"icon-60@2x.png"),((180,180),"icon-60@3x.png"),((72,72),"icon-72.png"),((114,114),"icon-72@2x.png"),((152,152),"icon-76@2x.png"),((76,76),"icon-76.png"),((58,58),"icon-small@2x.png"),((29,29),"icon-small.png"),((57,57),"icon.png"),((114,114),"icon@2x.png")]  
  
im = PIL.Image.open("1024.png")  
i = 0  
for i in range(len(imgNames)):  
    imt = im  
    size = imgNames[i][0]   
    #print size  
    name = imgNames[i][1]  
    #print name+type(name)  
    imt_r = imt.resize(size,PIL.Image.LANCZOS)  
    imt_r.save(name)  
    i = i+1  


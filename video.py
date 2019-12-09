import pafy

#enter the url of the video you want to download
url="https://www.youtube.com/watch?v=ozTvBsrf1as"    # link of video url you want to download
video=pafy.new(url)


##to see the list of available streams for a video
streams=video.streams
for s in streams:
    print(s)
##To see all the formats
for s in streams:
    print(s.resolution,s.extension, s.get_filesize(), s.url)

##get best resolution of the video
best=video.getbest()
print(best.resolution,best.extension)

###best resolution in required format[give your req format in "preftype"]
best = video.getbest(preftype="mp4")
print(best.resolution, best.extension)

#get url for download
print(best.url)
#download video
#best.download(quiet=False) #this will download directly 
#if you want to specify a particular path for the video
filename = best.download(filepath="/home/diwas/Desktop/")     # change the location as per your need . 


## credit :- aihubprojects.com


import pafy

#enter the url of the video you want to download
url="https://www.youtube.com/watch?v=ozTvBsrf1as"    # link of video url you want to download
video=pafy.new(url)

##get best resolution of the video
best=video.getbest()

###best resolution in required format[give your req format in "preftype"]
best = video.getbest(preftype="mp4")


#if you want to specify a particular path for the video
filename = best.download(filepath="/home/diwas/Desktop/")     # change the location as per your need . 


## credit :- aihubprojects.com

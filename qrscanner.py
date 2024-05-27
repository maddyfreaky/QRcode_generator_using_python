import qrcode

link=input("Enter a value or link:")
savename=input("Enter a name for the file to be saved:")
save_it= savename+".png"

myqr= qrcode.make(link)
myqr.save(save_it)
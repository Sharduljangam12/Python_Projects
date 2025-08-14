#This is the project in which whenyou give an emoji it will tell what that emoji is for
import emoji

giv_txt=input("Enter your string with emoji: ")

t_txt=emoji.demojize(giv_txt)


print(t_txt)

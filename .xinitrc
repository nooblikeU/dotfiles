#!/bin/sh

#userresources=$HOME/.Xresources
#usermodmap=$HOME/.Xmodmap
#sysresources=/etc/X11/xinit/.Xresources
#sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

#if [ -f $sysresources ]; then







 #   xrdb -merge $sysresources

#fi

#if [ -f $sysmodmap ]; then
 #   xmodmap $sysmodmap
#fi

#if [ -f "$userresources" ]; then







#    xrdb -merge "$userresources"

#fi

#if [ -f "$usermodmap" ]; then
#   xmodmap "$usermodmap"
#fi

# start some nice programs

#if [ -d /etc/X11/xinit/xinitrc.d ] ; then
# for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
#  [ -x "$f" ] && . "$f"
# done
# unset f
#fi


#monitor
xrandr --output DP-2 --mode 1920x1080 --rate 144 --output HDMI-0 --off

#dwmblocks
dwmblocks &

#Reload preview color scheme settings
wal -R

xrdb -merge ~/.xinitrc


#Reload wallpaper
img=$(cat /home/john/.cache/wal/wal)
xwallpaper --zoom $img

#Load compositor
xcompmgr &

#Load sxhkd
sxhkd &

#Notification
dunst &

#loop dwm

#while true;do
#	dwm >/dev/null 2>&1
#done

#Execte dwm
exec dwm

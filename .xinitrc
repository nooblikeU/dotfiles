#!/bin/sh

#.xprofile
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

#fcitx
fcitx -d &

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

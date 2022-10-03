#!/bin/sh

#.xprofile
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

#fcitx
fcitx -d &

#monitor
nvidia-settings --assign CurrentMetaMode="DP-4: nvidia-auto-select +0+0 {ForceCompositionPipeline=On}"
xrandr --output DP-4 --mode 1920x1080 --rate 144 --output HDMI-0 --off

#dwmblocks
dwmblocks &

#Reload preview color scheme settings
wal -R

#xrdb -merge ~/.xinitrc


#Reload wallpaper
img=$(cat /home/john/.cache/wal/wal)
xwallpaper --zoom $img

#Load compositor
xcompmgr &

#Load sxhkd
sxhkd &

#Notification
dunst &

#Denoise
rnnoise activate & 

#loop dwm

#while true;do
#	dwm >/dev/null 2>&1
#done

#Execte dwm
exec dwm

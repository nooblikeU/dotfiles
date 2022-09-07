#!/bin/sh

#part1
cd $HOME
mkdir .src
git clone https://github.com/nooblikeU/dotfiles.git
mv dotfiles .dotfiles
cp -r .dotfiles/. $HOME
rm -rf fonts
cd ~/.dotfiles/fonts
sudo cp "Hack Regular Nerd Font Complete.ttf" /usr/share/fonts
cd ~/.dotfiles
sudo pacman -S --needed $(comm -12 <(pacman -Slq | sort) <(sort pkglist.txt))

#part2
sudo pacman -S --needed base-devel
cd ~/.src
git clone https://aur.archlinux.org/paru.git
cd paru
chmod 777 . 
makepkg -si

#part3
cd ~/.dotfiles
paru -S --needed --noconfirm - < foreignpkglist.txt

#part4

sudo cp ~/.dotfiles/.scripts/dwmblocks_scripts/* /usr/local/sbin

cd ~/.src
git clone https://github.com/nooblikeU/dwm.git
cd dwm && sudo make clean install

cd ~/.src
git clone https://github.com/nooblikeU/dmenu.git
cd dmenu && sudo make clean install

cd ~/.src
git clone https://github.com/nooblikeU/dwmblocks.git
cd dwmblocks && sudo make clean install

#part5 
cd ~/.src
chsh -s /bin/zsh john
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
cp ~/.dotfiles/.zshrc $HOME


#part6
systemctl enable ly.service

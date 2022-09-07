#!/bin/sh

#part1
cd $HOME
mkdir .src
git clone https://github.com/nooblikeU/dotfiles.git
mv dotfiles .dotfiles
cp -r .dotfiles/. ~/$HOME
rm -rf fonts 
cd ~/.dotfiles/fonts
cp "Hack Regular Nerd Font Complete.ttf" ~/.local/share/fonts
cd ~/.dotfiles
pacman -S --needed -noconfirm $(comm -12 <(pacman -Slq | sort) <(sort pkglist.txt))

#part2
sudo pacman -S --needed --noconfirm base-devel
cd ~/.src
git clone https://aur.archlinux.org/paru.git
cd paru
chmod 777 . 
makepkg -si

#part3
cd ~/.dotfiles
paru -S --needed --noconfirm - < foreignpkglist.txt

#part4 
cd ~/.src
chsh -s /bin/zsh john
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

#part5

cp ~/.dotfiles/.scripts/dwmblocks_scripts/. /usr/local/sbin

git clone https://github.com/nooblikeU/dwm.git ~/.src
sudo make -C ~/.src/dwm clean install

git clone https://github.com/nooblikeU/dmenu.git ~/.src
sudo make -C ~/.src/dmenu clean install

git clone https://github.com/nooblikeU/dwmblocks.git ~/.src
sudo make -C ~/.src/dwmblocks clean install

#part6
systemctl enable ly.service
systemctl start ly.service

exit


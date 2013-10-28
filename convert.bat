@echo off
color 0A
title heightmap2colormap
echo Converting...
python main.py heightmap.bmp
cls
echo Done!
pause
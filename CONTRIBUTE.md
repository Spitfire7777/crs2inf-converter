# Contributing

This is a guide on contributing to this tool. If you happen to stumble with this tool, thanks for your help pointing bugs and adding features!

When I created this tool, I thought that there might be people that had the same problem: they download a RealWorld Cursor pack, but no .INF file to install, but instead a .CRS file. So this tool aims to solve that problem, which the only solution at the moment was using a deprecated program for WinXP called [Change Cursor](https://www.rw-designer.com/change-cursor) which is as old as 2006. 

## Dependencies

This tool was written in Python 3.12.10. Uses ConfigParser for dealing with the original CRS file and to write the INF file. The installing happens through windll in ctypes and the pathing is handled by path in the os library. All of these are included within the default Python installation.

Yea, this is that simple.

## New feature

If you wish to suggest a new feature, you can title it "Feature: " followed by a small paragraph of your suggestion in Issues, with the body explaining what should be added to it. I'll try to stay in contact, since I am kinda new to GitHub.

## Bugs and problems

The same happens with bugs and problems, in that case you can write it down and explain your problem with the tool.
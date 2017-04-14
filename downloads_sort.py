#!/usr/bin/env python3

# This Python script sorts files in your Downloads folder

import os

# path to your downloads folder
path = '/Users/artemio/downloads/'

# pathes to folders where you want to store some types of files
audio_path = '/Users/artemio/downloads/audio'
compressed_path = '/Users/artemio/downloads/compressed'
disk_images_path = '/Users/artemio/downloads/disk_images'
images_path = '/Users/artemio/downloads/images'
data_path = '/Users/artemio/downloads/data'
video_path = '/Users/artemio/downloads/video'
documents_path = '/Users/artemio/downloads/documents'

# you can expand this dictionary
extension_dict = {
    audio_path: [
        '.mid', '.midi', '.mp3', '.aif', '.cda', '.mpa',
        '.ogg', '.wav', '.wma', '.wpl'],
    compressed_path: [
        '.7z', '.arj', '.deb', '.pkg', '.rar',
        '.rpm', '.tar.gz', '.zip', '.z'],
    disk_images_path: ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
    images_path: [
        '.jpg', '.gif', '.png', '.jpeg', '.ai', '.bmp',
        '.ico', '.ps', '.psd', '.svg', '.tif', '.tiff'],
    data_path: [
        '.csv', '.dat', '.db', '.dbf', '.log', '.mdb',
        '.sav', '.sql', '.tar', '.xml'],
    video_path: [
        '.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
        '.mov', '.mp4', '.mpg', '.rm', '.swf', '.vob', '.wmv'],
    documents_path: [
        '.xls', '.xlm', '.xlt', '.ppt', '.pptx', '.doc',
        '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wks',
        '.wps', '.wpd']}


def detect_and_rename(extension_list, path_to_make):
    for file in os.listdir(path):
        for extension in extension_list:
            if file.lower().endswith(extension):
                if not os.path.exists(path_to_make):
                    os.mkdir(path_to_make)
                old_path = os.path.join(path, file)
                new_path = os.path.join(path_to_make, file)
                os.rename(old_path, new_path)

for key in extension_dict:
    detect_and_rename(extension_dict[key], key)

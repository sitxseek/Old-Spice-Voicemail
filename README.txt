Notes:
  - Python version: 3.5.2
  - mp3 files are downloaded to the current directory
  - command line method should be in a format like this: python3 voicemail.py -g m -n 012.345.6789 -r 23 -e 13 -o voicemailname
  - when asked for output filename, do not include '.mp3' extension
  - if you create multiple voicemails, they will all appear as separate entries in the file name list('mp3list.txt')

The approach I took in writing this voicemail program is to make the mp3 file downloading as simple as possible. I did this by parsing the user input and adding to it a ".mp3" extension so each list contained all the mp3 filenames chosen by the user. Once I gathered all the filenames, I looped through each of the lists and concatenated all the filenames into one string for each list (greetingCommand, digitCommand, reasonCommand, endingCommand). In the same loop I downloaded the mp3 files into the current directory. Combining the mp3s is easy now that I have the strings for each list since all I have to do is combine them with the command. Removing the mp3 files is simply iterating through each list and deleting any file that matches the filename in that list using the remove function from the os module.

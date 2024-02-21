# Inspect an iOS app
This set of scripts was designed to speed up basic static analysis of an iOS IPA.

#### Run

`python yd_main.py [file path]Payload`

The scripts only take an unzip Payload folder.

#### Invoke the console output
```
[-]********** script started **********[-]
[+]Version 	0-0-1
[+]Found app bundle name: myapp.app
[+]Searching plist: /Payload/myapp.app/Info.plist
.......
.....
....
```


#### Design Pattern

To make the code simple to read and maintain, I tried to only use Python's Object-Orientated features.
 
Inheritance, Overrides and Classes that encapsulated the ability to return strings, dicts and lists.

#### Future features

 - Threading
 - parse sub plists for permissions 


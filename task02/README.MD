## Summary
Python CLI directory tree synchronisation tool.  
Syncs folders (copy, update, remove) with given time interval. Works from command line

### Options:

* -s, --source TEXT             Source folder for sync  [required]
* -t, --target TEXT             Target folder for sync  [required]
* -i, --interval INTEGER RANGE  Folder sync time interval (sec). If omitted sync will run once  [x>=0]
* --help                        Show this message and exit.


### Example usages:

>This example will synchronize ***'\target_folder'*** with ***'\source_folder'*** every 10 seconds 
> 
>`>>> python folder_sync.py -s "\source_folder" -t "\target_folder" -i 10`

>Interval may be omitted, in that case sync will run once 
> 
>`>>> python folder_sync.py -s "\source_folder" -t "\target_folder"`


### Logging:  
Synchronization log will be collected in **dirsync.log** file at script directory. Log file will be created automatically.
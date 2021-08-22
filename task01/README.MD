## Summary
This is a Python CLI script for logging CPU and memory data for file and time interval specified by user.
Data will contain: CPU usage in percents, memory usage (Working  Set  and Private Bytes) in bytes 
and number of files, opened by the process.    
Script will log data with given time intervals until process is running.

### Options:

* -f, --file TEXT        File to launch. REQUIRED argument  [required]  
* -i, --interval INTEGER  Logging interval in seconds. Default: 1 sec  
* --help                  Show this message and exit.

### Example usages:

>This example will launch ***'file.exe'*** and will log its stats every 5 seconds 
> 
>`>>> python stat_logger.py -f "\path\to\the\file.exe" -i 5`

>Interval may be omitted, 1 second will be used by default 
> 
>`>>> python stat_logger.py -f "\path\to\the\file.exe"`


### Output:  
CSV file will be formed as an output at **.\log\\** folder (will be automatically created, if not existent).  
File naming convention: "log_PROCESSNAME_DATETIME_.csv"

# statcom-v1


## 1. Packages

Here's the list of package to install:

1. pyhton3-tkinter
2. python

## 2. Update TLE

Here's the instruction to update the TLE information:

- Step 1: Open a terminal Create a a file named "UpdateTLE.sh" in the "/home/statcom" directory
- Step 2: Copy in the file the code below:

```
#!/bin/sh
wget -qr www.celestrak.com/NORAD/elements/amateur.txt -O amateur.txt
wget -qr www.celestrak.com/NORAD/elements/visual.txt -O visual.txt
wget -qr www.celestrak.com/NORAD/elements/weather.txt -O weather.txt
/usr/local/bin/predict -u amateur.txt visual.txt weather.txt
```
- Step 3: Make sure the file is executable:
```
sudo chmod +x UpdateTLE.sh
```

At this point, you can simply run the script through the terminal to update the TLE manually. You can also make it so 
it updates everyday. For this feature, go to step 4.

- Step 4: Open crontab:
```
crontab -e
```

-Step 5: Insert the following line to the file:
```
0 2 * * * UpdateTLE.sh
```

Predict will now automatically update everyday at 2 AM.

## 3. Chrony

Chrony is used to maintain the system clock up-to-date for better precision  with Predict.

To install Chrony, open a terminal and type :
```
sudo apt install chrony
```

To verify the status of chrony, use:
```
sudo systemctl status chronyd
```

If chronyd is inactive, you can start it with:
```
sudo systemctl start chronyd
```

To make sure chronyd starts at boot, type:
```
sudo systemctl enable chronyd
```
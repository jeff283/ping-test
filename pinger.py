import subprocess as sp
import re
import sys
import os
import csv


def ping():
    try:
        res = str(sp.run("ping  www.google.com", shell=True, capture_output=True, text=True))
        #finds numbers between 00 and 9999
        pattern="time=[0-9]{0,9}"
        search = re.findall(pattern, res)
        time = []
        for i in search:
            i = i.replace("time=", "")
            time.append(i)
        if len(time) != 0:
            return time
        else:
            time.append(0)
            return time
    
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        return 0


def fileExist():    
    BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
    # cwd = os.getcwd()
    items = os.listdir(BASE_DIR)

    if 'pings.csv' in items:
        path = os.path.join(BASE_DIR, "pings.csv")
        os.remove(path)
    else:
        print("Creating File")


def main():
    print("Staring...")
    fileExist()
    count = 0
    fieldnames = ["count", "pings"]
    with open("pings.csv", "w") as csv_file:
        csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_write.writeheader()

    while True:
        res = ping()
        for i in res:
            with open("pings.csv", "a") as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                info = {
                    "count":count,
                    "pings":i
                }

                csv_writer.writerow(info)
                count += 1
                print("\r{}".format(i))


if __name__ == "__main__":
    main()
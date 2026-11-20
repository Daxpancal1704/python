import time
import threading
from pathlib import Path
import requests



#create Dowloded folder
DOWNLODED_DIR=Path("download")
DOWNLODED_DIR.mkdir(exist_ok=True)

def download_file(url,filename):
    print(f"Starting Downloded {filename}")

    try:
        response=requests.get(url, timeout=30)
        response.raise_for_status()

        file_path=DOWNLODED_DIR/filename

        with open(filename,"w")as file:
            file.write(response.content)


        print(f"Download Completed : {filename}")

    except requests.RequestException as e:
        print(f"Download failed {filename}-{e}")


files = [
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
     "file1.pdf"),

    ("https://www.w3.org/TR/PNG/iso_8859-1.txt",
     "file2.txt"),

    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
     "file3.pdf"),

    ("https://www.w3.org/TR/PNG/iso_8859-1.txt",
     "file4.txt"),

    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
     "file5.pdf")
]

#Start timer

start=time.perf_counter()
thread=[]

#create and start threads

for urls,filename in files:
    t=threading.Thread(target=download_file,args=(urls,filename))
    thread.append(t)
    t.start()


#wait for all threads
for t in thread:
    t.join()

end=time.perf_counter()

print(f"All downloads finished")
print(f"total time {end-start:.2f} s")
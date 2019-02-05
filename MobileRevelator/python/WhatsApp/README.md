# WhatsApp Xtract #

### Usage ###

* Install python 2.7 or python 3.5 (preferred), install PyCrypto module (3.7 alpha needed!)
* Copy needed regular files to "Report\com.whatsapp" and WhatsApp SDCard folder to "Report\WhatsApp"
* If using android, run using "python whatsapp_xtract.py", which will put the report files into the Report folder
* You may choose a different directory for output, for example "python whatsapp_xtract.py e:\wa\msgstore.db -o e:\report\Bericht"
  will export the report to e:\report folder and creates Bericht.html files. Make sure you copy then SD-Card WhatsApp folder to e:\report\WhatsApp before running the script to make video/picture/voice note links working.
* For extraction and report generation of cryptX files, just replace msgstore.db as input with msgstore.db.cryptX


### Who do I talk to? ###

* Bjoern Kerler (maintainer)
* Albert Prauser
* Rüdiger Fischaleck
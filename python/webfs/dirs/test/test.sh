#!/bin/bash
log='../log/data/req.log'
cdn='-o /dev/null -s -w %{time_total}/%{time_namelookup}/%{time_connect}/%{time_appconnect}/%{time_pretransfer}/%{time_redirect}/%{time_starttransfer}/%{size_download}/%{size_upload}/%{size_header}/%{size_request}'
host='http://localhost:8800'
index='&index=63a9f0ea7bb98050796b649e85481845'
curl $cdn $host/root/home/asura/document?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/download?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/picture?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/soft?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/document/filea?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/document/fileb?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/bin/nginx/nginx.conf?cmd=mkdir$index >> $log
echo '' >> $log
curl $cdn $host/root/bin/nginx?cmd=ls$index >> $log
echo '' >> $log
curl $cdn $host/root?cmd=ls$index >> $log
echo '' >> $log

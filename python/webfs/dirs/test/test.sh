#!/bin/bash
log='../log/data/req.log'
cdn='-o /dev/null -s -w %{time_total}/%{time_namelookup}/%{time_connect}/%{time_appconnect}/%{time_pretransfer}/%{time_redirect}/%{time_starttransfer}/%{size_download}/%{size_upload}/%{size_header}/%{size_request}'
host='http://localhost:8800'
curl $cdn $host/root/home/asura/document?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/download?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/picture?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/soft?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/document/filea?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/home/asura/document/fileb?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/bin/nginx/nginx.conf?cmd=mkdir >> $log
echo '' >> $log
curl $cdn $host/root/bin/nginx?cmd=ls >> $log
echo '' >> $log
curl $cdn $host/root?cmd=ls >> $log
echo '' >> $log

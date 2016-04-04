#!/bin/bash
kill `ps -ef| grep server | awk '{ print $2}' | sed -n '1p'`

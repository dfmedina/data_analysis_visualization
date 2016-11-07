#!/bin/bash
psql postgresql://dba:root@localhost:5432/dav << EOF          
           \x
           select * from dav.data_landing limit 2;
           EOF
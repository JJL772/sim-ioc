#!../../bin/linux-x86_64/simIOC

#- You may have to change simIOC to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/simIOC.dbd"
simIOC_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/simIOC.db","user=jeremy")


cd "${TOP}/iocBoot/${IOC}"

dbLoadRecords("records.db")

iocInit

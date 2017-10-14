#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 5"""

import csv
import urllib2
from StringIO import StringIO

class Server:
    """implements Server class,modeled as a Print Queue"""
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_time()



class Request:
    """implements Request class to represent tasks for the Server Queue"""
    def __init__(self, req_sec, proc_time):
        self.timestamp = req_sec
        self.proc_time = proc_time
    def get_stamp(self):
        return self.timestamp
    def proc_time(self):
        return self.timestamp - self.proc_time

def simulateOneServer(filein):
    """This function downloads csv file data"""
    data = urllib2.urlopen(filein)
    csvdata = data.read()
    count_rows = 0
    reader = csv.reader(StringIO(csvdata))
    waiting_times = []
    for row in reader:
        waiting_times.append(int(row[2]))
  
    addlist = sum(waiting_times)
    totalreqs = len(waiting_times)
    avg = addlist/totalreqs
    print "Average wait time was", avg, "seconds"

def simulateManyServers(filein, servers=None):

    waiting_times = []

    for row in reader:
        waiting_times.append(int(row[2]))

    addlist = sum(waiting_times)
    totalreqs = len(waiting_times)
    avg = addlist/totalreqs
    print "Average wait time was", avg, "seconds"

def main(filein):
    """process csv file and call simulateOneServer if only one server is selected, otherwise run simulateManyServers"""
        
    data = urllib2.urlopen(filein)
    csvdata = data.read()
    count_rows = 0
    reader = csv.reader(StringIO(csvdata))
    parser = argparse.ArgumentParser()

    try:
        parser.parse_args()
        simulateOneServer(filein)
    except:
        simulateManyServers(filein)

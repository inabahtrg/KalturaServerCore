###### generated by PhPy.py ######
import time
import sys

from phpLibrary import *
from simulationEngine import *
def filterBadJobs(batchJob):
    return (batchJob.getStatus() == BatchJob.BATCHJOB_STATUS_FINISHED)
    
UNLIMITED_ONLY_TOPOLOGY = {'name' : 'Unlimited linuxes',
	0 : [{'type' : 'linux', 
				'count' : 32,},],
	1 : [{'type' : 'linux', 
				'count' : 32,},],}
SIMULATIONS = ['actual', 
	{'scheduler' : {'class' : 'ExistingJobScheduler', 'name' : 'FCFS'},			'topology' : UNLIMITED_ONLY_TOPOLOGY}, 
	{'scheduler' : {'class' : 'ShorterJobsFirstScheduler', 'name' : 'SJF'},		'topology' : UNLIMITED_ONLY_TOPOLOGY},
	{'scheduler' : {'class' : 'ShorterVideosFirstScheduler', 'name' : 'SVF'},	'topology' : UNLIMITED_ONLY_TOPOLOGY}, 
	{'scheduler' : {'class' : 'RelWaitTimeScheduler', 'name' : 'RWT'},			'topology' : UNLIMITED_ONLY_TOPOLOGY},]
PARAMETERS = {'startTime' : 				time.mktime((2010, 12, 22, 0, 0, 0, 0, 0, 0)),
	'endTime' : 				time.mktime((2011, 1, 22, 0, 0, 0, 0, 0, 0)),
	'simulatedSchedulerIds' : 	[50, 60, 70, 80, 150, 160, 170, 180],
	'simulations' :			SIMULATIONS,
	'categories' :				['all', 'dc', 'duration', 'ff'],
	'filterCallback' :			filterBadJobs,
	'minDuration' :			60,
	'minProcessTime' :			60,
	'debugLogEnabled' :		False,
	'durationGroups' : 		[5,10,20,30,45,60,90],}
(vars, cats, simulations) = simulationMain(PARAMETERS)
sys.stdout.write("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
for cat in cats:
    # print column header
    sys.stdout.write("%s\t" % (cat))
    for var in vars:
        sys.stdout.write("%s\t" % (var))
        
    sys.stdout.write("\n")
    # print data
    for simulation in simulations.values():
        sys.stdout.write("%s\t" % (simulation.name))
        for var in vars:
            measures = simulation.getMeasures(cat, var)
            if (measures.has_key('average')):
                sys.stdout.write("%s\t" % (measures['average']))
                
            
        sys.stdout.write("\n")
        
    


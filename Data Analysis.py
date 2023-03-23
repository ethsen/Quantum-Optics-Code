import numpy as np
import matplotlib.pyplot as plt


def degreeOfCoherence(data):
    T = .3 #integration Time
    deltaT = 7.5 * (10**(-9)) #Time window of measurement

    gSquared = (data[2] /(data[0] * data[1])) * T/deltaT

    return gSquared

def threeDetectorDegreeOfCoherence(data):

    gSquared = ((data[0] * data[1]) /(data[2] * data[3])) 

    return gSquared


def twoDetectorAnalysis():
    darkCount = np.loadtxt('./Dark Count.txt')
    aCount = darkCount[:,0]
    bCount = darkCount[:,1]
    abCount = darkCount[:,2]

    avgA_DarkCount = (aCount.sum())/100
    avgB_DarkCount = (bCount.sum())/100
    avgAB_DarkCount = (abCount.sum())/100
    #avgAB_DarkCountUncert = (np.sqrt(abCount.sum()) / abCount.sum()) * avgAB_DarkCount

    darkCountData =[avgA_DarkCount,avgB_DarkCount,avgAB_DarkCount]

    #print(degreeOfCoherence(darkCountData))
    
    coincidenceCount_Short = np.loadtxt('./Coincidence Count - Short BNC Cable.txt')
    aCount = coincidenceCount_Short[:,0]
    bCount = coincidenceCount_Short[:,1]
    abCount = coincidenceCount_Short[:,2]

    avgA_coincidenceCount_Short = (aCount.sum())/100
    avgB_coincidenceCount_Short = (bCount.sum())/100
    avgAB_coincidenceCount_Short = (abCount.sum())/100

    coincidenceCount_Long = np.loadtxt('./Coincidence Count - 20m Cable.txt')
    aCount = coincidenceCount_Long[:,0]
    bCount = coincidenceCount_Long[:,1]
    abCount = coincidenceCount_Long[:,2]

    avgA_coincidenceCount_Long = (aCount.sum())/100
    avgB_coincidenceCount_Long = (bCount.sum())/100
    avgAB_coincidenceCount_Long = (abCount.sum())/100


    beamSplitter = np.loadtxt('./2 Detector measurement with Beam Splitter.txt')
    aCount = beamSplitter[:,0]
    bCount = beamSplitter[:,1]
    abCount = beamSplitter[:,2]

    avgB_beamSplitter = (aCount.sum())/100
    avgBprime_beamSplitter = (bCount.sum())/100
    avgBBprime_beamSplitter = (abCount.sum())/100

    beamSplitterData = [avgB_beamSplitter,avgBprime_beamSplitter,avgBBprime_beamSplitter,aCount.std(),bCount.std(),abCount.std(),0]

    beamSplitterGSquared = degreeOfCoherence(beamSplitterData)
    beamSplitterData[6] = beamSplitterGSquared
    print(beamSplitterData) 

def threeDetectorAnalysis():
    inputData = np.loadtxt('./3 Detector measurement with Beam Splitter.txt')
    aCount = inputData[:,0]
    avgACount = aCount.sum()/100

    bCount = inputData[:,1]
    avgBCount = bCount.sum()/100

    bPrimeCount = inputData[:,2]
    avgBPrimeCount = bPrimeCount.sum()/100

    aBCount = inputData[:,3]
    avgABCount = aBCount.sum()/100

    aBPrimeCount = inputData[:,4]
    avgABPrimeCount = aBPrimeCount.sum()/100

    bBPrimeCount = inputData[:,5]
    avgbBPrimeCount = bBPrimeCount.sum()/100

    abBPrimeCount = inputData[:,6]
    avgabBPrimeCount = abBPrimeCount.sum()/100

    threeDetectorData = [avgabBPrimeCount, avgACount, avgABCount, avgABPrimeCount, avgBCount,avgBPrimeCount]

    darkCountData = np.loadtxt('./Dark Count 3 detector.txt')
    threeDetectorDarkCount = darkCountData[:,2]
    
    #print("Counting error for A: " + str(aCount.std()) + " Counting error for B: " + str(bCount.std()) + " Counting error for B':  " + str(bPrimeCount.std()))
    #`print("Counting error for AB: " + str(aBCount.std()) + " Counting error for AB': " + str(aBPrimeCount.std()) + " Counting error for BB':  " + str(bBPrimeCount.std()) + " Counting error for ABB: " + str(abBPrimeCount.std()))

    print(threeDetectorData)
    print(threeDetectorDegreeOfCoherence(threeDetectorData))


    


twoDetectorAnalysis()
threeDetectorAnalysis()
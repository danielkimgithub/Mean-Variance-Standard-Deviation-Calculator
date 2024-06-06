import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    m = np.array([list])
    n = np.reshape(m,(3,3))

    # mean
    axis1mean = n.mean(axis=1).tolist()
    axis0mean = n.mean(axis=0).tolist()
    flattenedmean = m.mean()
    mean = [axis0mean, axis1mean,flattenedmean]

    # variance
    axis1var = n.var(axis=1).tolist()
    axis0var = n.var(axis=0).tolist()
    flattenedvar = m.var()
    var = [axis0var, axis1var,flattenedvar]


    # std
    axis1std = n.std(axis=1).tolist()
    axis0std = n.std(axis=0).tolist()
    flattenedstd = m.std() 
    std = [axis0std, axis1std,flattenedstd]


    # max 
    axis1max = n.max(axis=1).tolist()
    axis0max = n.max(axis=0).tolist()
    flattenedmax = m.max()
    nmax = [axis0max, axis1max,flattenedmax]


    # min
    axis1min = n.min(axis=1).tolist()
    axis0min = n.min(axis=0).tolist()
    flattenedmin = m.min()
    nmin = [axis0min, axis1min,flattenedmin]


    # sum   
    axis1sum = n.sum(axis=1).tolist()
    axis0sum = n.sum(axis=0).tolist()
    flattenedsum = m.sum()
    nsum = [axis0sum, axis1sum,flattenedsum]


    calculations = {
    'mean': mean,
    'variance': var,
    'standard deviation': std,
    'max': nmax,
    'min': nmin,
    'sum': nsum
    }

    return calculations


import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if isinstance(loc, (int, float)) == False:
        raise ValueError("needs to be an intager or float")
    
    if isinstance(scale, (int, float)) == False:
        raise ValueError("needs to be an intager or float")
    
    if isinstance(lower_bound, (int, float)) == False:
        raise ValueError("needs to be an intager or float")
    
    if isinstance(upper_bound, (int, float)) == False:
        raise ValueError("needs to be an intager or float")
    

    elif (lower_bound > upper_bound):
        raise ValueError("lower_bound needs to be smaller then upper_bound")
        
    
    samples = np.random.normal(loc=loc, scale=scale, size=100)
    mask = (samples >= lower_bound) & (samples <= upper_bound)
    samples = samples[mask]

    return (np.mean(samples), np.std(samples))


if __name__ == "__main__":
    # use this for your own testing!

    pass

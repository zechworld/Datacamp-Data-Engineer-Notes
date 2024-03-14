# Importing HDF5 Files

The `Hierarchical Data Format Version 5` or `HDF5` for short, is a type of file that is been consider as standard mechanism for `storing large quantities` of numerical data. Normal datasets deal with gigabytes or even terabytes, the HDF5 deals with up to `exabytes (one million terabytes)`.

```python
import h5py
filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5"
data = h5py.File(filename, 'r') # 'r' is to read
print(type(data))
```
Here we used the `h5py` package and the function `h5py.File()`. We specify the argument `r for read` and use the type function to make sure we are dealing with a hdf5 file.

The structure of this files comes in different HDF groups that conforms a hierchy. Lets see the LIGO's HDF5 file used to validate the `Einstein's Theory of Gravitational Waves`:

```python
# Using the data variable from before
for key in data.keys():
	print(keys)

# meta
# quality
# strain
```
Those three keys are the HDF groups. The `meta` group holds meta-data for the file, `quality` contains the data quality, and `strain` contains the data from the interferometer.

We then can enter each of this groups using a `for loop` and therefore access any of the data that is of interest. Then we can convert this keys into a NumPy array through the `np.array()` function.


```python
for key in data['meta'].keys():
	print(key)

# Description
# DescriptionURL
# Detector
# Duration
# GPSstart
# Observatory
# Type
# UTCstart

print(np.array(data['meta']['Description'])
# data in file --> b'Strain data time series from LIGO'

print(np.array(data['meta']['Detector'])
# detector used --> b'H1'
```


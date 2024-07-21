#numpy save i load
import numpy as np

arr = np.arange(10)
np.save('some array', arr)
np.load('some array.npy')
print(arr)

#wiele tablic w nieskompresowanym archiwum
np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
print(arch['b'])

#zapis tablic podatnych na kompresję
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)
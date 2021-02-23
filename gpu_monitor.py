from pynvml import *



nvmlInit()

def system_info():
    driver_version = nvmlSystemGetDriverVersion()
    print(f"Driver Version: {driver_version}")


def device_count():    
    device_count = nvmlDeviceGetCount()
    for i in range(device_count):
        handle = nvmlDeviceGetHandleByIndex(i)
        device_name = nvmlDeviceGetName(handle)
        print(f"Device {i} : {device_name}")
        info = nvmlDeviceGetUtilizationRates(handle)
        print(info.gpu)


if __name__ == '__main__':
    system_info()

    device_count()
    
    


    # nvsmi = nvidia_smi.getInstance()
    # nvsmi.DeviceQuery('memory.free, memory.total')





from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def increase_volume(step=0.1):
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + step, 1.0), None)

def decrease_volume(step=0.1):
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - step, 0.0), None)

def mute_volume():
    volume = get_volume_interface()
    volume.SetMute(1, None)

def unmute_volume():
    volume = get_volume_interface()
    volume.SetMute(0, None)

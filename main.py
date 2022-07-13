import soco
import config
import time
sonos_list = list(soco.discover())
sonos = sonos_list[0]
print(sonos_list)
if sonos.fixed_volume == True:
    print(f"Error: {sonos} has a static volume and can not be changed.")
    exit()
while True:
    volume_current = sonos.volume
    print(volume_current)
    if volume_current > config.max_volume:
        if config.volume_lowering_mode == 2:
            sonos.ramp_to_volume(config.volume_lowering_goal, ramp_type="AUTOPLAY_RAMP_TYPE")
        else:
            sonos.volume = config.volume_damping_speed
    time.sleep(config.check_interval)



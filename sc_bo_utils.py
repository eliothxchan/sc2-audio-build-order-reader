from datetime import time, timedelta
import re

def time_difference(old_time, new_time):
    old_delta = timedelta(hours=0, minutes=old_time.minute, seconds=old_time.second)
    new_delta = timedelta(hours=0, minutes=new_time.minute, seconds=new_time.second)
    return new_delta - old_delta

def generate_timer_duration(clock_timestamp):
    minute = int(clock_timestamp.split(":")[0])
    second = int(clock_timestamp.split(":")[1])
    new_time = time(minute = minute, second = second)
    # One second early as reader takes a bit of time to boot up
    old_time = time(minute = 0, second = 1) 

    return time_difference(old_time, new_time).seconds


def to_shorthand(text):
    final_text = text.lower()
    
    shorthand = {
        # Terran
        "supply depot": "depot",
        "barracks": "rax",
        "command center": "CC",
        "engineering bay": "E bay",
        "planetary fortress": "planetary",
        "missile turret": "turret",
        "siege tank": "tank",
        "widow mine": "mine",
        "orbital command": "orbital",
        "hyperflight rotors": "banshee speed",
        "rapid reignition system": "medivac speed",
        "advanced ballistics": "liberator range",
        "mag-field accelerator": "mag-field",
        "cloaking field": "banshee cloak",
        "personal cloaking": "ghost cloak",
        "weapon refit": "yamato",
        "stimpack": "stim",
        "infernal pre-igniter": "blue flame",

        
        # Zerg
        "zergling": "ling",
        "hydralisk": "hydra",
        "mutalisk": "muta",
        "baneling": "bane",
        "hatchery": "hatch",
        "spawning pool": "pool",
        "evolution chamber": "evo chamber",
        "spine crawler": "spine",
        "spore crawler": "spore",
        "glial reconstitution": "roach speed",
        "muscular augments": "hydra speed",
        "metabolic boost": "zergling speed",
        "anabolic synthesis": "ultralisk speed",
        "centrifugal hooks": "baneling speed",
        "pneumatized carapace": "overlord speed",
        "grooved spines": "hydralisk range",
        "seismic spines": "lurker range",

        # Protoss
        "photon cannon": "cannon",
        "cybernetics core": "cyber core",
        "robotics facility": "robo",
        "robotics bay": "robo bay",
        "warp prism": "prism",
        "gravitic boosters": "observer speed",
        "flux vanes": "void ray speed",
        "resonating glaives": "glaives",
        "gravitic drive": "prism speed",
        "anion pluse-crystals": "phoenix range",
        "extended thermal lance": "thermal lance",
        "psionic storm": "psi storm",
        "shadow stride": "DT blink"
    }
    
    for word in shorthand:
        if word in final_text:
            final_text = final_text.replace(word, shorthand[word])
    
    return final_text

def cleanup_row(row):
    # Remove leading and trailing spaces
    row = row.strip()

    # Replace all instances of two or more spaces with a comma
    row = re.sub(r'\s{2,}', ',', row)
    return row
from src.packages.constants.config_constants import ConfigConstants


class APIDocumentation:
    RL_DOCS: str = """ 
API Documentation 
     
The endpoint {base_uri}/command/simulate accepts command, a flank to choose, a group name, the weather year period, and strategy.

Parameter Format Required Default Description
command String Yes ATTACK Describes the main action that main unit group performs. Possible values: ATTACK
group String Yes ALPHA The name of group that is going to be used for simulation. After training, the simulation will show how this group performs attack on target, Possible values: ALPHA, DELTA, OMEGA
flank String No CENTER The path that main group try to use to find optimal way to reach the target, Possible values, CENTER, LEFT, RIGHT
weather Strig No SUMMER Season of the year that is used in simulation. SUMMER or WINTER supported. If WINTER chosen it would be considered as difficult terrain conditions that will make agent to stop at some point if the path is too long, Possible values: SUMMBER, WINTER
strategy String NO SAFE The way that main unit group will behave in respect to safeness. If chosen AGGRESSIVE, than agent will almost ignore the enemies. If SAFE then main unit group will try to ommit the enemies and try to find other safer path, Possible values: SAFE, AGGRESSIVE

    
""".format(base_uri=ConfigConstants.RL_API_URL)

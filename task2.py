good = r"""


                 \..,.-
                 .\   |         __
                 .|    .-     /  .;
           _      _|      \__/..     \
          \ ...\|   X Hamburg        :_
           |                           \
          /                            /
         -.                           |
          \  X Rheine      Berlin X    \
       __/                              |
      |                                 /
      |                                 \
     /                                   |
     \     X Cologne        Dresden  X . ,
      \                            ._-. .
     /                        __.-/
     |         X Frankfurt    \
      \                        \
       \                        \
        ...,.                    \
            /                     \.
           /                       ,.
          /                      ./
         |         Munich X     |
         \,......,__  __,  __.-. .
                    \/   -/     ..
"""
bad = r""" +------------------+
 |       ___        |
 |   _  (,~ |   _   |
 |  (____/  |____)  |
 |  |||||    |||||  |
 |  |||||    |||||  |
 |  |||||\  /|||||  |
 |  |||'//\/\\`|||  |
 |  |' m' /\ `m `|  |
 |       /||\       |
  \_              _/
    `-----92-KSR-'
 

"""
has_key = False
if has_key:
    outcome = "Click: I can get in!"
    print(good)
else:
    outcome = "Doom: I am stuck here!"
    print(bad)
print(outcome)
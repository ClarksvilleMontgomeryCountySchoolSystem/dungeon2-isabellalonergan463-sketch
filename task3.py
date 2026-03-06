good = r"""
        
              _            _.,----,
   __  _.-._ / '-.        -  ,._  \) 
  |  `-)_   '-.   \       / < _ )/" }
  /__    '-.   \   '-, ___(c-(6)=(6)
   , `'.    `._ '.  _,'   >\    "  )
   :;;,,'-._   '---' (  ( "/`. -='/
  ;:;;:;;,  '..__    ,`-.`)'- '--'
  ;';:;;;;;'-._ /'._|   Y/   _/' \
        '''"._ F    |  _/ _.'._   `\
               L    \   \/     '._  \
        .-,-,_ |     `.  `'---,  \_ _|
        //    'L    /  \,   ("--',=`)7
       | `._       : _,  \  /'`-._L,_'-._
       '--' '-.\__/ _L   .`'         './/
                   [ (  /
                    ) `{
         snd        \__)
"""
bad = r"""
                                _
                           /b_,dM\__,_
                         _/MMMMMMMMMMMm,
                        _YMMMMMMMMMMMM(
                       `MMMMMM/   /   \   _   ,    
                        MMM|  __  / __/  ( |_|
                        YMM/_/# \__/# \    | |_)arry
                        (.   \__/  \__/     ___  
                          )       _,  |    '_|_)
                     _____/\     _   /       | otter
                         \  `._____,'
                          `..___(__
                                   ``-.
                                       \
                                   gnv  )
"""
guard_awake = True
if not guard_awake:
    outcome = "Shadow: I can pass freely!"
    print(good)
else:
    outcome = "Doom: Oh no! What do I do?"
    print(bad)
print(outcome)
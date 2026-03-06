good = r"""                    .. - ----.                                  
                     I'__. ..- '';                                 
                     |           .                                 
                     J.                                            
                      L:..._.- -' .                                
                      |.                                           
                      J:.                                          
                       L::. ..- -' .                               
                       |.                                          
                       J::.                                        
                        LP::_..- -' .                              
                        |:.                                        
       ________________ J88:.         ______________a:f____        
             a88888baaa. LPP::..- -' .                             
               `"88888888|88:.       .                             
                   `"8888:8888:.    _J                             
                        " `""PPPPP""'                        
"""
bad = r""" tower of Pisa.
                          |         
       +                _./_         
 __:_._|               | .  |        
      / \             | . . ;        
 ____/   \          |---...__        
     |   |          "---...__|       
     |   |         :  | | |  ;       
     |   |         :        "        
 ____|   |         "---...__;        
    /     \       :  | | |  ;        
 __/       \      : | | |  "         
   |   |   |      "---...__;         
   |   |   |     :  | | |  ;         
   |   |   |     : | | |  "          
   |   |   |     "---...__;          
   | 8 | 8 |    :  | | |  ;          
___|_8_|_8_|____:_|#|#|#|_;lka____   
"""
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: I can pass by!"
    print(good)
else:
    outcome = "Doom: What am I supposed to do?"
    print(bad)
print(outcome)
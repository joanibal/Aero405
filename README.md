                                                        
     MMMMMMMMMMMMM                            MMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMM                        MMMMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMMMM                    MMMMMMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMMMMMM                MMMMMMMMMMMMMMMMMMMM  
        MMMMMMMMMMMMMMMMMMM            MMMMMMMMMMMMMMMMMM     
        MMMMMMMMMMMMMMMMMMMMM        MMMMMMMMMMMMMMMMMMMM     
        MMMMMMMMMMMMMMMMMMMMMMM    MMMMMMMMMMMMMMMMMMMMMM      
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     
        MMMMMMMMM   MMMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMM     
        MMMMMMMMM     MMMMMMMMMMMMMMMMMMMMM     MMMMMMMMM     
        MMMMMMMMM       MMMMMMMMMMMMMMMMM       MMMMMMMMM     
        MMMMMMMMM         MMMMMMMMMMMMM         MMMMMMMMM     
        MMMMMMMMM           MMMMMMMMM           MMMMMMMMM     
        MMMMMMMMM             MMMMM             MMMMMMMMM     
     MMMMMMMMMMMMMMM            M            MMMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMM                         MMMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMM                         MMMMMMMMMMMMMMM  
     MMMMMMMMMMMMMMM                         MMMMMMMMMMMMMMM  



# AEROSPACE 405 code
the code in this repository is used to process the data for our 405 poject, a blown wing surface.

# Authors 
Matt Gilbert   
Kathryn Wallace   
Becky Hill  
Josh Anibal   

# How to use the code

Everything must be called from the Aero405 file level

for example 
$ python ./Sizing/sizing.py

If you add another directory, you will need to include a __init__.py file 
to import from the folder


# In order to prevent bugs...
-  if you add anything to this file not in imperial, you are a bad person and karma will get you.
-  if you do add something in SI add a _[units] at the end. Again SI is frowned upon.
-  use pot_hole for variables, camelCase for functions and files, and  all folders are capitalized CamelCase
-  every thing should have a descriptive name, i.e Mach instead of M, nun_passengers instead of num_pass
-  Don't name a variable according to a letter typically used to represent to b =/= span, lambda =/= taper
-  if you are creating a lot of related variables ( weight_wing, weight_landing_gear, weight_mis) use a dictionary instead
-  try not to use the j481 properties module in the lower level functions 
-  Copying and Pasting is the source of all evil -> try to write general non repetitive code 


'''
Template for the wrapper plugin.
See standard Python documentation for the Template module. Briefly: $placeholder
No copyright or license for the wrapper plugin.

!!! Note the indentation in the template must meet Python requirements.
Some indentation is generated.
'''

# TODO in the summary
# TODO The shortcut requires ephemeral zed when it runs.
# TODO The shortcut replaced an existing shortcut.
# TODO The wrapper plugin is for images of modes: $wrappingimagetype.


from string import Template

wrappingtemplate = Template(
r'''#!/usr/bin/env python

# This plugin was created by the GIMP plugin "GimpScripter..." i.e. plugin-gimpscripter.py
# This *wrapper* plugin calls one or more *wrapped* or *target* plugins or PDB procedures.
# Below, "# <=" indicates lines that had substitutions by GimpScripter


$wrappingruntimelibrary

def plugin_main($wrappingmainformalparams): # <= formal parameters
  # Call the wrapped procedures.
  # If the wrapped procedure requires (image, drawable), they are passed through.
  # Any other non-constant arguments have names which match formal parameters to plugin_main above 
  # and paramdefs in register() below: they are deferred and a Gimp dialog will ask user for values.
$prelude # <= prelude
  #
$wrappingmainbody # <= body
  #
$postlude # <= postlude

  
if __name__ == "__main__": # invoked at top level, from GIMP

  from gimpfu import *  
  
  gettext.install("gimp20-python", gimp.locale_directory, unicode=True)
  
  register(
    "$wrappingprocedurename",  # <= procedure name
    "$wrappingblurb", # <= blurb
    "This plugin was created using 'GimpScripter...'",
    "Anonymous",
    "Uncopyrighted",
    "No copyright date",
    "$wrappinglabel",  # <= menu item
    "$wrappingimagetype",  # <= image type
    [$wrappingparameterdefs], # <= hidden and deferred parameters
    [],
    plugin_main,
    $wrappingmenuarg, # <= menu path
    domain=("gimp20-python", gimp.locale_directory))
 
    
  main()
'''
)


'''
Template for the summary.
'''
summarytemplate = Template(
r'''
  Created wrapper plugin $wrappingmenupath.
  
  Its description is: $wrappingblurb
  
  The wrapper plugin requires an image of any mode to be open.
  
  To change the wrapper plugin later, create a wrapper plugin with the same name.
  
  To remove the wrapper plugin, delete the file: $filepath. To distribute the wrapper plugin, distribute the same file.
  
  The wrapper plugin will not appear in Gimp menus until you restart Gimp.
'''
)









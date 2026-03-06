good = r"""      ,-----------.
    |    R.I.P.   |
    | Elvis Aaron | ,*
   .|,  Presley  \|/, 
"""
bad = r""" |      ,sss.
| | |    $^,^$
|_|_|   _/$$$\_
  |   /'  ?$?  `.
  ;,-' /\ ,, /. |
  '-./' ;    ;: |
  |     |`  '|`,;
~~~~~~~~~~~~~~~~~~~~
"""
escaped = True
if escaped:
    outcome = "Legend: I am so skilled"
    print(good)
else:
    outcome = "Doom: I can't leave!"
    print(bad)
print(outcome)
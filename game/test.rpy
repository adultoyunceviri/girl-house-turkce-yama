label testing_and_debugging_hand_function(sprite, pose):
    python:
        if len(pose):
            renpy.show('%s %s'%(sprite,pose))
        else:
            renpy.show('%s'%(sprite))
        narrator('show %s %s'%(sprite,pose))

        hand(sprite.split()[0])
        narrator('hand("%s")'%(sprite.split()[0]))
    return

label testing_and_debugging:












































































































    call language_chooser
    show screen debug_mute


    $ credits = 5000
    $ hero_smartphone = True
    $ dhl.jump('dhl_hero_room')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

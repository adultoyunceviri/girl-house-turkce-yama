
init -100000:
    $ Extra = [False,]
    $ Extra = [True,]

    define Razrab = False


    $ version = '1.1.01'

    $ RazNum = 0

init -1:
    if Razrab:
        $ RazNum = 100
        define config.developer = True
    else:
        define config.developer = False


    $ extra_word = 'ExtraContent' if Extra[0] else ''



    if persistent.sprite_animation == None:
        $ persistent.sprite_animation = True

    if Razrab:
        default preferences.skip_unseen = True


init:
    define config.window_show_transition = { "screens" : Dissolve(.25) }
    define config.window_hide_transition = { "screens" : Dissolve(.25) }
    define config.say_attribute_transition = { "master" : Dissolve(.25) }

    define config.name = _("GirlHouse")


    define config.layers = ['master', 'transient', 'screens', 'over_screens', 'overlay']

    define gui.show_name = True


    if Extra[0]:
        define config.version = "{}.extra".format(version)
    else:
        define config.version = "{}".format(version)




    define gui.about = _p("""
    """)









    define build.name = "GirlHouse"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "sound/music/SeriousDocumentaryc.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 20





default preferences.afm_time = 15
















define config.save_directory = "GirlHouse2"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.rar', None)
    build.classify('**.zip', None)
    build.classify('**.cmd', None)
    build.classify('**.old', None)
    build.classify('**.py', None)
    build.classify('log*.txt', None)
    build.classify('game/!function/**.rpy', None)
    build.classify('game/ascript/**.rpy', None)
    build.classify('game/*.rpy', None)

    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/cache/**', None)
    build.classify('game/saves/**', None)
    build.classify('_trash_/**', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.jpg', 'archive')

    if Extra[0]:
        build.classify('**/extra/*', 'archive')
    else:
        build.classify('**/extra/*', None)




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

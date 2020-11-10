init:
    define config.default_voice_volume = 0.0
    define show_quick_menu = False
    define config.hard_rollback_limit = 100

    $ menu_horizont = False


translate korean python:
    style.default.font = "fonts/NanumBarunGothic.ttf"
    gui.text_font = "fonts/NanumBarunGothic.ttf"
    gui.name_text_font = "fonts/NanumBarunGothic.ttf"
    gui.interface_text_font = "fonts/NanumBarunGothic.ttf"
    gui.choice_button_text_font = "fonts/NanumBarunGothic.ttf"
    gui.button_text_font = "fonts/NanumBarunGothic.ttf"

translate Chinese python:
    style.default.font = "fonts/msyh.ttf"
    gui.text_font = "fonts/msyh.ttf"
    gui.name_text_font = "fonts/msyh.ttf"
    gui.interface_text_font = "fonts/msyh.ttf"
    gui.choice_button_text_font = "fonts/msyh.ttf"
    gui.button_text_font = "fonts/msyh.ttf"
    gui.button_text_font = "fonts/msyh.ttf"
    gui.button_text_font = "fonts/msyh.ttf"
    gui.choice_button_text_font = "fonts/msyh.ttf"
    gui.choice_button_text_font = "fonts/msyh.ttf"

init python:
    config.has_quicksave = False
    config.has_autosave = False

transform main_menu_moveinleft:
    xalign -.2
    easein .5 xalign .1

style main_menu_textStyle:
    font "fonts/crashctt.ttf"
    size 120
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
    idle_color "#FFF"
    hover_color "#d33502"

style patreon_menu_textStyle:
    font "fonts/crashctt.ttf"
    size 120
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
    idle_color "#f96854"
    hover_color "#d33502"




screen main_menu():
    tag menu

    vbox:
        at main_menu_moveinleft
        align (.01,.5)
        spacing 10
        textbutton _("NEW GAME") action Start(label=u'start'), Hide("main_menu") text_style 'main_menu_textStyle'
        textbutton _("LOAD") action ShowMenu("load") text_style 'main_menu_textStyle'

        textbutton _("GALLERY") text_idle_color "#ffce38" text_hover_color "#d33502" text_font "fonts/crashctt.ttf" text_size 120 action ShowMenu("gallery")
        textbutton _("OPTIONS") action ShowMenu("preferences") text_style 'main_menu_textStyle'
        textbutton _("PATREON") action OpenURL("https://www.patreon.com/astaros3d") text_style 'patreon_menu_textStyle'
        textbutton _("QUIT") action Quit(confirm=False) text_style 'main_menu_textStyle'



label splashscreen3:


    python:

        if not persistent.set_volumes:
            persistent.set_volumes = True
            
            _preferences.volumes['music'] = .50

    scene menu_warning with Fade(0,1,3)
    $ menu_pos(.5)

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        call language_chooser

    if persistent.difficulty == None:
        call difficulty_chooser

    scene astaros with Fade(.5,0,3)
    $ renpy.pause(.5, hard=True)
    return

label language_chooser:
    scene black with dissolve
    $ menu_pos(.5,.5)

    menu:
        "English":
            $ renpy.run(Language(None))
        "Türkçe":
            $ renpy.run(Language('turkish'))

























    return


label difficulty_chooser:
    scene black with dissolve
    $ menu_pos(.5,.5)
    menu:
        "Choose the difficulty of the mini-games:"
        "Normal":
            $ persistent.difficulty = 'normal'
        "Hard":

            $ persistent.difficulty = 'hard'


    return



label main_menu:




    $ renpy.music.set_volume(1.0, channel='music')
    show curbg with dissolve:
        yanchor 0
        ypos 0
    $ renpy.pause(.5)
    play sound s_intro

    show logo with Dissolve(.5):
        align (.5,.5)
    show curbg:
        yanchor 0
        ease 1.8 ypos -1080

    $ renpy.pause(2, hard = True)
    show logo:
        linear .7 align (.99,.99) zoom 0.8

    show menu_portret with Dissolve(2.0)

    show snow with dissolve
    show screen patreon_button
    show text "Versiyon: 1.1.01 - Ekstra İçerik":
        alpha 0.5
        align (0.01,0.99)
    with dissolve
    $ renpy.pause(1, hard = True)

    show screen main_menu
    call screen main_menu
    return

label start:
    stop music fadeout 1.0
    window auto
    call initial







    $ pda.setup_localised_app_names()

    jump ep1


    return



label after_load:
    if not Razrab:
        $ config.developer = False

    if config.developer:
        show screen debug_mute
        $ config.console = True

    if persistent.difficulty == None:
        $ persistent.difficulty = 'normal'

    python:
        if not hasattr(store,'Nmlf'):
            Nmlf = Girls('Nmlf', nmlf)

        if not Nmlf in GIRLS:
            GIRLS.append(Nmlf)

        if not hasattr(store,'Adv'):
            Adv = Girls('Adv', adv)

        if not Adv in GIRLS:
            GIRLS.append(Adv)

        if not hasattr(date,'week_day_index'): 
            setattr(date,'week_day_index',0)
            setattr(date,'week_day_names',['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])

        if not hasattr(dhl,'location'): 
            setattr(dhl,'location','mlf_house')

        inventory.reload_item_data()
        quests.reload()
        dhl.reload(date.weekday)
        dhl.reload_additional_character('neighbor','nmlf')
        pda_shop_refresh()
        pda_bio_setup()

        phrasing_engine = Phrase()

        if not hasattr(pda,'gallery'): setattr(pda,'gallery',[])
        if not hasattr(pda,'media'):setattr(pda,'media',dict(photo={},video={}))
        if 'video' not in pda.apps_list: pda.apps_list.append('video')
        if 'photo' not in pda.apps_list: pda.apps_list.append('photo')
        if 'gallery' not in pda.apps_list: pda.apps_list.append('gallery')
        pda.setup_localised_app_names()
        pda.app_enable('gallery')
        pda.app_enable('photo')
        pda.app_enable('video')

        if not pda.messenger.has_key('nmlf'):
            pda.messenger['nmlf'] = PDA_Contact(name=Nmlf.char.name,face=pda_app_face['nmlf'],id='nmlf')
            pda.bio['nmlf'] = {}
            for cat in pda.bio_categories:
                pda.bio['nmlf'][cat] = 0

        if not pda.messenger.has_key('adv'):
            pda.messenger['adv'] = PDA_Contact(name=Adv.char.name,face=pda_app_face['adv'],id='adv')
            pda.bio['adv'] = {}
            for cat in pda.bio_categories:
                pda.bio['adv'][cat] = 0

        for char_id in pda.messenger:
            pda.messenger[char_id].name = getattr(getattr(store,char_id),'name')

        if not flags.has('event_mds_photo_help'):
            if quests['event_mds_photo_help'].complete:
                flags.set('event_mds_photo_help',date.day - 1)

        if flags.has('mlf_saw_phone') and hero_smartphone:
            if 'ols' not in pda.enabled_chars():
                pda.new_contact(['lts','mds','ols','mlf'])
                pda.app_enable('love')
                pda.app_enable('biography')

        if quests['event_doctor_come_second_time'].completed and quests['events_kitchen_mlf_phone'].inactive:
            if flags.value('doc_come2_milf_talk_kitchen') == 0:
                flags.set('doc_come2_milf_talk_kitchen',date.day)

        if Mlf.slut > 0 and Mlf.hj:
            flags.set('mlf_anointed_dick')





















    return



label end_game:
    $ gui_off()
    play music s_Inspirational_Cinematic_Ambient fadein 1 fadeout 1
    scene black with Dissolve(2.0)
    fin "{size=60}Congratulation!{/size}\n\nYou have passed version 0.6 of the game 'Girl House'. This doesn't mean that you have seen all the content. Much depends on your choice in the game. The game is under development. Keep for updates.\n\n[cRed]Many thanks to my PATRONS![sC] Thanks to their support, I can devote all my time to creating this and other games. Thank you very much for that.\n\n[cRed]Big thanks to:[sC] Arjan Kuiper, Captain Karacho, Christian Zach, CLBullet, Jacky, JJJHOO, Kim Berge, Kuroinekota, Lone Wolf, N L P, Ron k, Scott, Steady2247, Steven McGuire, Spencer Watland,\nSutthikan Sakulrungsap, Thorgal Aegirson, Tyler Smith, Valken77,\nVitor Gonçalves, Yakidori.\n\nThank you for playing my game. Hope you enjoyed it.\n\n{space=850}{i}Astaros3d{/i}"
    ang "If you are a member of the platinum team and your name isn't here, be sure to contact Astaros."
    ang "If you like this game, support Astaros on the {a=https://www.patreon.com/astaros3d} Patreon{/a} website. You can also follow the news on {a=https://twitter.com/Astaros3d} Twitter{/a}."
    dem "To be continued..."
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

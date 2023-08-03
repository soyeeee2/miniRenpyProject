image amber_eyes_normal:
    "images/amber/a_eye1.png"
    pause 0.5
    "images/amber/a_blink.png"
    pause 0.15
    repeat
    
image amber_eyes_blank:
    "images/amber/a_eye2.png"
    pause 0.5
    "images/amber/a_blink.png"
    pause 0.15
    repeat

layeredimage amber:
    zoom 0.7
    at sprite_highlight('amber')
    always:
        "amber_base1"
    group base:
        attribute base1 default:
            "amber_base1"
        attribute base2:
            "amber_base2"
        attribute blush:
            "amber_blush"
    group eyes auto:
        attribute normal default
        attribute blank:
            "amber_eyes_blank"
    group mouth:
        attribute calm default:
            "a_calm"
        attribute happy_mouth:
            "a_happy"
    group brow:
        attribute cool_brow default:
            "a_cool"
    group outfit:
        attribute outfit1 default:
            "a_normwear"
        attribute outfit2:
            "a_uni"

image jane_eyes_normal:
    "images/jane/eye_full.png"
    pause 0.5
    "images/jane/eye_half.png"
    pause 0.15
    repeat

layeredimage jane:
    zoom 0.7
    at sprite_highlight('jane')
    always:
        "base"
    # grow blush:
    #     attribute blush default:
    #         "ex_blush"
    group eyes auto:
        attribute normal default
    group mouth:
        attribute mouth_c default:
            "mouth_c"
        attribute mouth_d:
            "mouth_d"
        attribute mouth_l:
            "mouth_l"
        attribute mouth_o:
            "mouth_o"
        attribute mouth_s:
            "mouth_s"
    group brow:
        attribute brow_down default:
            "brow_down"
        attribute brow_high:
            "brow_high"
        attribute brow_low:
            "brow_low"
        attribute brow_up:
            "brow_up"
            
define amber = Character('amber', color="#c8ffc8", callback = name_callback, cb_name="amber")
define jane = Character('jane', color="#c8ffc8", callback = name_callback, cb_name="jane")
define narrator = Character(callback = name_callback, cb_name = None)


label layeredimage_test:
    
    show amber at right
    show jane at left
    
    amber "하루만에 가능하다고?"
    
    narrator "이건 사회자여~"
    show amber happy_mouth
    show jane mouth_o
    jane "당연한거 아니냐~"

    amber "말도 안돼!"
    amber "말도 안돼!!!"
    show amber blush outfit2
    amber "말도 안돼!!!!!"
    show amber base2 outfit1
    narrator "hhh"
# # 이 파일에 게임 스크립트를 입력합니다.

# # image 문을 사용해 이미지를 정의합니다.
# # image eileen happy = "eileen_happy.png"
# # image im cat = 'images/im cat.png'

# # 게임에서 사용할 캐릭터를 정의합니다.
# define soyee = Character('쏘이', color="#c8ffc8")
# define cat = Character('아이엠', color="#bdd", image="cat")

# image side cat default = "images/cat default.png"

# transform catLeft:
#     yoffset 100
#     zoom 0.5

# init python:
#     print("안녕!")

# # 여기에서부터 게임이 시작합니다.
# label start:

#     """

#     새로운 렌파이 게임에 온 걸 환영해!

#     이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어!

#     """

#     soyee " 나는 이 이야기의 주인공 쏘이"
#     soyee " 00살이야! "

    
#     show cat default at catlLeft
    
#     # cat default "나는 아이엠"

#     return

define soyee = Character(name='쏘이', color="#c8ffc8")
define cat = Character(name='아이엠', color="#bdd", image="cat")

image side cat default = "images/cat default.png"

transform catlLeft:
    zoom 2.0
    yoffset 100
    linear 2.0 yoffset 500
    repeat

init python:
    def cursorPos(trans, st, at):
        trans.pos = renpy.get_mouse_pos()
        return None

transform followCursor:
    function cursorPos
    pause 0.01
    repeat

label start:
    scene bg stage with fade

    """

    새로운 렌파이 게임에 온 걸 환영해!

    이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어!

    """

    soyee " 나는 이 이야기의 주인공 쏘이"
    soyee " 00살이야! "

    show cat default at followCursor
    "{bt=10}{sc=5}나는 {color=#cfe}아이엠{/color}{/sc}{/bt}"

    jump layeredimage_test
    return
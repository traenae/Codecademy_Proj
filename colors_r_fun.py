class myColors:
    # color reset and new page
        c_reset = "\x1b[0m"
        new_page = "\033[2J\033[1;1H"
    # Use color reset after any non-normal color to remove specials before calling something different. Sometimes things don't clear when you call something different, so you get overlap. New page will clear screen and set cursor in upper left corner.

    #*************************************
    # normal text colors
        n_black = "\x1b[30m"
        n_red = "\x1b[31m"
        n_green = "\x1b[32m"
        n_yellow = "\x1b[33m"
        n_blue = "\x1b[34m"
        n_magenta = "\x1b[35m"
        n_cyan = "\x1b[36m"
        n_white = "\x1b[37m"
        n_violet = "\x1b[38;2;178;102;255m"
    # normal background colors
        nb_black = "\x1b[40m"
        nb_red = "\x1b[41m"
        nb_green = "\x1b[42m"
        nb_yellow = "\x1b[43m"
        nb_blue = "\x1b[44m"
        nb_magenta = "\x1b[45m"
        nb_cyan = "\x1b[46m"
        nb_white = "\x1b[47m"
    # bright text colors
        b_black = "\x1b[90m"
        b_red = "\x1b[91m"
        b_green = "\x1b[92m"
        b_yellow = "\x1b[93m"
        b_blue = "\x1b[94m"
        b_magenta = "\x1b[95m"
        b_cyan = "\x1b[96m"
        b_white = "\x1b[97m"
        b_lgreen = "\x1b[38;2;146;255;12m"
    # bright background colors
        bb_black = "\x1b[100m"
        bb_red = "\x1b[101m"
        bb_green = "\x1b[102m"
        bb_yellow = "\x1b[103m"
        bb_blue = "\x1b[104m"
        bb_magenta = "\x1b[105m"
        bb_cyan = "\x1b[106m"
        bb_white = "\x1b[107m"
    # bold normal text colors
        on_black = "\x1b[1;30m"
        on_red = "\x1b[1;31m"
        on_green = "\x1b[1;32m"
        on_yellow = "\x1b[1;33m"
        on_blue = "\x1b[1;34m"
        on_magenta = "\x1b[1;35m"
        on_cyan = "\x1b[1;36m"
        on_white = "\x1b[1;37m"
        on_violet = "\x1b[1;38;2;178;102;255m"
    # bright text colors
        ob_black = "\x1b[1;90m"
        ob_red = "\x1b[1;91m"
        ob_green = "\x1b[1;92m"
        ob_yellow = "\x1b[1;93m"
        ob_blue = "\x1b[1;94m"
        ob_magenta = "\x1b[1;95m"
        ob_cyan = "\x1b[1;96m"
        ob_white = "\x1b[1;97m"
        ob_lgreen = "\x1b[1;38;2;146;255;12m"
    # underline normal text
        un_red = "\x1b[1;4;31m"
        un_green = "\x1b[1;4;32m"
        un_yellow = "\x1b[1;4;33m"
        un_blue = "\x1b[1;4;34m"
        un_magenta = "\x1b[1;4;35m"
        un_cyan = "\x1b[1;4;36m"
        un_white = "\x1b[1;4;37m"
    # italic normal text
        in_red = "\x1b[1;3;31m"
        in_green = "\x1b[1;3;32m"
        in_yellow = "\x1b[1;3;33m"
        in_blue = "\x1b[1;3;34m"
        in_magenta = "\x1b[1;3;35m"
        in_cyan = "\x1b[1;3;36m"
        in_white = "\x1b[1;3;37m"
    # swap background color and foreground color
        sp_black = "\x1b[1;7;30m"
        sp_red = "\x1b[1;7;31m"
        sp_green = "\x1b[1;7;32m"
        sp_yellow = "\x1b[1;7;33m"
        sp_blue = "\x1b[1;7;34m"
        sp_magenta = "\x1b[1;7;35m"
        sp_cyan = "\x1b[1;7;36m"
        sp_white = "\x1b[1;7;37m"
    # crossout text
        cx_black = "\x1b[1;9;30m"
        cx_red = "\x1b[1;9;31m"
        cx_green = "\x1b[1;9;32m"
        cx_yellow = "\x1b[1;9;33m"
        cx_blue = "\x1b[1;9;34m"
        cx_magenta = "\x1b[1;9;35m"
        cx_cyan = "\x1b[1;9;36m"
        cx_white = "\x1b[1;9;37m"
    #overline text
        ov_black = "\x1b[1;53;30m"
        ov_red = "\x1b[1;53;31m"
        ov_green = "\x1b[1;53;32m"
        ov_yellow = "\x1b[1;53;33m"
        ov_blue = "\x1b[1;53;34m"
        ov_magenta = "\x1b[1;53;35m"
        ov_cyan = "\x1b[1;53;36m"
        ov_white = "\x1b[1;53;37m"
    # It blinks! Sometimes. Not all consoles will blink.
        bl_black = "\x1b[1;5;30m"
        bl_red = "\x1b[1;5;31m"
        bl_green = "\x1b[1;5;32m"
        bl_yellow = "\x1b[1;5;33m"
        bl_blue = "\x1b[1;5;34m"
        bl_magenta = "\x1b[1;5;35m"
        bl_cyan = "\x1b[1;5;36m"
        bl_white = "\x1b[1;5;37m"
    # Let's try RGB.
        
        bk_lime_green = "\033[48;2;146;255;12m"
        
#print(myColors.n_violet + "Testing colors out" + myColors.c_reset)

#print(myColors.b_lgreen + "Does RGB work?" + myColors.c_reset)

#print("{}This could be fun.{}".format(myColors.n_magenta, myColors.c_reset))

#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <string>


/* ANSI Color Codes
Black	   30    Bright Black   90
Red      31    Bright Red     91
Green    32    Bright Green   92
Yellow   33    Bright Yellow  93
Blue     34    Bright Blue    94
Magenta  35    Bright Magenta 95
Cyan     36    Bright Cyan    96
White    37    Bright White   97
*/

/* I have setup these definitions so I can easily add color to my cout statements. 

Syntax:
std::cout << n_red << "Some text here." << c_reset;

remember, things can always get complicated:

std::cout << new_page << b_white << nb_magenta << "A magenta background would be horrible I think." << c_reset << nb_white << "White background wouldn't be sickening, at least." << c_reset;
*/

#pragma region color_define
// color reset and new page
#define c_reset      "\x1b[0m"
#define new_page     "\033[2J\033[1;1H"
/* Use color reset after any non-normal color to remove specials before calling something different. Sometimes things don't clear when you call something different, so you get overlap. New page will clear screen and set cursor in upper left corner. */

//*************************************
// normal text colors
#define n_black      "\x1b[30m"
#define n_red        "\x1b[31m"
#define n_green      "\x1b[32m"
#define n_yellow     "\x1b[33m"
#define n_blue       "\x1b[34m"
#define n_magenta    "\x1b[35m"
#define n_cyan       "\x1b[36m"
#define n_white      "\x1b[37m"
// normal background colors
#define nb_black      "\x1b[40m"
#define nb_red        "\x1b[41m"
#define nb_green      "\x1b[42m"
#define nb_yellow     "\x1b[43m"
#define nb_blue       "\x1b[44m"
#define nb_magenta    "\x1b[45m"
#define nb_cyan       "\x1b[46m"
#define nb_white      "\x1b[47m"
// bright text colors
#define b_black      "\x1b[90m"
#define b_red        "\x1b[91m"
#define b_green      "\x1b[92m"
#define b_yellow     "\x1b[93m"
#define b_blue       "\x1b[94m"
#define b_magenta    "\x1b[95m"
#define b_cyan       "\x1b[96m"
#define b_white      "\x1b[97m"
// bright background colors
#define bb_black      "\x1b[100m"
#define bb_red        "\x1b[101m"
#define bb_green      "\x1b[102m"
#define bb_yellow     "\x1b[103m"
#define bb_blue       "\x1b[104m"
#define bb_magenta    "\x1b[105m"
#define bb_cyan       "\x1b[106m"
#define bb_white      "\x1b[107m"
// underline normal text
#define un_red       "\x1b[1;4;31m"
#define un_green     "\x1b[1;4;32m"
#define un_yellow    "\x1b[1;4;33m"
#define un_blue      "\x1b[1;4;34m"
#define un_magenta   "\x1b[1;4;35m"
#define un_cyan      "\x1b[1;4;36m"
#define un_white     "\x1b[1;4;37m"
// italic normal text
#define in_red       "\x1b[1;3;31m"
#define in_green     "\x1b[1;3;32m"
#define in_yellow    "\x1b[1;3;33m"
#define in_blue      "\x1b[1;3;34m"
#define in_magenta   "\x1b[1;3;35m"
#define in_cyan      "\x1b[1;3;36m"
#define in_white     "\x1b[1;3;37m"
// swap background color and foreground color
#define sp_black      "\x1b[1;7;30m"
#define sp_red        "\x1b[1;7;31m"
#define sp_green      "\x1b[1;7;32m"
#define sp_yellow     "\x1b[1;7;33m"
#define sp_blue       "\x1b[1;7;34m"
#define sp_magenta    "\x1b[1;7;35m"
#define sp_cyan       "\x1b[1;7;36m"
#define sp_white      "\x1b[1;7;37m"
// crossout text
#define cx_black      "\x1b[1;9;30m"
#define cx_red        "\x1b[1;9;31m"
#define cx_green      "\x1b[1;9;32m"
#define cx_yellow     "\x1b[1;9;33m"
#define cx_blue       "\x1b[1;9;34m"
#define cx_magenta    "\x1b[1;9;35m"
#define cx_cyan       "\x1b[1;9;36m"
#define cx_white      "\x1b[1;9;37m"
//overline text
#define ov_black      "\x1b[1;53;30m"
#define ov_red        "\x1b[1;53;31m"
#define ov_green      "\x1b[1;53;32m"
#define ov_yellow     "\x1b[1;53;33m"
#define ov_blue       "\x1b[1;53;34m"
#define ov_magenta    "\x1b[1;53;35m"
#define ov_cyan       "\x1b[1;53;36m"
#define ov_white      "\x1b[1;53;37m"
// It blinks! Sometimes. Not all consoles will blink.
#define bl_black      "\x1b[1;5;30m"
#define bl_red        "\x1b[1;5;31m"
#define bl_green      "\x1b[1;5;32m"
#define bl_yellow     "\x1b[1;5;33m"
#define bl_blue       "\x1b[1;5;34m"
#define bl_magenta    "\x1b[1;5;35m"
#define bl_cyan       "\x1b[1;5;36m"
#define bl_white      "\x1b[1;5;37m"
#pragma endregion color_define

int main() {

   //Basic setup for colored text
   std::cout << new_page << "\x1b[1;5;31m" << "\x1b[48m" << "\n\n\nThis is a test of something stupid\n\n" << c_reset;
   std::cout << "\x1b[1;6;32m" << "\x1b[40m" << "\n\n\nMore Stupidity!\n\n\n" << c_reset;
}

@echo off
echo.
mode con: cols=42 lines=15


echo.
echo    Checking for Updates...
echo.
echo.
echo.
curl -LJO -s  "https://raw.githubusercontent.com/AdityaAparadh/Calculator/master/src/update.version"

color 0F
echo ###
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                        ###
ping localhost -n 1 >nul
cls

echo ######
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                     ######
ping localhost -n 1.5 >nul
cls


echo #########
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                  #########
ping localhost -n 1 >nul
cls

echo ############
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                               ############
ping localhost -n 1.5 >nul
cls

echo ###############
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                            ###############
ping localhost -n 1 >nul
cls

echo ##################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                         ##################
ping localhost -n 1.5 >nul
cls


echo #####################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                      #####################
ping localhost -n 1 >nul
cls


echo #########################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                  #########################
ping localhost -n 1.5 >nul
cls


echo #############################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo              #############################
ping localhost -n 1 >nul
cls

echo #################################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo          #################################
ping localhost -n 1.5 >nul
cls


echo ######################################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo     ######################################
ping localhost -n 1 >nul
cls



echo #########################################
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo #########################################
ping localhost -n 1.5 >nul
cls

echo #########################################
echo.                                       ##
echo.                                       ##
echo.
echo.
echo.
echo.
echo ##
echo ##
echo #########################################
ping localhost -n 1 >nul
cls


echo #########################################
echo.                                       ##
echo.                                       ##
echo.                                       ##
echo                                        ##
echo ##
echo ##
echo ##
echo ##
echo #########################################
ping localhost -n 1.5 >nul
cls

echo #########################################
echo.                                       ##
echo.                                       ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##
echo ##
echo #########################################
ping localhost -n 1 >nul
cls

echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo #########################################
ping localhost -n 1.5 >nul

cls
echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##      ^>      CALCULATOR      ^<       ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo #########################################
ping localhost -n 2 >nul

cls
echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##       ^>     CALCULATOR     ^<        ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo #########################################
ping localhost -n 2 >nul


cls
echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##         ^>   CALCULATOR   ^<          ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo #########################################



set /p updateVersion=<update.version
set /p currentVersion=<current.version

del update.version

ping localhost -n 1 >nul

if %updateVersion% == %currentVersion% goto :uptodate

:updater
mode con: cols=42 lines=30

cls
color 6
echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##         ^>   CALCULATOR   ^<          ##
echo ##                                     ##
echo ##         Update Available:           ##
echo ##         %currentVersion% -^> %updateVersion%              ##
echo ##                                     ##
echo #########################################
echo.
echo.
echo.
echo (1)- Update Now
echo.
echo (2)- Ignore Update for now
echo.
echo,
choice /c 12 /N /M "Press your Option Key Number: "
echo.
echo.
echo.

if %errorlevel%==1 goto :update
if %errorlevel%==2 goto :ignore











:ignore
cls
echo.
echo.
echo UPDATE IGNORED
echo.
echo.
echo.

pause
exit



:update
cls
echo UPDATING
echo.
pause
exit



























:uptodate
cls
color a

echo #########################################
echo ##                                     ##
echo ##                                     ##
echo ##                                     ##
echo ##         ^>   CALCULATOR   ^<          ##
echo ##                                     ##
echo ##         Already Up to Date          ##
echo ##         Version %currentVersion%               ##
echo ##                                     ##
echo #########################################
echo.
echo.
echo.
echo.
pause
exit

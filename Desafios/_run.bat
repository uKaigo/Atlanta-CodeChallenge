@echo off
title Carregando 
chcp 65001
python --version
cls
if ERRORLEVEL 1 goto NOPY
:start 
cls
title CodeChallenge - Atlanta by Kaigo
set /p number="Digite o número do desafio (3 algarismos/000: Sair): "
if number 000 exit
cls
title CodeChallenge - Atlanta by Kaigo [Desafio#%number%]
python Desafio#%number%.py
if ERRORLEVEL 1 goto error
pause
goto start
exit
:error
cls
title CodeChallenge - Atlanta by Kaigo [ERROR]
echo Digite um número válido.
pause
goto start
:NOPY 
title CodeChallenge - Atlanta by Kaigo [ERROR]
echo "Python é necessário para prosseguir.
exit

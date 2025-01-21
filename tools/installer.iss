[Setup]
AppName=Activity Usage PM Tokoweb
AppVersion=1.0
DefaultDirName={pf}\ActivityUsagePM
DefaultGroupName=Activity Usage PM Tokoweb
OutputDir=Output
OutputBaseFilename=PMTokowebActivityUsage
SetupIconFile=..\assets\fav-1-1.ico

[Files]
Source: "..\assets\fav-1-1.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\activity-monitor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\.env"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Activity Usage PM Tokoweb"; Filename: "{app}\activity-monitor.exe"; IconFilename: "{app}\fav-1-1.ico"
Name: "{group}\Uninstall Activity Usage PM Tokoweb"; Filename: "{uninstallexe}"; IconFilename: "{app}\fav-1-1.ico"
Name: "{autodesktop}\Activity Usage PM Tokoweb"; Filename: "{app}\activity-monitor.exe"; IconFilename: "{app}\fav-1-1.ico"

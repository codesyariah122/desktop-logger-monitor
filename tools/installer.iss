[Setup]
AppName=Activity Usage PM Tokoweb
AppVersion=1.0
DefaultDirName={pf}\ActivityUsagePM
DefaultGroupName=Activity Usage PM
OutputDir=Output
OutputBaseFilename=ActivityUsageInstaller

[Files]
Source: "..\dist\activity-monitor.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Activity Usage PM"; Filename: "{app}\activity-monitor.exe"; IconFilename: "{app}\../assets/logo-master.png"
Name: "{group}\Uninstall Activity Usage PM"; Filename: "{uninstallexe}";  IconFilename: "{app}\../assets/logo-master.png"

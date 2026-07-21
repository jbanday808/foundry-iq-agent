# HUNT-003 RemcosRAT Threat Hunt

## Prompt

Create a threat hunt for possible RemcosRAT activity using the following validated indicators and behavioral artifacts.

### Threat Intelligence Indicators

SHA-256:

```text
356106324c797ba967a2a8cde2156e866fe008332046747866efa82a99e62083
```

SHA-1:

```text
7e6fc1213ce2ca016d2d577d09a0c91d9f47a533
```

MD5:

```text
4713cea293132831a83cdb6ecf9d7637
```

Domain:

```text
nameless-scene-7204.uploadeeeesclientess.workers.dev
```

URL:

```text
https://nameless-scene-7204.uploadeeeesclientess.workers.dev/9VKJ-WXKE-YYQN-63FX/img_xxdd6n.png
```

Downloaded filename:

```text
img_xxdd6n.png
```

### Behavioral Artifacts

Self-copied filename:

```text
WWIvxS4BHi.vbs
```

Self-copy path:

```text
C:\Users\Public\Downloads\WWIvxS4BHi.vbs
```

Environment variable:

```text
buckskins
```

PowerShell command:

```text
powershell.exe -NoProfile -Command "Invoke-Expression $env:buckskins"
```

VBScript objects:

```text
Scripting.FileSystemObject
Wscript.Shell
WScript.ScriptFullName
```

WMI artifacts:

```text
winmgmts:\\.\root\cimv2
Win32_ProcessStartup
Win32_Process
ShowWindow = 0
```

PowerShell and decoding artifacts:

```text
New-Object Net.WebClient
DownloadData
FromBase64String
[Array]::Reverse
CurrentDomain
GetMethod
```

Extraction markers:

```text
IN-
-in1
```

Obfuscated .NET artifacts:

```text
OtnmpxnddVnptbN.mpxnddVn
Otnmpxn
```

Custom YARA rule:

```text
RemcosRAT_Obfuscated_VBS_Loader
```

## Hunt Objective

Determine whether any device, user, process, file, or network activity in Microsoft Sentinel or Microsoft Defender XDR matches or resembles the documented RemcosRAT execution chain.

The hunt must distinguish between:

- Exact IOC matches
- Behavioral similarities
- Confirmed execution evidence
- Assumptions
- Unknowns

Do not claim compromise unless telemetry confirms malicious execution or multiple correlated signals.

## Documented Execution Chain

```text
User opens malicious VBS
        ↓
VBS copies itself to C:\Users\Public\Downloads\WWIvxS4BHi.vbs
        ↓
PowerShell code is stored in the user variable buckskins
        ↓
WMI launches hidden PowerShell
        ↓
PowerShell downloads img_xxdd6n.png
        ↓
Text is extracted between IN- and -in1
        ↓
Characters are modified and reversed
        ↓
Base64 content is decoded
        ↓
.NET assembly is loaded directly into memory
        ↓
Embedded method is invoked
```

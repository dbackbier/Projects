d = {
    "#": "=repeat_last_translation",
    "#SH": "{^}.sh",
    "#SH*": "{^}.sh",
    "#SR*ERGS": "Date: 2024-11-30\t Plugin version: 1.3.7\t",
    "#TPH*FPLT": "{;}",
    "#TPH-FPLT": "{:}",
    "#KP*PL": "{^}.xml",
    "#KP-PL": "{^}.xml",
    "#KR": "{^}.c",
    "#KRA": "{^}.ca",
    "#KRA*": "{^}.ca",
    "#KRO*PL": "{^}.com",
    "#KROPL": "{^}.com",
    "#KR*": "{^}.c",
    "#KOPL": "com",
    "#PH*FRP": "{^}.mp4",
    "#PH*PG": "{^}.mp3",
    "#PH-FRP": "{^}.mp4",
    "#P*EU": "{^}.py",
    "#PEU": "{^}.py",
    "#O*RG": "{^}.org",
    "#ORG": "{^}.org",
    "S": "is",
    "ST": "is it",
    "STKPW/TAO*EUP": "ztype",
    "STKPW/TAOEUP": "ztype",
    "STKPW/WAOEU/PWA*BG": "zwieback",
    "STKPW/WAOEU/PWABG": "zwieback",
    "STKPW/WEU/TER": "zwitter",
    "STKPW/WEU/TER/KWROPB": "zwitterion",
    "STKPW/WEURT": "zwitter",
    "STKPWHRAOEF": "disbelief",
    "STKPWHRAEU": "display",
    "STKPWHURB": "zhuzh",
    "STKPWRAOE": "disagree",
    "STKPWRAOEU/PWA*BG": "zwieback",
    "STKPWRAOEU/PWABG": "zwieback",
    "STKPWRAOEG": "disagreeing",
    "STKPWRAEF": "stenography"}
d_keys = list(d.keys())
ans = {}
for key in d_keys:
    if "/" in key:
        parts = key.split("/")
        for part in parts:
            if part.startswith("-"):
                # Only consider the length after the "-"
                length = len(part[1:])
                ans[length] = ans.get(length, 0) + 1
            elif not part.startswith("#"):
                # Include the full part if it doesn't start with "#"
                length = len(part)
                ans[length] = ans.get(length, 0) + 1
    else:
        if key.startswith("-"):
            # Only consider the length after the "-"
            length = len(key[1:])
            ans[length] = ans.get(length, 0) + 1
        elif not key.startswith("#"):
            # Include the full key if it doesn't start with "#"
            length = len(key)
            ans[length] = ans.get(length, 0) + 1
ans = dict(sorted(ans.items()))
print(ans)

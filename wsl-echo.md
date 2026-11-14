THEME="chroot/usr/share/plasma/desktoptheme/default"

python3 - <<'PY'
import gzip
import re
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path("chroot/usr/share/plasma/desktoptheme/default")

files = [
    "widgets/panel-background.svgz",
    "widgets/tooltip.svgz",
    "widgets/button.svgz",
    "widgets/background.svgz",
    "opaque/widgets/panel-background.svgz",
    "opaque/widgets/tooltip.svgz",
    "solid/widgets/panel-background.svgz",
    "solid/widgets/tooltip.svgz",
    "translucent/widgets/panel-background.svgz",
    "translucent/widgets/tooltip.svgz",
]

for relative in files:
    path = root / relative
    print(f"\n===== {relative} =====")

    try:
        content = gzip.open(path, "rt", encoding="utf-8").read()
        xml = ET.fromstring(content)

        print("VIEWBOX:", xml.attrib.get("viewBox"))
        print("ELEMENT IDS:")

        for element in xml.iter():
            element_id = element.attrib.get("id")
            if element_id:
                print(" ", element_id)

        roles = sorted(set(re.findall(
            r"ColorScheme-[A-Za-z0-9_-]+", content
        )))
        print("COLOR ROLES:", ", ".join(roles) or "None")

        print("NINE-PATCH / MARGIN MARKERS:")
        for line in content.splitlines():
            if re.search(r"(hint|margin|tile|stretch|center|border)", line, re.I):
                line = line.strip()
                if line:
    -W -f='${Package} ${Version}\n' plasma-workspace"me

===== widgets/panel-background.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  radialGradient3268-6-6
  linearGradient4945
  linearGradient1734
  linearGradient1984
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  shadow-bottomright-9
  thick-center
  thick-hint-right-margin
  thick-hint-left-margin
  thick-hint-top-margin
  thick-hint-bottom-margin
  hint-tile-center
  top
  rect4152
  path1337
  bottom
  rect4148
  path1671
  left
  rect4144
  path1785
  right
  rect4140
  path1902
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  path838
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="thick-center"
  id="thick-hint-right-margin"
  id="thick-hint-left-margin"
  id="thick-hint-top-margin"
  id="thick-hint-bottom-margin"
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str

===== widgets/tooltip.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  radialGradient3268-6-6
  linearGradient4945
  linearGradient1734
  linearGradient1984
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  shadow-bottomright-9
  hint-tile-center
  top
  rect4152
  path1337
  bottom
  rect4148
  path1671
  left
  rect4144
  path1785
  right
  rect4140
  path1902
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  path838
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str

===== widgets/button.svgz =====
VIEWBOX: 0 0 288 224
ELEMENT IDS:
  svg600
  defs354
  linearGradient6
  stop1
  stop2
  stop4
  stop6
  linearGradient10
  stop10
  stop15
  linearGradient19
  stop17
  stop19
  linearGradient2888
  stop2884
  stop2886
  linearGradient20110
  stop20100
  stop20102
  stop1754
  stop20108
  linearGradient6095
  linearGradient8469
  linearGradient11337
  radialGradient13221
  radialGradient3
  radialGradient4
  linearGradient15
  radialGradient6
  namedview352
  grid1173
  current-color-scheme
  a
  stop3
  stop5
  b
  stop3036
  stop3042
  stop3038
  c
  d
  e
  g
  rect28146
  text22
  tspan18
  tspan20
  shadow-bottomright
  shadow-bottom
  rect4
  sb
  shadow-bottomleft
  shadow-right
  rect4-6-7
  sr
  shadow-center
  shadow-left
  rect4-6
  sl
  shadow-topright
  shadow-top
  rect4-5
  st
  shadow-topleft
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  normal-center
  path72
  normal-bottom
  path84
  path86
  normal-topleft
  path3528
  path3528-2
  normal-top
  path100
  path102
  normal-right
  path116
  path118
  normal-left
  path132
  path134
  normal-hint-top-margin
  normal-hint-bottom-margin
  normal-hint-left-margin
  normal-hint-right-margin
  mask-normal-center
  hover-bottom
  path100-3-6
  path174
  hover-top
  path100-3
  path186
  hover-right
  path100-3-6-9
  path198
  hover-left
  path100-3-6-9-1
  path210
  hover-center
  hover-hint-top-margin
  hover-hint-bottom-margin
  hover-hint-right-margin
  hover-hint-left-margin
  toolbutton-hover-bottom
  path100-3-6-5-0-9
  path302
  toolbutton-hover-bottomright
  path100-3-6-5-0-5-2-9
  path308
  toolbutton-hover-right
  path100-3-6-5-0-9-3
  path314
  toolbutton-hover-bottomleft
  path100-3-6-5-0-5-2
  path344
  toolbutton-hover-left
  path100-3-6-5-0-9-3-6
  path332
  toolbutton-hover-center
  toolbutton-hover-topright
  path100-3-6-5-0-5
  path338
  toolbutton-hover-top
  path100-3-6-5-0
  path320
  toolbutton-hover-topleft
  path100-3-6-5-0-5-6
  path326
  toolbutton-hover-hint-top-margin
  toolbutton-hover-hint-bottom-margin
  toolbutton-hover-hint-right-margin
  toolbutton-hover-hint-left-margin
  toolbutton-focus-bottom
  path100-3-6-5-06
  path362
  path360
  toolbutton-focus-top
  path100-3-6-5-06-2
  path372
  path370
  toolbutton-focus-right
  path100-3-6-5-06-2-6
  path382
  path380
  toolbutton-focus-left
  path100-3-6-5-06-2-6-1
  path392
  path390
  toolbutton-focus-bottomleft
  path100-3-6-5-0-5-6-7
  path400
  path402
  toolbutton-focus-topleft
  path100-3-6-5-0-5-6-1
  path410
  path412
  toolbutton-focus-topright
  path100-3-6-5-0-5-6-7-9
  path420
  path422
  toolbutton-focus-bottomright
  path100-3-6-5-0-5-6-2
  path428
  path432
  toolbutton-focus-hint-top-margin
  toolbutton-focus-hint-bottom-margin
  toolbutton-focus-hint-left-margin
  toolbutton-focus-hint-right-margin
  toolbutton-focus-center
  focus-bottom
  path100-3-6-5-3
  path360-5
  path362-3
  focus-top
  path100-3-6-5
  path372-1
  path370-9
  focus-right
  path100-3-6-5-3-2
  path382-3
  path380-9
  focus-left
  path100-3-6-5-3-2-7
  path392-6
  path390-2
  focus-bottomleft
  path400-9
  path402-2
  focus-topleft
  path410-7
  path412-5
  focus-topright
  path420-8
  path422-9
  focus-bottomright
  path428-3
  path432-1
  focus-hint-top-margin
  focus-hint-bottom-margin
  focus-hint-left-margin
  focus-hint-right-margin
  focus-center
  toolbutton-pressed-top
  path448
  path446
  toolbutton-pressed-center
  toolbutton-pressed-bottom
  path452
  path454
  toolbutton-pressed-right
  path456
  path458
  toolbutton-pressed-left
  path460
  path462
  toolbutton-pressed-hint-top-margin
  toolbutton-pressed-hint-bottom-margin
  toolbutton-pressed-hint-left-margin
  toolbutton-pressed-hint-right-margin
  text476
  tspan474
  text480
  tspan478
  text484
  tspan482
  text488
  tspan486
  text492
  tspan490
  text496
  tspan494
  text500
  tspan498
  text504
  tspan502
  text508
  tspan506
  path510
  text514
  tspan512
  text562
  tspan1
  tspan2
  tspan3
  tspan4
  tspan5
  tspan6
  tspan7
  tspan8
  tspan9
  tspan10
  normal-hint-compose-over-border
  text570
  tspan568
  path572
  text576
  tspan574
  toolbutton-pressed-topright
  path578
  path580
  toolbutton-pressed-topleft
  path584
  path586
  toolbutton-pressed-bottomright
  path588
  path590
  toolbutton-pressed-bottomleft
  path594
  path596
  pressed-top
  path100-5
  path448-7
  path446-4
  pressed-center
  path72-3
  pc
  pressed-bottom
  path84-6
  path452-4
  path454-5
  pressed-right
  path116-3
  path456-0
  path458-3
  pressed-left
  path132-5
  path460-6
  path462-1
  pressed-hint-top-margin
  pressed-hint-bottom-margin
  pressed-hint-left-margin
  pressed-hint-right-margin
  pressed-topright
  path3528-1-6
  path578-6
  path580-1
  pressed-topleft
  path3528-7
  path584-5
  path586-5
  pressed-bottomright
  path3528-8-2
  path588-7
  path590-6
  pressed-bottomleft
  path3528-8-9-9
  path594-6
  path596-9
  hover-bottomright
  hover-bottomleft
  hover-topleft
  hover-topright
  normal-topright
  path3528-1
  path3528-2-4
  normal-bottomright
  path3528-8
  path3528-2-9
  normal-bottomleft
  path3528-8-9
  path3528-2-9-5
  mask-normal-bottom
  mask-normal-right
  mask-normal-left
  mask-normal-top
  mask-normal-topleft
  mask-normal-topright
  mask-normal-bottomright
  mask-normal-bottomleft
  path5587
  path3544
  pressed-hint-compose-over-border
COLOR ROLES: ColorScheme-ButtonBackground, ColorScheme-ButtonFocus, ColorScheme-ButtonHover, ColorScheme-ButtonText, ColorScheme-Highlight
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  inkscape:label="hint" />
  inkscape:label="hint" />
  id="shadow-center"
  inkscape:label="hint" />
  inkscape:label="hint" />
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="normal-center"
  inkscape:label="border" />
  inkscape:label="border"
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  id="normal-hint-top-margin"
  id="normal-hint-bottom-margin"
  id="normal-hint-left-margin"
  id="normal-hint-right-margin"
  id="mask-normal-center"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  id="hover-center"
  id="hover-hint-top-margin"
  id="hover-hint-bottom-margin"
  id="hover-hint-right-margin"
  id="hover-hint-left-margin"
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border"
  id="toolbutton-hover-center"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border"
  id="toolbutton-hover-hint-top-margin"
  id="toolbutton-hover-hint-bottom-margin"
  id="toolbutton-hover-hint-right-margin"
  id="toolbutton-hover-hint-left-margin"
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  id="toolbutton-focus-hint-top-margin"
  id="toolbutton-focus-hint-bottom-margin"
  id="toolbutton-focus-hint-left-margin"
  id="toolbutton-focus-hint-right-margin"
  id="toolbutton-focus-center"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border"
  inkscape:label="hint" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="hint" />
  inkscape:label="border" />
  id="focus-hint-top-margin"
  id="focus-hint-bottom-margin"
  id="focus-hint-left-margin"
  id="focus-hint-right-margin"
  id="focus-center"
  inkscape:label="border"
  id="toolbutton-pressed-center"
  inkscape:label="border"
  inkscape:label="border"
  inkscape:label="border"
  id="toolbutton-pressed-hint-top-margin"
  id="toolbutton-pressed-hint-bottom-margin"
  id="toolbutton-pressed-hint-left-margin"
  id="toolbutton-pressed-hint-right-margin"
  y="-28">margin hint</tspan></text>
  id="tspan1">NOTE: Some margin hints have 0.001 width or height because you can't use exactly 0! </tspan><tspan
  id="tspan2">NOTE: shadow, hover and focus (not focus-background) use negative margins! </tspan><tspan
  id="tspan8">We should add support for a negative margins hint to FrameSvg and document it instead of requiring people to read source </tspan><tspan
  id="normal-hint-compose-over-border"
  y="12">other hints</tspan></text>
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  id="pressed-center">
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  id="pressed-hint-top-margin"
  id="pressed-hint-bottom-margin"
  id="pressed-hint-left-margin"
  id="pressed-hint-right-margin"
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border" />
  inkscape:label="border"
  inkscape:label="border" />
  id="pressed-hint-compose-over-border"

===== widgets/background.svgz =====
VIEWBOX: None
ELEMENT IDS:
  svg3642
  base
  grid3357
  defs3644
  current-color-scheme
  linearGradient3809-7
  stop3811-0
  stop3817-7
  stop3815-7
  linearGradient3908
  linearGradient3809-3
  stop3811-1
  stop3817-3
  stop3815-2
  linearGradient3945
  linearGradient3809-4
  stop3811-5
  stop3817-6
  stop3815-73
  linearGradient3982
  linearGradient3809-8
  stop3811-4
  stop3817-2
  stop3815-20
  linearGradient4019
  linearGradient3828-6
  stop3830-5
  stop3836-0
  stop3832-2
  stop3834-3
  radialGradient4057
  linearGradient3828-0
  stop3830-7
  stop3836-9
  stop3832-0
  stop3834-0
  radialGradient4097
  linearGradient3828-4
  stop3830-4
  stop3836-3
  stop3832-8
  stop3834-9
  radialGradient4137
  linearGradient3828-2
  stop3830-75
  stop3836-31
  stop3832-9
  stop3834-7
  radialGradient4177
  linearGradient1072
  linearGradient1074
  linearGradient1076
  radialGradient1078
  radialGradient1080
  radialGradient1082
  linearGradient1084
  radialGradient1086
  metadata3647
  layer1
  hint-stretch-borders
  text4270
  tspan4272
  g3041
  top
  path2667
  path5283
  rect3800-4
  right
  path2679
  path5344
  rect3862-6
  bottom
  path2691
  path5362
  rect3880-4
  bottomleft
  path2697
  path3814
  shadow-bottomleft-9
  center
  toolbutton-pressed-center
  path11378
  topright
  path5336
  path5338
  shadow-topright-0
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  topleft
  path4234
  path4236
  shadow-topleft-2
  left
  path4246
  path4248
  rect3844-2
  bottomright
  path4279
  path3046
  shadow-bottomright-2
  hint-left-margin
  hint-right-inset
  hint-left-inset
  hint-top-inset
  hint-bottom-inset
  shadow-top
  path983
  rect987
  shadow-right
  path991
  rect995
  shadow-bottom
  path999
  rect1005
  shadow-bottomleft
  path1010
  path1014
  shadow-center
  g1020
  path1018
  shadow-topright
  path1024
  path1028
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-topleft
  path1038
  path1042
  shadow-left
  path1046
  rect1050
  shadow-bottomright
  path1054
  path1058
  shadow-hint-left-margin
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-hint-top-inset
  shadow-hint-bottom-inset
COLOR ROLES: ColorScheme-Background, ColorScheme-ButtonBackground, ColorScheme-ButtonFocus, ColorScheme-ButtonHover, ColorScheme-ButtonText, ColorScheme-Highlight, ColorScheme-Text, ColorScheme-ViewBackground, ColorScheme-ViewFocus, ColorScheme-ViewHover, ColorScheme-ViewText
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#666666"
  borderopacity="1.0"
  id="hint-stretch-borders"
  style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;line-height:0%;font-family:'Gill Sans';text-align:justify;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;str
  inkscape:transform-center-y="5"
  inkscape:transform-center-x="5"
  id="center">
  id="toolbutton-pressed-center">
  inkscape:transform-center-y="-2.5"
  inkscape:transform-center-x="2.5"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  inkscape:transform-center-x="2.4999995"
  inkscape:transform-center-y="-2.5"
  inkscape:transform-center-x="5"
  inkscape:transform-center-y="5"
  id="hint-left-margin"
  id="hint-right-inset"
  id="hint-left-inset"
  id="hint-top-inset"
  id="hint-bottom-inset"
  inkscape:transform-center-y="5"
  inkscape:transform-center-x="5"
  id="shadow-center">
  inkscape:transform-center-y="-2.5"
  inkscape:transform-center-x="2.5"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  inkscape:transform-center-x="2.4999995"
  inkscape:transform-center-y="-2.5"
  inkscape:transform-center-x="5"
  inkscape:transform-center-y="5"
  id="shadow-hint-left-margin"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"

===== opaque/widgets/panel-background.svgz =====
VIEWBOX: 0 0 173 56.000004
ELEMENT IDS:
  svg2
  defs4
  current-color-scheme
  base
  grid3336
  metadata7
  layer1
  hint-tile-center
  center
  rect4401
  rect4138
  topright
  rect4177
  path4842
  mask-top
  rect4265
  mask-topleft
  path4277
  mask-topright
  path4287
  mask-bottom
  rect4291
  mask-bottomleft
  path4303
  mask-bottomright
  path4313
  mask-left
  rect4317
  mask-right
  rect4323
  mask-center
  rect4329
  rect4331
  right
  rect4140
  rect4902-0
  top
  rect3146
  rect3148
  bottom
  rect3152
  rect3154
  left
  rect3164
  rect3166
  bottomright
  path3176
  path3178
  bottomleft
  path3182
  path3184
  topleft
  path3188
  path3190
  thick-hint-top-margin
  thick-hint-bottom-margin
  thick-hint-right-margin
  thick-hint-left-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-margin
  thick-center
COLOR ROLES: ColorScheme-Background, ColorScheme-ButtonBackground, ColorScheme-ButtonFocus, ColorScheme-ButtonHover, ColorScheme-ButtonText, ColorScheme-Highlight, ColorScheme-Text, ColorScheme-ViewBackground, ColorScheme-ViewFocus, ColorScheme-ViewHover, ColorScheme-ViewText
NINE-PATCH / MARGIN MARKERS:
  <sodipodi:namedview id="base" pagecolor="#b0dba0" bordercolor="#cc0000" borderopacity="1" inkscape:pageopacity="0" inkscape:pageshadow="2" inkscape:zoom="11.699422" inkscape:cx="32.83686" inkscape:cy="27.287711" inkscape
  <rect style="opacity:1;fill:#ff6600;fill-opacity:1;stroke:none" id="hint-tile-center" width="5" height="5" x="0" y="904.36218" />
  <g id="center">
  <g id="mask-center" transform="translate(116,0)">
  <rect style="fill:#ff00ff" id="thick-hint-top-margin" x="35" y="910.36218" width="4.0000019" height="8.0000048" />
  <rect style="fill:#ff00ff" id="thick-hint-bottom-margin" x="31" y="946.36218" width="4" height="8.0001907" />
  <rect style="fill:#ff00ff" id="thick-hint-right-margin" transform="rotate(90)" x="932.36218" y="-56.999985" width="3.9999771" height="7.9999847" />
  <rect style="fill:#ff00ff" id="thick-hint-left-margin" transform="rotate(90)" x="928.36218" y="-21" width="4.0000229" height="8.0000076" />
  <rect style="fill:#800080" id="hint-bottom-margin" x="35" y="950.36218" width="4" height="4.0002136" />
  <rect style="fill:#800080" id="hint-right-margin" transform="rotate(90)" x="928.36218" y="-56.999985" width="3.9999771" height="3.9999847" />
  <rect style="fill:#800080" id="hint-left-margin" transform="rotate(90)" x="932.36218" y="-17" width="4.0000229" height="4.0000076" />
  <rect style="fill:#800080" id="hint-top-margin" x="31" y="910.36218" width="4.0000019" height="3.9999795" />
  <rect x="1" id="thick-center" y="960.36218" width="2" height="2" />

===== opaque/widgets/tooltip.svgz =====
VIEWBOX: 0 0 173 56.000004
ELEMENT IDS:
  svg2
  defs4
  current-color-scheme
  base
  grid3336
  metadata7
  layer1
  hint-tile-center
  center
  rect4401
  rect4138
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  topright
  rect4177
  path4842
  mask-top
  rect4265
  mask-topleft
  path4277
  mask-topright
  path4287
  mask-bottom
  rect4291
  mask-bottomleft
  path4303
  mask-bottomright
  path4313
  mask-left
  rect4317
  mask-right
  rect4323
  mask-center
  rect4329
  rect4331
  right
  rect4140
  rect4902-0
  top
  rect3146
  rect3148
  bottom
  rect3152
  rect3154
  left
  rect3164
  rect3166
  bottomright
  path3176
  path3178
  bottomleft
  path3182
  path3184
  topleft
  path3188
  path3190
COLOR ROLES: ColorScheme-Background, ColorScheme-ButtonBackground, ColorScheme-ButtonFocus, ColorScheme-ButtonHover, ColorScheme-ButtonText, ColorScheme-Highlight, ColorScheme-Text, ColorScheme-ViewBackground, ColorScheme-ViewFocus, ColorScheme-ViewHover, ColorScheme-ViewText
NINE-PATCH / MARGIN MARKERS:
  <sodipodi:namedview id="base" pagecolor="#b0dba0" bordercolor="#cc0000" borderopacity="1" inkscape:pageopacity="0" inkscape:pageshadow="2" inkscape:zoom="4.1363703" inkscape:cx="186.5729" inkscape:cy="40.90524" inkscape:
  <rect style="opacity:1;fill:#ff6600;fill-opacity:1;stroke:none" id="hint-tile-center" width="5" height="5" x="0" y="904.36218" />
  <g id="center">
  <rect style="fill:#ff00ff;fill-opacity:1;stroke:none" id="hint-top-margin" width="4" height="6.0000248" x="33" y="916.36218" />
  <rect y="942.36218" x="33" height="5.9999752" width="4" id="hint-bottom-margin" style="fill:#ff00ff;fill-opacity:1;stroke:none" />
  <rect y="-51" x="930.36218" height="6.0000153" width="4" id="hint-right-margin" style="fill:#ff00ff;fill-opacity:1;stroke:none" transform="matrix(0,1,-1,0,0,0)" />
  <rect style="fill:#ff00ff;fill-opacity:1;stroke:none" id="hint-left-margin" width="4" height="6.0000038" x="930.36218" y="-25.000004" transform="matrix(0,1,-1,0,0,0)" />
  <g id="mask-center" transform="translate(116,0)">

===== solid/widgets/panel-background.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  radialGradient3268-6-6
  linearGradient4945
  linearGradient1734
  linearGradient1984
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  shadow-bottomright-9
  thick-center
  thick-hint-right-margin
  thick-hint-left-margin
  thick-hint-top-margin
  thick-hint-bottom-margin
  hint-tile-center
  top
  rect4152
  bottom
  rect4148
  left
  rect4144
  right
  rect4140
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  path838
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="thick-center"
  id="thick-hint-right-margin"
  id="thick-hint-left-margin"
  id="thick-hint-top-margin"
  id="thick-hint-bottom-margin"
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str

===== solid/widgets/tooltip.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  radialGradient3268-6-6
  linearGradient4945
  linearGradient1734
  linearGradient1984
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  shadow-bottomright-9
  hint-tile-center
  top
  rect4152
  bottom
  rect4148
  left
  rect4144
  right
  rect4140
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  path838
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str

===== translucent/widgets/panel-background.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  linearGradient1734
  linearGradient1984
  linearGradient4945
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  radialGradient3268-6-6
  hint-tile-center
  top
  rect4152
  path1337
  bottom
  rect4148
  path1671
  left
  rect4144
  path1785
  right
  rect4140
  path1902
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  path838
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomright-9
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  thick-center
  thick-hint-right-margin
  thick-hint-left-margin
  thick-hint-top-margin
  thick-hint-bottom-margin
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  id="thick-center"
  id="thick-hint-right-margin"
  id="thick-hint-left-margin"
  id="thick-hint-top-margin"
  id="thick-hint-bottom-margin"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str

===== translucent/widgets/tooltip.svgz =====
VIEWBOX: 0 0 157 64
ELEMENT IDS:
  svg2
  namedview108
  grid988
  defs15
  current-color-scheme
  shadow-side
  stop1762
  stop1760
  stop1758
  stop1756
  stop1754
  shadow-corner
  stop11958
  stop11960
  stop11962
  stop11966
  stop11968
  stop11970
  radialGradient3268-6-6
  linearGradient4945
  linearGradient1734
  linearGradient1984
  linearGradient8667
  radialGradient3268
  radialGradient3268-4
  radialGradient3268-6
  shadow-bottomright-9
  mask-top
  mask-center
  mask-bottom
  mask-left
  mask-right
  mask-topleft
  shadow-center
  rect4908
  path838
  shadow-topleft
  path95-4-2
  path2368-7-5
  shadow-top
  st
  rect1546
  shadow-bottom
  rect1546-6
  sb
  shadow-left
  sl
  rect1546-3-7
  shadow-right
  rect1546-3
  sr
  shadow-hint-top-margin
  shadow-hint-bottom-margin
  shadow-hint-right-margin
  shadow-hint-left-margin
  shadow-hint-top-inset
  shadow-hint-bottom-inset
  shadow-hint-right-inset
  shadow-hint-left-inset
  shadow-bottomright
  path95
  path2368
  shadow-bottomleft
  path95-1
  path2368-0
  shadow-topright
  path95-4
  path2368-7
  mask-topright
  mask-bottomright
  mask-bottomleft
  text1204
  tspan1202
  tspan1358
  tspan1360
  tspan1362
  tspan1364
  hint-tile-center
  top
  rect4152
  path1337
  bottom
  rect4148
  path1671
  left
  rect4144
  path1785
  right
  rect4140
  path1902
  center
  rect4138
  topleft
  path3115
  topright
  path3118
  bottomleft
  path3124
  bottomright
  path3121
  hint-top-margin
  hint-bottom-margin
  hint-right-margin
  hint-left-margin
  hint-top-inset
  hint-bottom-inset
  hint-left-inset
  hint-right-inset
COLOR ROLES: ColorScheme-Background, ColorScheme-Text
NINE-PATCH / MARGIN MARKERS:
  bordercolor="#111111"
  borderopacity="1"
  id="mask-center"
  id="shadow-center"
  id="shadow-hint-top-margin"
  id="shadow-hint-bottom-margin"
  id="shadow-hint-right-margin"
  id="shadow-hint-left-margin"
  id="shadow-hint-top-inset"
  id="shadow-hint-bottom-inset"
  id="shadow-hint-right-inset"
  id="shadow-hint-left-inset"
  style="font-stretch:condensed;font-size:1.25217px;font-family:Impact;-inkscape-font-specification:'Impact Condensed';text-align:start;text-anchor:start;fill:#ff0000;stroke:#000000;stroke-width:5.72866;stroke-linecap:roun
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.25217px;font-family:'Noto Sans';-inkscape-font-specification:'Noto Sans';text-align:start;text-anchor:start;fill:#000000;str
  id="hint-tile-center"
  id="center"
  id="hint-top-margin"
  id="hint-bottom-margin"
  id="hint-right-margin"
  id="hint-left-margin"
  id="hint-top-inset"
  id="hint-bottom-inset"
  id="hint-left-inset"
  id="hint-right-inset"

===== THEME PACKAGE VERSION =====
plasma-desktoptheme 6.3.5-1

===== INSTALLED PLASMA WORKSPACE VERSION =====
plasma-workspace 4:6.3.6-2

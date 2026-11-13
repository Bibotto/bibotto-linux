Bibotto@Bibotto:/tmp/breath-upstream-forgejo$ cd /tmp/breath-upstream-forgejo

echo "========== DUPLICATION COMMIT =========="
git show --stat 59b6057
git show --format=fuller --find-renames 59b6057 -- sddm-theme

echo
echo "========== NEXT SDDM SYNC COMMIT =========="
git show --stat 2eb6abb
git show --format=fuller 2eb6abb -- sddm-theme

echo
echo "========== CURRENT COMPONENTS FILE =========="
git log -p -5 -- sddm-theme/components

echo
echo "========== ROOT CMAKE =========="
sed -n '1,240p' CMakeLists.txt

echo
echo "========== ALL CMAKE FILES =========="
find . -name CMakeLists.txt -o -name '*.cmake' | sort
========== DUPLICATION COMMIT ==========
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 2 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), 964 bytes | 964.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
commit 59b6057a6af7f77d17b5d93ecdb4ecbeb752aa0b
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Sat Dec 4 15:37:56 2021 +0400

    [sddm-theme] Duplicate components instead of symlinking

 CMakeLists.txt                                      |   4 --
 sddm-theme/components                               |   1 -
 sddm-theme/components/ActionButton.qml              | 115 ++++++++++++++++++++++++++++++++++++++
 sddm-theme/components/Battery.qml                   |  43 +++++++++++++++
 sddm-theme/components/Clock.qml                     |  37 +++++++++++++
 sddm-theme/components/SessionManagementScreen.qml   | 109 ++++++++++++++++++++++++++++++++++++
 sddm-theme/components/UserDelegate.qml              | 180 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 sddm-theme/components/UserList.qml                  |  88 +++++++++++++++++++++++++++++
 sddm-theme/components/VirtualKeyboard.qml           |  70 +++++++++++++++++++++++
 sddm-theme/components/VirtualKeyboard_wayland.qml   |  24 ++++++++
 sddm-theme/components/WallpaperFader.qml            | 162 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 sddm-theme/components/artwork/README.txt            |   1 +
 sddm-theme/components/artwork/logout_primary.svgz   | Bin 0 -> 2514 bytes
 sddm-theme/components/artwork/restart_primary.svgz  | Bin 0 -> 1860 bytes
 sddm-theme/components/artwork/shutdown_primary.svgz | Bin 0 -> 1738 bytes
 15 files changed, 829 insertions(+), 5 deletions(-)
commit 59b6057a6af7f77d17b5d93ecdb4ecbeb752aa0b
Author:     Artem Grinev <agrinev@manjaro.org>
AuthorDate: Sat Dec 4 15:37:56 2021 +0400
Commit:     Artem Grinev <agrinev@manjaro.org>
CommitDate: Sat Dec 4 15:37:56 2021 +0400

    [sddm-theme] Duplicate components instead of symlinking

diff --git a/sddm-theme/components b/sddm-theme/components
deleted file mode 120000
index 250c60d..0000000
--- a/sddm-theme/components
+++ /dev/null
@@ -1 +0,0 @@
-/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/
\ No newline at end of file
diff --git a/sddm-theme/components/ActionButton.qml b/sddm-theme/components/ActionButton.qml
new file mode 100644
index 0000000..af278f6
--- /dev/null
+++ b/sddm-theme/components/ActionButton.qml
@@ -0,0 +1,115 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: root
+    property alias text: label.text
+    property alias iconSource: icon.source
+    property alias containsMouse: mouseArea.containsMouse
+    property alias font: label.font
+    property alias labelRendering: label.renderType
+    property alias circleOpacity: iconCircle.opacity
+    property alias circleVisiblity: iconCircle.visible
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 1
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+    signal clicked
+
+    activeFocusOnTab: true
+
+    property int iconSize: PlasmaCore.Units.gridUnit * 3
+
+    implicitWidth: Math.max(iconSize + PlasmaCore.Units.largeSpacing * 2, label.contentWidth)
+    implicitHeight: iconSize + PlasmaCore.Units.smallSpacing + label.implicitHeight
+
+    opacity: activeFocus || containsMouse ? 1 : 0.85
+    Behavior on opacity {
+        PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
+            duration: PlasmaCore.Units.longDuration
+            easing.type: Easing.InOutQuad
+        }
+    }
+
+    Rectangle {
+        id: iconCircle
+        anchors.centerIn: icon
+        width: iconSize + PlasmaCore.Units.smallSpacing
+        height: width
+        radius: width / 2
+        color: softwareRendering ?  PlasmaCore.ColorScope.backgroundColor : PlasmaCore.ColorScope.textColor
+        opacity: root.activeFocus || containsMouse ? (softwareRendering ? 0.8 : 0.15) : (softwareRendering ? 0.6 : 0)
+        Behavior on opacity {
+            PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
+                duration: PlasmaCore.Units.longDuration
+                easing.type: Easing.InOutQuad
+            }
+        }
+    }
+
+    Rectangle {
+        anchors.centerIn: iconCircle
+        width: iconCircle.width
+        height: width
+        radius: width / 2
+        scale: mouseArea.containsPress ? 1 : 0
+        color: PlasmaCore.ColorScope.textColor
+        opacity: 0.15
+        Behavior on scale {
+            PropertyAnimation {
+                duration: PlasmaCore.Units.shortDuration
+                easing.type: Easing.InOutQuart
+            }
+        }
+    }
+
+    PlasmaCore.IconItem {
+        id: icon
+        anchors {
+            top: parent.top
+            horizontalCenter: parent.horizontalCenter
+        }
+        width: iconSize
+        height: iconSize
+
+        colorGroup: PlasmaCore.ColorScope.colorGroup
+        active: mouseArea.containsMouse || root.activeFocus
+    }
+
+    PlasmaComponents3.Label {
+        id: label
+        font.pointSize: root.fontSize
+        anchors {
+            top: icon.bottom
+            topMargin: (softwareRendering ? 1.5 : 1) * PlasmaCore.Units.smallSpacing
+            left: parent.left
+            right: parent.right
+        }
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        horizontalAlignment: Text.AlignHCenter
+        verticalAlignment: Text.AlignTop
+        wrapMode: Text.WordWrap
+        font.underline: root.activeFocus
+    }
+
+    MouseArea {
+        id: mouseArea
+        hoverEnabled: true
+        onClicked: root.clicked()
+        anchors.fill: parent
+    }
+
+    Keys.onEnterPressed: clicked()
+    Keys.onReturnPressed: clicked()
+    Keys.onSpacePressed: clicked()
+
+    Accessible.onPressAction: clicked()
+    Accessible.role: Accessible.Button
+    Accessible.name: label.text
+}
diff --git a/sddm-theme/components/Battery.qml b/sddm-theme/components/Battery.qml
new file mode 100644
index 0000000..05be535
--- /dev/null
+++ b/sddm-theme/components/Battery.qml
@@ -0,0 +1,43 @@
+/*
+    SPDX-FileCopyrightText: 2016 Kai Uwe Broulik <kde@privat.broulik.de>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+import org.kde.plasma.workspace.components 2.0 as PW
+
+Row {
+    id: row
+
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize
+
+    spacing: PlasmaCore.Units.smallSpacing
+    visible: pmSource.data["Battery"]["Has Cumulative"]
+
+    PlasmaCore.DataSource {
+        id: pmSource
+        engine: "powermanagement"
+        connectedSources: ["Battery", "AC Adapter"]
+    }
+
+    PW.BatteryIcon {
+        id: battery
+        hasBattery: pmSource.data["Battery"]["Has Battery"] || false
+        percent: pmSource.data["Battery"]["Percent"] || 0
+        pluggedIn: pmSource.data["AC Adapter"] ? pmSource.data["AC Adapter"]["Plugged in"] : false
+
+        height: batteryLabel.height
+        width: height
+    }
+
+    PlasmaComponents3.Label {
+        id: batteryLabel
+        font.pointSize: row.fontSize
+        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","%1%", battery.percent)
+        Accessible.name: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Battery at %1%", battery.percent)
+    }
+}
diff --git a/sddm-theme/components/Clock.qml b/sddm-theme/components/Clock.qml
new file mode 100644
index 0000000..fbe0c7c
--- /dev/null
+++ b/sddm-theme/components/Clock.qml
@@ -0,0 +1,37 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import QtQuick.Layouts 1.1
+import QtQuick.Controls 2.5 as QQC2
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+ColumnLayout {
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+
+    QQC2.Label {
+        text: Qt.formatTime(timeSource.data["Local"]["DateTime"])
+        color: PlasmaCore.ColorScope.textColor
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        font.pointSize: 48
+        Layout.alignment: Qt.AlignHCenter
+    }
+    QQC2.Label {
+        text: Qt.formatDate(timeSource.data["Local"]["DateTime"], Qt.DefaultLocaleLongDate)
+        color: PlasmaCore.ColorScope.textColor
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        font.pointSize: 24
+        Layout.alignment: Qt.AlignHCenter
+    }
+    PlasmaCore.DataSource {
+        id: timeSource
+        engine: "time"
+        connectedSources: ["Local"]
+        interval: 1000
+    }
+}
diff --git a/sddm-theme/components/SessionManagementScreen.qml b/sddm-theme/components/SessionManagementScreen.qml
new file mode 100644
index 0000000..f002e51
--- /dev/null
+++ b/sddm-theme/components/SessionManagementScreen.qml
@@ -0,0 +1,109 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+
+import QtQuick.Layouts 1.1
+import QtQuick.Controls 1.1
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: root
+
+    /*
+     * Any message to be displayed to the user, visible above the text fields
+     */
+    property alias notificationMessage: notificationsLabel.text
+
+    /*
+     * A list of Items (typically ActionButtons) to be shown in a Row beneath the prompts
+     */
+    property alias actionItems: actionItemsLayout.children
+
+    /*
+     * A model with a list of users to show in the view
+     * The following roles should exist:
+     *  - name
+     *  - iconSource
+     *
+     * The following are also handled:
+     *  - vtNumber
+     *  - displayNumber
+     *  - session
+     *  - isTty
+     */
+    property alias userListModel: userListView.model
+
+    /*
+     * Self explanatory
+     */
+    property alias userListCurrentIndex: userListView.currentIndex
+    property alias userListCurrentItem: userListView.currentItem
+    property bool showUserList: true
+
+    property alias userList: userListView
+
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+
+    default property alias _children: innerLayout.children
+
+    UserList {
+        id: userListView
+        visible: showUserList && y > 0
+        anchors {
+            bottom: parent.verticalCenter
+            left: parent.left
+            right: parent.right
+        }
+        fontSize: root.fontSize
+    }
+
+    //goal is to show the prompts, in ~16 grid units high, then the action buttons
+    //but collapse the space between the prompts and actions if there's no room
+    //ui is constrained to 16 grid units wide, or the screen
+    ColumnLayout {
+        id: prompts
+        anchors.top: parent.verticalCenter
+        anchors.topMargin: PlasmaCore.Units.gridUnit * 0.5
+        anchors.left: parent.left
+        anchors.right: parent.right
+        anchors.bottom: parent.bottom
+        PlasmaComponents3.Label {
+            id: notificationsLabel
+            font.pointSize: root.fontSize
+            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
+            Layout.alignment: Qt.AlignHCenter
+            Layout.fillWidth: true
+            horizontalAlignment: Text.AlignHCenter
+            wrapMode: Text.WordWrap
+            font.italic: true
+        }
+        ColumnLayout {
+            Layout.minimumHeight: implicitHeight
+            Layout.maximumHeight: PlasmaCore.Units.gridUnit * 10
+            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
+            Layout.alignment: Qt.AlignHCenter
+            ColumnLayout {
+                id: innerLayout
+                Layout.alignment: Qt.AlignHCenter
+                Layout.fillWidth: true
+            }
+            Item {
+                Layout.fillHeight: true
+            }
+        }
+        Row { //deliberately not rowlayout as I'm not trying to resize child items
+            id: actionItemsLayout
+            spacing: PlasmaCore.Units.largeSpacing / 2
+            Layout.alignment: Qt.AlignHCenter
+        }
+        Item {
+            Layout.fillHeight: true
+        }
+    }
+}
diff --git a/sddm-theme/components/UserDelegate.qml b/sddm-theme/components/UserDelegate.qml
new file mode 100644
index 0000000..9a823a2
--- /dev/null
+++ b/sddm-theme/components/UserDelegate.qml
@@ -0,0 +1,180 @@
+/*
+    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
+    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import QtQuick.Window 2.15
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: wrapper
+
+    // If we're using software rendering, draw outlines instead of shadows
+    // See https://bugs.kde.org/show_bug.cgi?id=398317
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+
+    property bool isCurrent: true
+
+    property string name
+    property string userName
+    property string avatarPath
+    property string iconSource
+    property bool needsPassword
+    property var vtNumber
+    property bool constrainText: true
+    property alias nameFontSize: usernameDelegate.font.pointSize
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+    signal clicked()
+
+    property real faceSize: PlasmaCore.Units.gridUnit * 7
+
+    opacity: isCurrent ? 1.0 : 0.5
+
+    Behavior on opacity {
+        OpacityAnimator {
+            duration: PlasmaCore.Units.longDuration
+        }
+    }
+
+    // Draw a translucent background circle under the user picture
+    Rectangle {
+        anchors.centerIn: imageSource
+        width: imageSource.width - 2 // Subtract to prevent fringing
+        height: width
+        radius: width / 2
+
+        color: PlasmaCore.ColorScope.backgroundColor
+        opacity: 0.6
+    }
+
+    Item {
+        id: imageSource
+        anchors {
+            bottom: usernameDelegate.top
+            bottomMargin: PlasmaCore.Units.largeSpacing
+            horizontalCenter: parent.horizontalCenter
+        }
+        Behavior on width {
+            PropertyAnimation {
+                from: faceSize
+                duration: PlasmaCore.Units.longDuration;
+            }
+        }
+        width: isCurrent ? faceSize : faceSize - PlasmaCore.Units.largeSpacing
+        height: width
+
+        //Image takes priority, taking a full path to a file, if that doesn't exist we show an icon
+        Image {
+            id: face
+            source: wrapper.avatarPath
+            sourceSize: Qt.size(faceSize * Screen.devicePixelRatio, faceSize * Screen.devicePixelRatio)
+            fillMode: Image.PreserveAspectCrop
+            anchors.fill: parent
+        }
+
+        PlasmaCore.IconItem {
+            id: faceIcon
+            source: iconSource
+            visible: (face.status == Image.Error || face.status == Image.Null)
+            anchors.fill: parent
+            anchors.margins: PlasmaCore.Units.gridUnit * 0.5 // because mockup says so...
+            colorGroup: PlasmaCore.ColorScope.colorGroup
+        }
+    }
+
+    ShaderEffect {
+        anchors {
+            bottom: usernameDelegate.top
+            bottomMargin: PlasmaCore.Units.largeSpacing
+            horizontalCenter: parent.horizontalCenter
+        }
+
+        width: imageSource.width
+        height: imageSource.height
+
+        supportsAtlasTextures: true
+
+        property var source: ShaderEffectSource {
+            sourceItem: imageSource
+            // software rendering is just a fallback so we can accept not having a rounded avatar here
+            hideSource: wrapper.GraphicsInfo.api !== GraphicsInfo.Software
+            live: true // otherwise the user in focus will show a blurred avatar
+        }
+
+        property var colorBorder: PlasmaCore.ColorScope.textColor
+
+        //draw a circle with an antialiased border
+        //innerRadius = size of the inner circle with contents
+        //outerRadius = size of the border
+        //blend = area to blend between two colours
+        //all sizes are normalised so 0.5 == half the width of the texture
+
+        //if copying into another project don't forget to connect themeChanged to update()
+        //but in SDDM that's a bit pointless
+        fragmentShader: "
+                        varying highp vec2 qt_TexCoord0;
+                        uniform highp float qt_Opacity;
+                        uniform lowp sampler2D source;
+
+                        uniform lowp vec4 colorBorder;
+                        highp float blend = 0.01;
+                        highp float innerRadius = 0.47;
+                        highp float outerRadius = 0.49;
+                        lowp vec4 colorEmpty = vec4(0.0, 0.0, 0.0, 0.0);
+
+                        void main() {
+                            lowp vec4 colorSource = texture2D(source, qt_TexCoord0.st);
+
+                            highp vec2 m = qt_TexCoord0 - vec2(0.5, 0.5);
+                            highp float dist = sqrt(m.x * m.x + m.y * m.y);
+
+                            if (dist < innerRadius)
+                                gl_FragColor = colorSource;
+                            else if (dist < innerRadius + blend)
+                                gl_FragColor = mix(colorSource, colorBorder, ((dist - innerRadius) / blend));
+                            else if (dist < outerRadius)
+                                gl_FragColor = colorBorder;
+                            else if (dist < outerRadius + blend)
+                                gl_FragColor = mix(colorBorder, colorEmpty, ((dist - outerRadius) / blend));
+                            else
+                                gl_FragColor = colorEmpty ;
+
+                            gl_FragColor = gl_FragColor * qt_Opacity;
+                    }
+        "
+    }
+
+    PlasmaComponents3.Label {
+        id: usernameDelegate
+
+        // Make it bigger than other fonts to match the scale of the avatar better
+        font.pointSize: wrapper.fontSize + 4
+        anchors {
+            bottom: parent.bottom
+            horizontalCenter: parent.horizontalCenter
+        }
+        width: constrainText ? parent.width : implicitWidth
+        text: wrapper.name
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        elide: Text.ElideRight
+        horizontalAlignment: Text.AlignHCenter
+        //make an indication that this has active focus, this only happens when reached with keyboard navigation
+        font.underline: wrapper.activeFocus
+    }
+
+    MouseArea {
+        anchors.fill: parent
+        hoverEnabled: true
+
+        onClicked: wrapper.clicked();
+    }
+
+    Accessible.name: name
+    Accessible.role: Accessible.Button
+    function accessiblePressAction() { wrapper.clicked() }
+}
diff --git a/sddm-theme/components/UserList.qml b/sddm-theme/components/UserList.qml
new file mode 100644
index 0000000..49f38eb
--- /dev/null
+++ b/sddm-theme/components/UserList.qml
@@ -0,0 +1,88 @@
+/*
+    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+ListView {
+    id: view
+    readonly property string selectedUser: currentItem ? currentItem.userName : ""
+    readonly property int userItemWidth: PlasmaCore.Units.gridUnit * 8
+    readonly property int userItemHeight: PlasmaCore.Units.gridUnit * 8
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+
+    implicitHeight: userItemHeight
+
+    activeFocusOnTab : true
+
+    /*
+     * Signals that a user was explicitly selected
+     */
+    signal userSelected;
+
+    orientation: ListView.Horizontal
+    highlightRangeMode: ListView.StrictlyEnforceRange
+
+    //centre align selected item (which implicitly centre aligns the rest
+    preferredHighlightBegin: width/2 - userItemWidth/2
+    preferredHighlightEnd: preferredHighlightBegin
+
+    // Disable flicking if we only have on user (like on the lockscreen)
+    interactive: count > 1
+
+    delegate: UserDelegate {
+        avatarPath: model.icon || ""
+        iconSource: model.iconName || "user-identity"
+        fontSize: view.fontSize
+        vtNumber: model.vtNumber
+        needsPassword: model.needsPassword
+
+        name: {
+            var displayName = model.realName || model.name
+
+            if (model.vtNumber === undefined || model.vtNumber < 0) {
+                return displayName
+            }
+
+            if (!model.session) {
+                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Nobody logged in on that session", "Unused")
+            }
+
+
+            var location = ""
+            if (model.isTty) {
+                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console number", "TTY %1", model.vtNumber)
+            } else if (model.displayNumber) {
+                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console (X display number)", "on TTY %1 (Display %2)", model.vtNumber, model.displayNumber)
+            }
+
+            if (location) {
+                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Username (location)", "%1 (%2)", displayName, location)
+            }
+
+            return displayName
+        }
+
+        userName: model.name
+
+        width: userItemWidth
+        height: userItemHeight
+
+        //if we only have one delegate, we don't need to clip the text as it won't be overlapping with anything
+        constrainText: ListView.view.count > 1
+
+        isCurrent: ListView.isCurrentItem
+
+        onClicked: {
+            ListView.view.currentIndex = index;
+            ListView.view.userSelected();
+        }
+    }
+
+    Keys.onEscapePressed: view.userSelected()
+    Keys.onEnterPressed: view.userSelected()
+    Keys.onReturnPressed: view.userSelected()
+}
diff --git a/sddm-theme/components/VirtualKeyboard.qml b/sddm-theme/components/VirtualKeyboard.qml
new file mode 100644
index 0000000..503a35b
--- /dev/null
+++ b/sddm-theme/components/VirtualKeyboard.qml
@@ -0,0 +1,70 @@
+/*
+    SPDX-FileCopyrightText: 2017 Martin Gräßlin <mgraesslin@kde.org>
+
+    SPDX-License-Identifier: GPL-2.0-or-later
+*/
+
+import QtQuick 2.5
+import QtQuick.VirtualKeyboard 2.1
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+InputPanel {
+    id: inputPanel
+    property bool activated: false
+    active: activated && Qt.inputMethod.visible
+    width: parent.width
+
+    states: [
+        State {
+            name: "visible"
+            when: inputPanel.active
+            PropertyChanges {
+                target: inputPanel
+                y: inputPanel.parent.height - inputPanel.height
+                opacity: 1
+                visible: true
+            }
+        },
+        State {
+            name: "hidden"
+            when: !inputPanel.active
+            PropertyChanges {
+                target: inputPanel
+                y: inputPanel.parent.height
+                opacity: 0
+                visible:false
+            }
+        }
+    ]
+
+    transitions: [
+        Transition {
+            to: "visible"
+            ParallelAnimation {
+                YAnimator {
+                    // NOTE this is necessary as otherwise the keyboard always starts the transition with Y as 0, due to the internal reparenting happening when becomes active
+                    from: inputPanel.parent.height
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.OutQuad
+                }
+                OpacityAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.OutQuad
+                }
+            }
+        },
+        Transition {
+            to: "hidden"
+            ParallelAnimation {
+                YAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.InQuad
+                }
+                OpacityAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.InQuad
+                }
+            }
+        }
+    ]
+}
diff --git a/sddm-theme/components/VirtualKeyboard_wayland.qml b/sddm-theme/components/VirtualKeyboard_wayland.qml
new file mode 100644
index 0000000..1328ee8
--- /dev/null
+++ b/sddm-theme/components/VirtualKeyboard_wayland.qml
@@ -0,0 +1,24 @@
+/*
+    SPDX-FileCopyrightText: 2021 Aleix Pol Gonzalez <aleixpol@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
+*/
+
+import QtQuick 2.15
+import org.kde.plasma.workspace.keyboardlayout 1.0 as Keyboards
+
+Item {
+    id: inputPanel
+    readonly property bool active: Qt.inputMethod.visible
+    property bool activated: false
+    visible: Qt.inputMethod.visible
+
+    x: Qt.inputMethod.keyboardRectangle.x
+    y: Qt.inputMethod.keyboardRectangle.y
+    height: Qt.inputMethod.keyboardRectangle.height
+    width: Qt.inputMethod.keyboardRectangle.width
+
+    onActivatedChanged: if (activated) {
+        Keyboards.KWinVirtualKeyboard.enabled = true
+    }
+}
diff --git a/sddm-theme/components/WallpaperFader.qml b/sddm-theme/components/WallpaperFader.qml
new file mode 100644
index 0000000..5c885d1
--- /dev/null
+++ b/sddm-theme/components/WallpaperFader.qml
@@ -0,0 +1,162 @@
+/*
+    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
+
+    SPDX-License-Identifier: GPL-2.0-or-later
+*/
+
+import QtQuick 2.6
+import QtQuick.Controls 1.1
+import QtQuick.Layouts 1.1
+import QtGraphicalEffects 1.0
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+import org.kde.plasma.private.sessions 2.0
+import "../components"
+
+Item {
+    id: wallpaperFader
+    property Item clock
+    property Item mainStack
+    property Item footer
+    property alias source: wallpaperBlur.source
+    state: lockScreenRoot.uiVisible ? "on" : "off"
+    property real factor: 0
+    readonly property bool lightBackground: Math.max(PlasmaCore.ColorScope.backgroundColor.r, PlasmaCore.ColorScope.backgroundColor.g, PlasmaCore.ColorScope.backgroundColor.b) > 0.5
+
+    property bool alwaysShowClock: typeof config === "undefined" || typeof config.alwaysShowClock === "undefined" || config.alwaysShowClock === true
+
+    Behavior on factor {
+        NumberAnimation {
+            target: wallpaperFader
+            property: "factor"
+            duration: PlasmaCore.Units.veryLongDuration * 2
+            easing.type: Easing.InOutQuad
+        }
+    }
+    FastBlur {
+        id: wallpaperBlur
+        anchors.fill: parent
+        radius: 50 * wallpaperFader.factor
+    }
+    ShaderEffect {
+        id: wallpaperShader
+        anchors.fill: parent
+        supportsAtlasTextures: true
+        property var source: ShaderEffectSource {
+            sourceItem: wallpaperBlur
+            live: true
+            hideSource: true
+            textureMirroring: ShaderEffectSource.NoMirroring
+        }
+
+        readonly property real contrast: 0.65 * wallpaperFader.factor + (1 - wallpaperFader.factor)
+        readonly property real saturation: 1.6 * wallpaperFader.factor + (1 - wallpaperFader.factor)
+        readonly property real intensity: (wallpaperFader.lightBackground ? 1.7 : 0.6) * wallpaperFader.factor + (1 - wallpaperFader.factor)
+
+        readonly property real transl: (1.0 - contrast) / 2.0;
+        readonly property real rval: (1.0 - saturation) * 0.2126;
+        readonly property real gval: (1.0 - saturation) * 0.7152;
+        readonly property real bval: (1.0 - saturation) * 0.0722;
+
+        property var colorMatrix: Qt.matrix4x4(
+            contrast, 0,        0,        0.0,
+            0,        contrast, 0,        0.0,
+            0,        0,        contrast, 0.0,
+            transl,   transl,   transl,   1.0).times(Qt.matrix4x4(
+                rval + saturation, rval,     rval,     0.0,
+                gval,     gval + saturation, gval,     0.0,
+                bval,     bval,     bval + saturation, 0.0,
+                0,        0,        0,        1.0)).times(Qt.matrix4x4(
+                    intensity, 0,         0,         0,
+                    0,         intensity, 0,         0,
+                    0,         0,         intensity, 0,
+                    0,         0,         0,         1
+                ));
+
+
+        fragmentShader: "
+            uniform mediump mat4 colorMatrix;
+            uniform mediump sampler2D source;
+            varying mediump vec2 qt_TexCoord0;
+            uniform lowp float qt_Opacity;
+
+            void main(void)
+            {
+                mediump vec4 tex = texture2D(source, qt_TexCoord0);
+                gl_FragColor = tex * colorMatrix * qt_Opacity;
+            }"
+    }
+
+    states: [
+        State {
+            name: "on"
+            PropertyChanges {
+                target: mainStack
+                opacity: 1
+            }
+            PropertyChanges {
+                target: footer
+                opacity: 1
+            }
+            PropertyChanges {
+                target: wallpaperFader
+                factor: 1
+            }
+            PropertyChanges {
+                target: clock.shadow
+                opacity: 0
+            }
+            PropertyChanges {
+                target: clock
+                opacity: 1
+            }
+        },
+        State {
+            name: "off"
+            PropertyChanges {
+                target: mainStack
+                opacity: 0
+            }
+            PropertyChanges {
+                target: footer
+                opacity: 0
+            }
+            PropertyChanges {
+                target: wallpaperFader
+                factor: 0
+            }
+            PropertyChanges {
+                target: clock.shadow
+                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
+            }
+            PropertyChanges {
+                target: clock
+                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
+            }
+        }
+    ]
+    transitions: [
+        Transition {
+            from: "off"
+            to: "on"
+            //Note: can't use animators as they don't play well with parallelanimations
+            NumberAnimation {
+                targets: [mainStack, footer, clock]
+                property: "opacity"
+                duration: PlasmaCore.Units.veryLongDuration
+                easing.type: Easing.InOutQuad
+            }
+        },
+        Transition {
+            from: "on"
+            to: "off"
+            NumberAnimation {
+                targets: [mainStack, footer, clock]
+                property: "opacity"
+                duration: PlasmaCore.Units.veryLongDuration
+                easing.type: Easing.InOutQuad
+            }
+        }
+    ]
+}
diff --git a/sddm-theme/components/artwork/README.txt b/sddm-theme/components/artwork/README.txt
new file mode 100644
index 0000000..1885a36
--- /dev/null
+++ b/sddm-theme/components/artwork/README.txt
@@ -0,0 +1 @@
+After editing SVG files be sure to run currentColorFillFix.sh from plasma-framework
\ No newline at end of file
diff --git a/sddm-theme/components/artwork/logout_primary.svgz b/sddm-theme/components/artwork/logout_primary.svgz
new file mode 100644
index 0000000..6a9423f
Binary files /dev/null and b/sddm-theme/components/artwork/logout_primary.svgz differ
diff --git a/sddm-theme/components/artwork/restart_primary.svgz b/sddm-theme/components/artwork/restart_primary.svgz
new file mode 100644
index 0000000..e2312bd
Binary files /dev/null and b/sddm-theme/components/artwork/restart_primary.svgz differ
diff --git a/sddm-theme/components/artwork/shutdown_primary.svgz b/sddm-theme/components/artwork/shutdown_primary.svgz
new file mode 100644
index 0000000..1c60152
Binary files /dev/null and b/sddm-theme/components/artwork/shutdown_primary.svgz differ

========== NEXT SDDM SYNC COMMIT ==========
remote: Enumerating objects: 24, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 24 (delta 7), reused 20 (delta 5), pack-reused 0 (from 0)
Receiving objects: 100% (24/24), 19.01 KiB | 237.00 KiB/s, done.
Resolving deltas: 100% (7/7), done.
commit 2eb6abb68a8c0eaf599f59e94058816dc8e05323
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Wed Mar 13 19:49:08 2024 +0500

    [sddm-theme] Sync with upstream

 sddm-theme/Background.qml                           |  23 +---
 sddm-theme/BreezeMenuStyle.qml                      |  25 ----
 sddm-theme/KeyboardButton.qml                       |  62 +++++++---
 sddm-theme/Login.qml                                |  79 ++++++++----
 sddm-theme/Main.qml                                 | 404 ++++++++++++++++++++++++++++++------------------------------
 sddm-theme/SessionButton.qml                        |  64 +++++-----
 sddm-theme/components                               |   1 +
 sddm-theme/components/ActionButton.qml              | 115 -----------------
 sddm-theme/components/Battery.qml                   |  43 -------
 sddm-theme/components/Clock.qml                     |  37 ------
 sddm-theme/components/SessionManagementScreen.qml   | 109 ----------------
 sddm-theme/components/UserDelegate.qml              | 180 ---------------------------
 sddm-theme/components/UserList.qml                  |  88 -------------
 sddm-theme/components/VirtualKeyboard.qml           |  70 -----------
 sddm-theme/components/VirtualKeyboard_wayland.qml   |  24 ----
 sddm-theme/components/WallpaperFader.qml            | 162 ------------------------
 sddm-theme/components/artwork/README.txt            |   1 -
 sddm-theme/components/artwork/logout_primary.svgz   | Bin 2514 -> 0 bytes
 sddm-theme/components/artwork/restart_primary.svgz  | Bin 1860 -> 0 bytes
 sddm-theme/components/artwork/shutdown_primary.svgz | Bin 1738 -> 0 bytes
 sddm-theme/dummydata/config.qml                     |   9 +-
 sddm-theme/dummydata/keyboard.qml                   |  11 +-
 sddm-theme/dummydata/screenModel.qml                |   6 +-
 sddm-theme/dummydata/sddm.qml                       |   6 +-
 sddm-theme/dummydata/sessionModel.qml               |   2 +-
 sddm-theme/dummydata/userModel.qml                  |   2 +-
 sddm-theme/manjarologo.svgz                         | Bin 0 -> 5366 bytes
 sddm-theme/metadata.desktop                         |   7 +-
 sddm-theme/theme.conf.cmake                         |   1 +
 29 files changed, 357 insertions(+), 1174 deletions(-)
commit 2eb6abb68a8c0eaf599f59e94058816dc8e05323
Author:     Artem Grinev <agrinev@manjaro.org>
AuthorDate: Wed Mar 13 19:49:08 2024 +0500
Commit:     Artem Grinev <agrinev@manjaro.org>
CommitDate: Wed Mar 13 19:49:08 2024 +0500

    [sddm-theme] Sync with upstream

diff --git a/sddm-theme/Background.qml b/sddm-theme/Background.qml
index 5a38415..6721e57 100644
--- a/sddm-theme/Background.qml
+++ b/sddm-theme/Background.qml
@@ -1,23 +1,10 @@
 /*
- *   Copyright 2016 Boudhayan Gupta <bgupta@kde.org>
- *
- *   This program is free software; you can redistribute it and/or modify
- *   it under the terms of the GNU Library General Public License as
- *   published by the Free Software Foundation; either version 2 or
- *   (at your option) any later version.
- *
- *   This program is distributed in the hope that it will be useful,
- *   but WITHOUT ANY WARRANTY; without even the implied warranty of
- *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
- *   GNU General Public License for more details
- *
- *   You should have received a copy of the GNU Library General Public
- *   License along with this program; if not, write to the
- *   Free Software Foundation, Inc.,
- *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
- */
+    SPDX-FileCopyrightText: 2016 Boudhayan Gupta <bgupta@kde.org>

-import QtQuick 2.2
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.15

 FocusScope {
     id: sceneBackground
diff --git a/sddm-theme/BreezeMenuStyle.qml b/sddm-theme/BreezeMenuStyle.qml
deleted file mode 100644
index 7d56c14..0000000
--- a/sddm-theme/BreezeMenuStyle.qml
+++ /dev/null
@@ -1,25 +0,0 @@
-import QtQuick 2.2
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-import QtQuick.Controls.Styles 1.4 as QQCS
-import QtQuick.Controls 1.3 as QQC
-
-QQCS.MenuStyle {
-    frame: Rectangle {
-        color: PlasmaCore.ColorScope.backgroundColor
-        border.color: Qt.tint(PlasmaCore.ColorScope.textColor, Qt.rgba(color.r, color.g, color.b, 0.7))
-        border.width: 1
-    }
-    itemDelegate.label: QQC.Label {
-        height: contentHeight * 1.2
-        verticalAlignment: Text.AlignVCenter
-        color: styleData.selected ? PlasmaCore.ColorScope.highlightedTextColor : PlasmaCore.ColorScope.textColor
-        font.pointSize: config.fontSize
-        text: styleData.text
-    }
-    itemDelegate.background: Rectangle {
-        visible: styleData.selected
-        color: PlasmaCore.ColorScope.highlightColor
-    }
-}
diff --git a/sddm-theme/KeyboardButton.qml b/sddm-theme/KeyboardButton.qml
index d5d5a44..6731c30 100644
--- a/sddm-theme/KeyboardButton.qml
+++ b/sddm-theme/KeyboardButton.qml
@@ -1,35 +1,59 @@
-import QtQuick 2.2
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+    SPDX-FileCopyrightText: 2022 Aleix Pol Gonzalez <aleixpol@kde.org>

-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 2.0 as PlasmaComponents // Because PC3 ToolButton can't take a menu
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/

-import QtQuick.Controls 1.3 as QQC
+import QtQuick 2.15
+
+import org.kde.plasma.components 3.0 as PlasmaComponents
+import org.kde.kirigami 2.20 as Kirigami

 PlasmaComponents.ToolButton {
-    id: keyboardButton
+    id: root
+
+    property int currentIndex: keyboard.currentLayout
+    onCurrentIndexChanged: keyboard.currentLayout = currentIndex

-    property int currentIndex: -1
+    text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Keyboard Layout: %1", keyboard.layouts[currentIndex].longName)
+    visible: keyboard.layouts.length > 1

-    text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Keyboard Layout: %1", instantiator.objectAt(currentIndex).shortName)
-    implicitWidth: minimumWidth
+    checkable: true
+    checked: menu.opened
+    onToggled: {
+        if (checked) {
+            menu.popup(root, 0, 0)
+        } else {
+            menu.dismiss()
+        }
+    }

-    visible: menu.items.length > 1
+    signal keyboardLayoutChanged()

-    Component.onCompleted: currentIndex = Qt.binding(function() {return keyboard.currentLayout});
+    PlasmaComponents.Menu {
+        id: menu
+        Kirigami.Theme.colorSet: Kirigami.Theme.Window
+        Kirigami.Theme.inherit: false
+
+        onAboutToShow: {
+            if (instantiator.model === null) {
+                let layouts = keyboard.layouts;
+                layouts.sort((a, b) => a.longName.localeCompare(b.longName));
+                instantiator.model = layouts;
+            }
+        }

-    menu: QQC.Menu {
-        id: keyboardMenu
-        style: BreezeMenuStyle {}
         Instantiator {
             id: instantiator
-            model: keyboard.layouts
-            onObjectAdded: keyboardMenu.insertItem(index, object)
-            onObjectRemoved: keyboardMenu.removeItem( object )
-            delegate: QQC.MenuItem {
+            model: null
+            onObjectAdded: (index, object) => menu.insertItem(index, object)
+            onObjectRemoved: (index, object) => menu.removeItem(object)
+            delegate: PlasmaComponents.MenuItem {
                 text: modelData.longName
-                property string shortName: modelData.shortName
                 onTriggered: {
-                    keyboard.currentLayout = model.index
+                    keyboard.currentLayout = keyboard.layouts.indexOf(modelData)
+                    root.keyboardLayoutChanged()
                 }
             }
         }
diff --git a/sddm-theme/Login.qml b/sddm-theme/Login.qml
index bde6d8b..4a09aea 100644
--- a/sddm-theme/Login.qml
+++ b/sddm-theme/Login.qml
@@ -1,10 +1,12 @@
-import "components"
+import org.kde.breeze.components

-import QtQuick 2.0
-import QtQuick.Layouts 1.2
+import QtQuick 2.15
+import QtQuick.Layouts 1.15
+import QtQuick.Controls 2.15 as QQC2

-import org.kde.plasma.core 2.0 as PlasmaCore
 import org.kde.plasma.components 3.0 as PlasmaComponents3
+import org.kde.plasma.extras 2.0 as PlasmaExtras
+import org.kde.kirigami 2.20 as Kirigami

 SessionManagementScreen {
     id: root
@@ -17,7 +19,7 @@ SessionManagementScreen {

     //the y position that should be ensured visible when the on screen keyboard is visible
     property int visibleBoundary: mapFromItem(loginButton, 0, 0).y
-    onHeightChanged: visibleBoundary = mapFromItem(loginButton, 0, 0).y + loginButton.height + PlasmaCore.Units.smallSpacing
+    onHeightChanged: visibleBoundary = mapFromItem(loginButton, 0, 0).y + loginButton.height + Kirigami.Units.smallSpacing

     property int fontSize: parseInt(config.fontSize)

@@ -29,23 +31,45 @@ SessionManagementScreen {
         }
     }

+    onUserSelected: {
+        // Don't startLogin() here, because the signal is connected to the
+        // Escape key as well, for which it wouldn't make sense to trigger
+        // login.
+        focusFirstVisibleFormControl();
+    }
+
+    QQC2.StackView.onActivating: {
+        // Controls are not visible yet.
+        Qt.callLater(focusFirstVisibleFormControl);
+    }
+
+    function focusFirstVisibleFormControl() {
+        const nextControl = (userNameInput.visible
+            ? userNameInput
+            : (passwordBox.visible
+                ? passwordBox
+                : loginButton));
+        // Using TabFocusReason, so that the loginButton gets the visual highlight.
+        nextControl.forceActiveFocus(Qt.TabFocusReason);
+    }
+
     /*
-    * Login has been requested with the following username and password
-    * If username field is visible, it will be taken from that, otherwise from the "name" property of the currentIndex
-    */
+     * Login has been requested with the following username and password
+     * If username field is visible, it will be taken from that, otherwise from the "name" property of the currentIndex
+     */
     function startLogin() {
-        var username = showUsernamePrompt ? userNameInput.text : userList.selectedUser
-        var password = passwordBox.text
-        passwordRow.visible = false
-
+        const username = showUsernamePrompt ? userNameInput.text : userList.selectedUser
+        const password = passwordBox.text

         footer.enabled = false
         mainStack.enabled = false
         userListComponent.userList.opacity = 0.5

-        //this is partly because it looks nicer
-        //but more importantly it works round a Qt bug that can trigger if the app is closed with a TextField focused
-        //DAVE REPORT THE FRICKING THING AND PUT A LINK
+        // This is partly because it looks nicer, but more importantly it
+        // works round a Qt bug that can trigger if the app is closed with a
+        // TextField focused.
+        //
+        // See https://bugreports.qt.io/browse/QTBUG-55460
         loginButton.forceActiveFocus();
         loginRequest(username, password);
     }
@@ -60,25 +84,26 @@ SessionManagementScreen {
         focus: showUsernamePrompt && !lastUserName //if there's a username prompt it gets focus first, otherwise password does
         placeholderText: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Username")

-        onAccepted:
+        onAccepted: {
             if (root.loginScreenUiVisible) {
                 passwordBox.forceActiveFocus()
             }
+        }
     }

     RowLayout {
         Layout.fillWidth: true
-        id: passwordRow

-        PlasmaComponents3.TextField {
+        PlasmaExtras.PasswordField {
             id: passwordBox
             font.pointSize: fontSize + 1
             Layout.fillWidth: true

             placeholderText: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Password")
             focus: !showUsernamePrompt || lastUserName
-            echoMode: TextInput.Password
-            revealPasswordButtonShown: true
+
+            // Disable reveal password action because SDDM does not have the breeze icon set loaded
+            rightActions: []

             onAccepted: {
                 if (root.loginScreenUiVisible) {
@@ -86,13 +111,15 @@ SessionManagementScreen {
                 }
             }

+            visible: root.showUsernamePrompt || userList.currentItem.needsPassword
+
             Keys.onEscapePressed: {
                 mainStack.currentItem.forceActiveFocus();
             }

             //if empty and left or right is pressed change selection in user switch
             //this cannot be in keys.onLeftPressed as then it doesn't reach the password box
-            Keys.onPressed: {
+            Keys.onPressed: event => {
                 if (event.key === Qt.Key_Left && !text) {
                     userList.decrementCurrentIndex();
                     event.accepted = true
@@ -106,7 +133,6 @@ SessionManagementScreen {
             Connections {
                 target: sddm
                 function onLoginFailed() {
-                    passwordRow.visible = true
                     passwordBox.selectAll()
                     passwordBox.forceActiveFocus()
                 }
@@ -117,11 +143,14 @@ SessionManagementScreen {
             id: loginButton
             Accessible.name: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Log In")
             Layout.preferredHeight: passwordBox.implicitHeight
-            Layout.preferredWidth: loginButton.Layout.preferredHeight
+            Layout.preferredWidth: text.length === 0 ? loginButton.Layout.preferredHeight : -1

-            icon.name: "go-next"
+            icon.name: text.length === 0 ? (root.LayoutMirroring.enabled ? "go-previous" : "go-next") : ""

-            onClicked: startLogin();
+            text: root.showUsernamePrompt || userList.currentItem.needsPassword ? "" : i18n("Log In")
+            onClicked: startLogin()
+            Keys.onEnterPressed: clicked()
+            Keys.onReturnPressed: clicked()
         }
     }
 }
diff --git a/sddm-theme/Main.qml b/sddm-theme/Main.qml
index 16fdd38..f5da14c 100644
--- a/sddm-theme/Main.qml
+++ b/sddm-theme/Main.qml
@@ -1,48 +1,34 @@
 /*
- *   Copyright 2016 David Edmundson <davidedmundson@kde.org>
- *
- *   This program is free software; you can redistribute it and/or modify
- *   it under the terms of the GNU Library General Public License as
- *   published by the Free Software Foundation; either version 2 or
- *   (at your option) any later version.
- *
- *   This program is distributed in the hope that it will be useful,
- *   but WITHOUT ANY WARRANTY; without even the implied warranty of
- *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
- *   GNU General Public License for more details
- *
- *   You should have received a copy of the GNU Library General Public
- *   License along with this program; if not, write to the
- *   Free Software Foundation, Inc.,
- *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
- */
-
-import QtQuick 2.8
-
-import QtQuick.Layouts 1.1
-import QtQuick.Controls 1.1
-import QtGraphicalEffects 1.0
-
-import org.kde.plasma.core 2.0 as PlasmaCore
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.15
+import QtQuick.Layouts 1.15
+import QtQuick.Controls 2.15 as QQC2
+import Qt5Compat.GraphicalEffects
+
 import org.kde.plasma.components 3.0 as PlasmaComponents3
-import org.kde.plasma.extras 2.0 as PlasmaExtras
+import org.kde.plasma.private.keyboardindicator as KeyboardIndicator
+import org.kde.kirigami 2.20 as Kirigami

-import "components"
+import org.kde.breeze.components

 // TODO: Once SDDM 0.19 is released and we are setting the font size using the
 // SDDM KCM's syncing feature, remove the `config.fontSize` overrides here and
 // the fontSize properties in various components, because the theme's default
 // font size will be correctly propagated to the login screen

-PlasmaCore.ColorScope {
+Item {
     id: root

     // If we're using software rendering, draw outlines instead of shadows
     // See https://bugs.kde.org/show_bug.cgi?id=398317
     readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software

-    colorGroup: PlasmaCore.Theme.ComplementaryColorGroup
-    readonly property bool lightBackground: Math.max(PlasmaCore.ColorScope.backgroundColor.r, PlasmaCore.ColorScope.backgroundColor.g, PlasmaCore.ColorScope.backgroundColor.b) > 0.5
+    Kirigami.Theme.colorSet: Kirigami.Theme.Complementary
+    Kirigami.Theme.inherit: false

     width: 1600
     height: 900
@@ -52,10 +38,9 @@ PlasmaCore.ColorScope {
     LayoutMirroring.enabled: Qt.application.layoutDirection === Qt.RightToLeft
     LayoutMirroring.childrenInherit: true

-    PlasmaCore.DataSource {
-        id: keystateSource
-        engine: "keystate"
-        connectedSources: "Caps Lock"
+    KeyboardIndicator.KeyState {
+        id: capsLockState
+        key: Qt.Key_CapsLock
     }

     Item {
@@ -73,6 +58,11 @@ PlasmaCore.ColorScope {
         }
     }

+    RejectPasswordAnimation {
+        id: rejectPasswordAnimation
+        target: mainStack
+    }
+
     MouseArea {
         id: loginScreenRoot
         anchors.fill: parent
@@ -100,7 +90,7 @@ PlasmaCore.ColorScope {
             }
         }

-        Keys.onPressed: {
+        Keys.onPressed: event => {
             uiVisible = true;
             event.accepted = false;
         }
@@ -112,6 +102,7 @@ PlasmaCore.ColorScope {
             interval: 60000
             onTriggered: {
                 if (!loginScreenRoot.blockUI) {
+                    userListComponent.mainPasswordBox.showPassword = false;
                     loginScreenRoot.uiVisible = false;
                 }
             }
@@ -131,20 +122,13 @@ PlasmaCore.ColorScope {
             anchors.fill: clock
             source: clock
             visible: !softwareRendering
-            horizontalOffset: 1
-            verticalOffset: 1
             radius: 6
             samples: 14
             spread: 0.3
-                                          // Soften the color a bit so it doesn't look so stark against light backgrounds
-            color: root.lightBackground ? Qt.rgba(PlasmaCore.ColorScope.backgroundColor.r,
-                                                  PlasmaCore.ColorScope.backgroundColor.g,
-                                                  PlasmaCore.ColorScope.backgroundColor.b,
-                                                  0.6)
-                                        : "black" // black matches Breeze window decoration and desktopcontainment
+            color : "black" // shadows should always be black
             Behavior on opacity {
                 OpacityAnimator {
-                    duration: PlasmaCore.Units.veryLongDuration * 2
+                    duration: Kirigami.Units.veryLongDuration * 2
                     easing.type: Easing.InOutQuad
                 }
             }
@@ -152,19 +136,27 @@ PlasmaCore.ColorScope {

         Clock {
             id: clock
-            visible: y > 0
             property Item shadow: clockShadow
-            y: (userListComponent.userList.y + mainStack.y)/2 - height/2
+            visible: y > 0
             anchors.horizontalCenter: parent.horizontalCenter
+            y: (userListComponent.userList.y + mainStack.y)/2 - height/2
+            Layout.alignment: Qt.AlignBaseline
         }

-        StackView {
+        QQC2.StackView {
             id: mainStack
             anchors {
                 left: parent.left
                 right: parent.right
             }
-            height: root.height + PlasmaCore.Units.gridUnit * 3
+            height: root.height + Kirigami.Units.gridUnit * 3
+
+            // If true (depends on the style and environment variables), hover events are always accepted
+            // and propagation stopped. This means the parent MouseArea won't get them and the UI won't be shown.
+            // Disable capturing those events while the UI is hidden to avoid that, while still passing events otherwise.
+            // One issue is that while the UI is visible, mouse activity won't keep resetting the timer, but when it
+            // finally expires, the next event should immediately set uiVisible = true again.
+            hoverEnabled: loginScreenRoot.uiVisible ? undefined : false

             focus: true //StackView is an implicit focus scope, so we need to give this focus so the item inside will have it

@@ -186,61 +178,63 @@ PlasmaCore.ColorScope {
                 userListCurrentIndex: userModel.lastIndex >= 0 ? userModel.lastIndex : 0
                 lastUserName: userModel.lastUser
                 showUserList: {
-                    if ( !userListModel.hasOwnProperty("count")
-                    || !userListModel.hasOwnProperty("disableAvatarsThreshold"))
-                        return (userList.y + mainStack.y) > 0
+                    if (!userListModel.hasOwnProperty("count")
+                        || !userListModel.hasOwnProperty("disableAvatarsThreshold")) {
+                        return false
+                    }

-                    if ( userListModel.count === 0 ) return false
+                    if (userListModel.count === 0 ) {
+                        return false
+                    }

-                    if ( userListModel.hasOwnProperty("containsAllUsers") && !userListModel.containsAllUsers ) return false
+                    if (userListModel.hasOwnProperty("containsAllUsers") && !userListModel.containsAllUsers) {
+                        return false
+                    }

-                    return userListModel.count <= userListModel.disableAvatarsThreshold && (userList.y + mainStack.y) > 0
+                    return userListModel.count <= userListModel.disableAvatarsThreshold
                 }

                 notificationMessage: {
-                    var text = ""
-                    if (keystateSource.data["Caps Lock"]["Locked"]) {
-                        text += i18nd("plasma_lookandfeel_org.kde.lookandfeel","Caps Lock is on")
-                        if (root.notificationMessage) {
-                            text += " • "
-                        }
+                    const parts = [];
+                    if (capsLockState.locked) {
+                        parts.push(i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Caps Lock is on"));
+                    }
+                    if (root.notificationMessage) {
+                        parts.push(root.notificationMessage);
                     }
-                    text += root.notificationMessage
-                    return text
+                    return parts.join(" • ");
                 }

+                actionItemsVisible: !inputPanel.keyboardActive
                 actionItems: [
                     ActionButton {
                         iconSource: "system-suspend"
-                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel","Suspend to RAM","Sleep")
+                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Suspend to RAM", "Sleep")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.suspend()
                         enabled: sddm.canSuspend
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-reboot"
-                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Restart")
+                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Restart")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.reboot()
                         enabled: sddm.canReboot
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-shutdown"
-                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Shut Down")
+                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Shut Down")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.powerOff()
                         enabled: sddm.canPowerOff
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-user-prompt"
-                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "For switching to a username and password prompt", "Other...")
+                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "For switching to a username and password prompt", "Other…")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: mainStack.push(userPromptComponent)
                         enabled: true
-                        visible: !userListComponent.showUsernamePrompt && !inputPanel.keyboardActive
+                        visible: !userListComponent.showUsernamePrompt
                     }]

                 onLoginRequest: {
@@ -251,126 +245,83 @@ PlasmaCore.ColorScope {

             Behavior on opacity {
                 OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
+                    duration: Kirigami.Units.longDuration
                 }
             }
-        }

-        Loader {
-            id: inputPanel
-            state: "hidden"
-            property bool keyboardActive: item ? item.active : false
-            onKeyboardActiveChanged: {
-                if (keyboardActive) {
-                    state = "visible"
-                    // Otherwise the password field loses focus and virtual keyboard
-                    // keystrokes get eaten
-                    userListComponent.mainPasswordBox.forceActiveFocus();
-                } else {
-                    state = "hidden";
+            readonly property real zoomFactor: 1.5
+
+            popEnter: Transition {
+                ScaleAnimator {
+                    from: mainStack.zoomFactor
+                    to: 1
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
+                }
+                OpacityAnimator {
+                    from: 0
+                    to: 1
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
                 }
             }
-            source: "components/VirtualKeyboard.qml"
-            anchors {
-                left: parent.left
-                right: parent.right
+
+            popExit: Transition {
+                ScaleAnimator {
+                    from: 1
+                    to: 1 / mainStack.zoomFactor
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
+                }
+                OpacityAnimator {
+                    from: 1
+                    to: 0
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
+                }
             }

-            function showHide() {
-                state = state == "hidden" ? "visible" : "hidden";
+            pushEnter: Transition {
+                ScaleAnimator {
+                    from: 1 / mainStack.zoomFactor
+                    to: 1
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
+                }
+                OpacityAnimator {
+                    from: 0
+                    to: 1
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
+                }
             }

-            states: [
-                State {
-                    name: "visible"
-                    PropertyChanges {
-                        target: mainStack
-                        y: Math.min(0, root.height - inputPanel.height - userListComponent.visibleBoundary)
-                    }
-                    PropertyChanges {
-                        target: inputPanel
-                        y: root.height - inputPanel.height
-                        opacity: 1
-                    }
-                },
-                State {
-                    name: "hidden"
-                    PropertyChanges {
-                        target: mainStack
-                        y: 0
-                    }
-                    PropertyChanges {
-                        target: inputPanel
-                        y: root.height - root.height/4
-                        opacity: 0
-                    }
+            pushExit: Transition {
+                ScaleAnimator {
+                    from: 1
+                    to: mainStack.zoomFactor
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
                 }
-            ]
-            transitions: [
-                Transition {
-                    from: "hidden"
-                    to: "visible"
-                    SequentialAnimation {
-                        ScriptAction {
-                            script: {
-                                inputPanel.item.activated = true;
-                                Qt.inputMethod.show();
-                            }
-                        }
-                        ParallelAnimation {
-                            NumberAnimation {
-                                target: mainStack
-                                property: "y"
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.InOutQuad
-                            }
-                            NumberAnimation {
-                                target: inputPanel
-                                property: "y"
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.OutQuad
-                            }
-                            OpacityAnimator {
-                                target: inputPanel
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.OutQuad
-                            }
-                        }
-                    }
-                },
-                Transition {
-                    from: "visible"
-                    to: "hidden"
-                    SequentialAnimation {
-                        ParallelAnimation {
-                            NumberAnimation {
-                                target: mainStack
-                                property: "y"
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.InOutQuad
-                            }
-                            NumberAnimation {
-                                target: inputPanel
-                                property: "y"
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.InQuad
-                            }
-                            OpacityAnimator {
-                                target: inputPanel
-                                duration: PlasmaCore.Units.longDuration
-                                easing.type: Easing.InQuad
-                            }
-                        }
-                        ScriptAction {
-                            script: {
-                                Qt.inputMethod.hide();
-                            }
-                        }
-                    }
+                OpacityAnimator {
+                    from: 1
+                    to: 0
+                    duration: Kirigami.Units.veryLongDuration
+                    easing.type: Easing.OutCubic
                 }
-            ]
+            }
         }

+        VirtualKeyboardLoader {
+            id: inputPanel
+
+            z: 1
+
+            screenRoot: root
+            mainStack: mainStack
+            mainBlock: userListComponent
+            passwordField: userListComponent.mainPasswordBox
+        }

         Component {
             id: userPromptComponent
@@ -384,11 +335,12 @@ PlasmaCore.ColorScope {
                 userListModel: ListModel {
                     ListElement {
                         name: ""
-                        iconSource: ""
+                        icon: ""
                     }
                     Component.onCompleted: {
                         // as we can't bind inside ListElement
                         setProperty(0, "name", i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Type in Username and Password"));
+                        setProperty(0, "icon", Qt.resolvedUrl("faces/.face.icon"))
                     }
                 }

@@ -397,37 +349,34 @@ PlasmaCore.ColorScope {
                     sddm.login(username, password, sessionButton.currentIndex)
                 }

+                actionItemsVisible: !inputPanel.keyboardActive
                 actionItems: [
                     ActionButton {
                         iconSource: "system-suspend"
-                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel","Suspend to RAM","Sleep")
+                        text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Suspend to RAM", "Sleep")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.suspend()
                         enabled: sddm.canSuspend
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-reboot"
-                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Restart")
+                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Restart")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.reboot()
                         enabled: sddm.canReboot
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-shutdown"
-                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Shut Down")
+                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Shut Down")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: sddm.powerOff()
                         enabled: sddm.canPowerOff
-                        visible: !inputPanel.keyboardActive
                     },
                     ActionButton {
                         iconSource: "system-user-list"
-                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","List Users")
+                        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "List Users")
                         fontSize: parseInt(config.fontSize) + 1
                         onClicked: mainStack.pop()
-                        visible: !inputPanel.keyboardActive
                     }
                 ]
             }
@@ -437,23 +386,18 @@ PlasmaCore.ColorScope {
             id: logoShadow
             anchors.fill: logo
             source: logo
-            visible: !softwareRendering && config.showlogo == "shown"
+            visible: !softwareRendering && config.showlogo === "shown"
             horizontalOffset: 1
             verticalOffset: 1
             radius: 6
             samples: 14
             spread: 0.3
-                                          // Soften the color a bit so it doesn't look so stark against light backgrounds
-            color: root.lightBackground ? Qt.rgba(PlasmaCore.ColorScope.backgroundColor.r,
-                                                  PlasmaCore.ColorScope.backgroundColor.g,
-                                                  PlasmaCore.ColorScope.backgroundColor.b,
-                                                  0.6)
-                                        : "black" // black matches Breeze window decoration and desktopcontainment
+            color : "black" // shadows should always be black
             opacity: loginScreenRoot.uiVisible ? 0 : 1
             Behavior on opacity {
                 //OpacityAnimator when starting from 0 is buggy (it shows one frame with opacity 1)"
                 NumberAnimation {
-                    duration: PlasmaCore.Units.longDuration
+                    duration: Kirigami.Units.longDuration
                     easing.type: Easing.InOutQuad
                 }
             }
@@ -461,56 +405,109 @@ PlasmaCore.ColorScope {

         Image {
             id: logo
-            visible: config.showlogo == "shown"
+            visible: config.showlogo === "shown"
             source: config.logo
             anchors.horizontalCenter: parent.horizontalCenter
             anchors.bottom: footer.top
-            anchors.bottomMargin: PlasmaCore.Units.largeSpacing
+            anchors.bottomMargin: Kirigami.Units.largeSpacing
             asynchronous: true
             sourceSize.height: height
             opacity: loginScreenRoot.uiVisible ? 0 : 1
             fillMode: Image.PreserveAspectFit
-            height: Math.round(PlasmaCore.Units.gridUnit * 3.5)
+            height: Math.round(Kirigami.Units.gridUnit * 3.5)
             Behavior on opacity {
                 // OpacityAnimator when starting from 0 is buggy (it shows one frame with opacity 1)"
                 NumberAnimation {
-                    duration: PlasmaCore.Units.longDuration
+                    duration: Kirigami.Units.longDuration
                     easing.type: Easing.InOutQuad
                 }
             }
         }

-        //Footer
+        // Note: Containment masks stretch clickable area of their buttons to
+        // the screen edges, essentially making them adhere to Fitts's law.
+        // Due to virtual keyboard button having an icon, buttons may have
+        // different heights, so fillHeight is required.
+        //
+        // Note for contributors: Keep this in sync with LockScreenUi.qml footer.
         RowLayout {
             id: footer
             anchors {
                 bottom: parent.bottom
                 left: parent.left
                 right: parent.right
-                margins: PlasmaCore.Units.smallSpacing
+                margins: Kirigami.Units.smallSpacing
             }
+            spacing: Kirigami.Units.smallSpacing

             Behavior on opacity {
                 OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
+                    duration: Kirigami.Units.longDuration
                 }
             }

             PlasmaComponents3.ToolButton {
+                id: virtualKeyboardButton
+
                 text: i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Button to show/hide virtual keyboard", "Virtual Keyboard")
                 font.pointSize: config.fontSize
                 icon.name: inputPanel.keyboardActive ? "input-keyboard-virtual-on" : "input-keyboard-virtual-off"
-                onClicked: inputPanel.showHide()
-                visible: inputPanel.status == Loader.Ready
+                onClicked: {
+                    // Otherwise the password field loses focus and virtual keyboard
+                    // keystrokes get eaten
+                    userListComponent.mainPasswordBox.forceActiveFocus();
+                    inputPanel.showHide()
+                }
+                visible: inputPanel.status === Loader.Ready
+
+                Layout.fillHeight: true
+                containmentMask: Item {
+                    parent: virtualKeyboardButton
+                    anchors.fill: parent
+                    anchors.leftMargin: -footer.anchors.margins
+                    anchors.bottomMargin: -footer.anchors.margins
+                }
             }

             KeyboardButton {
+                id: keyboardButton
+
                 font.pointSize: config.fontSize
+
+                onKeyboardLayoutChanged: {
+                    // Otherwise the password field loses focus and virtual keyboard
+                    // keystrokes get eaten
+                    userListComponent.mainPasswordBox.forceActiveFocus();
+                }
+
+                Layout.fillHeight: true
+                containmentMask: Item {
+                    parent: keyboardButton
+                    anchors.fill: parent
+                    anchors.leftMargin: virtualKeyboardButton.visible ? 0 : -footer.anchors.margins
+                    anchors.bottomMargin: -footer.anchors.margins
+                }
             }

             SessionButton {
                 id: sessionButton
+
                 font.pointSize: config.fontSize
+
+                onSessionChanged: {
+                    // Otherwise the password field loses focus and virtual keyboard
+                    // keystrokes get eaten
+                    userListComponent.mainPasswordBox.forceActiveFocus();
+                }
+
+                Layout.fillHeight: true
+                containmentMask: Item {
+                    parent: sessionButton
+                    anchors.fill: parent
+                    anchors.leftMargin: virtualKeyboardButton.visible || keyboardButton.visible
+                        ? 0 : -footer.anchors.margins
+                    anchors.bottomMargin: -footer.anchors.margins
+                }
             }

             Item {
@@ -530,6 +527,7 @@ PlasmaCore.ColorScope {
             footer.enabled = true
             mainStack.enabled = true
             userListComponent.userList.opacity = 1
+            rejectPasswordAnimation.start()
         }
         function onLoginSucceeded() {
             //note SDDM will kill the greeter at some random point after this
diff --git a/sddm-theme/SessionButton.qml b/sddm-theme/SessionButton.qml
index cdd730a..dceecd7 100644
--- a/sddm-theme/SessionButton.qml
+++ b/sddm-theme/SessionButton.qml
@@ -1,55 +1,53 @@
 /*
- *   Copyright 2016 David Edmundson <davidedmundson@kde.org>
- *
- *   This program is free software; you can redistribute it and/or modify
- *   it under the terms of the GNU Library General Public License as
- *   published by the Free Software Foundation; either version 2 or
- *   (at your option) any later version.
- *
- *   This program is distributed in the hope that it will be useful,
- *   but WITHOUT ANY WARRANTY; without even the implied warranty of
- *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
- *   GNU General Public License for more details
- *
- *   You should have received a copy of the GNU Library General Public
- *   License along with this program; if not, write to the
- *   Free Software Foundation, Inc.,
- *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
- */
-
-import QtQuick 2.2
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 2.0 as PlasmaComponents // Because PC3 ToolButton can't take a menu
-
-import QtQuick.Controls 1.3 as QQC
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+    SPDX-FileCopyrightText: 2022 Aleix Pol Gonzalez <aleixpol@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.15
+
+import org.kde.plasma.components 3.0 as PlasmaComponents
+import org.kde.kirigami 2.20 as Kirigami

 PlasmaComponents.ToolButton {
     id: root
-    property int currentIndex: -1
-
-    implicitWidth: minimumWidth

-    visible: menu.items.length > 1
+    property int currentIndex: -1

     text: i18nd("plasma_lookandfeel_org.kde.lookandfeel", "Desktop Session: %1", instantiator.objectAt(currentIndex).text || "")
+    visible: menu.count > 1

     Component.onCompleted: {
         currentIndex = sessionModel.lastIndex
     }
+    checkable: true
+    checked: menu.opened
+    onToggled: {
+        if (checked) {
+            menu.popup(root, 0, 0)
+        } else {
+            menu.dismiss()
+        }
+    }
+
+    signal sessionChanged()
+
+    PlasmaComponents.Menu {
+        Kirigami.Theme.colorSet: Kirigami.Theme.Window
+        Kirigami.Theme.inherit: false

-    menu: QQC.Menu {
         id: menu
-        style: BreezeMenuStyle {}
         Instantiator {
             id: instantiator
             model: sessionModel
-            onObjectAdded: menu.insertItem(index, object)
-            onObjectRemoved: menu.removeItem( object )
-            delegate: QQC.MenuItem {
+            onObjectAdded: (index, object) => menu.insertItem(index, object)
+            onObjectRemoved: (index, object) => menu.removeItem(object)
+            delegate: PlasmaComponents.MenuItem {
                 text: model.name
                 onTriggered: {
                     root.currentIndex = model.index
+                    sessionChanged()
                 }
             }
         }
diff --git a/sddm-theme/components b/sddm-theme/components
new file mode 100755
index 0000000..0d764f5
--- /dev/null
+++ b/sddm-theme/components
@@ -0,0 +1 @@
+../lnf/org.manjaro.breath/contents/components
diff --git a/sddm-theme/components/ActionButton.qml b/sddm-theme/components/ActionButton.qml
deleted file mode 100644
index af278f6..0000000
--- a/sddm-theme/components/ActionButton.qml
+++ /dev/null
@@ -1,115 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: root
-    property alias text: label.text
-    property alias iconSource: icon.source
-    property alias containsMouse: mouseArea.containsMouse
-    property alias font: label.font
-    property alias labelRendering: label.renderType
-    property alias circleOpacity: iconCircle.opacity
-    property alias circleVisiblity: iconCircle.visible
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 1
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-    signal clicked
-
-    activeFocusOnTab: true
-
-    property int iconSize: PlasmaCore.Units.gridUnit * 3
-
-    implicitWidth: Math.max(iconSize + PlasmaCore.Units.largeSpacing * 2, label.contentWidth)
-    implicitHeight: iconSize + PlasmaCore.Units.smallSpacing + label.implicitHeight
-
-    opacity: activeFocus || containsMouse ? 1 : 0.85
-    Behavior on opacity {
-        PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
-            duration: PlasmaCore.Units.longDuration
-            easing.type: Easing.InOutQuad
-        }
-    }
-
-    Rectangle {
-        id: iconCircle
-        anchors.centerIn: icon
-        width: iconSize + PlasmaCore.Units.smallSpacing
-        height: width
-        radius: width / 2
-        color: softwareRendering ?  PlasmaCore.ColorScope.backgroundColor : PlasmaCore.ColorScope.textColor
-        opacity: root.activeFocus || containsMouse ? (softwareRendering ? 0.8 : 0.15) : (softwareRendering ? 0.6 : 0)
-        Behavior on opacity {
-            PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
-                duration: PlasmaCore.Units.longDuration
-                easing.type: Easing.InOutQuad
-            }
-        }
-    }
-
-    Rectangle {
-        anchors.centerIn: iconCircle
-        width: iconCircle.width
-        height: width
-        radius: width / 2
-        scale: mouseArea.containsPress ? 1 : 0
-        color: PlasmaCore.ColorScope.textColor
-        opacity: 0.15
-        Behavior on scale {
-            PropertyAnimation {
-                duration: PlasmaCore.Units.shortDuration
-                easing.type: Easing.InOutQuart
-            }
-        }
-    }
-
-    PlasmaCore.IconItem {
-        id: icon
-        anchors {
-            top: parent.top
-            horizontalCenter: parent.horizontalCenter
-        }
-        width: iconSize
-        height: iconSize
-
-        colorGroup: PlasmaCore.ColorScope.colorGroup
-        active: mouseArea.containsMouse || root.activeFocus
-    }
-
-    PlasmaComponents3.Label {
-        id: label
-        font.pointSize: root.fontSize
-        anchors {
-            top: icon.bottom
-            topMargin: (softwareRendering ? 1.5 : 1) * PlasmaCore.Units.smallSpacing
-            left: parent.left
-            right: parent.right
-        }
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        horizontalAlignment: Text.AlignHCenter
-        verticalAlignment: Text.AlignTop
-        wrapMode: Text.WordWrap
-        font.underline: root.activeFocus
-    }
-
-    MouseArea {
-        id: mouseArea
-        hoverEnabled: true
-        onClicked: root.clicked()
-        anchors.fill: parent
-    }
-
-    Keys.onEnterPressed: clicked()
-    Keys.onReturnPressed: clicked()
-    Keys.onSpacePressed: clicked()
-
-    Accessible.onPressAction: clicked()
-    Accessible.role: Accessible.Button
-    Accessible.name: label.text
-}
diff --git a/sddm-theme/components/Battery.qml b/sddm-theme/components/Battery.qml
deleted file mode 100644
index 05be535..0000000
--- a/sddm-theme/components/Battery.qml
+++ /dev/null
@@ -1,43 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 Kai Uwe Broulik <kde@privat.broulik.de>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-import org.kde.plasma.workspace.components 2.0 as PW
-
-Row {
-    id: row
-
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize
-
-    spacing: PlasmaCore.Units.smallSpacing
-    visible: pmSource.data["Battery"]["Has Cumulative"]
-
-    PlasmaCore.DataSource {
-        id: pmSource
-        engine: "powermanagement"
-        connectedSources: ["Battery", "AC Adapter"]
-    }
-
-    PW.BatteryIcon {
-        id: battery
-        hasBattery: pmSource.data["Battery"]["Has Battery"] || false
-        percent: pmSource.data["Battery"]["Percent"] || 0
-        pluggedIn: pmSource.data["AC Adapter"] ? pmSource.data["AC Adapter"]["Plugged in"] : false
-
-        height: batteryLabel.height
-        width: height
-    }
-
-    PlasmaComponents3.Label {
-        id: batteryLabel
-        font.pointSize: row.fontSize
-        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","%1%", battery.percent)
-        Accessible.name: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Battery at %1%", battery.percent)
-    }
-}
diff --git a/sddm-theme/components/Clock.qml b/sddm-theme/components/Clock.qml
deleted file mode 100644
index fbe0c7c..0000000
--- a/sddm-theme/components/Clock.qml
+++ /dev/null
@@ -1,37 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import QtQuick.Layouts 1.1
-import QtQuick.Controls 2.5 as QQC2
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-ColumnLayout {
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-
-    QQC2.Label {
-        text: Qt.formatTime(timeSource.data["Local"]["DateTime"])
-        color: PlasmaCore.ColorScope.textColor
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        font.pointSize: 48
-        Layout.alignment: Qt.AlignHCenter
-    }
-    QQC2.Label {
-        text: Qt.formatDate(timeSource.data["Local"]["DateTime"], Qt.DefaultLocaleLongDate)
-        color: PlasmaCore.ColorScope.textColor
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        font.pointSize: 24
-        Layout.alignment: Qt.AlignHCenter
-    }
-    PlasmaCore.DataSource {
-        id: timeSource
-        engine: "time"
-        connectedSources: ["Local"]
-        interval: 1000
-    }
-}
diff --git a/sddm-theme/components/SessionManagementScreen.qml b/sddm-theme/components/SessionManagementScreen.qml
deleted file mode 100644
index f002e51..0000000
--- a/sddm-theme/components/SessionManagementScreen.qml
+++ /dev/null
@@ -1,109 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-
-import QtQuick.Layouts 1.1
-import QtQuick.Controls 1.1
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: root
-
-    /*
-     * Any message to be displayed to the user, visible above the text fields
-     */
-    property alias notificationMessage: notificationsLabel.text
-
-    /*
-     * A list of Items (typically ActionButtons) to be shown in a Row beneath the prompts
-     */
-    property alias actionItems: actionItemsLayout.children
-
-    /*
-     * A model with a list of users to show in the view
-     * The following roles should exist:
-     *  - name
-     *  - iconSource
-     *
-     * The following are also handled:
-     *  - vtNumber
-     *  - displayNumber
-     *  - session
-     *  - isTty
-     */
-    property alias userListModel: userListView.model
-
-    /*
-     * Self explanatory
-     */
-    property alias userListCurrentIndex: userListView.currentIndex
-    property alias userListCurrentItem: userListView.currentItem
-    property bool showUserList: true
-
-    property alias userList: userListView
-
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-
-    default property alias _children: innerLayout.children
-
-    UserList {
-        id: userListView
-        visible: showUserList && y > 0
-        anchors {
-            bottom: parent.verticalCenter
-            left: parent.left
-            right: parent.right
-        }
-        fontSize: root.fontSize
-    }
-
-    //goal is to show the prompts, in ~16 grid units high, then the action buttons
-    //but collapse the space between the prompts and actions if there's no room
-    //ui is constrained to 16 grid units wide, or the screen
-    ColumnLayout {
-        id: prompts
-        anchors.top: parent.verticalCenter
-        anchors.topMargin: PlasmaCore.Units.gridUnit * 0.5
-        anchors.left: parent.left
-        anchors.right: parent.right
-        anchors.bottom: parent.bottom
-        PlasmaComponents3.Label {
-            id: notificationsLabel
-            font.pointSize: root.fontSize
-            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
-            Layout.alignment: Qt.AlignHCenter
-            Layout.fillWidth: true
-            horizontalAlignment: Text.AlignHCenter
-            wrapMode: Text.WordWrap
-            font.italic: true
-        }
-        ColumnLayout {
-            Layout.minimumHeight: implicitHeight
-            Layout.maximumHeight: PlasmaCore.Units.gridUnit * 10
-            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
-            Layout.alignment: Qt.AlignHCenter
-            ColumnLayout {
-                id: innerLayout
-                Layout.alignment: Qt.AlignHCenter
-                Layout.fillWidth: true
-            }
-            Item {
-                Layout.fillHeight: true
-            }
-        }
-        Row { //deliberately not rowlayout as I'm not trying to resize child items
-            id: actionItemsLayout
-            spacing: PlasmaCore.Units.largeSpacing / 2
-            Layout.alignment: Qt.AlignHCenter
-        }
-        Item {
-            Layout.fillHeight: true
-        }
-    }
-}
diff --git a/sddm-theme/components/UserDelegate.qml b/sddm-theme/components/UserDelegate.qml
deleted file mode 100644
index 9a823a2..0000000
--- a/sddm-theme/components/UserDelegate.qml
+++ /dev/null
@@ -1,180 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
-    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import QtQuick.Window 2.15
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: wrapper
-
-    // If we're using software rendering, draw outlines instead of shadows
-    // See https://bugs.kde.org/show_bug.cgi?id=398317
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-
-    property bool isCurrent: true
-
-    property string name
-    property string userName
-    property string avatarPath
-    property string iconSource
-    property bool needsPassword
-    property var vtNumber
-    property bool constrainText: true
-    property alias nameFontSize: usernameDelegate.font.pointSize
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-    signal clicked()
-
-    property real faceSize: PlasmaCore.Units.gridUnit * 7
-
-    opacity: isCurrent ? 1.0 : 0.5
-
-    Behavior on opacity {
-        OpacityAnimator {
-            duration: PlasmaCore.Units.longDuration
-        }
-    }
-
-    // Draw a translucent background circle under the user picture
-    Rectangle {
-        anchors.centerIn: imageSource
-        width: imageSource.width - 2 // Subtract to prevent fringing
-        height: width
-        radius: width / 2
-
-        color: PlasmaCore.ColorScope.backgroundColor
-        opacity: 0.6
-    }
-
-    Item {
-        id: imageSource
-        anchors {
-            bottom: usernameDelegate.top
-            bottomMargin: PlasmaCore.Units.largeSpacing
-            horizontalCenter: parent.horizontalCenter
-        }
-        Behavior on width {
-            PropertyAnimation {
-                from: faceSize
-                duration: PlasmaCore.Units.longDuration;
-            }
-        }
-        width: isCurrent ? faceSize : faceSize - PlasmaCore.Units.largeSpacing
-        height: width
-
-        //Image takes priority, taking a full path to a file, if that doesn't exist we show an icon
-        Image {
-            id: face
-            source: wrapper.avatarPath
-            sourceSize: Qt.size(faceSize * Screen.devicePixelRatio, faceSize * Screen.devicePixelRatio)
-            fillMode: Image.PreserveAspectCrop
-            anchors.fill: parent
-        }
-
-        PlasmaCore.IconItem {
-            id: faceIcon
-            source: iconSource
-            visible: (face.status == Image.Error || face.status == Image.Null)
-            anchors.fill: parent
-            anchors.margins: PlasmaCore.Units.gridUnit * 0.5 // because mockup says so...
-            colorGroup: PlasmaCore.ColorScope.colorGroup
-        }
-    }
-
-    ShaderEffect {
-        anchors {
-            bottom: usernameDelegate.top
-            bottomMargin: PlasmaCore.Units.largeSpacing
-            horizontalCenter: parent.horizontalCenter
-        }
-
-        width: imageSource.width
-        height: imageSource.height
-
-        supportsAtlasTextures: true
-
-        property var source: ShaderEffectSource {
-            sourceItem: imageSource
-            // software rendering is just a fallback so we can accept not having a rounded avatar here
-            hideSource: wrapper.GraphicsInfo.api !== GraphicsInfo.Software
-            live: true // otherwise the user in focus will show a blurred avatar
-        }
-
-        property var colorBorder: PlasmaCore.ColorScope.textColor
-
-        //draw a circle with an antialiased border
-        //innerRadius = size of the inner circle with contents
-        //outerRadius = size of the border
-        //blend = area to blend between two colours
-        //all sizes are normalised so 0.5 == half the width of the texture
-
-        //if copying into another project don't forget to connect themeChanged to update()
-        //but in SDDM that's a bit pointless
-        fragmentShader: "
-                        varying highp vec2 qt_TexCoord0;
-                        uniform highp float qt_Opacity;
-                        uniform lowp sampler2D source;
-
-                        uniform lowp vec4 colorBorder;
-                        highp float blend = 0.01;
-                        highp float innerRadius = 0.47;
-                        highp float outerRadius = 0.49;
-                        lowp vec4 colorEmpty = vec4(0.0, 0.0, 0.0, 0.0);
-
-                        void main() {
-                            lowp vec4 colorSource = texture2D(source, qt_TexCoord0.st);
-
-                            highp vec2 m = qt_TexCoord0 - vec2(0.5, 0.5);
-                            highp float dist = sqrt(m.x * m.x + m.y * m.y);
-
-                            if (dist < innerRadius)
-                                gl_FragColor = colorSource;
-                            else if (dist < innerRadius + blend)
-                                gl_FragColor = mix(colorSource, colorBorder, ((dist - innerRadius) / blend));
-                            else if (dist < outerRadius)
-                                gl_FragColor = colorBorder;
-                            else if (dist < outerRadius + blend)
-                                gl_FragColor = mix(colorBorder, colorEmpty, ((dist - outerRadius) / blend));
-                            else
-                                gl_FragColor = colorEmpty ;
-
-                            gl_FragColor = gl_FragColor * qt_Opacity;
-                    }
-        "
-    }
-
-    PlasmaComponents3.Label {
-        id: usernameDelegate
-
-        // Make it bigger than other fonts to match the scale of the avatar better
-        font.pointSize: wrapper.fontSize + 4
-        anchors {
-            bottom: parent.bottom
-            horizontalCenter: parent.horizontalCenter
-        }
-        width: constrainText ? parent.width : implicitWidth
-        text: wrapper.name
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        elide: Text.ElideRight
-        horizontalAlignment: Text.AlignHCenter
-        //make an indication that this has active focus, this only happens when reached with keyboard navigation
-        font.underline: wrapper.activeFocus
-    }
-
-    MouseArea {
-        anchors.fill: parent
-        hoverEnabled: true
-
-        onClicked: wrapper.clicked();
-    }
-
-    Accessible.name: name
-    Accessible.role: Accessible.Button
-    function accessiblePressAction() { wrapper.clicked() }
-}
diff --git a/sddm-theme/components/UserList.qml b/sddm-theme/components/UserList.qml
deleted file mode 100644
index 49f38eb..0000000
--- a/sddm-theme/components/UserList.qml
+++ /dev/null
@@ -1,88 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-ListView {
-    id: view
-    readonly property string selectedUser: currentItem ? currentItem.userName : ""
-    readonly property int userItemWidth: PlasmaCore.Units.gridUnit * 8
-    readonly property int userItemHeight: PlasmaCore.Units.gridUnit * 8
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-
-    implicitHeight: userItemHeight
-
-    activeFocusOnTab : true
-
-    /*
-     * Signals that a user was explicitly selected
-     */
-    signal userSelected;
-
-    orientation: ListView.Horizontal
-    highlightRangeMode: ListView.StrictlyEnforceRange
-
-    //centre align selected item (which implicitly centre aligns the rest
-    preferredHighlightBegin: width/2 - userItemWidth/2
-    preferredHighlightEnd: preferredHighlightBegin
-
-    // Disable flicking if we only have on user (like on the lockscreen)
-    interactive: count > 1
-
-    delegate: UserDelegate {
-        avatarPath: model.icon || ""
-        iconSource: model.iconName || "user-identity"
-        fontSize: view.fontSize
-        vtNumber: model.vtNumber
-        needsPassword: model.needsPassword
-
-        name: {
-            var displayName = model.realName || model.name
-
-            if (model.vtNumber === undefined || model.vtNumber < 0) {
-                return displayName
-            }
-
-            if (!model.session) {
-                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Nobody logged in on that session", "Unused")
-            }
-
-
-            var location = ""
-            if (model.isTty) {
-                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console number", "TTY %1", model.vtNumber)
-            } else if (model.displayNumber) {
-                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console (X display number)", "on TTY %1 (Display %2)", model.vtNumber, model.displayNumber)
-            }
-
-            if (location) {
-                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Username (location)", "%1 (%2)", displayName, location)
-            }
-
-            return displayName
-        }
-
-        userName: model.name
-
-        width: userItemWidth
-        height: userItemHeight
-
-        //if we only have one delegate, we don't need to clip the text as it won't be overlapping with anything
-        constrainText: ListView.view.count > 1
-
-        isCurrent: ListView.isCurrentItem
-
-        onClicked: {
-            ListView.view.currentIndex = index;
-            ListView.view.userSelected();
-        }
-    }
-
-    Keys.onEscapePressed: view.userSelected()
-    Keys.onEnterPressed: view.userSelected()
-    Keys.onReturnPressed: view.userSelected()
-}
diff --git a/sddm-theme/components/VirtualKeyboard.qml b/sddm-theme/components/VirtualKeyboard.qml
deleted file mode 100644
index 503a35b..0000000
--- a/sddm-theme/components/VirtualKeyboard.qml
+++ /dev/null
@@ -1,70 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2017 Martin Gräßlin <mgraesslin@kde.org>
-
-    SPDX-License-Identifier: GPL-2.0-or-later
-*/
-
-import QtQuick 2.5
-import QtQuick.VirtualKeyboard 2.1
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-InputPanel {
-    id: inputPanel
-    property bool activated: false
-    active: activated && Qt.inputMethod.visible
-    width: parent.width
-
-    states: [
-        State {
-            name: "visible"
-            when: inputPanel.active
-            PropertyChanges {
-                target: inputPanel
-                y: inputPanel.parent.height - inputPanel.height
-                opacity: 1
-                visible: true
-            }
-        },
-        State {
-            name: "hidden"
-            when: !inputPanel.active
-            PropertyChanges {
-                target: inputPanel
-                y: inputPanel.parent.height
-                opacity: 0
-                visible:false
-            }
-        }
-    ]
-
-    transitions: [
-        Transition {
-            to: "visible"
-            ParallelAnimation {
-                YAnimator {
-                    // NOTE this is necessary as otherwise the keyboard always starts the transition with Y as 0, due to the internal reparenting happening when becomes active
-                    from: inputPanel.parent.height
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.OutQuad
-                }
-                OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.OutQuad
-                }
-            }
-        },
-        Transition {
-            to: "hidden"
-            ParallelAnimation {
-                YAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.InQuad
-                }
-                OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.InQuad
-                }
-            }
-        }
-    ]
-}
diff --git a/sddm-theme/components/VirtualKeyboard_wayland.qml b/sddm-theme/components/VirtualKeyboard_wayland.qml
deleted file mode 100644
index 1328ee8..0000000
--- a/sddm-theme/components/VirtualKeyboard_wayland.qml
+++ /dev/null
@@ -1,24 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2021 Aleix Pol Gonzalez <aleixpol@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
-*/
-
-import QtQuick 2.15
-import org.kde.plasma.workspace.keyboardlayout 1.0 as Keyboards
-
-Item {
-    id: inputPanel
-    readonly property bool active: Qt.inputMethod.visible
-    property bool activated: false
-    visible: Qt.inputMethod.visible
-
-    x: Qt.inputMethod.keyboardRectangle.x
-    y: Qt.inputMethod.keyboardRectangle.y
-    height: Qt.inputMethod.keyboardRectangle.height
-    width: Qt.inputMethod.keyboardRectangle.width
-
-    onActivatedChanged: if (activated) {
-        Keyboards.KWinVirtualKeyboard.enabled = true
-    }
-}
diff --git a/sddm-theme/components/WallpaperFader.qml b/sddm-theme/components/WallpaperFader.qml
deleted file mode 100644
index 5c885d1..0000000
--- a/sddm-theme/components/WallpaperFader.qml
+++ /dev/null
@@ -1,162 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
-
-    SPDX-License-Identifier: GPL-2.0-or-later
-*/
-
-import QtQuick 2.6
-import QtQuick.Controls 1.1
-import QtQuick.Layouts 1.1
-import QtGraphicalEffects 1.0
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-import org.kde.plasma.private.sessions 2.0
-import "../components"
-
-Item {
-    id: wallpaperFader
-    property Item clock
-    property Item mainStack
-    property Item footer
-    property alias source: wallpaperBlur.source
-    state: lockScreenRoot.uiVisible ? "on" : "off"
-    property real factor: 0
-    readonly property bool lightBackground: Math.max(PlasmaCore.ColorScope.backgroundColor.r, PlasmaCore.ColorScope.backgroundColor.g, PlasmaCore.ColorScope.backgroundColor.b) > 0.5
-
-    property bool alwaysShowClock: typeof config === "undefined" || typeof config.alwaysShowClock === "undefined" || config.alwaysShowClock === true
-
-    Behavior on factor {
-        NumberAnimation {
-            target: wallpaperFader
-            property: "factor"
-            duration: PlasmaCore.Units.veryLongDuration * 2
-            easing.type: Easing.InOutQuad
-        }
-    }
-    FastBlur {
-        id: wallpaperBlur
-        anchors.fill: parent
-        radius: 50 * wallpaperFader.factor
-    }
-    ShaderEffect {
-        id: wallpaperShader
-        anchors.fill: parent
-        supportsAtlasTextures: true
-        property var source: ShaderEffectSource {
-            sourceItem: wallpaperBlur
-            live: true
-            hideSource: true
-            textureMirroring: ShaderEffectSource.NoMirroring
-        }
-
-        readonly property real contrast: 0.65 * wallpaperFader.factor + (1 - wallpaperFader.factor)
-        readonly property real saturation: 1.6 * wallpaperFader.factor + (1 - wallpaperFader.factor)
-        readonly property real intensity: (wallpaperFader.lightBackground ? 1.7 : 0.6) * wallpaperFader.factor + (1 - wallpaperFader.factor)
-
-        readonly property real transl: (1.0 - contrast) / 2.0;
-        readonly property real rval: (1.0 - saturation) * 0.2126;
-        readonly property real gval: (1.0 - saturation) * 0.7152;
-        readonly property real bval: (1.0 - saturation) * 0.0722;
-
-        property var colorMatrix: Qt.matrix4x4(
-            contrast, 0,        0,        0.0,
-            0,        contrast, 0,        0.0,
-            0,        0,        contrast, 0.0,
-            transl,   transl,   transl,   1.0).times(Qt.matrix4x4(
-                rval + saturation, rval,     rval,     0.0,
-                gval,     gval + saturation, gval,     0.0,
-                bval,     bval,     bval + saturation, 0.0,
-                0,        0,        0,        1.0)).times(Qt.matrix4x4(
-                    intensity, 0,         0,         0,
-                    0,         intensity, 0,         0,
-                    0,         0,         intensity, 0,
-                    0,         0,         0,         1
-                ));
-
-
-        fragmentShader: "
-            uniform mediump mat4 colorMatrix;
-            uniform mediump sampler2D source;
-            varying mediump vec2 qt_TexCoord0;
-            uniform lowp float qt_Opacity;
-
-            void main(void)
-            {
-                mediump vec4 tex = texture2D(source, qt_TexCoord0);
-                gl_FragColor = tex * colorMatrix * qt_Opacity;
-            }"
-    }
-
-    states: [
-        State {
-            name: "on"
-            PropertyChanges {
-                target: mainStack
-                opacity: 1
-            }
-            PropertyChanges {
-                target: footer
-                opacity: 1
-            }
-            PropertyChanges {
-                target: wallpaperFader
-                factor: 1
-            }
-            PropertyChanges {
-                target: clock.shadow
-                opacity: 0
-            }
-            PropertyChanges {
-                target: clock
-                opacity: 1
-            }
-        },
-        State {
-            name: "off"
-            PropertyChanges {
-                target: mainStack
-                opacity: 0
-            }
-            PropertyChanges {
-                target: footer
-                opacity: 0
-            }
-            PropertyChanges {
-                target: wallpaperFader
-                factor: 0
-            }
-            PropertyChanges {
-                target: clock.shadow
-                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
-            }
-            PropertyChanges {
-                target: clock
-                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
-            }
-        }
-    ]
-    transitions: [
-        Transition {
-            from: "off"
-            to: "on"
-            //Note: can't use animators as they don't play well with parallelanimations
-            NumberAnimation {
-                targets: [mainStack, footer, clock]
-                property: "opacity"
-                duration: PlasmaCore.Units.veryLongDuration
-                easing.type: Easing.InOutQuad
-            }
-        },
-        Transition {
-            from: "on"
-            to: "off"
-            NumberAnimation {
-                targets: [mainStack, footer, clock]
-                property: "opacity"
-                duration: PlasmaCore.Units.veryLongDuration
-                easing.type: Easing.InOutQuad
-            }
-        }
-    ]
-}
diff --git a/sddm-theme/components/artwork/README.txt b/sddm-theme/components/artwork/README.txt
deleted file mode 100644
index 1885a36..0000000
--- a/sddm-theme/components/artwork/README.txt
+++ /dev/null
@@ -1 +0,0 @@
-After editing SVG files be sure to run currentColorFillFix.sh from plasma-framework
\ No newline at end of file
diff --git a/sddm-theme/components/artwork/logout_primary.svgz b/sddm-theme/components/artwork/logout_primary.svgz
deleted file mode 100644
index 6a9423f..0000000
Binary files a/sddm-theme/components/artwork/logout_primary.svgz and /dev/null differ
diff --git a/sddm-theme/components/artwork/restart_primary.svgz b/sddm-theme/components/artwork/restart_primary.svgz
deleted file mode 100644
index e2312bd..0000000
Binary files a/sddm-theme/components/artwork/restart_primary.svgz and /dev/null differ
diff --git a/sddm-theme/components/artwork/shutdown_primary.svgz b/sddm-theme/components/artwork/shutdown_primary.svgz
deleted file mode 100644
index 1c60152..0000000
Binary files a/sddm-theme/components/artwork/shutdown_primary.svgz and /dev/null differ
diff --git a/sddm-theme/dummydata/config.qml b/sddm-theme/dummydata/config.qml
index f19dabc..d488fe7 100644
--- a/sddm-theme/dummydata/config.qml
+++ b/sddm-theme/dummydata/config.qml
@@ -1,7 +1,8 @@
-import QtQuick 2.0
-QtObject
-{
+import QtQuick 2.15
+
+QtObject {
     property string type: "color"
-    property color color: "#1abc9c" // Maia green
+    property color color: "#1d99f3" // Plasma blue
     property string background: ""
+    property int fontSize: 12
 }
diff --git a/sddm-theme/dummydata/keyboard.qml b/sddm-theme/dummydata/keyboard.qml
index 973d848..4b6a237 100644
--- a/sddm-theme/dummydata/keyboard.qml
+++ b/sddm-theme/dummydata/keyboard.qml
@@ -1,10 +1,9 @@
-import QtQuick 2.0
+import QtQuick 2.15

-QtObject
-{
-    property int currentLayout : 0
-    property var layouts : [
+QtObject {
+    property int currentLayout: 0
+    property var layouts: [
         { shortName: "US", longName: "English" },
-        { shortName: "CZ", longName: "Czech" }
+        { shortName: "CZ", longName: "Czech" },
     ]
 }
diff --git a/sddm-theme/dummydata/screenModel.qml b/sddm-theme/dummydata/screenModel.qml
index 7454341..27a8521 100644
--- a/sddm-theme/dummydata/screenModel.qml
+++ b/sddm-theme/dummydata/screenModel.qml
@@ -1,15 +1,15 @@
-import QtQuick 2.0
+import QtQuick 2.15

 //NOTE: We do not implement a fully working dummy screenModel,
 //we only implement what's needed for a basic multi-monitor test

 ListModel {
     property int primary: 0
-
+
     //Creating multiple ListElement objects doesn't work, because a ListElement can only take numbers,
     //strings, booleans or enums, but we need a rect (it stores the screen size/position).
     //We can insert rects into the ListModel by using this workaround
-    //It's taken from: http://stackoverflow.com/questions/20537417/add-statically-object-to-listmodel
+    //It's taken from: https://stackoverflow.com/questions/20537417/add-statically-object-to-listmodel

     //We create two monitors here, the left one 800x600 and the right one 800x400 pixels
     //To disable a screen delete one of the "append" function calls
diff --git a/sddm-theme/dummydata/sddm.qml b/sddm-theme/dummydata/sddm.qml
index f400d2f..0eb1a40 100644
--- a/sddm-theme/dummydata/sddm.qml
+++ b/sddm-theme/dummydata/sddm.qml
@@ -1,7 +1,6 @@
-import QtQuick 2.2
+import QtQuick 2.15

-Item
-{
+Item {
     signal loginFailed()
     signal loginSucceeded()

@@ -21,7 +20,6 @@ Item
         console.log("SDDM - HYBRID SLEEP");
     }

-
     function login(user, password, sessionIndex) {
         console.log("SDDM - logging in as ", user, password, sessionIndex)

diff --git a/sddm-theme/dummydata/sessionModel.qml b/sddm-theme/dummydata/sessionModel.qml
index 3865bf0..1eb82f0 100644
--- a/sddm-theme/dummydata/sessionModel.qml
+++ b/sddm-theme/dummydata/sessionModel.qml
@@ -1,4 +1,4 @@
-import QtQuick 2.0
+import QtQuick 2.15

 ListModel {
     property int lastIndex: 1
diff --git a/sddm-theme/dummydata/userModel.qml b/sddm-theme/dummydata/userModel.qml
index b4b5ef4..c06de85 100644
--- a/sddm-theme/dummydata/userModel.qml
+++ b/sddm-theme/dummydata/userModel.qml
@@ -1,4 +1,4 @@
-import QtQuick 2.0
+import QtQuick 2.15

 ListModel {

diff --git a/sddm-theme/manjarologo.svgz b/sddm-theme/manjarologo.svgz
new file mode 100644
index 0000000..c8547ea
Binary files /dev/null and b/sddm-theme/manjarologo.svgz differ
diff --git a/sddm-theme/metadata.desktop b/sddm-theme/metadata.desktop
index 5e564aa..9d758a0 100644
--- a/sddm-theme/metadata.desktop
+++ b/sddm-theme/metadata.desktop
@@ -35,15 +35,16 @@ Description[sr@latin]=Tema Breath
 Description[sv]=Breath-tema
 Description[tr]=Breath Teması
 Description[uk]=Тема «Breath»
-Author=Manjaro Team
-Copyright=(c) 2021, Manjaro
+Author=KDE Visual Design Group, Manjaro Team
+Copyright=(c) 2024, Manjaro Team
 License=CC-BY-SA
 Type=sddm-theme
 Version=0.2.0
-Website=https://gitlab.manjaro.org/artwork/themes/breath2
+Website=https://gitlab.manjaro.org/artwork/themes/breath
 Screenshot=preview.png
 MainScript=Main.qml
 ConfigFile=theme.conf
 TranslationsDirectory=translations
 Theme-Id=Breath
 Theme-API=2.0
+QtVersion=6
diff --git a/sddm-theme/theme.conf.cmake b/sddm-theme/theme.conf.cmake
index e536697..1faf1de 100644
--- a/sddm-theme/theme.conf.cmake
+++ b/sddm-theme/theme.conf.cmake
@@ -1,5 +1,6 @@
 [General]
 showlogo=hidden
+logo=${KDE_INSTALL_FULL_DATADIR}/sddm/themes/breath/manjarologo.svgz
 type=image
 color=#1abc9c
 background=${CMAKE_INSTALL_PREFIX}/${WALLPAPER_INSTALL_DIR}/North/contents/images/5120x2880.png

========== CURRENT COMPONENTS FILE ==========
commit 2eb6abb68a8c0eaf599f59e94058816dc8e05323
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Wed Mar 13 19:49:08 2024 +0500

    [sddm-theme] Sync with upstream

diff --git a/sddm-theme/components b/sddm-theme/components
new file mode 100755
index 0000000..0d764f5
--- /dev/null
+++ b/sddm-theme/components
@@ -0,0 +1 @@
+../lnf/org.manjaro.breath/contents/components
diff --git a/sddm-theme/components/ActionButton.qml b/sddm-theme/components/ActionButton.qml
deleted file mode 100644
index af278f6..0000000
--- a/sddm-theme/components/ActionButton.qml
+++ /dev/null
@@ -1,115 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: root
-    property alias text: label.text
-    property alias iconSource: icon.source
-    property alias containsMouse: mouseArea.containsMouse
-    property alias font: label.font
-    property alias labelRendering: label.renderType
-    property alias circleOpacity: iconCircle.opacity
-    property alias circleVisiblity: iconCircle.visible
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 1
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-    signal clicked
-
-    activeFocusOnTab: true
-
-    property int iconSize: PlasmaCore.Units.gridUnit * 3
-
-    implicitWidth: Math.max(iconSize + PlasmaCore.Units.largeSpacing * 2, label.contentWidth)
-    implicitHeight: iconSize + PlasmaCore.Units.smallSpacing + label.implicitHeight
-
-    opacity: activeFocus || containsMouse ? 1 : 0.85
-    Behavior on opacity {
-        PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
-            duration: PlasmaCore.Units.longDuration
-            easing.type: Easing.InOutQuad
-        }
-    }
-
-    Rectangle {
-        id: iconCircle
-        anchors.centerIn: icon
-        width: iconSize + PlasmaCore.Units.smallSpacing
-        height: width
-        radius: width / 2
-        color: softwareRendering ?  PlasmaCore.ColorScope.backgroundColor : PlasmaCore.ColorScope.textColor
-        opacity: root.activeFocus || containsMouse ? (softwareRendering ? 0.8 : 0.15) : (softwareRendering ? 0.6 : 0)
-        Behavior on opacity {
-            PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
-                duration: PlasmaCore.Units.longDuration
-                easing.type: Easing.InOutQuad
-            }
-        }
-    }
-
-    Rectangle {
-        anchors.centerIn: iconCircle
-        width: iconCircle.width
-        height: width
-        radius: width / 2
-        scale: mouseArea.containsPress ? 1 : 0
-        color: PlasmaCore.ColorScope.textColor
-        opacity: 0.15
-        Behavior on scale {
-            PropertyAnimation {
-                duration: PlasmaCore.Units.shortDuration
-                easing.type: Easing.InOutQuart
-            }
-        }
-    }
-
-    PlasmaCore.IconItem {
-        id: icon
-        anchors {
-            top: parent.top
-            horizontalCenter: parent.horizontalCenter
-        }
-        width: iconSize
-        height: iconSize
-
-        colorGroup: PlasmaCore.ColorScope.colorGroup
-        active: mouseArea.containsMouse || root.activeFocus
-    }
-
-    PlasmaComponents3.Label {
-        id: label
-        font.pointSize: root.fontSize
-        anchors {
-            top: icon.bottom
-            topMargin: (softwareRendering ? 1.5 : 1) * PlasmaCore.Units.smallSpacing
-            left: parent.left
-            right: parent.right
-        }
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        horizontalAlignment: Text.AlignHCenter
-        verticalAlignment: Text.AlignTop
-        wrapMode: Text.WordWrap
-        font.underline: root.activeFocus
-    }
-
-    MouseArea {
-        id: mouseArea
-        hoverEnabled: true
-        onClicked: root.clicked()
-        anchors.fill: parent
-    }
-
-    Keys.onEnterPressed: clicked()
-    Keys.onReturnPressed: clicked()
-    Keys.onSpacePressed: clicked()
-
-    Accessible.onPressAction: clicked()
-    Accessible.role: Accessible.Button
-    Accessible.name: label.text
-}
diff --git a/sddm-theme/components/Battery.qml b/sddm-theme/components/Battery.qml
deleted file mode 100644
index 05be535..0000000
--- a/sddm-theme/components/Battery.qml
+++ /dev/null
@@ -1,43 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 Kai Uwe Broulik <kde@privat.broulik.de>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-import org.kde.plasma.workspace.components 2.0 as PW
-
-Row {
-    id: row
-
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize
-
-    spacing: PlasmaCore.Units.smallSpacing
-    visible: pmSource.data["Battery"]["Has Cumulative"]
-
-    PlasmaCore.DataSource {
-        id: pmSource
-        engine: "powermanagement"
-        connectedSources: ["Battery", "AC Adapter"]
-    }
-
-    PW.BatteryIcon {
-        id: battery
-        hasBattery: pmSource.data["Battery"]["Has Battery"] || false
-        percent: pmSource.data["Battery"]["Percent"] || 0
-        pluggedIn: pmSource.data["AC Adapter"] ? pmSource.data["AC Adapter"]["Plugged in"] : false
-
-        height: batteryLabel.height
-        width: height
-    }
-
-    PlasmaComponents3.Label {
-        id: batteryLabel
-        font.pointSize: row.fontSize
-        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","%1%", battery.percent)
-        Accessible.name: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Battery at %1%", battery.percent)
-    }
-}
diff --git a/sddm-theme/components/Clock.qml b/sddm-theme/components/Clock.qml
deleted file mode 100644
index fbe0c7c..0000000
--- a/sddm-theme/components/Clock.qml
+++ /dev/null
@@ -1,37 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import QtQuick.Layouts 1.1
-import QtQuick.Controls 2.5 as QQC2
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-ColumnLayout {
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-
-    QQC2.Label {
-        text: Qt.formatTime(timeSource.data["Local"]["DateTime"])
-        color: PlasmaCore.ColorScope.textColor
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        font.pointSize: 48
-        Layout.alignment: Qt.AlignHCenter
-    }
-    QQC2.Label {
-        text: Qt.formatDate(timeSource.data["Local"]["DateTime"], Qt.DefaultLocaleLongDate)
-        color: PlasmaCore.ColorScope.textColor
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        font.pointSize: 24
-        Layout.alignment: Qt.AlignHCenter
-    }
-    PlasmaCore.DataSource {
-        id: timeSource
-        engine: "time"
-        connectedSources: ["Local"]
-        interval: 1000
-    }
-}
diff --git a/sddm-theme/components/SessionManagementScreen.qml b/sddm-theme/components/SessionManagementScreen.qml
deleted file mode 100644
index f002e51..0000000
--- a/sddm-theme/components/SessionManagementScreen.qml
+++ /dev/null
@@ -1,109 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-
-import QtQuick.Layouts 1.1
-import QtQuick.Controls 1.1
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: root
-
-    /*
-     * Any message to be displayed to the user, visible above the text fields
-     */
-    property alias notificationMessage: notificationsLabel.text
-
-    /*
-     * A list of Items (typically ActionButtons) to be shown in a Row beneath the prompts
-     */
-    property alias actionItems: actionItemsLayout.children
-
-    /*
-     * A model with a list of users to show in the view
-     * The following roles should exist:
-     *  - name
-     *  - iconSource
-     *
-     * The following are also handled:
-     *  - vtNumber
-     *  - displayNumber
-     *  - session
-     *  - isTty
-     */
-    property alias userListModel: userListView.model
-
-    /*
-     * Self explanatory
-     */
-    property alias userListCurrentIndex: userListView.currentIndex
-    property alias userListCurrentItem: userListView.currentItem
-    property bool showUserList: true
-
-    property alias userList: userListView
-
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-
-    default property alias _children: innerLayout.children
-
-    UserList {
-        id: userListView
-        visible: showUserList && y > 0
-        anchors {
-            bottom: parent.verticalCenter
-            left: parent.left
-            right: parent.right
-        }
-        fontSize: root.fontSize
-    }
-
-    //goal is to show the prompts, in ~16 grid units high, then the action buttons
-    //but collapse the space between the prompts and actions if there's no room
-    //ui is constrained to 16 grid units wide, or the screen
-    ColumnLayout {
-        id: prompts
-        anchors.top: parent.verticalCenter
-        anchors.topMargin: PlasmaCore.Units.gridUnit * 0.5
-        anchors.left: parent.left
-        anchors.right: parent.right
-        anchors.bottom: parent.bottom
-        PlasmaComponents3.Label {
-            id: notificationsLabel
-            font.pointSize: root.fontSize
-            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
-            Layout.alignment: Qt.AlignHCenter
-            Layout.fillWidth: true
-            horizontalAlignment: Text.AlignHCenter
-            wrapMode: Text.WordWrap
-            font.italic: true
-        }
-        ColumnLayout {
-            Layout.minimumHeight: implicitHeight
-            Layout.maximumHeight: PlasmaCore.Units.gridUnit * 10
-            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
-            Layout.alignment: Qt.AlignHCenter
-            ColumnLayout {
-                id: innerLayout
-                Layout.alignment: Qt.AlignHCenter
-                Layout.fillWidth: true
-            }
-            Item {
-                Layout.fillHeight: true
-            }
-        }
-        Row { //deliberately not rowlayout as I'm not trying to resize child items
-            id: actionItemsLayout
-            spacing: PlasmaCore.Units.largeSpacing / 2
-            Layout.alignment: Qt.AlignHCenter
-        }
-        Item {
-            Layout.fillHeight: true
-        }
-    }
-}
diff --git a/sddm-theme/components/UserDelegate.qml b/sddm-theme/components/UserDelegate.qml
deleted file mode 100644
index 9a823a2..0000000
--- a/sddm-theme/components/UserDelegate.qml
+++ /dev/null
@@ -1,180 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
-    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.8
-import QtQuick.Window 2.15
-import org.kde.plasma.core 2.0 as PlasmaCore
-import org.kde.plasma.components 3.0 as PlasmaComponents3
-
-Item {
-    id: wrapper
-
-    // If we're using software rendering, draw outlines instead of shadows
-    // See https://bugs.kde.org/show_bug.cgi?id=398317
-    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
-
-    property bool isCurrent: true
-
-    property string name
-    property string userName
-    property string avatarPath
-    property string iconSource
-    property bool needsPassword
-    property var vtNumber
-    property bool constrainText: true
-    property alias nameFontSize: usernameDelegate.font.pointSize
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-    signal clicked()
-
-    property real faceSize: PlasmaCore.Units.gridUnit * 7
-
-    opacity: isCurrent ? 1.0 : 0.5
-
-    Behavior on opacity {
-        OpacityAnimator {
-            duration: PlasmaCore.Units.longDuration
-        }
-    }
-
-    // Draw a translucent background circle under the user picture
-    Rectangle {
-        anchors.centerIn: imageSource
-        width: imageSource.width - 2 // Subtract to prevent fringing
-        height: width
-        radius: width / 2
-
-        color: PlasmaCore.ColorScope.backgroundColor
-        opacity: 0.6
-    }
-
-    Item {
-        id: imageSource
-        anchors {
-            bottom: usernameDelegate.top
-            bottomMargin: PlasmaCore.Units.largeSpacing
-            horizontalCenter: parent.horizontalCenter
-        }
-        Behavior on width {
-            PropertyAnimation {
-                from: faceSize
-                duration: PlasmaCore.Units.longDuration;
-            }
-        }
-        width: isCurrent ? faceSize : faceSize - PlasmaCore.Units.largeSpacing
-        height: width
-
-        //Image takes priority, taking a full path to a file, if that doesn't exist we show an icon
-        Image {
-            id: face
-            source: wrapper.avatarPath
-            sourceSize: Qt.size(faceSize * Screen.devicePixelRatio, faceSize * Screen.devicePixelRatio)
-            fillMode: Image.PreserveAspectCrop
-            anchors.fill: parent
-        }
-
-        PlasmaCore.IconItem {
-            id: faceIcon
-            source: iconSource
-            visible: (face.status == Image.Error || face.status == Image.Null)
-            anchors.fill: parent
-            anchors.margins: PlasmaCore.Units.gridUnit * 0.5 // because mockup says so...
-            colorGroup: PlasmaCore.ColorScope.colorGroup
-        }
-    }
-
-    ShaderEffect {
-        anchors {
-            bottom: usernameDelegate.top
-            bottomMargin: PlasmaCore.Units.largeSpacing
-            horizontalCenter: parent.horizontalCenter
-        }
-
-        width: imageSource.width
-        height: imageSource.height
-
-        supportsAtlasTextures: true
-
-        property var source: ShaderEffectSource {
-            sourceItem: imageSource
-            // software rendering is just a fallback so we can accept not having a rounded avatar here
-            hideSource: wrapper.GraphicsInfo.api !== GraphicsInfo.Software
-            live: true // otherwise the user in focus will show a blurred avatar
-        }
-
-        property var colorBorder: PlasmaCore.ColorScope.textColor
-
-        //draw a circle with an antialiased border
-        //innerRadius = size of the inner circle with contents
-        //outerRadius = size of the border
-        //blend = area to blend between two colours
-        //all sizes are normalised so 0.5 == half the width of the texture
-
-        //if copying into another project don't forget to connect themeChanged to update()
-        //but in SDDM that's a bit pointless
-        fragmentShader: "
-                        varying highp vec2 qt_TexCoord0;
-                        uniform highp float qt_Opacity;
-                        uniform lowp sampler2D source;
-
-                        uniform lowp vec4 colorBorder;
-                        highp float blend = 0.01;
-                        highp float innerRadius = 0.47;
-                        highp float outerRadius = 0.49;
-                        lowp vec4 colorEmpty = vec4(0.0, 0.0, 0.0, 0.0);
-
-                        void main() {
-                            lowp vec4 colorSource = texture2D(source, qt_TexCoord0.st);
-
-                            highp vec2 m = qt_TexCoord0 - vec2(0.5, 0.5);
-                            highp float dist = sqrt(m.x * m.x + m.y * m.y);
-
-                            if (dist < innerRadius)
-                                gl_FragColor = colorSource;
-                            else if (dist < innerRadius + blend)
-                                gl_FragColor = mix(colorSource, colorBorder, ((dist - innerRadius) / blend));
-                            else if (dist < outerRadius)
-                                gl_FragColor = colorBorder;
-                            else if (dist < outerRadius + blend)
-                                gl_FragColor = mix(colorBorder, colorEmpty, ((dist - outerRadius) / blend));
-                            else
-                                gl_FragColor = colorEmpty ;
-
-                            gl_FragColor = gl_FragColor * qt_Opacity;
-                    }
-        "
-    }
-
-    PlasmaComponents3.Label {
-        id: usernameDelegate
-
-        // Make it bigger than other fonts to match the scale of the avatar better
-        font.pointSize: wrapper.fontSize + 4
-        anchors {
-            bottom: parent.bottom
-            horizontalCenter: parent.horizontalCenter
-        }
-        width: constrainText ? parent.width : implicitWidth
-        text: wrapper.name
-        style: softwareRendering ? Text.Outline : Text.Normal
-        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
-        elide: Text.ElideRight
-        horizontalAlignment: Text.AlignHCenter
-        //make an indication that this has active focus, this only happens when reached with keyboard navigation
-        font.underline: wrapper.activeFocus
-    }
-
-    MouseArea {
-        anchors.fill: parent
-        hoverEnabled: true
-
-        onClicked: wrapper.clicked();
-    }
-
-    Accessible.name: name
-    Accessible.role: Accessible.Button
-    function accessiblePressAction() { wrapper.clicked() }
-}
diff --git a/sddm-theme/components/UserList.qml b/sddm-theme/components/UserList.qml
deleted file mode 100644
index 49f38eb..0000000
--- a/sddm-theme/components/UserList.qml
+++ /dev/null
@@ -1,88 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.0-or-later
-*/
-
-import QtQuick 2.2
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-ListView {
-    id: view
-    readonly property string selectedUser: currentItem ? currentItem.userName : ""
-    readonly property int userItemWidth: PlasmaCore.Units.gridUnit * 8
-    readonly property int userItemHeight: PlasmaCore.Units.gridUnit * 8
-    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
-
-    implicitHeight: userItemHeight
-
-    activeFocusOnTab : true
-
-    /*
-     * Signals that a user was explicitly selected
-     */
-    signal userSelected;
-
-    orientation: ListView.Horizontal
-    highlightRangeMode: ListView.StrictlyEnforceRange
-
-    //centre align selected item (which implicitly centre aligns the rest
-    preferredHighlightBegin: width/2 - userItemWidth/2
-    preferredHighlightEnd: preferredHighlightBegin
-
-    // Disable flicking if we only have on user (like on the lockscreen)
-    interactive: count > 1
-
-    delegate: UserDelegate {
-        avatarPath: model.icon || ""
-        iconSource: model.iconName || "user-identity"
-        fontSize: view.fontSize
-        vtNumber: model.vtNumber
-        needsPassword: model.needsPassword
-
-        name: {
-            var displayName = model.realName || model.name
-
-            if (model.vtNumber === undefined || model.vtNumber < 0) {
-                return displayName
-            }
-
-            if (!model.session) {
-                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Nobody logged in on that session", "Unused")
-            }
-
-
-            var location = ""
-            if (model.isTty) {
-                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console number", "TTY %1", model.vtNumber)
-            } else if (model.displayNumber) {
-                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console (X display number)", "on TTY %1 (Display %2)", model.vtNumber, model.displayNumber)
-            }
-
-            if (location) {
-                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Username (location)", "%1 (%2)", displayName, location)
-            }
-
-            return displayName
-        }
-
-        userName: model.name
-
-        width: userItemWidth
-        height: userItemHeight
-
-        //if we only have one delegate, we don't need to clip the text as it won't be overlapping with anything
-        constrainText: ListView.view.count > 1
-
-        isCurrent: ListView.isCurrentItem
-
-        onClicked: {
-            ListView.view.currentIndex = index;
-            ListView.view.userSelected();
-        }
-    }
-
-    Keys.onEscapePressed: view.userSelected()
-    Keys.onEnterPressed: view.userSelected()
-    Keys.onReturnPressed: view.userSelected()
-}
diff --git a/sddm-theme/components/VirtualKeyboard.qml b/sddm-theme/components/VirtualKeyboard.qml
deleted file mode 100644
index 503a35b..0000000
--- a/sddm-theme/components/VirtualKeyboard.qml
+++ /dev/null
@@ -1,70 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2017 Martin Gräßlin <mgraesslin@kde.org>
-
-    SPDX-License-Identifier: GPL-2.0-or-later
-*/
-
-import QtQuick 2.5
-import QtQuick.VirtualKeyboard 2.1
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-InputPanel {
-    id: inputPanel
-    property bool activated: false
-    active: activated && Qt.inputMethod.visible
-    width: parent.width
-
-    states: [
-        State {
-            name: "visible"
-            when: inputPanel.active
-            PropertyChanges {
-                target: inputPanel
-                y: inputPanel.parent.height - inputPanel.height
-                opacity: 1
-                visible: true
-            }
-        },
-        State {
-            name: "hidden"
-            when: !inputPanel.active
-            PropertyChanges {
-                target: inputPanel
-                y: inputPanel.parent.height
-                opacity: 0
-                visible:false
-            }
-        }
-    ]
-
-    transitions: [
-        Transition {
-            to: "visible"
-            ParallelAnimation {
-                YAnimator {
-                    // NOTE this is necessary as otherwise the keyboard always starts the transition with Y as 0, due to the internal reparenting happening when becomes active
-                    from: inputPanel.parent.height
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.OutQuad
-                }
-                OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.OutQuad
-                }
-            }
-        },
-        Transition {
-            to: "hidden"
-            ParallelAnimation {
-                YAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.InQuad
-                }
-                OpacityAnimator {
-                    duration: PlasmaCore.Units.longDuration
-                    easing.type: Easing.InQuad
-                }
-            }
-        }
-    ]
-}
diff --git a/sddm-theme/components/VirtualKeyboard_wayland.qml b/sddm-theme/components/VirtualKeyboard_wayland.qml
deleted file mode 100644
index 1328ee8..0000000
--- a/sddm-theme/components/VirtualKeyboard_wayland.qml
+++ /dev/null
@@ -1,24 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2021 Aleix Pol Gonzalez <aleixpol@kde.org>
-
-    SPDX-License-Identifier: LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
-*/
-
-import QtQuick 2.15
-import org.kde.plasma.workspace.keyboardlayout 1.0 as Keyboards
-
-Item {
-    id: inputPanel
-    readonly property bool active: Qt.inputMethod.visible
-    property bool activated: false
-    visible: Qt.inputMethod.visible
-
-    x: Qt.inputMethod.keyboardRectangle.x
-    y: Qt.inputMethod.keyboardRectangle.y
-    height: Qt.inputMethod.keyboardRectangle.height
-    width: Qt.inputMethod.keyboardRectangle.width
-
-    onActivatedChanged: if (activated) {
-        Keyboards.KWinVirtualKeyboard.enabled = true
-    }
-}
diff --git a/sddm-theme/components/WallpaperFader.qml b/sddm-theme/components/WallpaperFader.qml
deleted file mode 100644
index 5c885d1..0000000
--- a/sddm-theme/components/WallpaperFader.qml
+++ /dev/null
@@ -1,162 +0,0 @@
-/*
-    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
-
-    SPDX-License-Identifier: GPL-2.0-or-later
-*/
-
-import QtQuick 2.6
-import QtQuick.Controls 1.1
-import QtQuick.Layouts 1.1
-import QtGraphicalEffects 1.0
-
-import org.kde.plasma.core 2.0 as PlasmaCore
-
-import org.kde.plasma.private.sessions 2.0
-import "../components"
-
-Item {
-    id: wallpaperFader
-    property Item clock
-    property Item mainStack
-    property Item footer
-    property alias source: wallpaperBlur.source
-    state: lockScreenRoot.uiVisible ? "on" : "off"
-    property real factor: 0
-    readonly property bool lightBackground: Math.max(PlasmaCore.ColorScope.backgroundColor.r, PlasmaCore.ColorScope.backgroundColor.g, PlasmaCore.ColorScope.backgroundColor.b) > 0.5
-
-    property bool alwaysShowClock: typeof config === "undefined" || typeof config.alwaysShowClock === "undefined" || config.alwaysShowClock === true
-
-    Behavior on factor {
-        NumberAnimation {
-            target: wallpaperFader
-            property: "factor"
-            duration: PlasmaCore.Units.veryLongDuration * 2
-            easing.type: Easing.InOutQuad
-        }
-    }
-    FastBlur {
-        id: wallpaperBlur
-        anchors.fill: parent
-        radius: 50 * wallpaperFader.factor
-    }
-    ShaderEffect {
-        id: wallpaperShader
-        anchors.fill: parent
-        supportsAtlasTextures: true
-        property var source: ShaderEffectSource {
-            sourceItem: wallpaperBlur
-            live: true
-            hideSource: true
-            textureMirroring: ShaderEffectSource.NoMirroring
-        }
-
-        readonly property real contrast: 0.65 * wallpaperFader.factor + (1 - wallpaperFader.factor)
-        readonly property real saturation: 1.6 * wallpaperFader.factor + (1 - wallpaperFader.factor)
-        readonly property real intensity: (wallpaperFader.lightBackground ? 1.7 : 0.6) * wallpaperFader.factor + (1 - wallpaperFader.factor)
-
-        readonly property real transl: (1.0 - contrast) / 2.0;
-        readonly property real rval: (1.0 - saturation) * 0.2126;
-        readonly property real gval: (1.0 - saturation) * 0.7152;
-        readonly property real bval: (1.0 - saturation) * 0.0722;
-
-        property var colorMatrix: Qt.matrix4x4(
-            contrast, 0,        0,        0.0,
-            0,        contrast, 0,        0.0,
-            0,        0,        contrast, 0.0,
-            transl,   transl,   transl,   1.0).times(Qt.matrix4x4(
-                rval + saturation, rval,     rval,     0.0,
-                gval,     gval + saturation, gval,     0.0,
-                bval,     bval,     bval + saturation, 0.0,
-                0,        0,        0,        1.0)).times(Qt.matrix4x4(
-                    intensity, 0,         0,         0,
-                    0,         intensity, 0,         0,
-                    0,         0,         intensity, 0,
-                    0,         0,         0,         1
-                ));
-
-
-        fragmentShader: "
-            uniform mediump mat4 colorMatrix;
-            uniform mediump sampler2D source;
-            varying mediump vec2 qt_TexCoord0;
-            uniform lowp float qt_Opacity;
-
-            void main(void)
-            {
-                mediump vec4 tex = texture2D(source, qt_TexCoord0);
-                gl_FragColor = tex * colorMatrix * qt_Opacity;
-            }"
-    }
-
-    states: [
-        State {
-            name: "on"
-            PropertyChanges {
-                target: mainStack
-                opacity: 1
-            }
-            PropertyChanges {
-                target: footer
-                opacity: 1
-            }
-            PropertyChanges {
-                target: wallpaperFader
-                factor: 1
-            }
-            PropertyChanges {
-                target: clock.shadow
-                opacity: 0
-            }
-            PropertyChanges {
-                target: clock
-                opacity: 1
-            }
-        },
-        State {
-            name: "off"
-            PropertyChanges {
-                target: mainStack
-                opacity: 0
-            }
-            PropertyChanges {
-                target: footer
-                opacity: 0
-            }
-            PropertyChanges {
-                target: wallpaperFader
-                factor: 0
-            }
-            PropertyChanges {
-                target: clock.shadow
-                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
-            }
-            PropertyChanges {
-                target: clock
-                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
-            }
-        }
-    ]
-    transitions: [
-        Transition {
-            from: "off"
-            to: "on"
-            //Note: can't use animators as they don't play well with parallelanimations
-            NumberAnimation {
-                targets: [mainStack, footer, clock]
-                property: "opacity"
-                duration: PlasmaCore.Units.veryLongDuration
-                easing.type: Easing.InOutQuad
-            }
-        },
-        Transition {
-            from: "on"
-            to: "off"
-            NumberAnimation {
-                targets: [mainStack, footer, clock]
-                property: "opacity"
-                duration: PlasmaCore.Units.veryLongDuration
-                easing.type: Easing.InOutQuad
-            }
-        }
-    ]
-}
diff --git a/sddm-theme/components/artwork/README.txt b/sddm-theme/components/artwork/README.txt
deleted file mode 100644
index 1885a36..0000000
--- a/sddm-theme/components/artwork/README.txt
+++ /dev/null
@@ -1 +0,0 @@
-After editing SVG files be sure to run currentColorFillFix.sh from plasma-framework
\ No newline at end of file
diff --git a/sddm-theme/components/artwork/logout_primary.svgz b/sddm-theme/components/artwork/logout_primary.svgz
deleted file mode 100644
index 6a9423f..0000000
Binary files a/sddm-theme/components/artwork/logout_primary.svgz and /dev/null differ
diff --git a/sddm-theme/components/artwork/restart_primary.svgz b/sddm-theme/components/artwork/restart_primary.svgz
deleted file mode 100644
index e2312bd..0000000
Binary files a/sddm-theme/components/artwork/restart_primary.svgz and /dev/null differ
diff --git a/sddm-theme/components/artwork/shutdown_primary.svgz b/sddm-theme/components/artwork/shutdown_primary.svgz
deleted file mode 100644
index 1c60152..0000000
Binary files a/sddm-theme/components/artwork/shutdown_primary.svgz and /dev/null differ

commit 59b6057a6af7f77d17b5d93ecdb4ecbeb752aa0b
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Sat Dec 4 15:37:56 2021 +0400

    [sddm-theme] Duplicate components instead of symlinking

diff --git a/sddm-theme/components b/sddm-theme/components
deleted file mode 120000
index 250c60d..0000000
--- a/sddm-theme/components
+++ /dev/null
@@ -1 +0,0 @@
-/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/
\ No newline at end of file
diff --git a/sddm-theme/components/ActionButton.qml b/sddm-theme/components/ActionButton.qml
new file mode 100644
index 0000000..af278f6
--- /dev/null
+++ b/sddm-theme/components/ActionButton.qml
@@ -0,0 +1,115 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: root
+    property alias text: label.text
+    property alias iconSource: icon.source
+    property alias containsMouse: mouseArea.containsMouse
+    property alias font: label.font
+    property alias labelRendering: label.renderType
+    property alias circleOpacity: iconCircle.opacity
+    property alias circleVisiblity: iconCircle.visible
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 1
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+    signal clicked
+
+    activeFocusOnTab: true
+
+    property int iconSize: PlasmaCore.Units.gridUnit * 3
+
+    implicitWidth: Math.max(iconSize + PlasmaCore.Units.largeSpacing * 2, label.contentWidth)
+    implicitHeight: iconSize + PlasmaCore.Units.smallSpacing + label.implicitHeight
+
+    opacity: activeFocus || containsMouse ? 1 : 0.85
+    Behavior on opacity {
+        PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
+            duration: PlasmaCore.Units.longDuration
+            easing.type: Easing.InOutQuad
+        }
+    }
+
+    Rectangle {
+        id: iconCircle
+        anchors.centerIn: icon
+        width: iconSize + PlasmaCore.Units.smallSpacing
+        height: width
+        radius: width / 2
+        color: softwareRendering ?  PlasmaCore.ColorScope.backgroundColor : PlasmaCore.ColorScope.textColor
+        opacity: root.activeFocus || containsMouse ? (softwareRendering ? 0.8 : 0.15) : (softwareRendering ? 0.6 : 0)
+        Behavior on opacity {
+            PropertyAnimation { // OpacityAnimator makes it turn black at random intervals
+                duration: PlasmaCore.Units.longDuration
+                easing.type: Easing.InOutQuad
+            }
+        }
+    }
+
+    Rectangle {
+        anchors.centerIn: iconCircle
+        width: iconCircle.width
+        height: width
+        radius: width / 2
+        scale: mouseArea.containsPress ? 1 : 0
+        color: PlasmaCore.ColorScope.textColor
+        opacity: 0.15
+        Behavior on scale {
+            PropertyAnimation {
+                duration: PlasmaCore.Units.shortDuration
+                easing.type: Easing.InOutQuart
+            }
+        }
+    }
+
+    PlasmaCore.IconItem {
+        id: icon
+        anchors {
+            top: parent.top
+            horizontalCenter: parent.horizontalCenter
+        }
+        width: iconSize
+        height: iconSize
+
+        colorGroup: PlasmaCore.ColorScope.colorGroup
+        active: mouseArea.containsMouse || root.activeFocus
+    }
+
+    PlasmaComponents3.Label {
+        id: label
+        font.pointSize: root.fontSize
+        anchors {
+            top: icon.bottom
+            topMargin: (softwareRendering ? 1.5 : 1) * PlasmaCore.Units.smallSpacing
+            left: parent.left
+            right: parent.right
+        }
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        horizontalAlignment: Text.AlignHCenter
+        verticalAlignment: Text.AlignTop
+        wrapMode: Text.WordWrap
+        font.underline: root.activeFocus
+    }
+
+    MouseArea {
+        id: mouseArea
+        hoverEnabled: true
+        onClicked: root.clicked()
+        anchors.fill: parent
+    }
+
+    Keys.onEnterPressed: clicked()
+    Keys.onReturnPressed: clicked()
+    Keys.onSpacePressed: clicked()
+
+    Accessible.onPressAction: clicked()
+    Accessible.role: Accessible.Button
+    Accessible.name: label.text
+}
diff --git a/sddm-theme/components/Battery.qml b/sddm-theme/components/Battery.qml
new file mode 100644
index 0000000..05be535
--- /dev/null
+++ b/sddm-theme/components/Battery.qml
@@ -0,0 +1,43 @@
+/*
+    SPDX-FileCopyrightText: 2016 Kai Uwe Broulik <kde@privat.broulik.de>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+import org.kde.plasma.workspace.components 2.0 as PW
+
+Row {
+    id: row
+
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize
+
+    spacing: PlasmaCore.Units.smallSpacing
+    visible: pmSource.data["Battery"]["Has Cumulative"]
+
+    PlasmaCore.DataSource {
+        id: pmSource
+        engine: "powermanagement"
+        connectedSources: ["Battery", "AC Adapter"]
+    }
+
+    PW.BatteryIcon {
+        id: battery
+        hasBattery: pmSource.data["Battery"]["Has Battery"] || false
+        percent: pmSource.data["Battery"]["Percent"] || 0
+        pluggedIn: pmSource.data["AC Adapter"] ? pmSource.data["AC Adapter"]["Plugged in"] : false
+
+        height: batteryLabel.height
+        width: height
+    }
+
+    PlasmaComponents3.Label {
+        id: batteryLabel
+        font.pointSize: row.fontSize
+        text: i18nd("plasma_lookandfeel_org.kde.lookandfeel","%1%", battery.percent)
+        Accessible.name: i18nd("plasma_lookandfeel_org.kde.lookandfeel","Battery at %1%", battery.percent)
+    }
+}
diff --git a/sddm-theme/components/Clock.qml b/sddm-theme/components/Clock.qml
new file mode 100644
index 0000000..fbe0c7c
--- /dev/null
+++ b/sddm-theme/components/Clock.qml
@@ -0,0 +1,37 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import QtQuick.Layouts 1.1
+import QtQuick.Controls 2.5 as QQC2
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+ColumnLayout {
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+
+    QQC2.Label {
+        text: Qt.formatTime(timeSource.data["Local"]["DateTime"])
+        color: PlasmaCore.ColorScope.textColor
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        font.pointSize: 48
+        Layout.alignment: Qt.AlignHCenter
+    }
+    QQC2.Label {
+        text: Qt.formatDate(timeSource.data["Local"]["DateTime"], Qt.DefaultLocaleLongDate)
+        color: PlasmaCore.ColorScope.textColor
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        font.pointSize: 24
+        Layout.alignment: Qt.AlignHCenter
+    }
+    PlasmaCore.DataSource {
+        id: timeSource
+        engine: "time"
+        connectedSources: ["Local"]
+        interval: 1000
+    }
+}
diff --git a/sddm-theme/components/SessionManagementScreen.qml b/sddm-theme/components/SessionManagementScreen.qml
new file mode 100644
index 0000000..f002e51
--- /dev/null
+++ b/sddm-theme/components/SessionManagementScreen.qml
@@ -0,0 +1,109 @@
+/*
+    SPDX-FileCopyrightText: 2016 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+
+import QtQuick.Layouts 1.1
+import QtQuick.Controls 1.1
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: root
+
+    /*
+     * Any message to be displayed to the user, visible above the text fields
+     */
+    property alias notificationMessage: notificationsLabel.text
+
+    /*
+     * A list of Items (typically ActionButtons) to be shown in a Row beneath the prompts
+     */
+    property alias actionItems: actionItemsLayout.children
+
+    /*
+     * A model with a list of users to show in the view
+     * The following roles should exist:
+     *  - name
+     *  - iconSource
+     *
+     * The following are also handled:
+     *  - vtNumber
+     *  - displayNumber
+     *  - session
+     *  - isTty
+     */
+    property alias userListModel: userListView.model
+
+    /*
+     * Self explanatory
+     */
+    property alias userListCurrentIndex: userListView.currentIndex
+    property alias userListCurrentItem: userListView.currentItem
+    property bool showUserList: true
+
+    property alias userList: userListView
+
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+
+    default property alias _children: innerLayout.children
+
+    UserList {
+        id: userListView
+        visible: showUserList && y > 0
+        anchors {
+            bottom: parent.verticalCenter
+            left: parent.left
+            right: parent.right
+        }
+        fontSize: root.fontSize
+    }
+
+    //goal is to show the prompts, in ~16 grid units high, then the action buttons
+    //but collapse the space between the prompts and actions if there's no room
+    //ui is constrained to 16 grid units wide, or the screen
+    ColumnLayout {
+        id: prompts
+        anchors.top: parent.verticalCenter
+        anchors.topMargin: PlasmaCore.Units.gridUnit * 0.5
+        anchors.left: parent.left
+        anchors.right: parent.right
+        anchors.bottom: parent.bottom
+        PlasmaComponents3.Label {
+            id: notificationsLabel
+            font.pointSize: root.fontSize
+            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
+            Layout.alignment: Qt.AlignHCenter
+            Layout.fillWidth: true
+            horizontalAlignment: Text.AlignHCenter
+            wrapMode: Text.WordWrap
+            font.italic: true
+        }
+        ColumnLayout {
+            Layout.minimumHeight: implicitHeight
+            Layout.maximumHeight: PlasmaCore.Units.gridUnit * 10
+            Layout.maximumWidth: PlasmaCore.Units.gridUnit * 16
+            Layout.alignment: Qt.AlignHCenter
+            ColumnLayout {
+                id: innerLayout
+                Layout.alignment: Qt.AlignHCenter
+                Layout.fillWidth: true
+            }
+            Item {
+                Layout.fillHeight: true
+            }
+        }
+        Row { //deliberately not rowlayout as I'm not trying to resize child items
+            id: actionItemsLayout
+            spacing: PlasmaCore.Units.largeSpacing / 2
+            Layout.alignment: Qt.AlignHCenter
+        }
+        Item {
+            Layout.fillHeight: true
+        }
+    }
+}
diff --git a/sddm-theme/components/UserDelegate.qml b/sddm-theme/components/UserDelegate.qml
new file mode 100644
index 0000000..9a823a2
--- /dev/null
+++ b/sddm-theme/components/UserDelegate.qml
@@ -0,0 +1,180 @@
+/*
+    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
+    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.8
+import QtQuick.Window 2.15
+import org.kde.plasma.core 2.0 as PlasmaCore
+import org.kde.plasma.components 3.0 as PlasmaComponents3
+
+Item {
+    id: wrapper
+
+    // If we're using software rendering, draw outlines instead of shadows
+    // See https://bugs.kde.org/show_bug.cgi?id=398317
+    readonly property bool softwareRendering: GraphicsInfo.api === GraphicsInfo.Software
+
+    property bool isCurrent: true
+
+    property string name
+    property string userName
+    property string avatarPath
+    property string iconSource
+    property bool needsPassword
+    property var vtNumber
+    property bool constrainText: true
+    property alias nameFontSize: usernameDelegate.font.pointSize
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+    signal clicked()
+
+    property real faceSize: PlasmaCore.Units.gridUnit * 7
+
+    opacity: isCurrent ? 1.0 : 0.5
+
+    Behavior on opacity {
+        OpacityAnimator {
+            duration: PlasmaCore.Units.longDuration
+        }
+    }
+
+    // Draw a translucent background circle under the user picture
+    Rectangle {
+        anchors.centerIn: imageSource
+        width: imageSource.width - 2 // Subtract to prevent fringing
+        height: width
+        radius: width / 2
+
+        color: PlasmaCore.ColorScope.backgroundColor
+        opacity: 0.6
+    }
+
+    Item {
+        id: imageSource
+        anchors {
+            bottom: usernameDelegate.top
+            bottomMargin: PlasmaCore.Units.largeSpacing
+            horizontalCenter: parent.horizontalCenter
+        }
+        Behavior on width {
+            PropertyAnimation {
+                from: faceSize
+                duration: PlasmaCore.Units.longDuration;
+            }
+        }
+        width: isCurrent ? faceSize : faceSize - PlasmaCore.Units.largeSpacing
+        height: width
+
+        //Image takes priority, taking a full path to a file, if that doesn't exist we show an icon
+        Image {
+            id: face
+            source: wrapper.avatarPath
+            sourceSize: Qt.size(faceSize * Screen.devicePixelRatio, faceSize * Screen.devicePixelRatio)
+            fillMode: Image.PreserveAspectCrop
+            anchors.fill: parent
+        }
+
+        PlasmaCore.IconItem {
+            id: faceIcon
+            source: iconSource
+            visible: (face.status == Image.Error || face.status == Image.Null)
+            anchors.fill: parent
+            anchors.margins: PlasmaCore.Units.gridUnit * 0.5 // because mockup says so...
+            colorGroup: PlasmaCore.ColorScope.colorGroup
+        }
+    }
+
+    ShaderEffect {
+        anchors {
+            bottom: usernameDelegate.top
+            bottomMargin: PlasmaCore.Units.largeSpacing
+            horizontalCenter: parent.horizontalCenter
+        }
+
+        width: imageSource.width
+        height: imageSource.height
+
+        supportsAtlasTextures: true
+
+        property var source: ShaderEffectSource {
+            sourceItem: imageSource
+            // software rendering is just a fallback so we can accept not having a rounded avatar here
+            hideSource: wrapper.GraphicsInfo.api !== GraphicsInfo.Software
+            live: true // otherwise the user in focus will show a blurred avatar
+        }
+
+        property var colorBorder: PlasmaCore.ColorScope.textColor
+
+        //draw a circle with an antialiased border
+        //innerRadius = size of the inner circle with contents
+        //outerRadius = size of the border
+        //blend = area to blend between two colours
+        //all sizes are normalised so 0.5 == half the width of the texture
+
+        //if copying into another project don't forget to connect themeChanged to update()
+        //but in SDDM that's a bit pointless
+        fragmentShader: "
+                        varying highp vec2 qt_TexCoord0;
+                        uniform highp float qt_Opacity;
+                        uniform lowp sampler2D source;
+
+                        uniform lowp vec4 colorBorder;
+                        highp float blend = 0.01;
+                        highp float innerRadius = 0.47;
+                        highp float outerRadius = 0.49;
+                        lowp vec4 colorEmpty = vec4(0.0, 0.0, 0.0, 0.0);
+
+                        void main() {
+                            lowp vec4 colorSource = texture2D(source, qt_TexCoord0.st);
+
+                            highp vec2 m = qt_TexCoord0 - vec2(0.5, 0.5);
+                            highp float dist = sqrt(m.x * m.x + m.y * m.y);
+
+                            if (dist < innerRadius)
+                                gl_FragColor = colorSource;
+                            else if (dist < innerRadius + blend)
+                                gl_FragColor = mix(colorSource, colorBorder, ((dist - innerRadius) / blend));
+                            else if (dist < outerRadius)
+                                gl_FragColor = colorBorder;
+                            else if (dist < outerRadius + blend)
+                                gl_FragColor = mix(colorBorder, colorEmpty, ((dist - outerRadius) / blend));
+                            else
+                                gl_FragColor = colorEmpty ;
+
+                            gl_FragColor = gl_FragColor * qt_Opacity;
+                    }
+        "
+    }
+
+    PlasmaComponents3.Label {
+        id: usernameDelegate
+
+        // Make it bigger than other fonts to match the scale of the avatar better
+        font.pointSize: wrapper.fontSize + 4
+        anchors {
+            bottom: parent.bottom
+            horizontalCenter: parent.horizontalCenter
+        }
+        width: constrainText ? parent.width : implicitWidth
+        text: wrapper.name
+        style: softwareRendering ? Text.Outline : Text.Normal
+        styleColor: softwareRendering ? PlasmaCore.ColorScope.backgroundColor : "transparent" //no outline, doesn't matter
+        elide: Text.ElideRight
+        horizontalAlignment: Text.AlignHCenter
+        //make an indication that this has active focus, this only happens when reached with keyboard navigation
+        font.underline: wrapper.activeFocus
+    }
+
+    MouseArea {
+        anchors.fill: parent
+        hoverEnabled: true
+
+        onClicked: wrapper.clicked();
+    }
+
+    Accessible.name: name
+    Accessible.role: Accessible.Button
+    function accessiblePressAction() { wrapper.clicked() }
+}
diff --git a/sddm-theme/components/UserList.qml b/sddm-theme/components/UserList.qml
new file mode 100644
index 0000000..49f38eb
--- /dev/null
+++ b/sddm-theme/components/UserList.qml
@@ -0,0 +1,88 @@
+/*
+    SPDX-FileCopyrightText: 2014 David Edmundson <davidedmundson@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.0-or-later
+*/
+
+import QtQuick 2.2
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+ListView {
+    id: view
+    readonly property string selectedUser: currentItem ? currentItem.userName : ""
+    readonly property int userItemWidth: PlasmaCore.Units.gridUnit * 8
+    readonly property int userItemHeight: PlasmaCore.Units.gridUnit * 8
+    property int fontSize: PlasmaCore.Theme.defaultFont.pointSize + 2
+
+    implicitHeight: userItemHeight
+
+    activeFocusOnTab : true
+
+    /*
+     * Signals that a user was explicitly selected
+     */
+    signal userSelected;
+
+    orientation: ListView.Horizontal
+    highlightRangeMode: ListView.StrictlyEnforceRange
+
+    //centre align selected item (which implicitly centre aligns the rest
+    preferredHighlightBegin: width/2 - userItemWidth/2
+    preferredHighlightEnd: preferredHighlightBegin
+
+    // Disable flicking if we only have on user (like on the lockscreen)
+    interactive: count > 1
+
+    delegate: UserDelegate {
+        avatarPath: model.icon || ""
+        iconSource: model.iconName || "user-identity"
+        fontSize: view.fontSize
+        vtNumber: model.vtNumber
+        needsPassword: model.needsPassword
+
+        name: {
+            var displayName = model.realName || model.name
+
+            if (model.vtNumber === undefined || model.vtNumber < 0) {
+                return displayName
+            }
+
+            if (!model.session) {
+                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Nobody logged in on that session", "Unused")
+            }
+
+
+            var location = ""
+            if (model.isTty) {
+                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console number", "TTY %1", model.vtNumber)
+            } else if (model.displayNumber) {
+                location = i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "User logged in on console (X display number)", "on TTY %1 (Display %2)", model.vtNumber, model.displayNumber)
+            }
+
+            if (location) {
+                return i18ndc("plasma_lookandfeel_org.kde.lookandfeel", "Username (location)", "%1 (%2)", displayName, location)
+            }
+
+            return displayName
+        }
+
+        userName: model.name
+
+        width: userItemWidth
+        height: userItemHeight
+
+        //if we only have one delegate, we don't need to clip the text as it won't be overlapping with anything
+        constrainText: ListView.view.count > 1
+
+        isCurrent: ListView.isCurrentItem
+
+        onClicked: {
+            ListView.view.currentIndex = index;
+            ListView.view.userSelected();
+        }
+    }
+
+    Keys.onEscapePressed: view.userSelected()
+    Keys.onEnterPressed: view.userSelected()
+    Keys.onReturnPressed: view.userSelected()
+}
diff --git a/sddm-theme/components/VirtualKeyboard.qml b/sddm-theme/components/VirtualKeyboard.qml
new file mode 100644
index 0000000..503a35b
--- /dev/null
+++ b/sddm-theme/components/VirtualKeyboard.qml
@@ -0,0 +1,70 @@
+/*
+    SPDX-FileCopyrightText: 2017 Martin Gräßlin <mgraesslin@kde.org>
+
+    SPDX-License-Identifier: GPL-2.0-or-later
+*/
+
+import QtQuick 2.5
+import QtQuick.VirtualKeyboard 2.1
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+InputPanel {
+    id: inputPanel
+    property bool activated: false
+    active: activated && Qt.inputMethod.visible
+    width: parent.width
+
+    states: [
+        State {
+            name: "visible"
+            when: inputPanel.active
+            PropertyChanges {
+                target: inputPanel
+                y: inputPanel.parent.height - inputPanel.height
+                opacity: 1
+                visible: true
+            }
+        },
+        State {
+            name: "hidden"
+            when: !inputPanel.active
+            PropertyChanges {
+                target: inputPanel
+                y: inputPanel.parent.height
+                opacity: 0
+                visible:false
+            }
+        }
+    ]
+
+    transitions: [
+        Transition {
+            to: "visible"
+            ParallelAnimation {
+                YAnimator {
+                    // NOTE this is necessary as otherwise the keyboard always starts the transition with Y as 0, due to the internal reparenting happening when becomes active
+                    from: inputPanel.parent.height
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.OutQuad
+                }
+                OpacityAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.OutQuad
+                }
+            }
+        },
+        Transition {
+            to: "hidden"
+            ParallelAnimation {
+                YAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.InQuad
+                }
+                OpacityAnimator {
+                    duration: PlasmaCore.Units.longDuration
+                    easing.type: Easing.InQuad
+                }
+            }
+        }
+    ]
+}
diff --git a/sddm-theme/components/VirtualKeyboard_wayland.qml b/sddm-theme/components/VirtualKeyboard_wayland.qml
new file mode 100644
index 0000000..1328ee8
--- /dev/null
+++ b/sddm-theme/components/VirtualKeyboard_wayland.qml
@@ -0,0 +1,24 @@
+/*
+    SPDX-FileCopyrightText: 2021 Aleix Pol Gonzalez <aleixpol@kde.org>
+
+    SPDX-License-Identifier: LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
+*/
+
+import QtQuick 2.15
+import org.kde.plasma.workspace.keyboardlayout 1.0 as Keyboards
+
+Item {
+    id: inputPanel
+    readonly property bool active: Qt.inputMethod.visible
+    property bool activated: false
+    visible: Qt.inputMethod.visible
+
+    x: Qt.inputMethod.keyboardRectangle.x
+    y: Qt.inputMethod.keyboardRectangle.y
+    height: Qt.inputMethod.keyboardRectangle.height
+    width: Qt.inputMethod.keyboardRectangle.width
+
+    onActivatedChanged: if (activated) {
+        Keyboards.KWinVirtualKeyboard.enabled = true
+    }
+}
diff --git a/sddm-theme/components/WallpaperFader.qml b/sddm-theme/components/WallpaperFader.qml
new file mode 100644
index 0000000..5c885d1
--- /dev/null
+++ b/sddm-theme/components/WallpaperFader.qml
@@ -0,0 +1,162 @@
+/*
+    SPDX-FileCopyrightText: 2014 Aleix Pol Gonzalez <aleixpol@blue-systems.com>
+
+    SPDX-License-Identifier: GPL-2.0-or-later
+*/
+
+import QtQuick 2.6
+import QtQuick.Controls 1.1
+import QtQuick.Layouts 1.1
+import QtGraphicalEffects 1.0
+
+import org.kde.plasma.core 2.0 as PlasmaCore
+
+import org.kde.plasma.private.sessions 2.0
+import "../components"
+
+Item {
+    id: wallpaperFader
+    property Item clock
+    property Item mainStack
+    property Item footer
+    property alias source: wallpaperBlur.source
+    state: lockScreenRoot.uiVisible ? "on" : "off"
+    property real factor: 0
+    readonly property bool lightBackground: Math.max(PlasmaCore.ColorScope.backgroundColor.r, PlasmaCore.ColorScope.backgroundColor.g, PlasmaCore.ColorScope.backgroundColor.b) > 0.5
+
+    property bool alwaysShowClock: typeof config === "undefined" || typeof config.alwaysShowClock === "undefined" || config.alwaysShowClock === true
+
+    Behavior on factor {
+        NumberAnimation {
+            target: wallpaperFader
+            property: "factor"
+            duration: PlasmaCore.Units.veryLongDuration * 2
+            easing.type: Easing.InOutQuad
+        }
+    }
+    FastBlur {
+        id: wallpaperBlur
+        anchors.fill: parent
+        radius: 50 * wallpaperFader.factor
+    }
+    ShaderEffect {
+        id: wallpaperShader
+        anchors.fill: parent
+        supportsAtlasTextures: true
+        property var source: ShaderEffectSource {
+            sourceItem: wallpaperBlur
+            live: true
+            hideSource: true
+            textureMirroring: ShaderEffectSource.NoMirroring
+        }
+
+        readonly property real contrast: 0.65 * wallpaperFader.factor + (1 - wallpaperFader.factor)
+        readonly property real saturation: 1.6 * wallpaperFader.factor + (1 - wallpaperFader.factor)
+        readonly property real intensity: (wallpaperFader.lightBackground ? 1.7 : 0.6) * wallpaperFader.factor + (1 - wallpaperFader.factor)
+
+        readonly property real transl: (1.0 - contrast) / 2.0;
+        readonly property real rval: (1.0 - saturation) * 0.2126;
+        readonly property real gval: (1.0 - saturation) * 0.7152;
+        readonly property real bval: (1.0 - saturation) * 0.0722;
+
+        property var colorMatrix: Qt.matrix4x4(
+            contrast, 0,        0,        0.0,
+            0,        contrast, 0,        0.0,
+            0,        0,        contrast, 0.0,
+            transl,   transl,   transl,   1.0).times(Qt.matrix4x4(
+                rval + saturation, rval,     rval,     0.0,
+                gval,     gval + saturation, gval,     0.0,
+                bval,     bval,     bval + saturation, 0.0,
+                0,        0,        0,        1.0)).times(Qt.matrix4x4(
+                    intensity, 0,         0,         0,
+                    0,         intensity, 0,         0,
+                    0,         0,         intensity, 0,
+                    0,         0,         0,         1
+                ));
+
+
+        fragmentShader: "
+            uniform mediump mat4 colorMatrix;
+            uniform mediump sampler2D source;
+            varying mediump vec2 qt_TexCoord0;
+            uniform lowp float qt_Opacity;
+
+            void main(void)
+            {
+                mediump vec4 tex = texture2D(source, qt_TexCoord0);
+                gl_FragColor = tex * colorMatrix * qt_Opacity;
+            }"
+    }
+
+    states: [
+        State {
+            name: "on"
+            PropertyChanges {
+                target: mainStack
+                opacity: 1
+            }
+            PropertyChanges {
+                target: footer
+                opacity: 1
+            }
+            PropertyChanges {
+                target: wallpaperFader
+                factor: 1
+            }
+            PropertyChanges {
+                target: clock.shadow
+                opacity: 0
+            }
+            PropertyChanges {
+                target: clock
+                opacity: 1
+            }
+        },
+        State {
+            name: "off"
+            PropertyChanges {
+                target: mainStack
+                opacity: 0
+            }
+            PropertyChanges {
+                target: footer
+                opacity: 0
+            }
+            PropertyChanges {
+                target: wallpaperFader
+                factor: 0
+            }
+            PropertyChanges {
+                target: clock.shadow
+                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
+            }
+            PropertyChanges {
+                target: clock
+                opacity: wallpaperFader.alwaysShowClock ? 1 : 0
+            }
+        }
+    ]
+    transitions: [
+        Transition {
+            from: "off"
+            to: "on"
+            //Note: can't use animators as they don't play well with parallelanimations
+            NumberAnimation {
+                targets: [mainStack, footer, clock]
+                property: "opacity"
+                duration: PlasmaCore.Units.veryLongDuration
+                easing.type: Easing.InOutQuad
+            }
+        },
+        Transition {
+            from: "on"
+            to: "off"
+            NumberAnimation {
+                targets: [mainStack, footer, clock]
+                property: "opacity"
+                duration: PlasmaCore.Units.veryLongDuration
+                easing.type: Easing.InOutQuad
+            }
+        }
+    ]
+}
diff --git a/sddm-theme/components/artwork/README.txt b/sddm-theme/components/artwork/README.txt
new file mode 100644
index 0000000..1885a36
--- /dev/null
+++ b/sddm-theme/components/artwork/README.txt
@@ -0,0 +1 @@
+After editing SVG files be sure to run currentColorFillFix.sh from plasma-framework
\ No newline at end of file
diff --git a/sddm-theme/components/artwork/logout_primary.svgz b/sddm-theme/components/artwork/logout_primary.svgz
new file mode 100644
index 0000000..6a9423f
Binary files /dev/null and b/sddm-theme/components/artwork/logout_primary.svgz differ
diff --git a/sddm-theme/components/artwork/restart_primary.svgz b/sddm-theme/components/artwork/restart_primary.svgz
new file mode 100644
index 0000000..e2312bd
Binary files /dev/null and b/sddm-theme/components/artwork/restart_primary.svgz differ
diff --git a/sddm-theme/components/artwork/shutdown_primary.svgz b/sddm-theme/components/artwork/shutdown_primary.svgz
new file mode 100644
index 0000000..1c60152
Binary files /dev/null and b/sddm-theme/components/artwork/shutdown_primary.svgz differ

commit cd33946c244143d1bcdbfa9b32101223a29ff7cc
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Wed Nov 24 05:35:52 2021 +0400

    [sddm] Return dummy components

diff --git a/sddm-theme/components b/sddm-theme/components
new file mode 120000
index 0000000..250c60d
--- /dev/null
+++ b/sddm-theme/components
@@ -0,0 +1 @@
+/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/
\ No newline at end of file
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 1 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (1/1), 72 bytes | 72.00 KiB/s, done.

commit 380787a00e14dbe38151fe52ac04cffc13be10cd
Author: Artem Grinev <agrinev@manjaro.org>
Date:   Wed Nov 24 03:55:41 2021 +0400

    [colors] Fix breath light naming

diff --git a/sddm-theme/components b/sddm-theme/components
deleted file mode 120000
index 6019cc9..0000000
--- a/sddm-theme/components
+++ /dev/null
@@ -1 +0,0 @@
-../lookandfeel/contents/components/
\ No newline at end of file

commit a2209ef314a9b4afc61d82b75fcb2df33544d61f
Author: Bernhard Landauer <oberon@manjaro.org>
Date:   Tue Nov 5 22:00:09 2019 +0100

    initial commit

diff --git a/sddm-theme/components b/sddm-theme/components
new file mode 120000
index 0000000..6019cc9
--- /dev/null
+++ b/sddm-theme/components
@@ -0,0 +1 @@
+../lookandfeel/contents/components/
\ No newline at end of file

========== ROOT CMAKE ==========
sed: can't read CMakeLists.txt: No such file or directory

========== ALL CMAKE FILES ==========
Bibotto@Bibotto:/tmp/breath-upstream-forgejo$

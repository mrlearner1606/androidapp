[app]
title = SensorCheckApp
package.name = sensorcheckapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer
android.permissions = 
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# buildozer.spec
android.ndk_path = /home/codespace/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/codespace/.buildozer/android/platform/android-sdk
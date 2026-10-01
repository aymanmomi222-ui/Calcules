[app]

# (str) Title of your application
title = آلة حاسبة

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android)
package.domain = org.bassam

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application is fullscreen
fullscreen = 0

# (str) Android API level
android.api = 35

# (str) Android minimum API level
android.minapi = 21

# (str) Android NDK version
android.ndk = 27c

# (str) Android architecture(s)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Android app to be private
android.allow_backup = True

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android activity class name
android.activity_class_name = org.kivy.android.PythonActivity

# (str) Python-for-Android branch to use
p4a.branch = master

# (str) Android app theme
android.apptheme = "@android:style/Theme.Material.Light.NoActionBar"

# (str) Log level
log_level = 2

[buildozer]

# (str) Build output directory
build_dir = .buildozer

# (str) Build artifact directory
bin_dir = bin

# (str) Warn for running as root
warn_on_root = 1

# Android-Activity-Tester
Enumerates all exported activities and launch them one by one using adb.

According to the [Android documentation](https://developer.android.com/guide/topics/manifest/activity-element#exported), an activity is considered exported in the following two cases:

* If the activity has `android:exported="true"` attribute in its definition.
* If `android:exported` is not defined at all then it should have at least one intent-filter in it.

In order to use this tool, specify an Android Manifest file, e.g.:

```
~ python3 android_activity_tester.py -m <path-to-decompiled-directory>/AndroidManifest.xml
```

Note that you can extract the manifest file from an APK using `apktool`, for example.
# Android-Activity-Tester
Enumerates all exported activities and launch them one by one using adb.

According to the android developer docs, an activity is considered exported in the following two cases:

* If the activity has `android:exported="true"` attribute in its definition.
* If `android:exported` is not defined at all then it should have at least one intent-filter in it.

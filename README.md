# Android-Activity-Tester
Enumerates all exported and non-exported activities, launches exported activities one by one using `adb`, and then non-exported activities as `root`.

According to the [Android documentation](https://developer.android.com/guide/topics/manifest/activity-element#exported), an activity is considered exported in the following two cases:

* If the activity declares the `android:exported="true"` attribute in its definition;
* If `android:exported` is not defined but the activity includes at least one intent-filter.

In order to use this tool, you need to specify the path to the app's `AndroidManifest.xml` file, as well as the package identifier:

```
~ python3 android_activity_tester.py \
  -m <path-to-decompiled-directory>/AndroidManifest.xml \
  -p <package-identifier>
```

Note that you can extract the manifest file from an APK using `apktool`, e.g.:

```
~ apktool d com.twitter.android.apk

[...]

~ python3 Android-Activity-Tester/android_activity_tester.py \
-m com.twitter.android/AndroidManifest.xml \
-p com.twitter.android

=================== Explicitly/Implicitly Exported Activities =================== 
com.twitter.app.dm.DMActivity
com.twitter.android.StartActivity
com.twitter.android.AuthorizeAppActivity
com.twitter.android.SingleSignOnActivity
com.twitter.app.profiles.ProfileActivity
[...]

=================== Non-Exported Activities ===================
com.twitter.android.login.LoginActivity
com.twitter.android.login.LoginChallengeActivity
com.twitter.android.login.WebauthnChallengeActivity
com.twitter.android.login.PasswordResetActivity
com.twitter.notifications.settings.NotificationFiltersSettingsActivity
[...]

=================== Launch Exported Activities with ADB ===================
Starting: Intent { cmp=com.twitter.android/com.twitter.app.dm.DMActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.StartActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.AuthorizeAppActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.SingleSignOnActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/com.twitter.app.profiles.ProfileActivity }
Press Enter to continue...
[...]

=================== Launch Non-Exported Activities with ADB Root ===================
restarting adbd as root
Starting: Intent { cmp=com.twitter.android/.login.LoginActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.login.LoginChallengeActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.login.WebauthnChallengeActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.login.PasswordResetActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/com.twitter.notifications.settings.NotificationFiltersSettingsActivity }
Press Enter to continue...
[...]

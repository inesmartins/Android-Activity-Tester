# Android-Activity-Tester
Enumerates all exported and non-exported activities, launches exported activities one by one using `adb`.

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

~ python3 android_activity_tester.py \
 -m com.twitter.android/AndroidManifest.xml \
 -p com.twitter.android

=================== Exported =================== 
com.twitter.app.deeplink.UrlInterpreterActivity
com.twitter.android.StartActivity
com.twitter.android.settings.SettingsActivity
com.twitter.app.fleets.page.FleetThreadActivity
com.twitter.app.fleets.stickers.FleetStickerActivity
com.twitter.android.AuthorizeAppActivity
com.twitter.android.SingleSignOnActivity
com.twitter.app.profiles.ProfileActivity
com.twitter.android.search.filters.AdvancedSearchFiltersActivity
com.twitter.android.search.results.SearchActivity
com.twitter.android.topics.landing.TopicLandingActivity
com.twitter.android.topics.peek.activity.TopicPeekActivity
com.twitter.android.unifiedlanding.UnifiedLandingActivity

=================== Not Exported ===================
com.twitter.android.LoginActivity
com.twitter.android.LoginChallengeActivity
com.twitter.android.WebauthnChallengeActivity
com.twitter.android.PasswordResetActivity
com.twitter.android.settings.NotificationSettingsActivity
com.twitter.app.safety.notificationfilters.NotificationFiltersSettingsActivity
com.twitter.android.AdvancedDiscoSettingsActivity
com.twitter.android.ChangeScreenNameActivity
[...]

=================== ADB Test ===================
Starting: Intent { cmp=com.twitter.android/com.twitter.app.deeplink.UrlInterpreterActivity }
Press Enter to continue...
Starting: Intent { cmp=com.twitter.android/.StartActivity }
Press Enter to continue...
[...]

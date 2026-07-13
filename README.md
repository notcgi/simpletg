## SimpleTG (Telegram Android fork)

Fork of the official [Telegram for Android](https://github.com/DrKLO/Telegram) source.

### Build setup

1. Copy `local.properties.example` → `local.properties` and `keystore.properties.example` → `keystore.properties`.
2. Generate a release keystore (skip if you already have `TMessagesProj/config/release.keystore`):

```bash
keytool -genkeypair -v \
  -keystore TMessagesProj/config/release.keystore \
  -alias simpletg \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -storepass YOUR_STORE_PASSWORD -keypass YOUR_KEY_PASSWORD \
  -dname "CN=SimpleTG, OU=Mobile, O=notcgi, L=Unknown, ST=Unknown, C=US"
```

3. Fill `RELEASE_*` in `keystore.properties` (or `local.properties`).
4. Get **your own** `api_id` / `api_hash` at https://my.telegram.org/apps and put them in `local.properties` as `APP_ID` / `APP_HASH`.
5. Set `sdk.dir` in `local.properties` to your Android SDK path.
6. Open the project in Android Studio (Open, do not Import) or build:

```bash
./gradlew :TMessagesProj_App:assembleAfatRelease
```

Do **not** publish using Telegram’s sample `APP_ID` — it will hit `API_ID_PUBLISHED_FLOOD`.

Optional: create your own Firebase Android apps for `org.simpletg.messenger` / `org.simpletg.messenger.beta` and replace `google-services.json` files for push.

### Upstream notes

Telegram API manuals: https://core.telegram.org/api

MTproto protocol manuals: https://core.telegram.org/mtproto

### Localization

Translations: https://translations.telegram.org/en/android/

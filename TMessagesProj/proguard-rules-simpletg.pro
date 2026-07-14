# SimpleTG: treat disabled product flags as compile-time constants for R8 shrinking.
-assumevalues class org.telegram.messenger.BuildVars {
    public static boolean STORIES return false;
    public static boolean STARS_GIFTS return false;
}

// Honestly This might not be real javascript
// The documentation for [Openin](https://loshadki.app/openin4/) is more of a fever dream than useful spec
//
// None of the example scripts on the site work inside the app so expect this script to break 
//
// Anyway: this OpenIn custom rule script allows you to add #{profilename} to the end of URLs anywhere to have it automatically open with a specific browser. Additionally it could offer you a choice based on the 'fragement' [SIC?] openin sees. 
// In this example, the 'fragements' #porn,#fur,#school, and #work
// will automatically find their way into the correct browser profile. 
//
// NOTE that the 'app.name' is the name of the profile you must set up with this exact name (an exercise for the reader) in the GUI
// Also yes this would be better as a list object instead stacking elseifs until you die, however whatever is processing
// these scripts internally has quirks like: 'nothing working' or my favorite 'sometimes working', so this is what we got
//
// author = timmytimj (the cute one)
//

var apps = ctx.getApps();

if (ctx.url.fragement === "porn") {
    // Remove the 'porn' fragment from the url
    ctx.url.fragment = "";

    apps.forEach(function (app) {
        if (app.name === "PORN") {
            app.visible = true;
        } else {
            app.visible = false;
        }
    });
} else if (ctx.url.fragement === "fur") {
    // Remove the 'fur' fragment from the url
    ctx.url.fragement = "";

    apps.forEach(function (app) {
        if (app.name === "FUR") {
            app.visible = true;
        } else {
            app.visible = false;
        }
    });
} else if (ctx.url.fragement === "school") {
    // Remove the 'school' fragment from the url
    ctx.url.fragement = "";

    apps.forEach(function (app) {
        if (app.name === "SCHOOL") {
            app.visible = true;
        } else {
            app.visible = false;
        }
    });
} else if (ctx.url.fragement === "work") {
    // Remove the 'work' fragment from the url
    ctx.url.fragement = "";

    apps.forEach(function (app) {
        if (app.name === "WORK") {
            app.visible = true;
        } else {
            app.visible = false;
        }
    });
} else if (ctx.url.fragement === "priv") {
    // Remove the 'priv' fragment from the url
    ctx.url.fragement = "";

    apps.forEach(function (app) {
        if (app.name === "INCOGNITO") {
            app.visible = true;
        } else {
            app.visible = false;
        }
    });

 } else {
    // Your normal behavior when neither #porn nor #news is in the URL
}


# Version 5

## 5.0.0-alpha

### New Features

* ES6 rewrite
* Stripped UI/UX related code and shunted it into its own module
* More configuration based setup
* Bootstrap 4-esk plugin creation style
* All events are namespaced properly `{event}.datetimepicker`
* Added a jquery no conflict option
* Picker will also look for window.debug and will keep the picker from closing

### Other changes

* moved `showTodayButton`, `showClear` and `showClose` into `options.buttons`
* manually merged #1946, #1939, #1921, #1913
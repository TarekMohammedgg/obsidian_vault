const { Plugin } = require('obsidian');

module.exports = class WeekFixPlugin extends Plugin {
  onload() {
    console.log("Week Fix Plugin Loaded");

    // Set Saturday as start of week AND align week numbers with ISO
    moment.updateLocale('en', {
      week: {
        dow: 6, // Saturday
        doy: 11 // aligns locale week numbers with ISO week 47
      }
    });

    console.log("Locale week = ", moment().week());
    console.log("ISO week    = ", moment().isoWeek());
  }

  onunload() {
    console.log("Week Fix Plugin Unloaded");
  }
};

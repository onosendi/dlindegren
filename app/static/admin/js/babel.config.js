const presets = [
  [
    "@babel/env",
    {
      targets: {
        "ie": 8,
      },
      useBuiltIns: "usage",
      corejs: 3,
    },
  ],
];

module.exports = { presets };

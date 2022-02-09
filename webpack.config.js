const path = require('path');

module.exports = {
  devServer: {
    compress: true,
    port: 3000,
    static: {
      directory: path.resolve(__dirname, 'src'),
    },
  },
  entry: [
    './src/ts/index.ts',
    './src/scss/index.scss',
  ],
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.scss?$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'index.js',
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
};

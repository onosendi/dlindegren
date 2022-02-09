const path = require('path');
const HtmlPlugin = require('html-webpack-plugin');

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
        test: /\.tsx$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
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
  plugins: [
    new HtmlPlugin({
      template: 'src/index.html',
      filename: 'index.html',
    }),
    new HtmlPlugin({
      template: 'src/about.html',
      filename: 'about.html',
    }),
  ],
  resolve: {
    extensions: ['.ts', '.js'],
  },
};

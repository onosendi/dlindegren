const path = require('path');
const HtmlPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const { NODE_ENV } = process.env;
const IS_DEVELOPMENT = NODE_ENV === 'development';

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
          IS_DEVELOPMENT ? 'style-loader' : MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
  output: {
    clean: true,
    filename: 'bundle.[fullhash].js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new MiniCssExtractPlugin(),
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

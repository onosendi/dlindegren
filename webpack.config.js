const path = require('path');
const HtmlPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const isEnvProduction = process.env.NODE_ENV === 'production';
const isEnvDevelopment = process.env.NODE_ENV === 'development';

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
  mode: isEnvProduction ? 'production' : 'development',
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
          isEnvDevelopment ? 'style-loader' : MiniCssExtractPlugin.loader,
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
    isEnvProduction && new MiniCssExtractPlugin(),
    new HtmlPlugin({
      template: 'src/index.html',
      filename: 'index.html',
    }),
    new HtmlPlugin({
      template: 'src/about.html',
      filename: 'about.html',
    }),
  ].filter(Boolean),
  resolve: {
    extensions: ['.ts', '.js'],
  },
};

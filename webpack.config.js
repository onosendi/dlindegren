const path = require('path');

module.exports = {
  devServer: {
    compress: true,
    port: 3000,
  },
  entry: [
    './src/index.ts',
  ],
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'index.js',
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
};

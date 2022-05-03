const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
module.exports = {
  entry: "./app/views/src/index.tsx",
  target: "web",
  mode: "development",
  output: {
    path: path.resolve(__dirname, "app","views","static"),
    filename: "bundle.js",
  },
  resolve: {
    extensions: [".js", ".jsx", ".json", ".ts", ".tsx"],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: "awesome-typescript-loader",
      },
      {
        enforce: "pre",
        test: /\.js$/,
        loader: "source-map-loader",
      },
       {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          MiniCssExtractPlugin.loader,
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },
    ],
  },
  optimization:{
      minimizer:[
          new CssMinimizerPlugin(),
      ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname,"static", "index.html"),
      filename: path.resolve(__dirname,"app","views", "index.html"),
    
    }),
    new MiniCssExtractPlugin(),
  ],
};

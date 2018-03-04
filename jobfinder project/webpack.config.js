var path = require("path")

var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
module.exports = {
  context: __dirname,

  entry: ['./static/js/index'],// entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

  output:{
      path: path.resolve('./static/bundles/'),
      filename: "boundle.js",
  },


  module: {
  rules: [
      /*
      your other rules for JavaScript transpiling go in here
      */

      {
       test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader',
query:{
presets: ['es2015','react','stage-0'],
plugins:['transform-decorators-legacy']

}

      }
    ]

},
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],


  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['*', '.js', '.jsx']
  },
}

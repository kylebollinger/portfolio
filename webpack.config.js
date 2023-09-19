require('dotenv').config();
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const isDevelopment = (process.env.DEVELOPMENT_MODE || "false").toLowerCase() == "true";

console.log(`Running webpack in ${isDevelopment ? "development" : "production"} mode`);

module.exports = {
    target: 'web',
    context: path.resolve(),
    mode: isDevelopment ? "development" : "production",
    entry: {
        main: './assets/js/index.js',
        app: './assets/scss/index.scss',
    },
    output: {
        path: path.resolve('./assets/dist/'),
        filename: "[name]-[fullhash:6].js",
        clean: true,
        publicPath: isDevelopment ? 'http://localhost:9091/' : '/static/dist/',
    },
    plugins: [
        new BundleTracker({
            path: path.join(__dirname, 'assets'),
            filename: 'webpack-stats.json'
        }),
        new MiniCssExtractPlugin({
            filename: "[name]-[fullhash:6].css",
            chunkFilename: "[id]-[fullhash:6].css",
        }),
    ],
    devServer: {
        port: 9091,
        headers: {
            "Access-Control-Allow-Origin": "*",
        }
    },
    devtool: isDevelopment ? "eval" : "source-map",
    resolve: {
        fallback: {
            "path": require.resolve("path-browserify"),
            "crypto": require.resolve("crypto-browserify"),
            "stream": require.resolve("stream-browserify"),
            "os": require.resolve("os-browserify/browser"),
            "buffer": require.resolve("buffer/")
        }
    },
    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [
                    isDevelopment ? "style-loader" : MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: {
                            sourceMap: isDevelopment
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: isDevelopment
                        }
                    },
                ],
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                type: 'asset',
                generator: {
                    filename: 'fonts/en/[hash][ext][query]',
                },
            }
        ]
    }
}



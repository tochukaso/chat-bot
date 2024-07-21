const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/api/chat',
        createProxyMiddleware({
            target: 'http://localhost:4000',
            changeOrigin: true,
            pathRewrite: {'^/api/chat' : ''}
        })
    );
};
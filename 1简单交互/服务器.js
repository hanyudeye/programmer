var http = require('http')

function app(req, res) {
    // res.setHeader('Content-Type', 'application/json')
      res.setHeader('Content-Type', 'text/plain')
    //   res.write('hello, world!')
    res.write(req.url);
      res.end()
    // console.log(req);
    console.log("good");
}

http.createServer(app).listen(3000);
var baseUrl = 'http://www.zhihu.com/node/ExploreAnswerListV2'
superagent.get(baseUrl)
          .set({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Referrer': 'www.baidu.com'
          })
          .query({
            params: JSON.stringify(params)
          })
          .end(function(err, obj) {
            if(err) return null
            res.end(JSON.stringify(obj)) 
            //res是一个可写流里面传递的参数类型为string或buffer
            //故使用JSON.stringify()
          })
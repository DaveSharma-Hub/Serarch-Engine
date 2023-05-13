const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended:false}));

app.get('/getUrlList',(req,res) => {
    res.json(urls);
});

app.post('/addUrl', (req,res) => {
    const {url, title} = req.body;
    console.log(req.body);
    urls.push({
        url,
        title
    });
});

app.listen(PORT,()=>{console.log(`Listening on port ${PORT}`)});


const urls = [
    {
        url:"http://127.0.0.1:5500/test/application/index.html",
        title:"Local Test Application"
    }
];
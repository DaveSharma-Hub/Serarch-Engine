const express = require('express');
const cors = require('cors');
const axios = require('axios');
const { dataMatches } = require('./util/utils');
require('dotenv').config();

const PORT = parseInt(process.env.PORT,10) || 2000;

const app = express();
app.use(express.json());
app.use(express.urlencoded({extended:false}));
app.use(cors());

app.get('/search',async (req,res)=>{
    const searchValue = req.query.value;
    const url = `${process.env.DATABASE_URL}/getUrlList`;
    const result = await axios.get(url);
    const urlList = result.data;
    const searchResults = urlList.filter((item)=>dataMatches(item.title,searchValue));
    res.send(searchResults);
});

app.listen(PORT,()=>{
    console.log(`Listening on port ${PORT}`)
});

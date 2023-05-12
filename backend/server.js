const express = require('express');
const cors = require('cors');
require('dotenv');

const app = express();
app.use(cors());

app.get('/',(req,res)=>{
    
});

app.listen(process.env.PORT,()=>{
    console.log(`Listening on port ${process.env.PORT}`)
});

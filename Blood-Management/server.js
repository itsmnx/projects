const express = require('express')
const dotenv=require('dotenv');
const colors=require('colors');
const morgan=require('morgan');
const cors = require('cors')

//import mongodb connection
const connectDB=require('./config/db');

//dotenv config
dotenv.config();
//mogobd connection
connectDB();
//rest object creation
const app=express()
//middlewares
app.use(express.json())
app.use(cors())
app.use(morgan('dev'))

//routes
//1 test route
app.use('/api/v1/test',require('./routes/testRoute'));
app.use('/api/v1/auth',require('./routes/authRoutes'));
app.use('/api/v1/inventory',require('./routes/inventoryRoutes'));
//port
const PORT=process.env.PORT || 8080;
//listen method
app.listen(PORT,()=>{
    console.log(
    `Node server Running in ${process.env.DEV_MODE} ModeOn Port ${process.env.PORT}`
    .bgBlue.white
    );
});
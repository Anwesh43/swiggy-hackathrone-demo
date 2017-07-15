const express = require('express')
const http = require('http')
const app = express()
const path = require('path')
const bodyParser = require('body-parser')
app.use((req,res,next)=>{
  res.header('Access-Control-Allow-Credentials','true')
  res.header("Access-Control-Allow-Origin", "http://localhost:3000")
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  next()
})

app.use(bodyParser.urlencoded({extended:true}))
app.use(bodyParser.json())
app.use(express.static(path.join(__dirname,'public')))
app.post('/postorder',(req,res)=>{
    console.log(`new order ${req.body}`)
    sockets.forEach((socket)=>{
        socket.emit('new_order',req.body)
    })
    res.send("success")
})

const server = http.createServer(app)
const socketio = require('socket.io')
const io = socketio(server)


const sockets = []
io.on('connect',(socket)=>{
    console.log("connected")
    socket.emit("hello","welcome to socketio")
    sockets.push(socket)
})
server.listen(9000,()=>{
    console.log("listening")
})

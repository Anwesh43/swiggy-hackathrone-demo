const socket = io.connect('http://localhost:9000')
socket.on('hello',(greet)=> {
    alert(greet)
})
socket.on("new_order",(order)=>{
    document.write(order.place+" "+order.restaurant+" "+order.food_item+" "+order.cost)
    console.log(order)
})

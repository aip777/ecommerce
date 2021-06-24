new Vue({
    el:"#app",
    data:{
        title : "Vue",
        isTrue : true,
        cars : ["Ariful", "Islam"],
        age:53,
        number:32,
        robot:{
            name: "Funcry"
        },
        src: "https://cdn.pixabay.com/photo/2015/03/26/09/41/chain-690088_640.jpg",
        user:{
            name :"Khan",
            age:33,
            title:"Software Engineer"
        }
    },
    methods:{
        greeting(){
            return this.age>=this.number ? true:false
        },
        onClickChange(event){
            let result
            if (event.clientuser.name=="Khan") {
                
             } if (this.user.name=="Palash"){
                this.user.name="Khan"
             }
             else{
                this.user.name = "Ariful"
             }
            return result
        }
    }
})
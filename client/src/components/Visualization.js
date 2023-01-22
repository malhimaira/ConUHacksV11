import axios from "axios"
import {useEffect} from "react"

function Visualization(){
    
    function getAll(){
        axios.get("http://localhost:3030/users").then((res) =>{
            console.log(res)
        })    }
    useEffect(() => {
        getAll()
    }, [])

    return <p> "hey"</p>
}

export default Visualization;

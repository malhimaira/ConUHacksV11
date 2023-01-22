const cors = require("cors")
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const db = require('./pool')
const port = 3030

app.use(
	cors({
		origin: "http://localhost:3000",
		credentials: true,
	})
);


app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)

app.get('/', (request, response) => {
  response.json({ info: 'Node.js, Express, and Postgres API' })
})

app.get('/users', db.getUsers)
app.listen(port, () => {
  console.log(`App running on port ${port}.`)
})
// const { Client } = require("pg")
// const dotenv = require("dotenv")
// dotenv.config()
 



// const connectDb = async () => {
//     try {
//         const client = new Client({
//             user: process.env.PGUSER,
//             host: process.env.PGHOST,
//             database: process.env.PGDATABASE,
//             password: process.env.PGPASSWORD,
//             port: process.env.PGPORT
//         })
//  
//         await client.connect()
//         const res = await client.query('SELECT * FROM actors')
//         console.log(res)
//         await client.end()
//     } catch (error) {
//         console.log(error)
//     }
// }
//  
// connectDb()

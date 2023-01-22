import { Observable } from 'rxjs'
import * as d3 from "d3"
import ScatterPlot from "../utils/ScatterPlot"
import data from "../utils/mtcars.csv"
import { useEffect } from 'react'

 function Home() {

   let cars;
    let chart;
  console.log('next');
//   console.log(chart)
  useEffect(() => {

    const fetch = async ()=>{
        cars = await d3.csv(data, function(data) {
            console.log(data)
        })
    
         chart = ScatterPlot(cars, {
        x: d => d.mpg,
        y: d => d.hp,
        title: d => d.name,
        xLabel: "Miles per gallon →",
        yLabel: "↑ Horsepower",
        stroke: "steelblue",
        width: 400,
        height: 600
      })
      }

    fetch().then(()=>{console.log(chart)});
    }

    , [])

    console.log(chart);
    return <p> {chart}</p>;
}

export default Home;
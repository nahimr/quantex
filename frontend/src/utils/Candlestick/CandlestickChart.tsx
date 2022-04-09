// Copyright (c) 2016 - 2017 Uber Technologies, Inc.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

import React from "react";
import {
  XAxis,
  YAxis,
  LineSeries,
  FlexibleWidthXYPlot
} from "react-vis";
import Candlestick from "./CandlestickSeries"
import "react-vis/dist/style.css";
import { MarketData } from "./dto/MarketData";

const AXIS_STYLES = {
  line: { stroke: "transparent" },
  ticks: { stroke: "transparent" },
  text: { stroke: "none", fill: "#6b6b76", fontWeight: 600 }
};

const DEFAULT_AXIS_PROPS = {
  style: AXIS_STYLES,
  tickSize: 0
};

interface CandlestickChartProps 
{
  title?: string;
  data: MarketData;
}

interface CandlestickChartStates 
{
  hasError: boolean;
  data: MarketData;
}

class CandlestickChart extends React.Component<CandlestickChartProps, CandlestickChartStates>  {
  constructor(props: CandlestickChartProps | Readonly<CandlestickChartProps>)
  {
    super(props);
    this.state = {
    //   data: this.props.data.map(item => {
    //     return {
    //       ...item,
    //       x: moment(item.x).valueOf() // need these to be timestamps for some reason
    //     };
    //   })
      data: this.props.data,
      hasError: false,
      // data: [
      //   {
      //     "x": 1547087043927,
      //     "y": 106.0141016639479,
      //     "yHigh": 403.16668701171875,
      //     "yOpen": 214.0833511352539,
      //     "yClose": 3.0999999046325684,
      //     "yLow": 0,
      //     "color": "#1896FD"
      //   },
      // ]
    };
  }

  // getMaxAndMin = (data_: MarketData) => {
  //   const mins = data_.map((item: { yLow: any; }) => item.yLow);
  //   const maxs = data_.map((item: { yHigh: any; }) => item.yHigh);
  //   const min = Math.min(...mins);
  //   const max = Math.max(...maxs);
  //   return {
  //     max,
  //     min
  //   };
  // };

  componentDidCatch(error: any, info: any) {
    // Display fallback UI
    this.setState({ hasError: true });
    // You can also log the error to an error reporting service
    console.log({ title: this.props.title, error, info });
  }

  render() {
    // eslint-disable-next-line @typescript-eslint/no-shadow
    const { data } = this.state;
    

    if (this.state.hasError) {
      return null;
    }

    return (
      <div>
        <div>
          <FlexibleWidthXYPlot
            xType="linear"
            animation
            yDomain={[data.low, data.high]}
            height={300}
          >
            <XAxis {...DEFAULT_AXIS_PROPS} />
            <YAxis {...DEFAULT_AXIS_PROPS} />
            {/* <LineSeries color="#12939A" data={data} /> */}
            <Candlestick
              colorType="literal"
              opacityType="literal"
              stroke="#1896FD"
              data={data}
            />
          </FlexibleWidthXYPlot>
        </div>
      </div>
    );
  }
}

export default CandlestickChart;

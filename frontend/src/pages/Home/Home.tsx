import React, { useEffect } from "react";
import { useInstruments } from "../../hooks/api/useInstruments";
import CandlestickChart from "../../utils/Candlestick/CandlestickChart";
import { Instrument } from "../../utils/Candlestick/dto/Instrument";
import { MarketData } from "../../utils/Candlestick/dto/MarketData";


// interface HomeState
// {
//   data?: Instrument[];
// }

const Home: React.FC<any> = (props: any) => {
  const { instruments } = useInstruments();

  return (
    <>
      {/* <CandlestickChart /> */}
    </>
  );

};

export default Home;

import { MarketData } from "./MarketData";

export class Instrument {
    symbol?: string;
    name?: string;
    region?: string;
    data?: MarketData;
    details?: string;
}

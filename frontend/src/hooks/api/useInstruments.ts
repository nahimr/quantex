import { useEffect, useState } from 'react';
import { Instrument } from '../../utils/Candlestick/dto/Instrument';

const fetchInstruments = async (setInstruments: (instruments: Instrument[]) => void) => {
  const route = "instruments";
  const response = await fetch(`${process.env.REACT_APP_API_URL}/${route}`, {
    headers: {
      'Content-Type': 'application/json'
    },
    method: "GET",
  });
  setInstruments(await response.json());

};

export function useInstruments(): { instruments: Instrument[] } {
  const [instruments, setInstruments] = useState<Instrument[]>([]);

  useEffect(() => {
    (async () => {
      await fetchInstruments(setInstruments);
    })();
  }, []);


  return { instruments };
}
import React from "react";
import {
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
}
  from "@chakra-ui/react";

import "Header" from "./Header";


function App() {
  return (
    <div id="main">
      <Header />
      <Tag> Enter Input Latitude</Tag>
      <NumberInput defaultValue={15} precision={6} step={0.2}>
        <NumberInputField />
        <NumberInputStepper>
          <NumberIncrementStepper />
          <NumberDecrementStepper />
        </NumberInputStepper>
      </NumberInput>
    </div>
  )
}

export default App;

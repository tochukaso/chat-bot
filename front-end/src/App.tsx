import React from 'react';
import Chatbot from './components/Chatbot';
import styled from 'styled-components';

const AppContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
`;

function App() {
  return (
      <AppContainer>
        <Chatbot />
      </AppContainer>
  );
}

export default App;
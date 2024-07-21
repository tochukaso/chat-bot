import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import ChatMessage from './ChatMessage';

const ChatContainer = styled.div`
  width: 400px;
  height: 600px;
  border: 1px solid #ccc;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background-color: white;
`;

const ChatBox = styled.div`
  flex: 1;
  padding: 10px;
  overflow-y: scroll;
`;

const InputBox = styled.div`
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
`;

const Input = styled.input`
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
`;

const Button = styled.button`
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
`;

interface Message {
    text: string;
    sender: 'user' | 'bot';
}

function Chatbot() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputValue, setInputValue] = useState<string>('');

    const sendMessage = async () => {
        if (inputValue.trim() === '') return;

        const newMessage: Message = { text: inputValue, sender: 'user' };
        setMessages([...messages, newMessage]);
        setInputValue('');

        try {
            const mockResponse = await axios.post('http://localhost:4000/api/chat', {
                message: inputValue,
            });

            const botMessage: Message = { text: mockResponse.data.reply, sender: 'bot' };
            setMessages((prevMessages) => [...prevMessages, botMessage]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <ChatContainer>
            <ChatBox>
                {messages.map((msg, index) => (
                    <ChatMessage key={index} message={msg} />
                ))}
            </ChatBox>
            <InputBox>
                <Input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && sendMessage()} />
                <Button onClick={sendMessage}>Send</Button>
            </InputBox>
        </ChatContainer>
    );
}

export default Chatbot;
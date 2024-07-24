import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import ChatMessage from './ChatMessage';

const ChatContainer = styled.div`
  width: 800px;
  height: 1000px;
  border: 1px solid ${({ theme }) => theme.colors.secondary};
  border-radius: ${({ theme }) => theme.borderRadius};
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background-color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const ChatBox = styled.div`
  flex: 1;
  padding: 10px;
  overflow-y: auto;
`;

const InputBox = styled.div`
  display: flex;
  padding: 10px;
  border-top: 1px solid ${({ theme }) => theme.colors.secondary};
  background-color: ${({ theme }) => theme.colors.light};
`;

const Input = styled.input`
  flex: 1;
  padding: 10px;
  border: 1px solid ${({ theme }) => theme.colors.secondary};
  border-radius: ${({ theme }) => theme.borderRadius};
  margin-right: 10px;
  outline: none;
`;

const Button = styled.button`
  padding: 0 20px;
  border: none;
  background-color: ${({ theme }) => theme.colors.primary};
  color: white;
  border-radius: ${({ theme }) => theme.borderRadius};
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: ${({ theme }) => theme.colors.dark};
  }
`;

interface Message {
    text: string;
    sender: 'user' | 'bot';
}

const Chatbot: React.FC = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputValue, setInputValue] = useState<string>('');

    useEffect(() => {
        const fetchInitialMessage = async () => {
            try {
                const response = await axios.get('http://localhost:4000/chat');
                const initialMessage: Message = { text: response.data.reply, sender: 'bot' };
                setMessages([initialMessage]);
            } catch (error) {
                console.error('Error fetching initial message:', error);
            }
        };

        fetchInitialMessage();
    }, []);

    const sendMessage = async () => {
        if (inputValue.trim() === '') return;

        const newMessage: Message = { text: inputValue, sender: 'user' };
        setMessages([...messages, newMessage]);
        setInputValue('');

        try {
            const mockResponse = await axios.post('http://localhost:4000/chat', {
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
};

export default Chatbot;
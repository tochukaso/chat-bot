import React from 'react';
import styled from 'styled-components';

const MessageContainer = styled.div<{ sender: 'user' | 'bot' }>`
  display: flex;
  margin: 5px 0;
  justify-content: ${(props) => (props.sender === 'user' ? 'flex-end' : 'flex-start')};
`;

const MessageBubble = styled.div<{ sender: 'user' | 'bot' }>`
  max-width: 70%;
  padding: 10px;
  border-radius: 10px;
  background-color: ${(props) => (props.sender === 'user' ? '#007bff' : '#e5e5ea')};
  color: ${(props) => (props.sender === 'user' ? 'white' : 'black')};
`;

interface ChatMessageProps {
    message: {
        text: string;
        sender: 'user' | 'bot';
    };
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
    return (
        <MessageContainer sender={message.sender}>
            <MessageBubble sender={message.sender}>{message.text}</MessageBubble>
        </MessageContainer>
    );
};

export default ChatMessage;
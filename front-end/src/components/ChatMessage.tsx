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
  border-radius: ${({ theme }) => theme.borderRadius};
  background-color: ${(props) => (props.sender === 'user' ? props.theme.colors.primary : props.theme.colors.light)};
  color: ${(props) => (props.sender === 'user' ? 'white' : 'black')};
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
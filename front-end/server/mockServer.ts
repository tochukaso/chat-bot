import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const PORT = 4000;

app.use(bodyParser.json());

interface ChatRequest {
    message: string;
}

interface ChatResponse {
    reply: string;
}

app.post('/api/chat', (req, res) => {
    const request: ChatRequest = req.body;

    setTimeout(() => {
        const response: ChatResponse = { reply: 'This is a mock response from the AI.' };
        res.send(response);
    }, 1000);
});

app.listen(PORT, () => {
    console.log(`Mock server running on http://localhost:${PORT}`);
});
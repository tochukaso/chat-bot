import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
    body {
        margin: 0;
        font-family: 'Roboto', sans-serif;
        background-color: ${({ theme }) => theme.colors.light};
    }

    * {
        box-sizing: border-box;
    }
`;

export default GlobalStyles;
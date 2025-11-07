import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from '../comps/App03.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

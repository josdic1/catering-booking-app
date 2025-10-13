import { useState } from 'react'
import MaFullSchemaGenerator from './utils/MaReslationshipGenerator'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <header>

    </header>
    <main>
      <MaFullSchemaGenerator />
      </main>
    </>
  )
}

export default App

import { useState } from 'react'
import MarshmellowSchemaGenerator from './utils/MarshmellowSchemaGenerator'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <header>

    </header>
    <main>
      <MarshmellowSchemaGenerator />
      </main>
    </>
  )
}

export default App

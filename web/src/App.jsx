import { useState } from 'react'
import './index.css'

function App() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleAsk = async () => {
    if (!question.trim()) return

    setLoading(true)
    setError(null)
    setAnswer('')

    try {
      const response = await fetch('http://localhost:8000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      })

      if (!response.ok) {
        throw new Error('Failed to get response from AI')
      }

      const data = await response.json()
      setAnswer(data.answer)
    } catch (err) {
      setError('Error: Could not connect to local AI server. Make sure "py app/server.py" is running.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-white flex flex-col items-center pt-20 px-4">
      <div className="w-full max-w-2xl space-y-8">

        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-bold text-gray-900">Local AI Assistant</h1>
          <p className="text-gray-500">Private, offline, and secure.</p>
        </div>

        {/* Input Section */}
        <div className="space-y-4">
          <textarea
            className="w-full h-32 p-4 text-lg border border-gray-300 rounded-lg focus:ring-2 focus:ring-black focus:border-transparent outline-none resize-none placeholder-gray-400"
            placeholder="Ask a question about your documents..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button
            onClick={handleAsk}
            disabled={loading || !question.trim()}
            className="w-full py-3 bg-black text-white text-lg font-medium rounded-lg hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors cursor-pointer"
          >
            {loading ? 'Thinking...' : 'Ask'}
          </button>
        </div>

        {/* Error Message */}
        {error && (
          <div className="p-4 text-red-600 bg-red-50 rounded-lg border border-red-100">
            {error}
          </div>
        )}

        {/* Answer Section */}
        {answer && (
          <div className="space-y-2 animate-in fade-in duration-500">
            <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wide">Answer</h2>
            <div className="p-6 bg-gray-50 border border-gray-100 rounded-lg text-lg leading-relaxed text-gray-800 whitespace-pre-wrap">
              {answer}
            </div>
          </div>
        )}

      </div>
    </div>
  )
}

export default App

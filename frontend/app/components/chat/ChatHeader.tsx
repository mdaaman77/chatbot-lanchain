import { Provider } from "@/app/types/chat";

interface ChatHeaderProps {
  provider: Provider;
  onProviderChange: (provider: Provider) => void;
  onClearChat: () => void;
}

export default function ChatHeader({
  provider,
  onProviderChange,
  onClearChat,
}: ChatHeaderProps) {
  return (
    <header className="flex items-center justify-between border-b p-4">

      <div>
        <h1 className="text-2xl font-bold">
          Internal Knowledge Chatbot
        </h1>

        <p className="text-sm text-gray-500">
          Ask questions about your documents
        </p>
      </div>

      <div className="flex items-center gap-4">

        <select
          value={provider}
          onChange={(e) =>
            onProviderChange(e.target.value as Provider)
          }
          className="rounded border px-3 py-2"
        >
          <option value="gemini">
            Gemini
          </option>

          <option value="ollama">
            Ollama
          </option>
        </select>

        <button
          onClick={onClearChat}
          className="rounded bg-red-500 px-4 py-2 text-white hover:bg-red-600"
        >
          Clear Chat
        </button>

      </div>

    </header>
  );
}
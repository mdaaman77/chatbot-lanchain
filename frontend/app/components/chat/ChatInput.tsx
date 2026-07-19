"use client";

import { useState, KeyboardEvent } from "react";

interface ChatInputProps {
  loading: boolean;
  onSend: (message: string) => Promise<void>;
}

export default function ChatInput({
  loading,
  onSend,
}: ChatInputProps) {
  const [message, setMessage] = useState("");

  const handleSend = async () => {
    const trimmed = message.trim();

    if (!trimmed || loading) return;
    setMessage("");
    await onSend(trimmed);

    
  };

  const handleKeyDown = async (
    e: KeyboardEvent<HTMLTextAreaElement>
  ) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      await handleSend();
    }
  };

  return (
    <div className="border-t bg-white p-4">
      <div className="flex gap-3">

        <textarea
          value={message}
          disabled={loading}
          rows={2}
          placeholder="Ask something about the documents..."
          className="flex-1 resize-none rounded-lg border p-3 outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
        />

        <button
          disabled={loading || !message.trim()}
          onClick={handleSend}
          className="rounded-lg bg-blue-600 px-6 text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-400"
        >
          {loading ? "..." : "Send"}
        </button>

      </div>
    </div>
  );
}
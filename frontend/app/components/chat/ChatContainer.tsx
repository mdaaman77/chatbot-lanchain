"use client";


import { useChat } from "@/app/hooks/useChat";


import ChatHeader from "./ChatHeader";

import ChatMessages from "./ChatMessages";

import ChatInput from "./ChatInput";



export default function ChatContainer() {


  const {

    messages,

    loading,

    provider,

    setProvider,

    sendMessage,

    clearChat,


  } = useChat();




  return (

    <main className="flex h-screen justify-center bg-slate-100 p-6">


      <div className="flex w-full max-w-5xl flex-col rounded-xl bg-white shadow-lg">


        <ChatHeader

          provider={provider}

          onProviderChange={setProvider}

          onClearChat={clearChat}

        />



        <ChatMessages

          messages={messages}

          loading={loading}

        />



        <ChatInput

          loading={loading}

          onSend={sendMessage}

        />


      </div>


    </main>

  );

}
"use client";

import { useEffect, useRef } from "react";

import type { Message } from "@/app/types/chat";

import EmptyChat from "../common/EmptyChat";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";


interface ChatMessagesProps {

  messages: Message[];

  loading: boolean;

}



export default function ChatMessages({

  messages,

  loading,

}: ChatMessagesProps) {


  const bottomRef =
    useRef<HTMLDivElement>(null);



  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });

  }, [messages, loading]);



  if (messages.length === 0) {

    return (

      <div className="flex-1">

        <EmptyChat />

      </div>

    );

  }



  return (

    <div className="flex-1 overflow-y-auto p-6">


      {
        messages.map((message) => (

          <MessageBubble

            key={message.id}

            message={message}

          />

        ))
      }



      {
        loading && <TypingIndicator />
      }



      <div ref={bottomRef} />

    </div>

  );

}
"use client";


import { useState } from "react";

import ChatService from "@/app/services/chat.service";

import type {
  Provider,
} from "@/app/types/chat";



export function useChat() {


  const [messages, setMessages] =
    useState<any[]>([]);


  const [loading, setLoading] =
    useState(false);



  const [provider, setProvider] =
    useState<Provider>("gemini");



  const [error, setError] =
    useState("");



  const sendMessage = async (
    question: string
  ) => {


    if (!question.trim()) return;


    setLoading(true);

    setError("");



    const userMessage = {

      id: crypto.randomUUID(),

      role: "user",

      content: question,

    };



    const updatedMessages = [
      ...messages,
      userMessage
    ];



    setMessages(updatedMessages);



    const history =
      updatedMessages
        .slice(-10)
        .map(
          message =>
            message.content
        );



    try {


      const response =
        await ChatService.chat({

          question,

          provider,

          history,

        });



      const aiMessage = {

  id: crypto.randomUUID(),

  role: "assistant",

  content: response.answer.answer,

  citations: response.answer.citations,

};



      setMessages([
        ...updatedMessages,
        aiMessage
      ]);



    } catch (err:any) {


      console.error(err);


      setError(
        err.response?.data?.detail ??
        "Something went wrong."
      );


    } finally {


      setLoading(false);

    }

  };




  const clearChat = () => {

    setMessages([]);

  };



  return {

    messages,

    loading,

    error,

    provider,

    setProvider,

    sendMessage,

    clearChat,

  };

}
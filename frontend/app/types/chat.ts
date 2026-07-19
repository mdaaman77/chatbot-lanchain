export type Provider =
  | "gemini"
  | "openai";



export interface Citation {

  source: string;

}



export interface Message {


  id: string;


  role:
    | "user"
    | "assistant";



  content: string;



  citations?: Citation[];


}



export interface ChatRequest {


  question: string;


  provider: Provider;


  history: string[];


}



export interface ChatResponse {


  answer: {


    answer: string;


    citations: Citation[];


  };

}
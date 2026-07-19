import { api } from "./api";
import type { ChatRequest, ChatResponse } from "@/app/types/chat";

class ChatService {
  async chat(data: ChatRequest): Promise<ChatResponse> {
  console.log(data);

  const response = await api.post<ChatResponse>(
    "/v1/chat",
    data
  );

  return response.data;
}
}


export default new ChatService();
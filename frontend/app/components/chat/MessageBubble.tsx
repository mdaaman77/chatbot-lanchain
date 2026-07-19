import {
  Message
} from "@/app/types/chat";



interface MessageBubbleProps {

  message: Message;

}



export default function MessageBubble({

  message,

}: MessageBubbleProps) {



  const isUser =
    message.role === "user";



  return (

    <div

      className={`mb-4 flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}

    >


      <div

        className={`max-w-[75%] rounded-xl px-4 py-3 whitespace-pre-wrap ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-200 text-gray-900"
        }`}

      >


        <div>

          {message.content}

        </div>



        {
          !isUser &&
          message.citations &&
          message.citations.length > 0 && (


            <div className="mt-4 border-t pt-3 text-sm">


              <p className="mb-2 font-semibold">

                Sources:

              </p>



              {
                message.citations.map(
                  (citation,index)=>(


                    <div
                      key={index}
                      className="text-gray-600"
                    >

                      📄{" "}

                      {
                        citation.source
                          .split("\\")
                          .pop()
                      }


                    </div>


                  )
                )
              }



            </div>


          )
        }



      </div>


    </div>

  );

}
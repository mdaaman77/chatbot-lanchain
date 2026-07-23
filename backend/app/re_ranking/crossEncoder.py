from typing import List, Tuple
from sentence_transformers import CrossEncoder
import torch



class CrossEncoder:

    def __init__(self, threshold_value: float = 0.25):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
        # Using the renamed import to avoid naming collision
        self.model = CrossEncoder(
            self.model_name,
            device=self.device,
            max_length=512
        )
        self.threshold_value = threshold_value


    
    async def rerank(self, query:str, documents:List[str],k:int = 5):
          if not query or not documents: return f"no query or document of chunk  {[]}"

          pairs = [
               (document,query)
               for document in documents
          ] 

          scores = self.model.predict(pairs,batch_size=16)

          ranked = sorted(
               zip(documents,scores),
               key=lambda x:x[1],
               reverse=True
          )

          filtered_ranked = [
            (doc, float(score)) 
            for doc, score in ranked 
            if score >= self.threshold_value
        ]

        #   filter_top_score = [
        #        pair 
        #        for pair in top_K_ranked:
        #        if pass['scores'] >= self.threeshold_value
        #   ]

          return filtered_ranked
         
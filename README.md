# BERT_Rasa_chatbot
This repo contains the basic conversations of the Rasa Chatbot Integrated with the BERT model. 

## Rasa NLU pipeline
The basic architecture used for the Rasa NLU pipeline is 
1. Language Model - HFTransformersNLP
2. Tokenizer - LanguageModelTokenizer
3. Featurizer - LanguageModelFeaturizer, RegexFeaturizer, LexicalSyntacticFeaturizer, CountVectorsFeaturizer
4. Intent classifier and Entity extractor - DIETClassifier

## Rasa Core



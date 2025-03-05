from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('./google-bert/bert-base-uncased')
model = BertModel.from_pretrained("./google-bert/bert-base-uncased")
text = "How are you?"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

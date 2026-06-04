from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("tencent/HY-MT1.5-1.8B")
model = AutoModelForCausalLM.from_pretrained("tencent/HY-MT1.5-1.8B")
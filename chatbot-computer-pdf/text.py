import spacy

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

# Procesar un texto en español
text = "El presidente de España, Pedro Sánchez, visitó México."

# Procesar el texto con spaCy
doc = nlp(text)

# Mostrar las entidades reconocidas
for ent in doc.ents:
    print(f"Entidad: {ent.text}, Tipo: {ent.label_}")

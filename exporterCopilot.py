import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(f"Datos cargados del JSON: {data}")  # Mensaje de depuración
        return data

def format_conversation(request):
    user_question = request['message']['text']
    assistant_response = request['response'][0]['value']

    markdown = f"### Pregunta del usuario\n\n{user_question}\n\n"
    markdown += f"### Respuesta del asistente\n\n{assistant_response}\n\n"
    return markdown

def json_to_markdown(json_data):
    markdown = ""
    requests = json_data.get('requests', [])
    print(f"Conversaciones encontradas: {len(requests)}")  # Mensaje de depuración
    for request in requests:
        markdown += format_conversation(request)
    return markdown

def save_markdown(markdown, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(markdown)
        print(f"Markdown guardado en {file_path}")  # Mensaje de depuración

def main():
    input_json_path = 'chat.json'
    output_markdown_path = 'chat_export.md'

    json_data = load_json(input_json_path)
    markdown = json_to_markdown(json_data)
    save_markdown(markdown, output_markdown_path)

if __name__ == "__main__":
    main()
# Vibe Coding AI Architecture

                    Developer Laptop
                           |
                +----------+----------+
                |                     |
             Continue               Aider
                |                     |
                +----------+----------+
                           |
                    Vibe Coding API
                     FastAPI Gateway
                           |
                    Task Classifier
                           |
              +------------+------------+
              |            |            |
           Coding       Reasoning     Vision
              |            |            |
         DeepSeek        Qwen3        Devstral
              |            |            |
              +------------+------------+
                           |
                         Ollama
                           |
                       Cloud GPU

The laptop does not perform model inference.

The cloud GPU performs inference.

The gateway is responsible for:
- task classification
- model selection
- fallback routing
- error handling
- logging
- API compatibility

The coding workflow remains:
Developer -> Aider/Continue -> Gateway -> Ollama -> Specialist Model

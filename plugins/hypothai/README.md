# HypothAI Plugin

Plugin for generating hypothesis statements from a structured knowledge graph.

### Endpoint:
- `POST /generate/hypotheses`: Accepts graph data → returns potential scientific hypotheses.

### Setup:

docker build -t hypothai .
docker run -p 8001:8001 hypothai
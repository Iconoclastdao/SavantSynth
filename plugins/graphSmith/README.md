# GraphSmith Plugin

A plugin for Eliza to extract scientific knowledge graphs from research text.

### Endpoints:
- `POST /parse/paper`: Accepts full scientific text, returns knowledge graph (nodes, edges, RDF, JSON).

### Setup:
docker build -t graphsmith .
docker run -p 8000:8000 graphsmith
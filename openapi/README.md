# OpenAI Genreater によるコンテナ起動コマンド

以下のコマンドによりOpenAPI仕様書に従ったAPIが立ち上がある(ただしコントローラー部分のみ)

```bash
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    -g typescript-fetch \
    -o /local/frontend/src/generated
```
# OpenAI Genreater によるコンテナ起動コマンド

以下のコマンドによりOpenAPI仕様書に従ったクライアント用のコードが自動で生成される

```bash
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    -g typescript-fetch \
    -o /local/frontend/src/generated
```

以下のようになればOK!

```bash
Unable to find image 'openapitools/openapi-generator-cli:latest' locally
latest: Pulling from openapitools/openapi-generator-cli
521f275cc58b: Pull complete 
4ec0d48772e2: Pull complete 
c206fa8d0304: Pull complete 
f36698d7f25c: Pull complete 
4f82fb5fa4a4: Pull complete 
b9d975650083: Pull complete 
623923ee917d: Pull complete 
5bc98693c95e: Pull complete 
Digest: sha256:db548a46433ebf4c302b905ef6db5f56c7db8d9946184fc8ae9247027326e27f
Status: Downloaded newer image for openapitools/openapi-generator-cli:latest
[main] INFO  o.o.codegen.DefaultGenerator - Generating with dryRun=false
[main] INFO  o.o.c.ignore.CodegenIgnoreProcessor - Output directory (/local/frontend/src/generated) does not exist, or is inaccessible. No file (.openapi-generator-ignore) will be evaluated.
[main] INFO  o.o.codegen.DefaultGenerator - OpenAPI Generator: typescript-fetch (client)
[main] INFO  o.o.codegen.DefaultGenerator - Generator 'typescript-fetch' is considered stable.
[main] INFO  o.o.c.l.AbstractTypeScriptClientCodegen - Hint: Environment variable 'TS_POST_PROCESS_FILE' (optional) not defined. E.g. to format the source code, please try 'export TS_POST_PROCESS_FILE="/usr/local/bin/prettier --write"' (Linux/Mac)
[main] INFO  o.o.c.l.AbstractTypeScriptClientCodegen - Note: To enable file post-processing, 'enablePostProcessFile' must be set to `true` (--enable-post-process-file for CLI).
[main] INFO  o.o.codegen.InlineModelResolver - Inline schema created as _greets_get_200_response. To have complete control of the model name, set the `title` field or use the modelNameMapping option (e.g. --model-name-mappings _greets_get_200_response=NewModel,ModelA=NewModelA in CLI) or inlineSchemaNameMapping option (--inline-schema-name-mappings _greets_get_200_response=NewModel,ModelA=NewModelA in CLI).
[main] INFO  o.o.codegen.InlineModelResolver - Inline schema created as _calculate_post_request. To have complete control of the model name, set the `title` field or use the modelNameMapping option (e.g. --model-name-mappings _calculate_post_request=NewModel,ModelA=NewModelA in CLI) or inlineSchemaNameMapping option (--inline-schema-name-mappings _calculate_post_request=NewModel,ModelA=NewModelA in CLI).
[main] INFO  o.o.codegen.InlineModelResolver - Inline schema created as _calculate_post_200_response. To have complete control of the model name, set the `title` field or use the modelNameMapping option (e.g. --model-name-mappings _calculate_post_200_response=NewModel,ModelA=NewModelA in CLI) or inlineSchemaNameMapping option (--inline-schema-name-mappings _calculate_post_200_response=NewModel,ModelA=NewModelA in CLI).
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/models/CalculatePost200Response.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/models/CalculatePostRequest.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/models/GreetsGet200Response.ts
[main] WARN  o.o.codegen.DefaultCodegen - Empty operationId found for path: get /greets. Renamed to auto-generated operationId: greetsGet
[main] WARN  o.o.codegen.DefaultCodegen - Empty operationId found for path: post /calculate. Renamed to auto-generated operationId: calculatePost
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/apis/DefaultApi.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/index.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/runtime.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/models/index.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/apis/index.ts
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/.openapi-generator-ignore
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/.openapi-generator/VERSION
[main] INFO  o.o.codegen.TemplateManager - writing file /local/frontend/src/generated/.openapi-generator/FILES
############################################################################################
# Thanks for using OpenAPI Generator.                                                      #
# We appreciate your support! Please consider donation to help us maintain this project.   #
# https://opencollective.com/openapi_generator/donate                                      #
############################################################################################
```

`frontend/src/generated` 配下に生成されたコードが入っていることを確認してください。


サーバー側も自動で生成する

```bash
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    -g python-flask \
    -o /local/backend
```

以下のようになればOK!

```bash
############################################################################################
# Thanks for using OpenAPI Generator.                                                      #
# We appreciate your support! Please consider donation to help us maintain this project.   #
# https://opencollective.com/openapi_generator/donate                                      #
############################################################################################
```

`backend` 配下に生成されたコードが入っていることを確認してください。


起動する

```bash
docker compose up --build
```
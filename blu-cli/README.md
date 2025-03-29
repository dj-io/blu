<br/>
<div align="center">
  <a href="https://www.stratumlabs.ai/blu">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="../assets/blue-fire-fx-for-game-design-free-png-1459789154.png">
      <source media="(prefers-color-scheme: light)" srcset="../assets/blue-fire-fx-for-game-design-free-png-1459789154.png">
      <img alt="logo" src="../assets/blue-fire-fx-for-game-design-free-png-1459789154.png" height="200" align="center">
    </picture>
  </a>
<br/>

<br/>

<!-- [![2023 Y Combinator Startup](https://img.shields.io/badge/Y%20Combinator-2025-orange)](https://www.ycombinator.com/companies/blu) -->

[![Pypi](https://img.shields.io/pypi/v/blu-cli.svg)](https://pypi.org/project/blu-cli/0.1.0/)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)

[![Discord](https://img.shields.io/badge/discord-purple.svg)](https://discord.gg/MrrccdMM)
[![Documentation](https://img.shields.io/badge/Read%20our%20Documentation-black?logo=book)](https://stratumlabs.ai/blu/learn/home?utm_source=blu-cli/blu/readme-read-our-documentation)

</div>

BLU is a platform that allows you to create or input any file or directory and scaffold project resources in a few commands.

<div align="center">
    <a href="../assets/Screenshot 2025-01-25 at 11.40.31 PM.png" target="_blank">
        <picture>
            <source srcset="../assets/Screenshot 2025-01-25 at 11.40.31 PM.png" media="(prefers-color-scheme: dark)">
            <source srcset="../assets/Screenshot 2025-01-25 at 11.40.31 PM.png" media="(prefers-color-scheme: light)">
            <img src="../assets/Screenshot 2025-01-25 at 11.40.31 PM.png" width="700" alt="CLI Output example">
        </picture>
    </a>
</div>

## ⚗️ Scaffolding

One medium to use the Blu platform is via a command line interface (CLI) and requires pip. To install it, run:

```bash
pip install blu-cli
```

Initialize BLU with your Project spec:

```bash
blu init <my-project>
```

Your directory should look like the following:

```yaml
<my-project>/
├─ blu.config.json
├─ generators.yml # generators you're using
└─ <project-type>/
  └─ config.json # your project type config
  └─ main.ts
```

Finally, to share your project, run:

```bash
blu deploy <project-name>
```

🎉 Once the command completes, you'll see your project configuration, status and domains at [BLU-PaaS](https://www.stratumlabs.ai/blu/user-id/<app-name>) .

## ⚗️ Generation

BLU can also generate project documentation using context provided from any file or directory on your system using [blu-services](https://github.com/dj-io/blu/blob/main/blu-services/README.md) generation API reference. Additionally MCP allows BLU to write what you generate directly in the apps you use. To generate docs run `blu generate <file-or-dir>`

<!-- Check out docs built with BLU:

- [some-company-public-docs](https://company-docs.com)
- [some-other-company-docs](https://some-other-company-docs.com/) -->

<!-- Get started [here](https://github.com/fern-api/docs-starter-openapi). -->

## ⚗️ CLI Commands

Here's a quick look at the most popular CLI commands. View the documentation for [all CLI commands](https://stratumlabs.ai/blu/learn/cli-api/cli-reference/commands).

`blu init <stack>`: Creates a repository using the latest build tools.

`blu auth`: Add auth to any existing server application

`blu generate`: Generate feature documentation, tickets, design docs etc..

`blu deploy aws/gcp/azure`: Deploy any repository to any cloud provider, and get access to cloud services management locally.

`blu add deploy-<infra>`: include additional infrastructure in your `infra.yml`. For example, `blu add deploy-observability`.

`blu open-sdk/api/doc`: initialize and generate a project using openapi spec to create a public sdk, api or doc for your repository.

`blu add open-sdk/api/doc-<generator>`: include a new generator in your `generators.yml`. For example, `blu add blu-python-sdk`.

`blu gh/gl/bb create/add`: Create or add a repository in any source control platform and initialize it locally.

## Advanced

### Optimized First

BLU supports developers and teams that want to be Optimized-first or Spec-first.

Define your Project type, and use BLU to generate build specs, networking code and boilerplate application code. The generated build spec adds plugins, modules and commands that add type safety, reduce bundle size and improve performance.

Tech Stacks and Frameworks currently supported:

- [VERT](./generators/vert)
- [Spring Boot](./generators/java)
- [FastAPI](./generators/python)


<!--
Checkout open source projects that are using BLU:

- [some OSS](https://github.com/some-company/blu-config)
- [some other OSS](https://github.com/some-company/blu-config) -->

## Inspiration

Blu is inspired by internal tooling built to enhance software development team experience, with the intended purpose streamlining development workflows.

## Community

[Join our Discord!](https://discord.gg/MrrccdMMG) We are here to answer questions and help you get the most out of BLU.

## Contributing

We welcome community contributions. For guidelines, refer to our [CONTRIBUTING.md](/CONTRIBUTING.md).

![BLU Contributors](https://contrib.rocks/image?repo=dj-io/blu)

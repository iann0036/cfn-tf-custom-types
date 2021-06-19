# TF::DigitalOcean::App SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>[ <a href="domaindefinition.md">DomainDefinition</a>, ... ]</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
    "<a href="#job" title="Job">Job</a>" : <i>[ <a href="jobdefinition.md">JobDefinition</a>, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
    "<a href="#staticsite" title="StaticSite">StaticSite</a>" : <i>[ <a href="staticsitedefinition.md">StaticSiteDefinition</a>, ... ]</i>,
    "<a href="#worker" title="Worker">Worker</a>" : <i>[ <a href="workerdefinition.md">WorkerDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
<a href="#domain" title="Domain">Domain</a>: <i>
      - <a href="domaindefinition.md">DomainDefinition</a></i>
<a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
<a href="#job" title="Job">Job</a>: <i>
      - <a href="jobdefinition.md">JobDefinition</a></i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
<a href="#staticsite" title="StaticSite">StaticSite</a>: <i>
      - <a href="staticsitedefinition.md">StaticSiteDefinition</a></i>
<a href="#worker" title="Worker">Worker</a>: <i>
      - <a href="workerdefinition.md">WorkerDefinition</a></i>
</pre>

## Properties

#### Domains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of <a href="domaindefinition.md">DomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Job

_Required_: No

_Type_: List of <a href="jobdefinition.md">JobDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticSite

_Required_: No

_Type_: List of <a href="staticsitedefinition.md">StaticSiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Worker

_Required_: No

_Type_: List of <a href="workerdefinition.md">WorkerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


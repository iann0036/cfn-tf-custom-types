# TF::Databricks::InstancePool PreloadedDockerImageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#basicauth" title="BasicAuth">BasicAuth</a>" : <i>[ <a href="basicauthdefinition.md">BasicAuthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#basicauth" title="BasicAuth">BasicAuth</a>: <i>
      - <a href="basicauthdefinition.md">BasicAuthDefinition</a></i>
</pre>

## Properties

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuth

_Required_: No

_Type_: List of <a href="basicauthdefinition.md">BasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


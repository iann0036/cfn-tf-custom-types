# Terraform::Rundeck::Job Plugin

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="plugin-config.md">Config</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="plugin-config.md">Config</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Config

Map of arbitrary configuration properties for the selected plugin.

_Required_: No

_Type_: List of <a href="plugin-config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The name of the plugin to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


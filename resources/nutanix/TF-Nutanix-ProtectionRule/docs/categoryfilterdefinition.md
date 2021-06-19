# TF::Nutanix::ProtectionRule CategoryFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kindlist" title="KindList">KindList</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#params" title="Params">Params</a>" : <i>[ <a href="paramsdefinition.md">ParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#kindlist" title="KindList">KindList</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#params" title="Params">Params</a>: <i>
      - <a href="paramsdefinition.md">ParamsDefinition</a></i>
</pre>

## Properties

#### KindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: No

_Type_: List of <a href="paramsdefinition.md">ParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


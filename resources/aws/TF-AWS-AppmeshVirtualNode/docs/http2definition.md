# TF::AWS::AppmeshVirtualNode Http2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idle" title="Idle">Idle</a>" : <i>[ <a href="idledefinition.md">IdleDefinition</a>, ... ]</i>,
    "<a href="#perrequest" title="PerRequest">PerRequest</a>" : <i>[ <a href="perrequestdefinition.md">PerRequestDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#idle" title="Idle">Idle</a>: <i>
      - <a href="idledefinition.md">IdleDefinition</a></i>
<a href="#perrequest" title="PerRequest">PerRequest</a>: <i>
      - <a href="perrequestdefinition.md">PerRequestDefinition</a></i>
</pre>

## Properties

#### Idle

_Required_: No

_Type_: List of <a href="idledefinition.md">IdleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerRequest

_Required_: No

_Type_: List of <a href="perrequestdefinition.md">PerRequestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


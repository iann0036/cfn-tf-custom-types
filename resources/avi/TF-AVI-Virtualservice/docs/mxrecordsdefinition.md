# TF::AVI::Virtualservice MxRecordsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#host" title="Host">Host</a>" : <i>[ <a href="hostdefinition.md">HostDefinition</a>, ... ]</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#host" title="Host">Host</a>: <i>
      - <a href="hostdefinition.md">HostDefinition</a></i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
</pre>

## Properties

#### Host

_Required_: Yes

_Type_: List of <a href="hostdefinition.md">HostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


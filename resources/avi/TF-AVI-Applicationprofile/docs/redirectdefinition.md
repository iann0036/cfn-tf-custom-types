# TF::AVI::Applicationprofile RedirectDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keepquery" title="KeepQuery">KeepQuery</a>" : <i>Boolean</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>[ <a href="hostdefinition.md">HostDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keepquery" title="KeepQuery">KeepQuery</a>: <i>Boolean</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>
      - <a href="hostdefinition.md">HostDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
</pre>

## Properties

#### KeepQuery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of <a href="hostdefinition.md">HostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


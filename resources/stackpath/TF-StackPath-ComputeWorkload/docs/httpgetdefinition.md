# TF::StackPath::ComputeWorkload HttpGetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpheaders" title="HttpHeaders">HttpHeaders</a>" : <i>[ <a href="httpheadersdefinition2.md">HttpHeadersDefinition2</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#httpheaders" title="HttpHeaders">HttpHeaders</a>: <i>
      - <a href="httpheadersdefinition2.md">HttpHeadersDefinition2</a></i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
</pre>

## Properties

#### HttpHeaders

_Required_: No

_Type_: List of <a href="httpheadersdefinition2.md">HttpHeadersDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


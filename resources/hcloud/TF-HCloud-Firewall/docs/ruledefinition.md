# TF::HCloud::Firewall RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationips" title="DestinationIps">DestinationIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceips" title="SourceIps">SourceIps</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationips" title="DestinationIps">DestinationIps</a>: <i>
      - String</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceips" title="SourceIps">SourceIps</a>: <i>
      - String</i>
</pre>

## Properties

#### DestinationIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


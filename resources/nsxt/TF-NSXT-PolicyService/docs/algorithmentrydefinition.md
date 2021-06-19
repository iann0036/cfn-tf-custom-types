# TF::NSXT::PolicyService AlgorithmEntryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationport" title="DestinationPort">DestinationPort</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#sourceports" title="SourcePorts">SourcePorts</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationport" title="DestinationPort">DestinationPort</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#sourceports" title="SourcePorts">SourcePorts</a>: <i>
      - String</i>
</pre>

## Properties

#### Algorithm

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPort

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePorts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


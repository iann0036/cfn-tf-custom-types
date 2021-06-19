# TF::AzureRM::FirewallPolicyRuleCollectionGroup RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationfqdns" title="DestinationFqdns">DestinationFqdns</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationipgroups" title="DestinationIpGroups">DestinationIpGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationports" title="DestinationPorts">DestinationPorts</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceipgroups" title="SourceIpGroups">SourceIpGroups</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
<a href="#destinationfqdns" title="DestinationFqdns">DestinationFqdns</a>: <i>
      - String</i>
<a href="#destinationipgroups" title="DestinationIpGroups">DestinationIpGroups</a>: <i>
      - String</i>
<a href="#destinationports" title="DestinationPorts">DestinationPorts</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protocols" title="Protocols">Protocols</a>: <i>
      - String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourceipgroups" title="SourceIpGroups">SourceIpGroups</a>: <i>
      - String</i>
</pre>

## Properties

#### DestinationAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationFqdns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationIpGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPorts

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


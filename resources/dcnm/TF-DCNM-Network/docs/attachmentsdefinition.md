# TF::DCNM::Network AttachmentsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attach" title="Attach">Attach</a>" : <i>Boolean</i>,
    "<a href="#dot1qvlan" title="Dot1Qvlan">Dot1Qvlan</a>" : <i>Double</i>,
    "<a href="#extensionvalues" title="ExtensionValues">ExtensionValues</a>" : <i>String</i>,
    "<a href="#freefromconfig" title="FreeFromConfig">FreeFromConfig</a>" : <i>String</i>,
    "<a href="#instancevalues" title="InstanceValues">InstanceValues</a>" : <i>String</i>,
    "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
    "<a href="#switchports" title="SwitchPorts">SwitchPorts</a>" : <i>[ String, ... ]</i>,
    "<a href="#untagged" title="Untagged">Untagged</a>" : <i>Boolean</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#attach" title="Attach">Attach</a>: <i>Boolean</i>
<a href="#dot1qvlan" title="Dot1Qvlan">Dot1Qvlan</a>: <i>Double</i>
<a href="#extensionvalues" title="ExtensionValues">ExtensionValues</a>: <i>String</i>
<a href="#freefromconfig" title="FreeFromConfig">FreeFromConfig</a>: <i>String</i>
<a href="#instancevalues" title="InstanceValues">InstanceValues</a>: <i>String</i>
<a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
<a href="#switchports" title="SwitchPorts">SwitchPorts</a>: <i>
      - String</i>
<a href="#untagged" title="Untagged">Untagged</a>: <i>Boolean</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
</pre>

## Properties

#### Attach

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dot1Qvlan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtensionValues

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeFromConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceValues

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchPorts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Untagged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


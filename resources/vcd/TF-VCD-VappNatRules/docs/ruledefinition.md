# TF::VCD::VappNatRules RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#externalip" title="ExternalIp">ExternalIp</a>" : <i>String</i>,
    "<a href="#externalport" title="ExternalPort">ExternalPort</a>" : <i>Double</i>,
    "<a href="#forwardtoport" title="ForwardToPort">ForwardToPort</a>" : <i>Double</i>,
    "<a href="#mappingmode" title="MappingMode">MappingMode</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#vmid" title="VmId">VmId</a>" : <i>String</i>,
    "<a href="#vmnicid" title="VmNicId">VmNicId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#externalip" title="ExternalIp">ExternalIp</a>: <i>String</i>
<a href="#externalport" title="ExternalPort">ExternalPort</a>: <i>Double</i>
<a href="#forwardtoport" title="ForwardToPort">ForwardToPort</a>: <i>Double</i>
<a href="#mappingmode" title="MappingMode">MappingMode</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#vmid" title="VmId">VmId</a>: <i>String</i>
<a href="#vmnicid" title="VmNicId">VmNicId</a>: <i>Double</i>
</pre>

## Properties

#### ExternalIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardToPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmNicId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


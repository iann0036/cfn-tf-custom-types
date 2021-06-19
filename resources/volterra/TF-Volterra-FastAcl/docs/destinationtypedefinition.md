# TF::Volterra::FastAcl DestinationTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allservices" title="AllServices">AllServices</a>" : <i>Boolean</i>,
    "<a href="#interfaceservices" title="InterfaceServices">InterfaceServices</a>" : <i>Boolean</i>,
    "<a href="#sharedvipservices" title="SharedVipServices">SharedVipServices</a>" : <i>Boolean</i>,
    "<a href="#vipservices" title="VipServices">VipServices</a>" : <i>Boolean</i>,
    "<a href="#destinationipaddress" title="DestinationIpAddress">DestinationIpAddress</a>" : <i>[ <a href="destinationipaddressdefinition.md">DestinationIpAddressDefinition</a>, ... ]</i>,
    "<a href="#selectedvipaddress" title="SelectedVipAddress">SelectedVipAddress</a>" : <i>[ <a href="selectedvipaddressdefinition.md">SelectedVipAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allservices" title="AllServices">AllServices</a>: <i>Boolean</i>
<a href="#interfaceservices" title="InterfaceServices">InterfaceServices</a>: <i>Boolean</i>
<a href="#sharedvipservices" title="SharedVipServices">SharedVipServices</a>: <i>Boolean</i>
<a href="#vipservices" title="VipServices">VipServices</a>: <i>Boolean</i>
<a href="#destinationipaddress" title="DestinationIpAddress">DestinationIpAddress</a>: <i>
      - <a href="destinationipaddressdefinition.md">DestinationIpAddressDefinition</a></i>
<a href="#selectedvipaddress" title="SelectedVipAddress">SelectedVipAddress</a>: <i>
      - <a href="selectedvipaddressdefinition.md">SelectedVipAddressDefinition</a></i>
</pre>

## Properties

#### AllServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedVipServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationIpAddress

_Required_: No

_Type_: List of <a href="destinationipaddressdefinition.md">DestinationIpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedVipAddress

_Required_: No

_Type_: List of <a href="selectedvipaddressdefinition.md">SelectedVipAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


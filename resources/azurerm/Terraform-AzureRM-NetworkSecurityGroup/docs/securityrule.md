# Terraform::AzureRM::NetworkSecurityGroup SecurityRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationaddressprefix" title="DestinationAddressPrefix">DestinationAddressPrefix</a>" : <i>String</i>,
    "<a href="#destinationaddressprefixes" title="DestinationAddressPrefixes">DestinationAddressPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationapplicationsecuritygroupids" title="DestinationApplicationSecurityGroupIds">DestinationApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>" : <i>String</i>,
    "<a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>" : <i>String</i>,
    "<a href="#sourceaddressprefixes" title="SourceAddressPrefixes">SourceAddressPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceapplicationsecuritygroupids" title="SourceApplicationSecurityGroupIds">SourceApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>String</i>,
    "<a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationaddressprefix" title="DestinationAddressPrefix">DestinationAddressPrefix</a>: <i>String</i>
<a href="#destinationaddressprefixes" title="DestinationAddressPrefixes">DestinationAddressPrefixes</a>: <i>
      - String</i>
<a href="#destinationapplicationsecuritygroupids" title="DestinationApplicationSecurityGroupIds">DestinationApplicationSecurityGroupIds</a>: <i>
      - String</i>
<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>: <i>String</i>
<a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>: <i>
      - String</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>: <i>String</i>
<a href="#sourceaddressprefixes" title="SourceAddressPrefixes">SourceAddressPrefixes</a>: <i>
      - String</i>
<a href="#sourceapplicationsecuritygroupids" title="SourceApplicationSecurityGroupIds">SourceApplicationSecurityGroupIds</a>: <i>
      - String</i>
<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>String</i>
<a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>: <i>
      - String</i>
</pre>

## Properties

#### Access

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationApplicationSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceApplicationSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


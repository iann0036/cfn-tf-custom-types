# TF::Aviatrix::Firenet FirewallInstanceAssociationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attached" title="Attached">Attached</a>" : <i>Boolean</i>,
    "<a href="#egressinterface" title="EgressInterface">EgressInterface</a>" : <i>String</i>,
    "<a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>" : <i>String</i>,
    "<a href="#firewallname" title="FirewallName">FirewallName</a>" : <i>String</i>,
    "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
    "<a href="#laninterface" title="LanInterface">LanInterface</a>" : <i>String</i>,
    "<a href="#managementinterface" title="ManagementInterface">ManagementInterface</a>" : <i>String</i>,
    "<a href="#vendortype" title="VendorType">VendorType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#attached" title="Attached">Attached</a>: <i>Boolean</i>
<a href="#egressinterface" title="EgressInterface">EgressInterface</a>: <i>String</i>
<a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>: <i>String</i>
<a href="#firewallname" title="FirewallName">FirewallName</a>: <i>String</i>
<a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
<a href="#laninterface" title="LanInterface">LanInterface</a>: <i>String</i>
<a href="#managementinterface" title="ManagementInterface">ManagementInterface</a>: <i>String</i>
<a href="#vendortype" title="VendorType">VendorType</a>: <i>String</i>
</pre>

## Properties

#### Attached

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirenetGwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LanInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


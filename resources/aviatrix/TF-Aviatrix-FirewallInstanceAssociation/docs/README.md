# TF::Aviatrix::FirewallInstanceAssociation

The **aviatrix_firewall_instance_association** resource allows for the creation and management of a firewall instance association. To use this resource you must also have an `aviatrix_firenet` resource with it's `manage_firewall_instance_association` attribute set to false.

Available in provider version R2.17.1+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FirewallInstanceAssociation",
    "Properties" : {
        "<a href="#attached" title="Attached">Attached</a>" : <i>Boolean</i>,
        "<a href="#egressinterface" title="EgressInterface">EgressInterface</a>" : <i>String</i>,
        "<a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>" : <i>String</i>,
        "<a href="#firewallname" title="FirewallName">FirewallName</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#laninterface" title="LanInterface">LanInterface</a>" : <i>String</i>,
        "<a href="#managementinterface" title="ManagementInterface">ManagementInterface</a>" : <i>String</i>,
        "<a href="#vendortype" title="VendorType">VendorType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FirewallInstanceAssociation
Properties:
    <a href="#attached" title="Attached">Attached</a>: <i>Boolean</i>
    <a href="#egressinterface" title="EgressInterface">EgressInterface</a>: <i>String</i>
    <a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>: <i>String</i>
    <a href="#firewallname" title="FirewallName">FirewallName</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#laninterface" title="LanInterface">LanInterface</a>: <i>String</i>
    <a href="#managementinterface" title="ManagementInterface">ManagementInterface</a>: <i>String</i>
    <a href="#vendortype" title="VendorType">VendorType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
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

_Required_: No

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

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


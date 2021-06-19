# TF::Aviatrix::Firenet

The **aviatrix_firenet** resource allows the creation and management of [Aviatrix Firewall Networks](https://docs.aviatrix.com/HowTos/firewall_network_faq.html).

~> **NOTE:** This resource is used in conjunction with multiple other resources that may include, and are not limited to: **firewall_instance**, **firewall_instance_association**, **aws_tgw**, and **transit_gateway** resources or even **aviatrix_fqdn**, under the Aviatrix FireNet solution. Explicit dependencies may be set using `depends_on`. For more information on proper FireNet configuration, please see the workflow [here](https://docs.aviatrix.com/HowTos/firewall_network_workflow.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Firenet",
    "Properties" : {
        "<a href="#egressenabled" title="EgressEnabled">EgressEnabled</a>" : <i>Boolean</i>,
        "<a href="#egressstaticcidrs" title="EgressStaticCidrs">EgressStaticCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#hashingalgorithm" title="HashingAlgorithm">HashingAlgorithm</a>" : <i>String</i>,
        "<a href="#inspectionenabled" title="InspectionEnabled">InspectionEnabled</a>" : <i>Boolean</i>,
        "<a href="#keepalivevialaninterfaceenabled" title="KeepAliveViaLanInterfaceEnabled">KeepAliveViaLanInterfaceEnabled</a>" : <i>Boolean</i>,
        "<a href="#managefirewallinstanceassociation" title="ManageFirewallInstanceAssociation">ManageFirewallInstanceAssociation</a>" : <i>Boolean</i>,
        "<a href="#tgwsegmentationforegressenabled" title="TgwSegmentationForEgressEnabled">TgwSegmentationForEgressEnabled</a>" : <i>Boolean</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#firewallinstanceassociation" title="FirewallInstanceAssociation">FirewallInstanceAssociation</a>" : <i>[ <a href="firewallinstanceassociationdefinition.md">FirewallInstanceAssociationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Firenet
Properties:
    <a href="#egressenabled" title="EgressEnabled">EgressEnabled</a>: <i>Boolean</i>
    <a href="#egressstaticcidrs" title="EgressStaticCidrs">EgressStaticCidrs</a>: <i>
      - String</i>
    <a href="#hashingalgorithm" title="HashingAlgorithm">HashingAlgorithm</a>: <i>String</i>
    <a href="#inspectionenabled" title="InspectionEnabled">InspectionEnabled</a>: <i>Boolean</i>
    <a href="#keepalivevialaninterfaceenabled" title="KeepAliveViaLanInterfaceEnabled">KeepAliveViaLanInterfaceEnabled</a>: <i>Boolean</i>
    <a href="#managefirewallinstanceassociation" title="ManageFirewallInstanceAssociation">ManageFirewallInstanceAssociation</a>: <i>Boolean</i>
    <a href="#tgwsegmentationforegressenabled" title="TgwSegmentationForEgressEnabled">TgwSegmentationForEgressEnabled</a>: <i>Boolean</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#firewallinstanceassociation" title="FirewallInstanceAssociation">FirewallInstanceAssociation</a>: <i>
      - <a href="firewallinstanceassociationdefinition.md">FirewallInstanceAssociationDefinition</a></i>
</pre>

## Properties

#### EgressEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressStaticCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashingAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveViaLanInterfaceEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageFirewallInstanceAssociation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwSegmentationForEgressEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallInstanceAssociation

_Required_: No

_Type_: List of <a href="firewallinstanceassociationdefinition.md">FirewallInstanceAssociationDefinition</a>

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


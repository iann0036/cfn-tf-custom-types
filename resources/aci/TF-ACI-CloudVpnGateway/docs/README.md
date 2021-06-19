# TF::ACI::CloudVpnGateway

CloudFormation equivalent of aci_cloud_vpn_gateway

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::CloudVpnGateway",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#cloudcontextprofiledn" title="CloudContextProfileDn">CloudContextProfileDn</a>" : <i>String</i>,
        "<a href="#cloudrouterprofiletype" title="CloudRouterProfileType">CloudRouterProfileType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#numinstances" title="NumInstances">NumInstances</a>" : <i>String</i>,
        "<a href="#relationcloudrstodirectconnpol" title="RelationCloudRsToDirectConnPol">RelationCloudRsToDirectConnPol</a>" : <i>String</i>,
        "<a href="#relationcloudrstohostrouterpol" title="RelationCloudRsToHostRouterPol">RelationCloudRsToHostRouterPol</a>" : <i>String</i>,
        "<a href="#relationcloudrstovpngwpol" title="RelationCloudRsToVpnGwPol">RelationCloudRsToVpnGwPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::CloudVpnGateway
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#cloudcontextprofiledn" title="CloudContextProfileDn">CloudContextProfileDn</a>: <i>String</i>
    <a href="#cloudrouterprofiletype" title="CloudRouterProfileType">CloudRouterProfileType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#numinstances" title="NumInstances">NumInstances</a>: <i>String</i>
    <a href="#relationcloudrstodirectconnpol" title="RelationCloudRsToDirectConnPol">RelationCloudRsToDirectConnPol</a>: <i>String</i>
    <a href="#relationcloudrstohostrouterpol" title="RelationCloudRsToHostRouterPol">RelationCloudRsToHostRouterPol</a>: <i>String</i>
    <a href="#relationcloudrstovpngwpol" title="RelationCloudRsToVpnGwPol">RelationCloudRsToVpnGwPol</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudContextProfileDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRouterProfileType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumInstances

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationCloudRsToDirectConnPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationCloudRsToHostRouterPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationCloudRsToVpnGwPol

_Required_: No

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


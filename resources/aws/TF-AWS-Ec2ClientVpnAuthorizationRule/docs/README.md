# TF::AWS::Ec2ClientVpnAuthorizationRule

Provides authorization rules for AWS Client VPN endpoints. For more information on usage, please see the
[AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Ec2ClientVpnAuthorizationRule",
    "Properties" : {
        "<a href="#accessgroupid" title="AccessGroupId">AccessGroupId</a>" : <i>String</i>,
        "<a href="#authorizeallgroups" title="AuthorizeAllGroups">AuthorizeAllGroups</a>" : <i>Boolean</i>,
        "<a href="#clientvpnendpointid" title="ClientVpnEndpointId">ClientVpnEndpointId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#targetnetworkcidr" title="TargetNetworkCidr">TargetNetworkCidr</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Ec2ClientVpnAuthorizationRule
Properties:
    <a href="#accessgroupid" title="AccessGroupId">AccessGroupId</a>: <i>String</i>
    <a href="#authorizeallgroups" title="AuthorizeAllGroups">AuthorizeAllGroups</a>: <i>Boolean</i>
    <a href="#clientvpnendpointid" title="ClientVpnEndpointId">ClientVpnEndpointId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#targetnetworkcidr" title="TargetNetworkCidr">TargetNetworkCidr</a>: <i>String</i>
</pre>

## Properties

#### AccessGroupId

The ID of the group to which the authorization rule grants access. One of `access_group_id` or `authorize_all_groups` must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizeAllGroups

Indicates whether the authorization rule grants access to all clients. One of `access_group_id` or `authorize_all_groups` must be set.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientVpnEndpointId

The ID of the Client VPN endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A brief description of the authorization rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetNetworkCidr

The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.

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


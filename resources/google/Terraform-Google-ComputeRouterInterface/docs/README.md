# Terraform::Google::ComputeRouterInterface

Manages a Cloud Router interface. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeRouterInterface",
    "Properties" : {
        "<a href="#interconnectattachment" title="InterconnectAttachment">InterconnectAttachment</a>" : <i>String</i>,
        "<a href="#iprange" title="IpRange">IpRange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>String</i>,
        "<a href="#vpntunnel" title="VpnTunnel">VpnTunnel</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeRouterInterface
Properties:
    <a href="#interconnectattachment" title="InterconnectAttachment">InterconnectAttachment</a>: <i>String</i>
    <a href="#iprange" title="IpRange">IpRange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>String</i>
    <a href="#vpntunnel" title="VpnTunnel">VpnTunnel</a>: <i>String</i>
</pre>

## Properties

#### InterconnectAttachment

The name or resource link to the
VLAN interconnect for this interface. Changing this forces a new interface to
be created. Only one of `vpn_tunnel` and `interconnect_attachment` can be
specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which this interface's router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region this interface's router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

The name of the router this interface will be attached to.
Changing this forces a new interface to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnTunnel

The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created. Only
one of `vpn_tunnel` and `interconnect_attachment` can be specified.

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


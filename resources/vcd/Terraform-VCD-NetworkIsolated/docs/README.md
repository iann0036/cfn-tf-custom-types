# Terraform::VCD::NetworkIsolated

Provides a vCloud Director Org VDC isolated Network. This can be used to create,
modify, and delete internal networks for vApps to connect. This network is not attached to external networks or routers.

Supported in provider *v2.0+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::NetworkIsolated",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dns1" title="Dns1">Dns1</a>" : <i>String</i>,
        "<a href="#dns2" title="Dns2">Dns2</a>" : <i>String</i>,
        "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#dhcppool" title="DhcpPool">DhcpPool</a>" : <i>[ <a href="dhcppool.md">DhcpPool</a>, ... ]</i>,
        "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ <a href="staticippool.md">StaticIpPool</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::NetworkIsolated
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dns1" title="Dns1">Dns1</a>: <i>String</i>
    <a href="#dns2" title="Dns2">Dns2</a>: <i>String</i>
    <a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#dhcppool" title="DhcpPool">DhcpPool</a>: <i>
      - <a href="dhcppool.md">DhcpPool</a></i>
    <a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - <a href="staticippool.md">StaticIpPool</a></i>
</pre>

## Properties

#### Description

An optional description of the network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns1

First DNS server to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns2

Second DNS server to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffix

A FQDN for the virtual machines on this network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

The netmask for the new network. Defaults to `255.255.255.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when
connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

Defines if this network is shared between multiple VDCs
in the Org.  Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpPool

_Required_: No

_Type_: List of <a href="dhcppool.md">DhcpPool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No

_Type_: List of <a href="staticippool.md">StaticIpPool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Href

Returns the <code>Href</code> value.


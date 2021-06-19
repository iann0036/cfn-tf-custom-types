# TF::FortiOS::VpnipsecManualkeyinterface

Configure IPsec manual keys.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnipsecManualkeyinterface",
    "Properties" : {
        "<a href="#addrtype" title="AddrType">AddrType</a>" : <i>String</i>,
        "<a href="#authalg" title="AuthAlg">AuthAlg</a>" : <i>String</i>,
        "<a href="#authkey" title="AuthKey">AuthKey</a>" : <i>String</i>,
        "<a href="#encalg" title="EncAlg">EncAlg</a>" : <i>String</i>,
        "<a href="#enckey" title="EncKey">EncKey</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
        "<a href="#localgw" title="LocalGw">LocalGw</a>" : <i>String</i>,
        "<a href="#localgw6" title="LocalGw6">LocalGw6</a>" : <i>String</i>,
        "<a href="#localspi" title="LocalSpi">LocalSpi</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotegw" title="RemoteGw">RemoteGw</a>" : <i>String</i>,
        "<a href="#remotegw6" title="RemoteGw6">RemoteGw6</a>" : <i>String</i>,
        "<a href="#remotespi" title="RemoteSpi">RemoteSpi</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnipsecManualkeyinterface
Properties:
    <a href="#addrtype" title="AddrType">AddrType</a>: <i>String</i>
    <a href="#authalg" title="AuthAlg">AuthAlg</a>: <i>String</i>
    <a href="#authkey" title="AuthKey">AuthKey</a>: <i>String</i>
    <a href="#encalg" title="EncAlg">EncAlg</a>: <i>String</i>
    <a href="#enckey" title="EncKey">EncKey</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
    <a href="#localgw" title="LocalGw">LocalGw</a>: <i>String</i>
    <a href="#localgw6" title="LocalGw6">LocalGw6</a>: <i>String</i>
    <a href="#localspi" title="LocalSpi">LocalSpi</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotegw" title="RemoteGw">RemoteGw</a>: <i>String</i>
    <a href="#remotegw6" title="RemoteGw6">RemoteGw6</a>: <i>String</i>
    <a href="#remotespi" title="RemoteSpi">RemoteSpi</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AddrType

IP version to use for IP packets. Valid values: `4`, `6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthAlg

Authentication algorithm. Must be the same for both ends of the tunnel. Valid values: `null`, `md5`, `sha1`, `sha256`, `sha384`, `sha512`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthKey

Hexadecimal authentication key in 16-digit (8-byte) segments separated by hyphens.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncAlg

Encryption algorithm. Must be the same for both ends of the tunnel. Valid values: `null`, `des`, `3des`, `aes128`, `aes192`, `aes256`, `aria128`, `aria192`, `aria256`, `seed`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncKey

Hexadecimal encryption key in 16-digit (8-byte) segments separated by hyphens.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Name of the physical, aggregate, or VLAN interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

IP version to use for VPN interface. Valid values: `4`, `6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGw

IPv4 address of the local gateway's external interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGw6

Local IPv6 address of VPN gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSpi

Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IPsec tunnel name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw

IPv4 address of the remote gateway's external interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw6

Remote IPv6 address of VPN gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSpi

Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns between two traffic streams with different encryption rules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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


# Terraform::OCI::CoreIpsecConnectionTunnelManagement

This resource provides the Ip Sec Connection Tunnel Management resource in Oracle Cloud Infrastructure Core service.

Updates the specified tunnel. This operation lets you change tunnel attributes such as the
routing type (BGP dynamic routing or static routing). Here are some important notes:

	* If you change the tunnel's routing type or BGP session configuration, the tunnel will go
	down while it's reprovisioned.

	* If you want to switch the tunnel's `routing` from `STATIC` to `BGP`, make sure the tunnel's
	BGP session configuration attributes have been set ([bgpSessionConfig](#/en/iaas/20160918/datatypes/BgpSessionInfo)).

	* If you want to switch the tunnel's `routing` from `BGP` to `STATIC`, make sure the
	[IPSecConnection](#/en/iaas/20160918/IPSecConnection/) already has at least one valid CIDR
	static route.

** IMPORTANT **
Destroying `the oci_core_ipsec_connection_tunnel_management` leaves the resource in its existing state. It will not destroy the tunnel and it will not return the tunnel to its default values.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreIpsecConnectionTunnelManagement",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
        "<a href="#ipsecid" title="IpsecId">IpsecId</a>" : <i>String</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>String</i>,
        "<a href="#sharedsecret" title="SharedSecret">SharedSecret</a>" : <i>String</i>,
        "<a href="#tunnelid" title="TunnelId">TunnelId</a>" : <i>String</i>,
        "<a href="#bgpsessioninfo" title="BgpSessionInfo">BgpSessionInfo</a>" : <i>[ <a href="bgpsessioninfo.md">BgpSessionInfo</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreIpsecConnectionTunnelManagement
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
    <a href="#ipsecid" title="IpsecId">IpsecId</a>: <i>String</i>
    <a href="#routing" title="Routing">Routing</a>: <i>String</i>
    <a href="#sharedsecret" title="SharedSecret">SharedSecret</a>: <i>String</i>
    <a href="#tunnelid" title="TunnelId">TunnelId</a>: <i>String</i>
    <a href="#bgpsessioninfo" title="BgpSessionInfo">BgpSessionInfo</a>: <i>
      - <a href="bgpsessioninfo.md">BgpSessionInfo</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DisplayName

A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `ike_version` - (Optional) Internet Key Exchange protocol version.
* `shared_secret` - (Optional) The shared secret (pre-shared key) to use for the IPSec tunnel. If you don't provide a value, Oracle generates a value for you. You can specify your own shared secret later if you like with [UpdateIPSecConnectionTunnelSharedSecret](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).  Example: `EXAMPLEToUis6j1c.p8G.dVQxcmdfMO0yXMLi.lZTbYCMDGu4V8o`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

Internet Key Exchange protocol version.
* `shared_secret` - (Optional) The shared secret (pre-shared key) to use for the IPSec tunnel. If you don't provide a value, Oracle generates a value for you. You can specify your own shared secret later if you like with [UpdateIPSecConnectionTunnelSharedSecret](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).  Example: `EXAMPLEToUis6j1c.p8G.dVQxcmdfMO0yXMLi.lZTbYCMDGu4V8o`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecId

The OCID of the IPSec connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

The type of routing to use for this tunnel (either BGP dynamic routing or static routing).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSecret

The shared secret (pre-shared key) to use for the IPSec tunnel. If you don't provide a value, Oracle generates a value for you. You can specify your own shared secret later if you like with [UpdateIPSecConnectionTunnelSharedSecret](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnelSharedSecret/UpdateIPSecConnectionTunnelSharedSecret).  Example: `EXAMPLEToUis6j1c.p8G.dVQxcmdfMO0yXMLi.lZTbYCMDGu4V8o`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelId

The OCID of the IPSec connection's tunnel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpSessionInfo

_Required_: No

_Type_: List of <a href="bgpsessioninfo.md">BgpSessionInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### CpeIp

Returns the <code>CpeIp</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### Status

Returns the <code>Status</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeStatusUpdated

Returns the <code>TimeStatusUpdated</code> value.

#### VpnIp

Returns the <code>VpnIp</code> value.


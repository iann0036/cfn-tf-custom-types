# Terraform::OCI::CoreIpsecConnectionTunnelManagement

CloudFormation equivalent of oci_core_ipsec_connection_tunnel_management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreIpsecConnectionTunnelManagement",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
        "<a href="#ipsecid" title="IpsecId">IpsecId</a>" : <i>String</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>String</i>,
        "<a href="#sharedsecret" title="SharedSecret">SharedSecret</a>" : <i>String</i>,
        "<a href="#tunnelid" title="TunnelId">TunnelId</a>" : <i>String</i>,
        "<a href="#bgpsessioninfo" title="BgpSessionInfo">BgpSessionInfo</a>" : <i>[ &lt;a href=&#34;bgpsessioninfo.md&#34;&gt;BgpSessionInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreIpsecConnectionTunnelManagement
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
    <a href="#ipsecid" title="IpsecId">IpsecId</a>: <i>String</i>
    <a href="#routing" title="Routing">Routing</a>: <i>String</i>
    <a href="#sharedsecret" title="SharedSecret">SharedSecret</a>: <i>String</i>
    <a href="#tunnelid" title="TunnelId">TunnelId</a>: <i>String</i>
    <a href="#bgpsessioninfo" title="BgpSessionInfo">BgpSessionInfo</a>: <i>
      - &lt;a href=&#34;bgpsessioninfo.md&#34;&gt;BgpSessionInfo&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpSessionInfo

_Required_: No

_Type_: List of &lt;a href=&#34;bgpsessioninfo.md&#34;&gt;BgpSessionInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;CompartmentId&lt;/code&gt; value.

#### CpeIp

Returns the &lt;code&gt;CpeIp&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

#### TimeStatusUpdated

Returns the &lt;code&gt;TimeStatusUpdated&lt;/code&gt; value.

#### VpnIp

Returns the &lt;code&gt;VpnIp&lt;/code&gt; value.


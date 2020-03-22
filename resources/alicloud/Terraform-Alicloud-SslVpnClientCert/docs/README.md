# Terraform::Alicloud::SslVpnClientCert

Provides a SSL VPN client cert resource.

-> **NOTE:** Terraform will auto build SSL VPN client certs while it uses `alicloud_ssl_vpn_client_cert` to build a ssl vpn client certs resource.
It depends on VPN instance and SSL VPN Server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SslVpnClientCert",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sslvpnserverid" title="SslVpnServerId">SslVpnServerId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SslVpnClientCert
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sslvpnserverid" title="SslVpnServerId">SslVpnServerId</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the client certificate.
- `ssl_vpn_server_id` - (Required, ForceNew) The ID of the SSL-VPN server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslVpnServerId

The ID of the SSL-VPN server.

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

#### CaCert

Returns the <code>CaCert</code> value.

#### ClientCert

Returns the <code>ClientCert</code> value.

#### ClientConfig

Returns the <code>ClientConfig</code> value.

#### ClientKey

Returns the <code>ClientKey</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.


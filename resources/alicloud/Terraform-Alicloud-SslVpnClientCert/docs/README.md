# Terraform::Alicloud::SslVpnClientCert

CloudFormation equivalent of alicloud_ssl_vpn_client_cert

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslVpnServerId

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

#### Status

Returns the <code>Status</code> value.


# Terraform::BIGIP::LtmProfileHttp2

`bigip_ltm_profile_http2` Configures a custom profile_http2 for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileHttp2",
    "Properties" : {
        "<a href="#activationmodes" title="ActivationModes">ActivationModes</a>" : <i>[ String, ... ]</i>,
        "<a href="#concurrentstreamsperconnection" title="ConcurrentStreamsPerConnection">ConcurrentStreamsPerConnection</a>" : <i>Double</i>,
        "<a href="#connectionidletimeout" title="ConnectionIdleTimeout">ConnectionIdleTimeout</a>" : <i>Double</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#headertablesize" title="HeaderTableSize">HeaderTableSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileHttp2
Properties:
    <a href="#activationmodes" title="ActivationModes">ActivationModes</a>: <i>
      - String</i>
    <a href="#concurrentstreamsperconnection" title="ConcurrentStreamsPerConnection">ConcurrentStreamsPerConnection</a>: <i>Double</i>
    <a href="#connectionidletimeout" title="ConnectionIdleTimeout">ConnectionIdleTimeout</a>: <i>Double</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#headertablesize" title="HeaderTableSize">HeaderTableSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ActivationModes

Specifies what will cause an incoming connection to be handled as a HTTP/2 connection. The default values npn and alpn specify that the TLS next-protocol-negotiation and application-layer-protocol-negotiation extensions will be used.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrentStreamsPerConnection

Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionIdleTimeout

Specifies the number of seconds that a connection is idle before the connection is eligible for deletion..

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderTableSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


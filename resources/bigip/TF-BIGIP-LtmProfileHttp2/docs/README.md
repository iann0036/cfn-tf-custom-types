# TF::BIGIP::LtmProfileHttp2

`bigip_ltm_profile_http2` Configures a custom profile_http2 for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmProfileHttp2",
    "Properties" : {
        "<a href="#activationmodes" title="ActivationModes">ActivationModes</a>" : <i>[ String, ... ]</i>,
        "<a href="#concurrentstreamsperconnection" title="ConcurrentStreamsPerConnection">ConcurrentStreamsPerConnection</a>" : <i>Double</i>,
        "<a href="#connectionidletimeout" title="ConnectionIdleTimeout">ConnectionIdleTimeout</a>" : <i>Double</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#enforcetlsrequirements" title="EnforceTlsRequirements">EnforceTlsRequirements</a>" : <i>String</i>,
        "<a href="#framesize" title="FrameSize">FrameSize</a>" : <i>Double</i>,
        "<a href="#headertablesize" title="HeaderTableSize">HeaderTableSize</a>" : <i>Double</i>,
        "<a href="#includecontentlength" title="IncludeContentLength">IncludeContentLength</a>" : <i>String</i>,
        "<a href="#insertheader" title="InsertHeader">InsertHeader</a>" : <i>String</i>,
        "<a href="#insertheadername" title="InsertHeaderName">InsertHeaderName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#receivewindow" title="ReceiveWindow">ReceiveWindow</a>" : <i>Double</i>,
        "<a href="#writesize" title="WriteSize">WriteSize</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmProfileHttp2
Properties:
    <a href="#activationmodes" title="ActivationModes">ActivationModes</a>: <i>
      - String</i>
    <a href="#concurrentstreamsperconnection" title="ConcurrentStreamsPerConnection">ConcurrentStreamsPerConnection</a>: <i>Double</i>
    <a href="#connectionidletimeout" title="ConnectionIdleTimeout">ConnectionIdleTimeout</a>: <i>Double</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#enforcetlsrequirements" title="EnforceTlsRequirements">EnforceTlsRequirements</a>: <i>String</i>
    <a href="#framesize" title="FrameSize">FrameSize</a>: <i>Double</i>
    <a href="#headertablesize" title="HeaderTableSize">HeaderTableSize</a>: <i>Double</i>
    <a href="#includecontentlength" title="IncludeContentLength">IncludeContentLength</a>: <i>String</i>
    <a href="#insertheader" title="InsertHeader">InsertHeader</a>: <i>String</i>
    <a href="#insertheadername" title="InsertHeaderName">InsertHeaderName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#receivewindow" title="ReceiveWindow">ReceiveWindow</a>: <i>Double</i>
    <a href="#writesize" title="WriteSize">WriteSize</a>: <i>Double</i>
</pre>

## Properties

#### ActivationModes

This setting specifies the condition that will cause the BIG-IP system to handle an incoming connection as an HTTP/2 connection, Allowed values : `[“alpn”]` (or) `[“always”]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrentStreamsPerConnection

Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionIdleTimeout

Specifies the number of seconds that a connection is idle before the connection is eligible for deletion.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceTlsRequirements

Enable or disable enforcement of TLS requirements,Allowed Values : `"enabled"/"disabled"` [Default:`"enabled"`].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrameSize

The size of the data frames, in bytes, that the HTTP/2 protocol sends to the client. `Default: 2048`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderTableSize

The size of the header table, in KB, for the HTTP headers that the HTTP/2 protocol compresses to save bandwidth.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeContentLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertHeader

This setting specifies whether the BIG-IP system should add an HTTP header to the HTTP request to show that the request was received over HTTP/2, Allowed Values : `"enabled"/"disabled"` [ Default: `"disabled"`].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertHeaderName

This setting specifies the name of the header that the BIG-IP system will add to the HTTP request when the Insert Header is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveWindow

The flow-control size for upload streams, in KB. `Default: 32`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteSize

The total size of combined data frames, in bytes, that the HTTP/2 protocol sends in a single write function. `Default: 16384`".

_Required_: No

_Type_: Double

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


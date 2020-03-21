# Terraform::TencentCloud::GaapLayer4Listener

Provides a resource to create a layer4 listener of GAAP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapLayer4Listener",
    "Properties" : {
        "<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>" : <i>Double</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>Boolean</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#proxyid" title="ProxyId">ProxyId</a>" : <i>String</i>,
        "<a href="#realservertype" title="RealserverType">RealserverType</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#realserverbindset" title="RealserverBindSet">RealserverBindSet</a>" : <i>[ <a href="realserverbindset.md">RealserverBindSet</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapLayer4Listener
Properties:
    <a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>: <i>Double</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>Boolean</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#proxyid" title="ProxyId">ProxyId</a>: <i>String</i>
    <a href="#realservertype" title="RealserverType">RealserverType</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#realserverbindset" title="RealserverBindSet">RealserverBindSet</a>: <i>
      - <a href="realserverbindset.md">RealserverBindSet</a></i>
</pre>

## Properties

#### ConnectTimeout

Timeout of the health check response, should less than interval, default value is 2s. NOTES: Only supports listeners of `TCP` protocol and require less than `interval`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Indicates whether health check is enable, default value is `false`. NOTES: Only supports listeners of `TCP` protocol.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Interval of the health check, default value is 5s. NOTES: Only supports listeners of `TCP` protocol.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the layer4 listener, the maximum length is 30.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port of the layer4 listener.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol of the layer4 listener, the available values include `TCP` and `UDP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyId

ID of the GAAP proxy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverType

Type of the realserver, the available values include `IP` and `DOMAIN`. NOTES: when the `protocol` is specified as `TCP` and the `scheduler` is specified as `wrr`, the item can only be set to `IP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling policy of the layer4 listener, default value is `rr`, the available values include `rr`, `wrr` and `lc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverBindSet

_Required_: No

_Type_: List of <a href="realserverbindset.md">RealserverBindSet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Status

Returns the <code>Status</code> value.


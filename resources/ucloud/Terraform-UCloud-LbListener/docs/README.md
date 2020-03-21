# Terraform::UCloud::LbListener

Provides a Load Balancer Listener resource.

~> **Note** This `listen_type` only support when `protocol` is `tcp` in the extranet mode and the default value is `request_proxy`. In addition, in the extranet mode, the `listen_type` is `request_proxy` if `protocol`is `http` or `https`, the `listen_type` is `packets_transmit` if `protocol`is `udp`. In the intranet mode, the `listen_type` is `packets_transmit`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::LbListener",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#listentype" title="ListenType">ListenType</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#persistence" title="Persistence">Persistence</a>" : <i>String</i>,
        "<a href="#persistencetype" title="PersistenceType">PersistenceType</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::LbListener
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#listentype" title="ListenType">ListenType</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#persistence" title="Persistence">Persistence</a>: <i>String</i>
    <a href="#persistencetype" title="PersistenceType">PersistenceType</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### Domain

Health check domain checking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

Health check method. Possible values are `port` as port checking and `path` as http checking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Keep alive timeout of the connection between the client and LB, measured in second. Range: 0-86400 when `listen_type` is `request_proxy`, range: 60-900 when `listen_type` is `packets_transmit` (Default: `60`). The connection will be closed as soon as no response between the client and LB if it set by `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenType

The type of listener. Possible values are `request_proxy` and `packets_transmit`. When `packets_transmit` was specified, you need to config the instances by yourself if the instances attach to the load balancer. You may refer to [configuration instruction](https://docs.ucloud.cn/network/ulb/fast/createulb/vservertype).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The ID of load balancer instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

The load balancer method in which the listener is. Possible values are: `roundrobin`, `source`, `consistent_hash`, `source_port` , `consistent_hash_port`, `weight_roundrobin` and `leastconn`. (Default: `roundrobin`).
- The `consistent_hash`, `source_port` , `consistent_hash_port`, `roundrobin`, `source` and `weight_roundrobin` are valid if `listen_type` is `packets_transmit`.
- The `roundrobin`, `source` and `weight_roundrobin` and `leastconn` are valid if `listen_type` is `request_proxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the listener. If not specified, terraform will auto-generate a name beginning with `tf-lb-listener`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Health check path checking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Persistence

Indicate whether the persistence session is enabled, it is invalid if `persistence_type` is `none`, an auto-generated string will be exported if `persistence_type` is `server_insert`, a custom string will be exported if `persistence_type` is `user_defined`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceType

The type of session persistence of listener. Possible values are: `none` as disabled, `server_insert` as auto-generated key and `user_defined` as customized key. (Default: `none`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port opened on the listeners to receive requests, range: 1-65535. The default value: `80` as `protocol` is `http`, `443` as `protocol` is `https`, `1024` as `protocol` is `tcp` or `udp`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Listener protocol. Possible values: `http`, `https`, `tcp` if `listen_type` is `request_proxy`, `tcp` and `udp` if `listen_type` is `packets_transmit`.

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

#### Status

Returns the <code>Status</code> value.


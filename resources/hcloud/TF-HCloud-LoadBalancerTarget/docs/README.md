# TF::HCloud::LoadBalancerTarget

Adds a target to a Hetzner Cloud Load Balancer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::LoadBalancerTarget",
    "Properties" : {
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>Double</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#useprivateip" title="UsePrivateIp">UsePrivateIp</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::LoadBalancerTarget
Properties:
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>Double</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#useprivateip" title="UsePrivateIp">UsePrivateIp</a>: <i>Boolean</i>
</pre>

## Properties

#### Ip

IP address for an IP Target. Required if
`type` is `ip`.
- `use_private_ip` - (Optional, bool) use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

Label Selector selecting targets
for this Load Balancer. Required if `type` is `label_selector`.
- `ip` - (Optional, string) IP address for an IP Target. Required if
`type` is `ip`.
- `use_private_ip` - (Optional, bool) use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

ID of the Load Balancer to which
the target gets attached.
- `server_id` - (Optional, int) ID of the server which should be a
target for this Load Balancer. Required if `type` is `server`
- `label_selector` - (Optional, string) Label Selector selecting targets
for this Load Balancer. Required if `type` is `label_selector`.
- `ip` - (Optional, string) IP address for an IP Target. Required if
`type` is `ip`.
- `use_private_ip` - (Optional, bool) use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

ID of the server which should be a
target for this Load Balancer. Required if `type` is `server`
- `label_selector` - (Optional, string) Label Selector selecting targets
for this Load Balancer. Required if `type` is `label_selector`.
- `ip` - (Optional, string) IP address for an IP Target. Required if
`type` is `ip`.
- `use_private_ip` - (Optional, bool) use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the target. Possible values
`server`, `label_selector`, `ip`.
- `load_balancer_id` - (Required, int) ID of the Load Balancer to which
the target gets attached.
- `server_id` - (Optional, int) ID of the server which should be a
target for this Load Balancer. Required if `type` is `server`
- `label_selector` - (Optional, string) Label Selector selecting targets
for this Load Balancer. Required if `type` is `label_selector`.
- `ip` - (Optional, string) IP address for an IP Target. Required if
`type` is `ip`.
- `use_private_ip` - (Optional, bool) use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePrivateIp

use the private IP to connect to
Load Balancer targets. Only allowed if type is `server` or
`label_selector`.

_Required_: No

_Type_: Boolean

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


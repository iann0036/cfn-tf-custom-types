# TF::HCloud::LoadBalancerService

Define services for Hetzner Cloud Load Balancers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::LoadBalancerService",
    "Properties" : {
        "<a href="#destinationport" title="DestinationPort">DestinationPort</a>" : <i>Double</i>,
        "<a href="#listenport" title="ListenPort">ListenPort</a>" : <i>Double</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#proxyprotocol" title="Proxyprotocol">Proxyprotocol</a>" : <i>Boolean</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::LoadBalancerService
Properties:
    <a href="#destinationport" title="DestinationPort">DestinationPort</a>: <i>Double</i>
    <a href="#listenport" title="ListenPort">ListenPort</a>: <i>Double</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#proxyprotocol" title="Proxyprotocol">Proxyprotocol</a>: <i>Boolean</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
</pre>

## Properties

#### DestinationPort

Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
- `proxyprotocol` - (Optional, bool) Enable proxyprotocol.
- `http` - (Optional, list) List of http configurations when `protocol` is `http` or `https`.
- `health_check` - (Optional, list) List of health check configurations when `protocol` is `http` or `https`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenPort

Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
- `destination_port` - (Optional, int) Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
- `proxyprotocol` - (Optional, bool) Enable proxyprotocol.
- `http` - (Optional, list) List of http configurations when `protocol` is `http` or `https`.
- `health_check` - (Optional, list) List of health check configurations when `protocol` is `http` or `https`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

Id of the load balancer this service belongs to.
- `protocol` - (Required, string) Protocol of the service. `http`, `https` or `tcp`
- `listen_port` - (Optional, int) Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
- `destination_port` - (Optional, int) Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
- `proxyprotocol` - (Optional, bool) Enable proxyprotocol.
- `http` - (Optional, list) List of http configurations when `protocol` is `http` or `https`.
- `health_check` - (Optional, list) List of health check configurations when `protocol` is `http` or `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol of the service. `http`, `https` or `tcp`
- `listen_port` - (Optional, int) Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
- `destination_port` - (Optional, int) Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
- `proxyprotocol` - (Optional, bool) Enable proxyprotocol.
- `http` - (Optional, list) List of http configurations when `protocol` is `http` or `https`.
- `health_check` - (Optional, list) List of health check configurations when `protocol` is `http` or `https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxyprotocol

Enable proxyprotocol.
- `http` - (Optional, list) List of http configurations when `protocol` is `http` or `https`.
- `health_check` - (Optional, list) List of health check configurations when `protocol` is `http` or `https`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

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


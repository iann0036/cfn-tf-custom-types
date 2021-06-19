# TF::OPC::LbaasServerPool

The `opc_lbaas_server_pool` resource creates and manages a Load Balancer Classic Origin Server Pool for a Load Balancer Classic instance. The Server Pool defines one or more servers (referred to as origin servers) to which the load balancer can distribute requests.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OPC::LbaasServerPool",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#vnicset" title="VnicSet">VnicSet</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OPC::LbaasServerPool
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#vnicset" title="VnicSet">VnicSet</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
</pre>

## Properties

#### Enabled

Boolean flag to enable or disable the Server Pool. Default is `true` (enabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

The parent Load Balancer the Origin Server Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Server Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

List of servers in the Server Pool. To define the server in the server pool, provide IP address or DNS name of the compute instances, and port for load balancer to direct traffic to, in the format `host:port`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicSet

Fully qualified three part name of a vNICSet to be associated with the server pool vNIC. Load Balancer uses this vNICSet to set the right ACLs to allow egress traffic from the load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Consumers

Returns the <code>Consumers</code> value.

#### Id

Returns the <code>Id</code> value.

#### OperationDetails

Returns the <code>OperationDetails</code> value.

#### State

Returns the <code>State</code> value.

#### Status

Returns the <code>Status</code> value.

#### Uri

Returns the <code>Uri</code> value.


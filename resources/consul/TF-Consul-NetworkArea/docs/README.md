# TF::Consul::NetworkArea

~> **NOTE:** This feature requires [Consul Enterprise](https://www.consul.io/docs/enterprise/index.html).

The `consul_network_area` resource manages a relationship between servers in two
different Consul datacenters.

Unlike Consul's WAN feature, network areas use just the server RPC port for
communication, and relationships can be made between independent pairs of
datacenters, so not all servers need to be fully connected. This allows for
complex topologies among Consul datacenters like hub/spoke and more general trees.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Consul::NetworkArea",
    "Properties" : {
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#peerdatacenter" title="PeerDatacenter">PeerDatacenter</a>" : <i>String</i>,
        "<a href="#retryjoin" title="RetryJoin">RetryJoin</a>" : <i>[ String, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#usetls" title="UseTls">UseTls</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Consul::NetworkArea
Properties:
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#peerdatacenter" title="PeerDatacenter">PeerDatacenter</a>: <i>String</i>
    <a href="#retryjoin" title="RetryJoin">RetryJoin</a>: <i>
      - String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#usetls" title="UseTls">UseTls</a>: <i>Boolean</i>
</pre>

## Properties

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerDatacenter

The name of the Consul datacenter that will be
joined to form the area.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryJoin

Specifies a list of Consul servers to attempt to
join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The ACL token to use. This overrides the
token that the agent provides by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTls

Specifies whether gossip over this area should be
encrypted with TLS if possible. Defaults to `false`.

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


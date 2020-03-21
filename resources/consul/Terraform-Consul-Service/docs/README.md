# Terraform::Consul::Service

A high-level resource for creating a Service in Consul in the Consul catalog. This
is appropriate for registering [external services](https://www.consul.io/docs/guides/external.html) and
can be used to create services addressable by Consul that cannot be registered
with a [local agent](https://www.consul.io/docs/agent/basics.html).

If the Consul agent is running on the node where this service is registered, it is
not recommended to use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::Service",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#external" title="External">External</a>" : <i>Boolean</i>,
        "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="meta.md">Meta</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#node" title="Node">Node</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#check" title="Check">Check</a>" : <i>[ <a href="check.md">Check</a>, ... ]</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="header.md">Header</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::Service
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#external" title="External">External</a>: <i>Boolean</i>
    <a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="meta.md">Meta</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#node" title="Node">Node</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#check" title="Check">Check</a>: <i>
      - <a href="check.md">Check</a></i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="header.md">Header</a></i>
</pre>

## Properties

#### Address

The address of the service. Defaults to the
address of the node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

A map of arbitrary KV metadata linked to the service
instance.

_Required_: No

_Type_: List of <a href="meta.md">Meta</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the header.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node

The name of the node the to register the service on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port of the service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Check

_Required_: No

_Type_: List of <a href="check.md">Check</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


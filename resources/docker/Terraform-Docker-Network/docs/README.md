# Terraform::Docker::Network

Manages a Docker Network. This can be used alongside
[docker\_container](/docs/providers/docker/r/container.html)
to create virtual networks within the docker environment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Docker::Network",
    "Properties" : {
        "<a href="#attachable" title="Attachable">Attachable</a>" : <i>Boolean</i>,
        "<a href="#checkduplicate" title="CheckDuplicate">CheckDuplicate</a>" : <i>Boolean</i>,
        "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>Boolean</i>,
        "<a href="#internal" title="Internal">Internal</a>" : <i>Boolean</i>,
        "<a href="#ipamdriver" title="IpamDriver">IpamDriver</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#ipamconfig" title="IpamConfig">IpamConfig</a>" : <i>[ <a href="ipamconfig.md">IpamConfig</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Docker::Network
Properties:
    <a href="#attachable" title="Attachable">Attachable</a>: <i>Boolean</i>
    <a href="#checkduplicate" title="CheckDuplicate">CheckDuplicate</a>: <i>Boolean</i>
    <a href="#driver" title="Driver">Driver</a>: <i>String</i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>Boolean</i>
    <a href="#internal" title="Internal">Internal</a>: <i>Boolean</i>
    <a href="#ipamdriver" title="IpamDriver">IpamDriver</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#ipamconfig" title="IpamConfig">IpamConfig</a>: <i>
      - <a href="ipamconfig.md">IpamConfig</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
</pre>

## Properties

#### Attachable

Enable manual container attachment to the network.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckDuplicate

Requests daemon to check for networks
with same name.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Driver

Name of the network driver to use. Defaults to
`bridge` driver.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

Create swarm routing-mesh network.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

Restrict external access to the network.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamDriver

Driver used by the custom IP scheme of the
network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

Enable IPv6 networking.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Docker network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Network specific options to be used by
the drivers.

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamConfig

_Required_: No

_Type_: List of <a href="ipamconfig.md">IpamConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

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

#### Scope

Returns the <code>Scope</code> value.


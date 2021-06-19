# TF::Thunder::RibRoute

`thunder_rib_route` Provides details about thunder rib route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RibRoute",
    "Properties" : {
        "<a href="#ipdestaddr" title="IpDestAddr">IpDestAddr</a>" : <i>String</i>,
        "<a href="#ipmask" title="IpMask">IpMask</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#ipnexthopipv4" title="IpNexthopIpv4">IpNexthopIpv4</a>" : <i>[ <a href="ipnexthopipv4definition.md">IpNexthopIpv4Definition</a>, ... ]</i>,
        "<a href="#ipnexthoplif" title="IpNexthopLif">IpNexthopLif</a>" : <i>[ <a href="ipnexthoplifdefinition.md">IpNexthopLifDefinition</a>, ... ]</i>,
        "<a href="#ipnexthoppartition" title="IpNexthopPartition">IpNexthopPartition</a>" : <i>[ <a href="ipnexthoppartitiondefinition.md">IpNexthopPartitionDefinition</a>, ... ]</i>,
        "<a href="#ipnexthoptunnel" title="IpNexthopTunnel">IpNexthopTunnel</a>" : <i>[ <a href="ipnexthoptunneldefinition.md">IpNexthopTunnelDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RibRoute
Properties:
    <a href="#ipdestaddr" title="IpDestAddr">IpDestAddr</a>: <i>String</i>
    <a href="#ipmask" title="IpMask">IpMask</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#ipnexthopipv4" title="IpNexthopIpv4">IpNexthopIpv4</a>: <i>
      - <a href="ipnexthopipv4definition.md">IpNexthopIpv4Definition</a></i>
    <a href="#ipnexthoplif" title="IpNexthopLif">IpNexthopLif</a>: <i>
      - <a href="ipnexthoplifdefinition.md">IpNexthopLifDefinition</a></i>
    <a href="#ipnexthoppartition" title="IpNexthopPartition">IpNexthopPartition</a>: <i>
      - <a href="ipnexthoppartitiondefinition.md">IpNexthopPartitionDefinition</a></i>
    <a href="#ipnexthoptunnel" title="IpNexthopTunnel">IpNexthopTunnel</a>: <i>
      - <a href="ipnexthoptunneldefinition.md">IpNexthopTunnelDefinition</a></i>
</pre>

## Properties

#### IpDestAddr

Destination prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMask

Destination prefix mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNexthopIpv4

_Required_: No

_Type_: List of <a href="ipnexthopipv4definition.md">IpNexthopIpv4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNexthopLif

_Required_: No

_Type_: List of <a href="ipnexthoplifdefinition.md">IpNexthopLifDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNexthopPartition

_Required_: No

_Type_: List of <a href="ipnexthoppartitiondefinition.md">IpNexthopPartitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNexthopTunnel

_Required_: No

_Type_: List of <a href="ipnexthoptunneldefinition.md">IpNexthopTunnelDefinition</a>

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


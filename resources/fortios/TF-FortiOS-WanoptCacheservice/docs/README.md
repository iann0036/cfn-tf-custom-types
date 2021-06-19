# TF::FortiOS::WanoptCacheservice

Designate cache-service for wan-optimization and webcache.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WanoptCacheservice",
    "Properties" : {
        "<a href="#acceptableconnections" title="AcceptableConnections">AcceptableConnections</a>" : <i>String</i>,
        "<a href="#collaboration" title="Collaboration">Collaboration</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#preferscenario" title="PreferScenario">PreferScenario</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#dstpeer" title="DstPeer">DstPeer</a>" : <i>[ <a href="dstpeerdefinition.md">DstPeerDefinition</a>, ... ]</i>,
        "<a href="#srcpeer" title="SrcPeer">SrcPeer</a>" : <i>[ <a href="srcpeerdefinition.md">SrcPeerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WanoptCacheservice
Properties:
    <a href="#acceptableconnections" title="AcceptableConnections">AcceptableConnections</a>: <i>String</i>
    <a href="#collaboration" title="Collaboration">Collaboration</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#preferscenario" title="PreferScenario">PreferScenario</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#dstpeer" title="DstPeer">DstPeer</a>: <i>
      - <a href="dstpeerdefinition.md">DstPeerDefinition</a></i>
    <a href="#srcpeer" title="SrcPeer">SrcPeer</a>: <i>
      - <a href="srcpeerdefinition.md">SrcPeerDefinition</a></i>
</pre>

## Properties

#### AcceptableConnections

Set strategy when accepting cache collaboration connection. Valid values: `any`, `peers`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Collaboration

Enable/disable cache-collaboration between cache-service clusters. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

Set identifier for this cache device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferScenario

Set the preferred cache behavior towards the balance between latency and hit-ratio. Valid values: `balance`, `prefer-speed`, `prefer-cache`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPeer

_Required_: No

_Type_: List of <a href="dstpeerdefinition.md">DstPeerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPeer

_Required_: No

_Type_: List of <a href="srcpeerdefinition.md">SrcPeerDefinition</a>

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


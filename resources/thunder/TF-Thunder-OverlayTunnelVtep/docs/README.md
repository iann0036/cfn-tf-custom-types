# TF::Thunder::OverlayTunnelVtep

`thunder_overlay_tunnel_vtep` Provides details about thunder overlay tunnel vtep

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::OverlayTunnelVtep",
    "Properties" : {
        "<a href="#encap" title="Encap">Encap</a>" : <i>String</i>,
        "<a href="#id2" title="Id2">Id2</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#destinationipaddresslist" title="DestinationIpAddressList">DestinationIpAddressList</a>" : <i>[ <a href="destinationipaddresslistdefinition.md">DestinationIpAddressListDefinition</a>, ... ]</i>,
        "<a href="#hostlist" title="HostList">HostList</a>" : <i>[ <a href="hostlistdefinition.md">HostListDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>,
        "<a href="#sourceipaddress" title="SourceIpAddress">SourceIpAddress</a>" : <i>[ <a href="sourceipaddressdefinition.md">SourceIpAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::OverlayTunnelVtep
Properties:
    <a href="#encap" title="Encap">Encap</a>: <i>String</i>
    <a href="#id2" title="Id2">Id2</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#destinationipaddresslist" title="DestinationIpAddressList">DestinationIpAddressList</a>: <i>
      - <a href="destinationipaddresslistdefinition.md">DestinationIpAddressListDefinition</a></i>
    <a href="#hostlist" title="HostList">HostList</a>: <i>
      - <a href="hostlistdefinition.md">HostListDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
    <a href="#sourceipaddress" title="SourceIpAddress">SourceIpAddress</a>: <i>
      - <a href="sourceipaddressdefinition.md">SourceIpAddressDefinition</a></i>
</pre>

## Properties

#### Encap

‘nvgre’: Tunnel Encapsulation Type is NVGRE; ‘vxlan’: Tunnel Encapsulation Type is VXLAN;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id2

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationIpAddressList

_Required_: No

_Type_: List of <a href="destinationipaddresslistdefinition.md">DestinationIpAddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostList

_Required_: No

_Type_: List of <a href="hostlistdefinition.md">HostListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpAddress

_Required_: No

_Type_: List of <a href="sourceipaddressdefinition.md">SourceIpAddressDefinition</a>

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

VTEP Identifier.


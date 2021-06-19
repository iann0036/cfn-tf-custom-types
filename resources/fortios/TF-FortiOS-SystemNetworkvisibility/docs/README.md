# TF::FortiOS::SystemNetworkvisibility

Configure network visibility settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemNetworkvisibility",
    "Properties" : {
        "<a href="#destinationhostnamevisibility" title="DestinationHostnameVisibility">DestinationHostnameVisibility</a>" : <i>String</i>,
        "<a href="#destinationlocation" title="DestinationLocation">DestinationLocation</a>" : <i>String</i>,
        "<a href="#destinationvisibility" title="DestinationVisibility">DestinationVisibility</a>" : <i>String</i>,
        "<a href="#hostnamelimit" title="HostnameLimit">HostnameLimit</a>" : <i>Double</i>,
        "<a href="#hostnamettl" title="HostnameTtl">HostnameTtl</a>" : <i>Double</i>,
        "<a href="#sourcelocation" title="SourceLocation">SourceLocation</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemNetworkvisibility
Properties:
    <a href="#destinationhostnamevisibility" title="DestinationHostnameVisibility">DestinationHostnameVisibility</a>: <i>String</i>
    <a href="#destinationlocation" title="DestinationLocation">DestinationLocation</a>: <i>String</i>
    <a href="#destinationvisibility" title="DestinationVisibility">DestinationVisibility</a>: <i>String</i>
    <a href="#hostnamelimit" title="HostnameLimit">HostnameLimit</a>: <i>Double</i>
    <a href="#hostnamettl" title="HostnameTtl">HostnameTtl</a>: <i>Double</i>
    <a href="#sourcelocation" title="SourceLocation">SourceLocation</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### DestinationHostnameVisibility

Enable/disable logging of destination hostname visibility. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationLocation

Enable/disable logging of destination geographical location visibility. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationVisibility

Enable/disable logging of destination visibility. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameLimit

Limit of the number of hostname table entries (0 - 50000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameTtl

TTL of hostname table entries (60 - 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceLocation

Enable/disable logging of source geographical location visibility. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.


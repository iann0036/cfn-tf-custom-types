# TF::FortiOS::FirewallInternetservice

Show Internet Service application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallInternetservice",
    "Properties" : {
        "<a href="#database" title="Database">Database</a>" : <i>String</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#extraiprangenumber" title="ExtraIpRangeNumber">ExtraIpRangeNumber</a>" : <i>Double</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#iconid" title="IconId">IconId</a>" : <i>Double</i>,
        "<a href="#ipnumber" title="IpNumber">IpNumber</a>" : <i>Double</i>,
        "<a href="#iprangenumber" title="IpRangeNumber">IpRangeNumber</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#obsolete" title="Obsolete">Obsolete</a>" : <i>Double</i>,
        "<a href="#reputation" title="Reputation">Reputation</a>" : <i>Double</i>,
        "<a href="#singularity" title="Singularity">Singularity</a>" : <i>Double</i>,
        "<a href="#sldid" title="SldId">SldId</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallInternetservice
Properties:
    <a href="#database" title="Database">Database</a>: <i>String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#extraiprangenumber" title="ExtraIpRangeNumber">ExtraIpRangeNumber</a>: <i>Double</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#iconid" title="IconId">IconId</a>: <i>Double</i>
    <a href="#ipnumber" title="IpNumber">IpNumber</a>: <i>Double</i>
    <a href="#iprangenumber" title="IpRangeNumber">IpRangeNumber</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#obsolete" title="Obsolete">Obsolete</a>: <i>Double</i>
    <a href="#reputation" title="Reputation">Reputation</a>: <i>Double</i>
    <a href="#singularity" title="Singularity">Singularity</a>: <i>Double</i>
    <a href="#sldid" title="SldId">SldId</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Database

Database name this Internet Service belongs to. Valid values: `isdb`, `irdb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

How this service may be used in a firewall policy (source, destination or both). Valid values: `src`, `dst`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraIpRangeNumber

Extra number of IP ranges.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Internet Service ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IconId

Icon ID of Internet Service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNumber

Total number of IP addresses.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRangeNumber

Total number of IP ranges.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Internet Service name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Obsolete

Indicates whether the Internet Service can be used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reputation

Reputation level of the Internet Service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Singularity

Singular level of the Internet Service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SldId

Second Level Domain.

_Required_: No

_Type_: Double

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


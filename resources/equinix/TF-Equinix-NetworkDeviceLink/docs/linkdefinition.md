# TF::Equinix::NetworkDeviceLink LinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountnumber" title="AccountNumber">AccountNumber</a>" : <i>String</i>,
    "<a href="#dstmetrocode" title="DstMetroCode">DstMetroCode</a>" : <i>String</i>,
    "<a href="#dstzonecode" title="DstZoneCode">DstZoneCode</a>" : <i>String</i>,
    "<a href="#srcmetrocode" title="SrcMetroCode">SrcMetroCode</a>" : <i>String</i>,
    "<a href="#srczonecode" title="SrcZoneCode">SrcZoneCode</a>" : <i>String</i>,
    "<a href="#throughput" title="Throughput">Throughput</a>" : <i>String</i>,
    "<a href="#throughputunit" title="ThroughputUnit">ThroughputUnit</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accountnumber" title="AccountNumber">AccountNumber</a>: <i>String</i>
<a href="#dstmetrocode" title="DstMetroCode">DstMetroCode</a>: <i>String</i>
<a href="#dstzonecode" title="DstZoneCode">DstZoneCode</a>: <i>String</i>
<a href="#srcmetrocode" title="SrcMetroCode">SrcMetroCode</a>: <i>String</i>
<a href="#srczonecode" title="SrcZoneCode">SrcZoneCode</a>: <i>String</i>
<a href="#throughput" title="Throughput">Throughput</a>: <i>String</i>
<a href="#throughputunit" title="ThroughputUnit">ThroughputUnit</a>: <i>String</i>
</pre>

## Properties

#### AccountNumber

billing account number to be used for
connection charges.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstMetroCode

connection destination metro code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstZoneCode

connection destination zone code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcMetroCode

connection source metro code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcZoneCode

connection source zone code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

connection throughput.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputUnit

connection throughput unit (Mbps or Gbps).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


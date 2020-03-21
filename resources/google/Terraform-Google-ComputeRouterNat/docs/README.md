# Terraform::Google::ComputeRouterNat

CloudFormation equivalent of google_compute_router_nat

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeRouterNat",
    "Properties" : {
        "<a href="#drainnatips" title="DrainNatIps">DrainNatIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#icmpidletimeoutsec" title="IcmpIdleTimeoutSec">IcmpIdleTimeoutSec</a>" : <i>Double</i>,
        "<a href="#minportspervm" title="MinPortsPerVm">MinPortsPerVm</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#natipallocateoption" title="NatIpAllocateOption">NatIpAllocateOption</a>" : <i>String</i>,
        "<a href="#natips" title="NatIps">NatIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>String</i>,
        "<a href="#sourcesubnetworkiprangestonat" title="SourceSubnetworkIpRangesToNat">SourceSubnetworkIpRangesToNat</a>" : <i>String</i>,
        "<a href="#tcpestablishedidletimeoutsec" title="TcpEstablishedIdleTimeoutSec">TcpEstablishedIdleTimeoutSec</a>" : <i>Double</i>,
        "<a href="#tcptransitoryidletimeoutsec" title="TcpTransitoryIdleTimeoutSec">TcpTransitoryIdleTimeoutSec</a>" : <i>Double</i>,
        "<a href="#udpidletimeoutsec" title="UdpIdleTimeoutSec">UdpIdleTimeoutSec</a>" : <i>Double</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfig.md">LogConfig</a>, ... ]</i>,
        "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>[ <a href="subnetwork.md">Subnetwork</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeRouterNat
Properties:
    <a href="#drainnatips" title="DrainNatIps">DrainNatIps</a>: <i>
      - String</i>
    <a href="#icmpidletimeoutsec" title="IcmpIdleTimeoutSec">IcmpIdleTimeoutSec</a>: <i>Double</i>
    <a href="#minportspervm" title="MinPortsPerVm">MinPortsPerVm</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#natipallocateoption" title="NatIpAllocateOption">NatIpAllocateOption</a>: <i>String</i>
    <a href="#natips" title="NatIps">NatIps</a>: <i>
      - String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>String</i>
    <a href="#sourcesubnetworkiprangestonat" title="SourceSubnetworkIpRangesToNat">SourceSubnetworkIpRangesToNat</a>: <i>String</i>
    <a href="#tcpestablishedidletimeoutsec" title="TcpEstablishedIdleTimeoutSec">TcpEstablishedIdleTimeoutSec</a>: <i>Double</i>
    <a href="#tcptransitoryidletimeoutsec" title="TcpTransitoryIdleTimeoutSec">TcpTransitoryIdleTimeoutSec</a>: <i>Double</i>
    <a href="#udpidletimeoutsec" title="UdpIdleTimeoutSec">UdpIdleTimeoutSec</a>: <i>Double</i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfig.md">LogConfig</a></i>
    <a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>
      - <a href="subnetwork.md">Subnetwork</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DrainNatIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpIdleTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPortsPerVm

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatIpAllocateOption

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSubnetworkIpRangesToNat

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpEstablishedIdleTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTransitoryIdleTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpIdleTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfig.md">LogConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

_Required_: No

_Type_: List of <a href="subnetwork.md">Subnetwork</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


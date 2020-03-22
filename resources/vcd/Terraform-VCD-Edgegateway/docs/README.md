# Terraform::VCD::Edgegateway

Provides a vCloud Director edge gateway directly connected to one or more external networks. This can be used to create
and delete edge gateways for Org VDC networks to connect.

Supported in provider *v2.4+*

~> **Note:** Only `System Administrator` can create an edge gateway.
You must use `System Adminstrator` account in `provider` configuration
and then provide `org` and `vdc` arguments for edge gateway to work.

~> **Note:** Load balancing capabilities will work only when edge gateway is `advanced`. Load
balancing settings will be **ignored** when it is not. Refer to [official vCloud Director documentation]
(https://docs.vmware.com/en/vCloud-Director/9.7/com.vmware.vcloud.tenantportal.doc/GUID-7E082E77-B459-4CE7-806D-2769F7CB5624.html) 
for more information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::Edgegateway",
    "Properties" : {
        "<a href="#advanced" title="Advanced">Advanced</a>" : <i>Boolean</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>String</i>,
        "<a href="#defaultgatewaynetwork" title="DefaultGatewayNetwork">DefaultGatewayNetwork</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#distributedrouting" title="DistributedRouting">DistributedRouting</a>" : <i>Boolean</i>,
        "<a href="#externalnetworks" title="ExternalNetworks">ExternalNetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#fipsmodeenabled" title="FipsModeEnabled">FipsModeEnabled</a>" : <i>Boolean</i>,
        "<a href="#fwdefaultruleaction" title="FwDefaultRuleAction">FwDefaultRuleAction</a>" : <i>String</i>,
        "<a href="#fwdefaultruleloggingenabled" title="FwDefaultRuleLoggingEnabled">FwDefaultRuleLoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#fwenabled" title="FwEnabled">FwEnabled</a>" : <i>Boolean</i>,
        "<a href="#haenabled" title="HaEnabled">HaEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbaccelerationenabled" title="LbAccelerationEnabled">LbAccelerationEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbenabled" title="LbEnabled">LbEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbloggingenabled" title="LbLoggingEnabled">LbLoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbloglevel" title="LbLoglevel">LbLoglevel</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#usedefaultroutefordnsrelay" title="UseDefaultRouteForDnsRelay">UseDefaultRouteForDnsRelay</a>" : <i>Boolean</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#externalnetwork" title="ExternalNetwork">ExternalNetwork</a>" : <i>[ <a href="externalnetwork.md">ExternalNetwork</a>, ... ]</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnet.md">Subnet</a>, ... ]</i>,
        "<a href="#suballocatepool" title="SuballocatePool">SuballocatePool</a>" : <i>[ <a href="suballocatepool.md">SuballocatePool</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::Edgegateway
Properties:
    <a href="#advanced" title="Advanced">Advanced</a>: <i>Boolean</i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>String</i>
    <a href="#defaultgatewaynetwork" title="DefaultGatewayNetwork">DefaultGatewayNetwork</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#distributedrouting" title="DistributedRouting">DistributedRouting</a>: <i>Boolean</i>
    <a href="#externalnetworks" title="ExternalNetworks">ExternalNetworks</a>: <i>
      - String</i>
    <a href="#fipsmodeenabled" title="FipsModeEnabled">FipsModeEnabled</a>: <i>Boolean</i>
    <a href="#fwdefaultruleaction" title="FwDefaultRuleAction">FwDefaultRuleAction</a>: <i>String</i>
    <a href="#fwdefaultruleloggingenabled" title="FwDefaultRuleLoggingEnabled">FwDefaultRuleLoggingEnabled</a>: <i>Boolean</i>
    <a href="#fwenabled" title="FwEnabled">FwEnabled</a>: <i>Boolean</i>
    <a href="#haenabled" title="HaEnabled">HaEnabled</a>: <i>Boolean</i>
    <a href="#lbaccelerationenabled" title="LbAccelerationEnabled">LbAccelerationEnabled</a>: <i>Boolean</i>
    <a href="#lbenabled" title="LbEnabled">LbEnabled</a>: <i>Boolean</i>
    <a href="#lbloggingenabled" title="LbLoggingEnabled">LbLoggingEnabled</a>: <i>Boolean</i>
    <a href="#lbloglevel" title="LbLoglevel">LbLoglevel</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#usedefaultroutefordnsrelay" title="UseDefaultRouteForDnsRelay">UseDefaultRouteForDnsRelay</a>: <i>Boolean</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#externalnetwork" title="ExternalNetwork">ExternalNetwork</a>: <i>
      - <a href="externalnetwork.md">ExternalNetwork</a></i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnet.md">Subnet</a></i>
    <a href="#suballocatepool" title="SuballocatePool">SuballocatePool</a>: <i>
      - <a href="suballocatepool.md">SuballocatePool</a></i>
</pre>

## Properties

#### Advanced

True if the gateway uses advanced networking. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

Configuration of the vShield edge VM for this gateway. One of: `compact`, `full` ("Large"), `x-large`, `full4` ("Quad Large").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGatewayNetwork

Name of the external network to be used as
default gateway. It must be included in the list of `external_networks`. Providing an empty string
or omitting the argument will create the edge gateway without a default gateway. **Please use**
the  [external network](#external-network) block structure and `use_for_default_route` to specify
a subnet which should be used as a default route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributedRouting

If advanced networking enabled, also enable distributed
routing. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworks

An array of external network names. This supports
simple external networks with one subnet only. **Please use** the [external
network](#external-network) block structure to define external networks.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FipsModeEnabled

When FIPS mode is enabled, any secure communication to or from
the NSX Edge uses cryptographic algorithms or protocols that are allowed by United States Federal
Information Processing Standards (FIPS). FIPS mode turns on the cipher suites that comply with
FIPS. Default is `false`. **Note:** to use FIPS mode it must be enabled in vCD system settings and
is only supported starting with vCD version 9.1. This field __must not__ be set for vCD 9.0.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwDefaultRuleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwDefaultRuleLoggingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEnabled

Enable high availability on this edge gateway. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAccelerationEnabled

Enable to configure the load balancer to use the faster L4
engine rather than L7 engine. The L4 TCP VIP is processed before the edge gateway firewall so no
`allow` firewall rule is required. Default is `false`. **Note:** L7 VIPs for HTTP and HTTPS are
processed after the firewall, so when Acceleration Enabled is not selected, an edge gateway firewall
rule must exist to allow access to the L7 VIP for those protocols. When Acceleration Enabled is
selected and the server pool is in non-transparent mode, an SNAT rule is added, so you must ensure
that the firewall is enabled on the edge gateway.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbEnabled

Enable load balancing. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbLoggingEnabled

Enables the edge gateway load balancer to collect traffic logs.
Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbLoglevel

Choose the severity of events to be logged. One of `emergency`,
`alert`, `critical`, `error`, `warning`, `notice`, `info`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the edge gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to which the VDC belongs. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultRouteForDnsRelay

When default route is set, it will be used for
gateways' default routing and DNS forwarding. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC that owns the edge gateway. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetwork

_Required_: No

_Type_: List of <a href="externalnetwork.md">ExternalNetwork</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnet.md">Subnet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuballocatePool

_Required_: No

_Type_: List of <a href="suballocatepool.md">SuballocatePool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultExternalNetworkIp

Returns the <code>DefaultExternalNetworkIp</code> value.

#### ExternalNetworkIps

Returns the <code>ExternalNetworkIps</code> value.

#### Id

Returns the <code>Id</code> value.


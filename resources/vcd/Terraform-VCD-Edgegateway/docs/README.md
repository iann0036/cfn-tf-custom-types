# Terraform::VCD::Edgegateway

CloudFormation equivalent of vcd_edgegateway

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGatewayNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributedRouting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FipsModeEnabled

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAccelerationEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbLoggingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbLoglevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultRouteForDnsRelay

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

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


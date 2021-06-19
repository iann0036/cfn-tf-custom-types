# TF::VCD::EdgegatewaySettings

Provides a resource that can update vCloud Director edge gateway global settings either as System Administrator or as
Organization user.

The main use case of this resource is to allow both providers and tenants to change edge gateways global settings (such as
enabling load balancing or firewall) when the edge gateway was created outside of Terraform.
A second use case is when the provider creates the edge gateway using Terraform, and then delegates the tenant to change
some settings for further operations.

~> **Warning:** The edge gateway settings info is tied to an edge gateway. Thus, there could be only one instance per 
edge gateway. Using a different definition for the same edge gateway ID will result in a previous instance to be overwritten.

!> **Warning:** Using a `vcd_edgegateway` and a `vcd_edgegateway_settings` for the same entity does not work correctly,
as the main purpose of this resource is to handle general settings when the edge gateway was created outside of Terraform.
If users can crea...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::EdgegatewaySettings",
    "Properties" : {
        "<a href="#edgegatewayid" title="EdgeGatewayId">EdgeGatewayId</a>" : <i>String</i>,
        "<a href="#edgegatewayname" title="EdgeGatewayName">EdgeGatewayName</a>" : <i>String</i>,
        "<a href="#fwdefaultruleaction" title="FwDefaultRuleAction">FwDefaultRuleAction</a>" : <i>String</i>,
        "<a href="#fwdefaultruleloggingenabled" title="FwDefaultRuleLoggingEnabled">FwDefaultRuleLoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#fwenabled" title="FwEnabled">FwEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbaccelerationenabled" title="LbAccelerationEnabled">LbAccelerationEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbenabled" title="LbEnabled">LbEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbloggingenabled" title="LbLoggingEnabled">LbLoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#lbloglevel" title="LbLoglevel">LbLoglevel</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::EdgegatewaySettings
Properties:
    <a href="#edgegatewayid" title="EdgeGatewayId">EdgeGatewayId</a>: <i>String</i>
    <a href="#edgegatewayname" title="EdgeGatewayName">EdgeGatewayName</a>: <i>String</i>
    <a href="#fwdefaultruleaction" title="FwDefaultRuleAction">FwDefaultRuleAction</a>: <i>String</i>
    <a href="#fwdefaultruleloggingenabled" title="FwDefaultRuleLoggingEnabled">FwDefaultRuleLoggingEnabled</a>: <i>Boolean</i>
    <a href="#fwenabled" title="FwEnabled">FwEnabled</a>: <i>Boolean</i>
    <a href="#lbaccelerationenabled" title="LbAccelerationEnabled">LbAccelerationEnabled</a>: <i>Boolean</i>
    <a href="#lbenabled" title="LbEnabled">LbEnabled</a>: <i>Boolean</i>
    <a href="#lbloggingenabled" title="LbLoggingEnabled">LbLoggingEnabled</a>: <i>Boolean</i>
    <a href="#lbloglevel" title="LbLoglevel">LbLoglevel</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### EdgeGatewayId

The edge gateway ID. (Required if `edge_gateway_name` is not set).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGatewayName

A unique name for the edge gateway. (Required if `edge_gateway_id` is not set).

_Required_: No

_Type_: String

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

#### LbAccelerationEnabled

Enable to configure the load balancer.

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
Default is `false`. Note: **only System administrators can change this property**. It is ignored by API for Org users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbLoglevel

Choose the severity of events to be logged. One of `emergency`,
`alert`, `critical`, `error`, `warning`, `notice`, `info`, `debug`. Note: **only System administrators can change this property**. It is ignored by API for Org users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to which the VDC belongs. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC that owns the edge gateway. Optional if defined at provider level.

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


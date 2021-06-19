# TF::AVI::Vrfcontext

The VrfContext resource allows the creation and management of Avi VrfContext

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Vrfcontext",
    "Properties" : {
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lldpenable" title="LldpEnable">LldpEnable</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#systemdefault" title="SystemDefault">SystemDefault</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#attrs" title="Attrs">Attrs</a>" : <i>[ <a href="attrsdefinition.md">AttrsDefinition</a>, ... ]</i>,
        "<a href="#bfdprofile" title="BfdProfile">BfdProfile</a>" : <i>[ <a href="bfdprofiledefinition.md">BfdProfileDefinition</a>, ... ]</i>,
        "<a href="#bgpprofile" title="BgpProfile">BgpProfile</a>" : <i>[ <a href="bgpprofiledefinition.md">BgpProfileDefinition</a>, ... ]</i>,
        "<a href="#debugvrfcontext" title="Debugvrfcontext">Debugvrfcontext</a>" : <i>[ <a href="debugvrfcontextdefinition.md">DebugvrfcontextDefinition</a>, ... ]</i>,
        "<a href="#gatewaymon" title="GatewayMon">GatewayMon</a>" : <i>[ <a href="gatewaymondefinition.md">GatewayMonDefinition</a>, ... ]</i>,
        "<a href="#internalgatewaymonitor" title="InternalGatewayMonitor">InternalGatewayMonitor</a>" : <i>[ <a href="internalgatewaymonitordefinition.md">InternalGatewayMonitorDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#staticroutes" title="StaticRoutes">StaticRoutes</a>" : <i>[ <a href="staticroutesdefinition.md">StaticRoutesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Vrfcontext
Properties:
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lldpenable" title="LldpEnable">LldpEnable</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#systemdefault" title="SystemDefault">SystemDefault</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#attrs" title="Attrs">Attrs</a>: <i>
      - <a href="attrsdefinition.md">AttrsDefinition</a></i>
    <a href="#bfdprofile" title="BfdProfile">BfdProfile</a>: <i>
      - <a href="bfdprofiledefinition.md">BfdProfileDefinition</a></i>
    <a href="#bgpprofile" title="BgpProfile">BgpProfile</a>: <i>
      - <a href="bgpprofiledefinition.md">BgpProfileDefinition</a></i>
    <a href="#debugvrfcontext" title="Debugvrfcontext">Debugvrfcontext</a>: <i>
      - <a href="debugvrfcontextdefinition.md">DebugvrfcontextDefinition</a></i>
    <a href="#gatewaymon" title="GatewayMon">GatewayMon</a>: <i>
      - <a href="gatewaymondefinition.md">GatewayMonDefinition</a></i>
    <a href="#internalgatewaymonitor" title="InternalGatewayMonitor">InternalGatewayMonitor</a>: <i>
      - <a href="internalgatewaymonitordefinition.md">InternalGatewayMonitorDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#staticroutes" title="StaticRoutes">StaticRoutes</a>: <i>
      - <a href="staticroutesdefinition.md">StaticRoutesDefinition</a></i>
</pre>

## Properties

#### CloudRef

It is a reference to an object of type cloud.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpEnable

Enable lldp. Field introduced in 18.2.10, 20.1.1. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDefault

Boolean flag to set system_default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attrs

_Required_: No

_Type_: List of <a href="attrsdefinition.md">AttrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

_Required_: No

_Type_: List of <a href="bfdprofiledefinition.md">BfdProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpProfile

_Required_: No

_Type_: List of <a href="bgpprofiledefinition.md">BgpProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Debugvrfcontext

_Required_: No

_Type_: List of <a href="debugvrfcontextdefinition.md">DebugvrfcontextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayMon

_Required_: No

_Type_: List of <a href="gatewaymondefinition.md">GatewayMonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalGatewayMonitor

_Required_: No

_Type_: List of <a href="internalgatewaymonitordefinition.md">InternalGatewayMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutes

_Required_: No

_Type_: List of <a href="staticroutesdefinition.md">StaticRoutesDefinition</a>

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


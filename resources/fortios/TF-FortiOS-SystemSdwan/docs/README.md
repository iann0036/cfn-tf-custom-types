# TF::FortiOS::SystemSdwan

Configure redundant internet connections using SD-WAN (formerly virtual WAN link). Applies to FortiOS Version `>= 6.4.2`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSdwan",
    "Properties" : {
        "<a href="#duplicationmaxnum" title="DuplicationMaxNum">DuplicationMaxNum</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#faildetect" title="FailDetect">FailDetect</a>" : <i>String</i>,
        "<a href="#loadbalancemode" title="LoadBalanceMode">LoadBalanceMode</a>" : <i>String</i>,
        "<a href="#neighborholdboottime" title="NeighborHoldBootTime">NeighborHoldBootTime</a>" : <i>Double</i>,
        "<a href="#neighborholddown" title="NeighborHoldDown">NeighborHoldDown</a>" : <i>String</i>,
        "<a href="#neighborholddowntime" title="NeighborHoldDownTime">NeighborHoldDownTime</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#duplication" title="Duplication">Duplication</a>" : <i>[ <a href="duplicationdefinition.md">DuplicationDefinition</a>, ... ]</i>,
        "<a href="#failalertinterfaces" title="FailAlertInterfaces">FailAlertInterfaces</a>" : <i>[ <a href="failalertinterfacesdefinition.md">FailAlertInterfacesDefinition</a>, ... ]</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ <a href="membersdefinition.md">MembersDefinition</a>, ... ]</i>,
        "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>[ <a href="zonedefinition.md">ZoneDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSdwan
Properties:
    <a href="#duplicationmaxnum" title="DuplicationMaxNum">DuplicationMaxNum</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#faildetect" title="FailDetect">FailDetect</a>: <i>String</i>
    <a href="#loadbalancemode" title="LoadBalanceMode">LoadBalanceMode</a>: <i>String</i>
    <a href="#neighborholdboottime" title="NeighborHoldBootTime">NeighborHoldBootTime</a>: <i>Double</i>
    <a href="#neighborholddown" title="NeighborHoldDown">NeighborHoldDown</a>: <i>String</i>
    <a href="#neighborholddowntime" title="NeighborHoldDownTime">NeighborHoldDownTime</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#duplication" title="Duplication">Duplication</a>: <i>
      - <a href="duplicationdefinition.md">DuplicationDefinition</a></i>
    <a href="#failalertinterfaces" title="FailAlertInterfaces">FailAlertInterfaces</a>: <i>
      - <a href="failalertinterfacesdefinition.md">FailAlertInterfacesDefinition</a></i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
    <a href="#members" title="Members">Members</a>: <i>
      - <a href="membersdefinition.md">MembersDefinition</a></i>
    <a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
    <a href="#zone" title="Zone">Zone</a>: <i>
      - <a href="zonedefinition.md">ZoneDefinition</a></i>
</pre>

## Properties

#### DuplicationMaxNum

Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailDetect

Enable/disable SD-WAN Internet connection status checking (failure detection). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalanceMode

Algorithm or mode to use for load balancing Internet traffic to SD-WAN members. Valid values: `source-ip-based`, `weight-based`, `usage-based`, `source-dest-ip-based`, `measured-volume-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborHoldBootTime

Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. (0 - 10000000, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborHoldDown

Enable/disable hold switching from the secondary neighbor to the primary neighbor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborHoldDownTime

Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. (0 - 10000000, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable SD-WAN. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duplication

_Required_: No

_Type_: List of <a href="duplicationdefinition.md">DuplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailAlertInterfaces

_Required_: No

_Type_: List of <a href="failalertinterfacesdefinition.md">FailAlertInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of <a href="membersdefinition.md">MembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: List of <a href="zonedefinition.md">ZoneDefinition</a>

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


# TF::FortiOS::WirelesscontrollerSnmp

Configure SNMP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerSnmp",
    "Properties" : {
        "<a href="#contactinfo" title="ContactInfo">ContactInfo</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#engineid" title="EngineId">EngineId</a>" : <i>String</i>,
        "<a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>" : <i>Double</i>,
        "<a href="#traphighmemthreshold" title="TrapHighMemThreshold">TrapHighMemThreshold</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#community" title="Community">Community</a>" : <i>[ <a href="communitydefinition.md">CommunityDefinition</a>, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>[ <a href="userdefinition.md">UserDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerSnmp
Properties:
    <a href="#contactinfo" title="ContactInfo">ContactInfo</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#engineid" title="EngineId">EngineId</a>: <i>String</i>
    <a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>: <i>Double</i>
    <a href="#traphighmemthreshold" title="TrapHighMemThreshold">TrapHighMemThreshold</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#community" title="Community">Community</a>: <i>
      - <a href="communitydefinition.md">CommunityDefinition</a></i>
    <a href="#user" title="User">User</a>: <i>
      - <a href="userdefinition.md">UserDefinition</a></i>
</pre>

## Properties

#### ContactInfo

Contact Information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineId

AC SNMP engineId string (maximum 24 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapHighCpuThreshold

CPU usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapHighMemThreshold

Memory usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Community

_Required_: No

_Type_: List of <a href="communitydefinition.md">CommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="userdefinition.md">UserDefinition</a>

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


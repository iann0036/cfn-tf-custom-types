# TF::FortiOS::EndpointcontrolProfile

Configure FortiClient endpoint control profiles. Applies to FortiOS Version `<= 6.2.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::EndpointcontrolProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#profilename" title="ProfileName">ProfileName</a>" : <i>String</i>,
        "<a href="#replacemsgoverridegroup" title="ReplacemsgOverrideGroup">ReplacemsgOverrideGroup</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#devicegroups" title="DeviceGroups">DeviceGroups</a>" : <i>[ <a href="devicegroupsdefinition.md">DeviceGroupsDefinition</a>, ... ]</i>,
        "<a href="#forticlientandroidsettings" title="ForticlientAndroidSettings">ForticlientAndroidSettings</a>" : <i>[ <a href="forticlientandroidsettingsdefinition.md">ForticlientAndroidSettingsDefinition</a>, ... ]</i>,
        "<a href="#forticlientiossettings" title="ForticlientIosSettings">ForticlientIosSettings</a>" : <i>[ <a href="forticlientiossettingsdefinition.md">ForticlientIosSettingsDefinition</a>, ... ]</i>,
        "<a href="#forticlientwinmacsettings" title="ForticlientWinmacSettings">ForticlientWinmacSettings</a>" : <i>[ <a href="forticlientwinmacsettingsdefinition.md">ForticlientWinmacSettingsDefinition</a>, ... ]</i>,
        "<a href="#onnetaddr" title="OnNetAddr">OnNetAddr</a>" : <i>[ <a href="onnetaddrdefinition.md">OnNetAddrDefinition</a>, ... ]</i>,
        "<a href="#srcaddr" title="SrcAddr">SrcAddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcAddrDefinition</a>, ... ]</i>,
        "<a href="#usergroups" title="UserGroups">UserGroups</a>" : <i>[ <a href="usergroupsdefinition.md">UserGroupsDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::EndpointcontrolProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#profilename" title="ProfileName">ProfileName</a>: <i>String</i>
    <a href="#replacemsgoverridegroup" title="ReplacemsgOverrideGroup">ReplacemsgOverrideGroup</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#devicegroups" title="DeviceGroups">DeviceGroups</a>: <i>
      - <a href="devicegroupsdefinition.md">DeviceGroupsDefinition</a></i>
    <a href="#forticlientandroidsettings" title="ForticlientAndroidSettings">ForticlientAndroidSettings</a>: <i>
      - <a href="forticlientandroidsettingsdefinition.md">ForticlientAndroidSettingsDefinition</a></i>
    <a href="#forticlientiossettings" title="ForticlientIosSettings">ForticlientIosSettings</a>: <i>
      - <a href="forticlientiossettingsdefinition.md">ForticlientIosSettingsDefinition</a></i>
    <a href="#forticlientwinmacsettings" title="ForticlientWinmacSettings">ForticlientWinmacSettings</a>: <i>
      - <a href="forticlientwinmacsettingsdefinition.md">ForticlientWinmacSettingsDefinition</a></i>
    <a href="#onnetaddr" title="OnNetAddr">OnNetAddr</a>: <i>
      - <a href="onnetaddrdefinition.md">OnNetAddrDefinition</a></i>
    <a href="#srcaddr" title="SrcAddr">SrcAddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcAddrDefinition</a></i>
    <a href="#usergroups" title="UserGroups">UserGroups</a>: <i>
      - <a href="usergroupsdefinition.md">UserGroupsDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileName

Profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgOverrideGroup

Select an endpoint control replacement message override group from available options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroups

_Required_: No

_Type_: List of <a href="devicegroupsdefinition.md">DeviceGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAndroidSettings

_Required_: No

_Type_: List of <a href="forticlientandroidsettingsdefinition.md">ForticlientAndroidSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientIosSettings

_Required_: No

_Type_: List of <a href="forticlientiossettingsdefinition.md">ForticlientIosSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWinmacSettings

_Required_: No

_Type_: List of <a href="forticlientwinmacsettingsdefinition.md">ForticlientWinmacSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnNetAddr

_Required_: No

_Type_: List of <a href="onnetaddrdefinition.md">OnNetAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcAddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroups

_Required_: No

_Type_: List of <a href="usergroupsdefinition.md">UserGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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


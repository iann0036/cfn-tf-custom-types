# TF::Intersight::CapabilitySwitchCapability

Type to represent additional switch specific capabilities.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::CapabilitySwitchCapability",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#defaultfcoevlan" title="DefaultFcoeVlan">DefaultFcoeVlan</a>" : <i>Double</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#dynamicvifssupported" title="DynamicVifsSupported">DynamicVifsSupported</a>" : <i>Boolean</i>,
        "<a href="#fanmodulessupported" title="FanModulesSupported">FanModulesSupported</a>" : <i>Boolean</i>,
        "<a href="#fcendhostmodereservedvsans" title="FcEndHostModeReservedVsans">FcEndHostModeReservedVsans</a>" : <i>[ <a href="fcendhostmodereservedvsansdefinition.md">FcEndHostModeReservedVsansDefinition</a>, ... ]</i>,
        "<a href="#fcuplinkportsautonegotiationsupported" title="FcUplinkPortsAutoNegotiationSupported">FcUplinkPortsAutoNegotiationSupported</a>" : <i>Boolean</i>,
        "<a href="#locatorbeaconsupported" title="LocatorBeaconSupported">LocatorBeaconSupported</a>" : <i>Boolean</i>,
        "<a href="#maxports" title="MaxPorts">MaxPorts</a>" : <i>Double</i>,
        "<a href="#maxslots" title="MaxSlots">MaxSlots</a>" : <i>Double</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networklimits" title="NetworkLimits">NetworkLimits</a>" : <i>[ <a href="networklimitsdefinition.md">NetworkLimitsDefinition</a>, ... ]</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#pid" title="Pid">Pid</a>" : <i>String</i>,
        "<a href="#portssupporting100gspeed" title="PortsSupporting100gSpeed">PortsSupporting100gSpeed</a>" : <i>[ <a href="portssupporting100gspeeddefinition.md">PortsSupporting100gSpeedDefinition</a>, ... ]</i>,
        "<a href="#portssupporting10gspeed" title="PortsSupporting10gSpeed">PortsSupporting10gSpeed</a>" : <i>[ <a href="portssupporting10gspeeddefinition.md">PortsSupporting10gSpeedDefinition</a>, ... ]</i>,
        "<a href="#portssupporting1gspeed" title="PortsSupporting1gSpeed">PortsSupporting1gSpeed</a>" : <i>[ <a href="portssupporting1gspeeddefinition.md">PortsSupporting1gSpeedDefinition</a>, ... ]</i>,
        "<a href="#portssupporting25gspeed" title="PortsSupporting25gSpeed">PortsSupporting25gSpeed</a>" : <i>[ <a href="portssupporting25gspeeddefinition.md">PortsSupporting25gSpeedDefinition</a>, ... ]</i>,
        "<a href="#portssupporting40gspeed" title="PortsSupporting40gSpeed">PortsSupporting40gSpeed</a>" : <i>[ <a href="portssupporting40gspeeddefinition.md">PortsSupporting40gSpeedDefinition</a>, ... ]</i>,
        "<a href="#portssupportingbreakout" title="PortsSupportingBreakout">PortsSupportingBreakout</a>" : <i>[ <a href="portssupportingbreakoutdefinition.md">PortsSupportingBreakoutDefinition</a>, ... ]</i>,
        "<a href="#portssupportingfcoe" title="PortsSupportingFcoe">PortsSupportingFcoe</a>" : <i>[ <a href="portssupportingfcoedefinition.md">PortsSupportingFcoeDefinition</a>, ... ]</i>,
        "<a href="#portssupportingserverrole" title="PortsSupportingServerRole">PortsSupportingServerRole</a>" : <i>[ <a href="portssupportingserverroledefinition.md">PortsSupportingServerRoleDefinition</a>, ... ]</i>,
        "<a href="#reservedvsans" title="ReservedVsans">ReservedVsans</a>" : <i>[ <a href="reservedvsansdefinition.md">ReservedVsansDefinition</a>, ... ]</i>,
        "<a href="#serenonetflowsupported" title="SerenoNetflowSupported">SerenoNetflowSupported</a>" : <i>Boolean</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#storagelimits" title="StorageLimits">StorageLimits</a>" : <i>[ <a href="storagelimitsdefinition.md">StorageLimitsDefinition</a>, ... ]</i>,
        "<a href="#switchingmodecapabilities" title="SwitchingModeCapabilities">SwitchingModeCapabilities</a>" : <i>[ <a href="switchingmodecapabilitiesdefinition.md">SwitchingModeCapabilitiesDefinition</a>, ... ]</i>,
        "<a href="#systemlimits" title="SystemLimits">SystemLimits</a>" : <i>[ <a href="systemlimitsdefinition.md">SystemLimitsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#unifiedports" title="UnifiedPorts">UnifiedPorts</a>" : <i>[ <a href="unifiedportsdefinition.md">UnifiedPortsDefinition</a>, ... ]</i>,
        "<a href="#unifiedrule" title="UnifiedRule">UnifiedRule</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#vid" title="Vid">Vid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::CapabilitySwitchCapability
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#defaultfcoevlan" title="DefaultFcoeVlan">DefaultFcoeVlan</a>: <i>Double</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#dynamicvifssupported" title="DynamicVifsSupported">DynamicVifsSupported</a>: <i>Boolean</i>
    <a href="#fanmodulessupported" title="FanModulesSupported">FanModulesSupported</a>: <i>Boolean</i>
    <a href="#fcendhostmodereservedvsans" title="FcEndHostModeReservedVsans">FcEndHostModeReservedVsans</a>: <i>
      - <a href="fcendhostmodereservedvsansdefinition.md">FcEndHostModeReservedVsansDefinition</a></i>
    <a href="#fcuplinkportsautonegotiationsupported" title="FcUplinkPortsAutoNegotiationSupported">FcUplinkPortsAutoNegotiationSupported</a>: <i>Boolean</i>
    <a href="#locatorbeaconsupported" title="LocatorBeaconSupported">LocatorBeaconSupported</a>: <i>Boolean</i>
    <a href="#maxports" title="MaxPorts">MaxPorts</a>: <i>Double</i>
    <a href="#maxslots" title="MaxSlots">MaxSlots</a>: <i>Double</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networklimits" title="NetworkLimits">NetworkLimits</a>: <i>
      - <a href="networklimitsdefinition.md">NetworkLimitsDefinition</a></i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#pid" title="Pid">Pid</a>: <i>String</i>
    <a href="#portssupporting100gspeed" title="PortsSupporting100gSpeed">PortsSupporting100gSpeed</a>: <i>
      - <a href="portssupporting100gspeeddefinition.md">PortsSupporting100gSpeedDefinition</a></i>
    <a href="#portssupporting10gspeed" title="PortsSupporting10gSpeed">PortsSupporting10gSpeed</a>: <i>
      - <a href="portssupporting10gspeeddefinition.md">PortsSupporting10gSpeedDefinition</a></i>
    <a href="#portssupporting1gspeed" title="PortsSupporting1gSpeed">PortsSupporting1gSpeed</a>: <i>
      - <a href="portssupporting1gspeeddefinition.md">PortsSupporting1gSpeedDefinition</a></i>
    <a href="#portssupporting25gspeed" title="PortsSupporting25gSpeed">PortsSupporting25gSpeed</a>: <i>
      - <a href="portssupporting25gspeeddefinition.md">PortsSupporting25gSpeedDefinition</a></i>
    <a href="#portssupporting40gspeed" title="PortsSupporting40gSpeed">PortsSupporting40gSpeed</a>: <i>
      - <a href="portssupporting40gspeeddefinition.md">PortsSupporting40gSpeedDefinition</a></i>
    <a href="#portssupportingbreakout" title="PortsSupportingBreakout">PortsSupportingBreakout</a>: <i>
      - <a href="portssupportingbreakoutdefinition.md">PortsSupportingBreakoutDefinition</a></i>
    <a href="#portssupportingfcoe" title="PortsSupportingFcoe">PortsSupportingFcoe</a>: <i>
      - <a href="portssupportingfcoedefinition.md">PortsSupportingFcoeDefinition</a></i>
    <a href="#portssupportingserverrole" title="PortsSupportingServerRole">PortsSupportingServerRole</a>: <i>
      - <a href="portssupportingserverroledefinition.md">PortsSupportingServerRoleDefinition</a></i>
    <a href="#reservedvsans" title="ReservedVsans">ReservedVsans</a>: <i>
      - <a href="reservedvsansdefinition.md">ReservedVsansDefinition</a></i>
    <a href="#serenonetflowsupported" title="SerenoNetflowSupported">SerenoNetflowSupported</a>: <i>Boolean</i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#storagelimits" title="StorageLimits">StorageLimits</a>: <i>
      - <a href="storagelimitsdefinition.md">StorageLimitsDefinition</a></i>
    <a href="#switchingmodecapabilities" title="SwitchingModeCapabilities">SwitchingModeCapabilities</a>: <i>
      - <a href="switchingmodecapabilitiesdefinition.md">SwitchingModeCapabilitiesDefinition</a></i>
    <a href="#systemlimits" title="SystemLimits">SystemLimits</a>: <i>
      - <a href="systemlimitsdefinition.md">SystemLimitsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#unifiedports" title="UnifiedPorts">UnifiedPorts</a>: <i>
      - <a href="unifiedportsdefinition.md">UnifiedPortsDefinition</a></i>
    <a href="#unifiedrule" title="UnifiedRule">UnifiedRule</a>: <i>String</i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#vid" title="Vid">Vid</a>: <i>String</i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultFcoeVlan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicVifsSupported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FanModulesSupported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcEndHostModeReservedVsans

_Required_: No

_Type_: List of <a href="fcendhostmodereservedvsansdefinition.md">FcEndHostModeReservedVsansDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcUplinkPortsAutoNegotiationSupported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocatorBeaconSupported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPorts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSlots

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkLimits

_Required_: No

_Type_: List of <a href="networklimitsdefinition.md">NetworkLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupporting100gSpeed

_Required_: No

_Type_: List of <a href="portssupporting100gspeeddefinition.md">PortsSupporting100gSpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupporting10gSpeed

_Required_: No

_Type_: List of <a href="portssupporting10gspeeddefinition.md">PortsSupporting10gSpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupporting1gSpeed

_Required_: No

_Type_: List of <a href="portssupporting1gspeeddefinition.md">PortsSupporting1gSpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupporting25gSpeed

_Required_: No

_Type_: List of <a href="portssupporting25gspeeddefinition.md">PortsSupporting25gSpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupporting40gSpeed

_Required_: No

_Type_: List of <a href="portssupporting40gspeeddefinition.md">PortsSupporting40gSpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupportingBreakout

_Required_: No

_Type_: List of <a href="portssupportingbreakoutdefinition.md">PortsSupportingBreakoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupportingFcoe

_Required_: No

_Type_: List of <a href="portssupportingfcoedefinition.md">PortsSupportingFcoeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsSupportingServerRole

_Required_: No

_Type_: List of <a href="portssupportingserverroledefinition.md">PortsSupportingServerRoleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedVsans

_Required_: No

_Type_: List of <a href="reservedvsansdefinition.md">ReservedVsansDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerenoNetflowSupported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageLimits

_Required_: No

_Type_: List of <a href="storagelimitsdefinition.md">StorageLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingModeCapabilities

_Required_: No

_Type_: List of <a href="switchingmodecapabilitiesdefinition.md">SwitchingModeCapabilitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemLimits

_Required_: No

_Type_: List of <a href="systemlimitsdefinition.md">SystemLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnifiedPorts

_Required_: No

_Type_: List of <a href="unifiedportsdefinition.md">UnifiedPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnifiedRule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vid

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


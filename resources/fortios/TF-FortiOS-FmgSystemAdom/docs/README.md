# TF::FortiOS::FmgSystemAdom

This resource supports Create/Read/Update/Delete system adom for FortiManager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgSystemAdom",
    "Properties" : {
        "<a href="#actionwhenconflictsoccurduringpolicycheck" title="ActionWhenConflictsOccurDuringPolicyCheck">ActionWhenConflictsOccurDuringPolicyCheck</a>" : <i>String</i>,
        "<a href="#autopushpolicypackageswhendevicebackonline" title="AutoPushPolicyPackagesWhenDeviceBackOnline">AutoPushPolicyPackagesWhenDeviceBackOnline</a>" : <i>String</i>,
        "<a href="#centralmanagementfortiap" title="CentralManagementFortiap">CentralManagementFortiap</a>" : <i>Boolean</i>,
        "<a href="#centralmanagementsdwan" title="CentralManagementSdwan">CentralManagementSdwan</a>" : <i>Boolean</i>,
        "<a href="#centralmanagementvpn" title="CentralManagementVpn">CentralManagementVpn</a>" : <i>Boolean</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#performpolicycheckbeforeeveryinstall" title="PerformPolicyCheckBeforeEveryInstall">PerformPolicyCheckBeforeEveryInstall</a>" : <i>Boolean</i>,
        "<a href="#status" title="Status">Status</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgSystemAdom
Properties:
    <a href="#actionwhenconflictsoccurduringpolicycheck" title="ActionWhenConflictsOccurDuringPolicyCheck">ActionWhenConflictsOccurDuringPolicyCheck</a>: <i>String</i>
    <a href="#autopushpolicypackageswhendevicebackonline" title="AutoPushPolicyPackagesWhenDeviceBackOnline">AutoPushPolicyPackagesWhenDeviceBackOnline</a>: <i>String</i>
    <a href="#centralmanagementfortiap" title="CentralManagementFortiap">CentralManagementFortiap</a>: <i>Boolean</i>
    <a href="#centralmanagementsdwan" title="CentralManagementSdwan">CentralManagementSdwan</a>: <i>Boolean</i>
    <a href="#centralmanagementvpn" title="CentralManagementVpn">CentralManagementVpn</a>: <i>Boolean</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#performpolicycheckbeforeeveryinstall" title="PerformPolicyCheckBeforeEveryInstall">PerformPolicyCheckBeforeEveryInstall</a>: <i>Boolean</i>
    <a href="#status" title="Status">Status</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ActionWhenConflictsOccurDuringPolicyCheck

True or False.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPushPolicyPackagesWhenDeviceBackOnline

True or False.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralManagementFortiap

True or False.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralManagementSdwan

True or False.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralManagementVpn

True or False.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Adom mode: Normal or Backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Administrative Domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerformPolicyCheckBeforeEveryInstall

True or False.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Adom status. 0 means off and 1 means on.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Domain type, Enum: ["FortiGate", "FortiCarrier], default is "FortiCarrier".

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


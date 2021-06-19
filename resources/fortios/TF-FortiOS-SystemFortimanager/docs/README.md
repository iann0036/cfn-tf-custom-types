# TF::FortiOS::SystemFortimanager

Configure FortiManager.

Due to the limitations of the current system, the feature is temporarily unavailable. Please use the following resource configuration as an alternative.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemFortimanager",
    "Properties" : {
        "<a href="#centralmanagement" title="CentralManagement">CentralManagement</a>" : <i>String</i>,
        "<a href="#centralmgmtautobackup" title="CentralMgmtAutoBackup">CentralMgmtAutoBackup</a>" : <i>String</i>,
        "<a href="#centralmgmtscheduleconfigrestore" title="CentralMgmtScheduleConfigRestore">CentralMgmtScheduleConfigRestore</a>" : <i>String</i>,
        "<a href="#centralmgmtschedulescriptrestore" title="CentralMgmtScheduleScriptRestore">CentralMgmtScheduleScriptRestore</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#ipsec" title="Ipsec">Ipsec</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemFortimanager
Properties:
    <a href="#centralmanagement" title="CentralManagement">CentralManagement</a>: <i>String</i>
    <a href="#centralmgmtautobackup" title="CentralMgmtAutoBackup">CentralMgmtAutoBackup</a>: <i>String</i>
    <a href="#centralmgmtscheduleconfigrestore" title="CentralMgmtScheduleConfigRestore">CentralMgmtScheduleConfigRestore</a>: <i>String</i>
    <a href="#centralmgmtschedulescriptrestore" title="CentralMgmtScheduleScriptRestore">CentralMgmtScheduleScriptRestore</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#ipsec" title="Ipsec">Ipsec</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### CentralManagement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralMgmtAutoBackup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralMgmtScheduleConfigRestore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CentralMgmtScheduleScriptRestore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipsec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

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


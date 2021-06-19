# TF::AVI::Actiongroupconfig

The ActionGroupConfig resource allows the creation and management of Avi ActionGroupConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Actiongroupconfig",
    "Properties" : {
        "<a href="#actionscriptconfigref" title="ActionScriptConfigRef">ActionScriptConfigRef</a>" : <i>String</i>,
        "<a href="#autoscaletriggernotification" title="AutoscaleTriggerNotification">AutoscaleTriggerNotification</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#emailconfigref" title="EmailConfigRef">EmailConfigRef</a>" : <i>String</i>,
        "<a href="#externalonly" title="ExternalOnly">ExternalOnly</a>" : <i>Boolean</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#snmptrapprofileref" title="SnmpTrapProfileRef">SnmpTrapProfileRef</a>" : <i>String</i>,
        "<a href="#syslogconfigref" title="SyslogConfigRef">SyslogConfigRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Actiongroupconfig
Properties:
    <a href="#actionscriptconfigref" title="ActionScriptConfigRef">ActionScriptConfigRef</a>: <i>String</i>
    <a href="#autoscaletriggernotification" title="AutoscaleTriggerNotification">AutoscaleTriggerNotification</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#emailconfigref" title="EmailConfigRef">EmailConfigRef</a>: <i>String</i>
    <a href="#externalonly" title="ExternalOnly">ExternalOnly</a>: <i>Boolean</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#snmptrapprofileref" title="SnmpTrapProfileRef">SnmpTrapProfileRef</a>: <i>String</i>
    <a href="#syslogconfigref" title="SyslogConfigRef">SyslogConfigRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### ActionScriptConfigRef

Reference of the action script configuration to be used. It is a reference to an object of type alertscriptconfig.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleTriggerNotification

Trigger notification to autoscale manager. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailConfigRef

Select the email notification configuration to use when sending alerts via email. It is a reference to an object of type alertemailconfig.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalOnly

Generate alert only to external destinations. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

When an alert is generated, mark its priority via the alert level. Enum options - ALERT_LOW, ALERT_MEDIUM, ALERT_HIGH.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpTrapProfileRef

Select the snmp trap notification to use when sending alerts via snmp trap. It is a reference to an object of type snmptrapprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogConfigRef

Select the syslog notification configuration to use when sending alerts via syslog. It is a reference to an object of type alertsyslogconfig.

_Required_: No

_Type_: String

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


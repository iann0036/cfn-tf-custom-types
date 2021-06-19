# TF::AVI::Alertconfig

The AlertConfig resource allows the creation and management of Avi AlertConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Alertconfig",
    "Properties" : {
        "<a href="#actiongroupref" title="ActionGroupRef">ActionGroupRef</a>" : <i>String</i>,
        "<a href="#autoscalealert" title="AutoscaleAlert">AutoscaleAlert</a>" : <i>Boolean</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#expirytime" title="ExpiryTime">ExpiryTime</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objuuid" title="ObjUuid">ObjUuid</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#recommendation" title="Recommendation">Recommendation</a>" : <i>String</i>,
        "<a href="#rollingwindow" title="RollingWindow">RollingWindow</a>" : <i>Double</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#summary" title="Summary">Summary</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
        "<a href="#throttle" title="Throttle">Throttle</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#alertrule" title="AlertRule">AlertRule</a>" : <i>[ <a href="alertruledefinition.md">AlertRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Alertconfig
Properties:
    <a href="#actiongroupref" title="ActionGroupRef">ActionGroupRef</a>: <i>String</i>
    <a href="#autoscalealert" title="AutoscaleAlert">AutoscaleAlert</a>: <i>Boolean</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#expirytime" title="ExpiryTime">ExpiryTime</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objuuid" title="ObjUuid">ObjUuid</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#recommendation" title="Recommendation">Recommendation</a>: <i>String</i>
    <a href="#rollingwindow" title="RollingWindow">RollingWindow</a>: <i>Double</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#summary" title="Summary">Summary</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
    <a href="#throttle" title="Throttle">Throttle</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#alertrule" title="AlertRule">AlertRule</a>: <i>
      - <a href="alertruledefinition.md">AlertRuleDefinition</a></i>
</pre>

## Properties

#### ActionGroupRef

The alert config will trigger the selected alert action, which can send notifications and execute a controlscript. It is a reference to an object of type actiongroupconfig.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleAlert

This alert config applies to auto scale alerts.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Determines whether an alert is raised immediately when event occurs (realtime) or after specified number of events occurs within rolling time window. Enum options - REALTIME, ROLLINGWINDOW, WATERMARK.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A custom description field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable or disable this alert config from generating new alerts.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiryTime

An alert is expired and deleted after the expiry time has elapsed. The original event triggering the alert remains in the event's log. Allowed values are 1-31536000. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the alert configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjUuid

Uuid of the resource for which alert was raised.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

The object type to which the alert config is associated with. Valid object types are - virtual service, pool, service engine. Enum options - VIRTUALSERVICE, POOL, HEALTHMONITOR, NETWORKPROFILE, APPLICATIONPROFILE, HTTPPOLICYSET, DNSPOLICY, SECURITYPOLICY, IPADDRGROUP, STRINGGROUP, SSLPROFILE, SSLKEYANDCERTIFICATE, NETWORKSECURITYPOLICY, APPLICATIONPERSISTENCEPROFILE, ANALYTICSPROFILE, VSDATASCRIPTSET, TENANT, PKIPROFILE, AUTHPROFILE, CLOUD...

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recommendation

Placeholder for description of property recommendation of obj type alertconfig field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingWindow

Only if the number of events is reached or exceeded within the time window will an alert be generated. Allowed values are 1-31536000. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Signifies system events or the type of client logsused in this alert configuration. Enum options - CONN_LOGS, APP_LOGS, EVENT_LOGS, METRICS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Summary

Summary of reason why alert is generated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

An alert is created only when the number of events meets or exceeds this number within the chosen time frame. Allowed values are 1-65536.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throttle

Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config. Allowed values are 0-31536000. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertRule

_Required_: No

_Type_: List of <a href="alertruledefinition.md">AlertRuleDefinition</a>

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


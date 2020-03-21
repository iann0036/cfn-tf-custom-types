# Terraform::AzureRM::SqlDatabase ThreatDetectionPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disabledalerts" title="DisabledAlerts">DisabledAlerts</a>" : <i>[ String, ... ]</i>,
    "<a href="#emailaccountadmins" title="EmailAccountAdmins">EmailAccountAdmins</a>" : <i>String</i>,
    "<a href="#emailaddresses" title="EmailAddresses">EmailAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>" : <i>String</i>,
    "<a href="#storageendpoint" title="StorageEndpoint">StorageEndpoint</a>" : <i>String</i>,
    "<a href="#useserverdefault" title="UseServerDefault">UseServerDefault</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#disabledalerts" title="DisabledAlerts">DisabledAlerts</a>: <i>
      - String</i>
<a href="#emailaccountadmins" title="EmailAccountAdmins">EmailAccountAdmins</a>: <i>String</i>
<a href="#emailaddresses" title="EmailAddresses">EmailAddresses</a>: <i>
      - String</i>
<a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>: <i>String</i>
<a href="#storageendpoint" title="StorageEndpoint">StorageEndpoint</a>: <i>String</i>
<a href="#useserverdefault" title="UseServerDefault">UseServerDefault</a>: <i>String</i>
</pre>

## Properties

#### DisabledAlerts

Specifies a list of alerts which should be disabled. Possible values include `Access_Anomaly`, `Sql_Injection` and `Sql_Injection_Vulnerability`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAccountAdmins

Should the account administrators be emailed when this alert is triggered?.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddresses

A list of email addresses which alerts should be sent to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

Specifies the number of days to keep in the Threat Detection audit logs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

The State of the Policy. Possible values are `Enabled`, `Disabled` or `New`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKey

Specifies the identifier key of the Threat Detection audit storage account. Required if `state` is `Enabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageEndpoint

Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. Required if `state` is `Enabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseServerDefault

Should the default server policy be used? Defaults to `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::AzureRM::MonitorLogProfile

Manages a [Log Profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile). A Log Profile configures how Activity Logs are exported.

-> **NOTE:** It's only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with `StatusCode=409` will occur.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::MonitorLogProfile",
    "Properties" : {
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ String, ... ]</i>,
        "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicebusruleid" title="ServicebusRuleId">ServicebusRuleId</a>" : <i>String</i>,
        "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicy.md">RetentionPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::MonitorLogProfile
Properties:
    <a href="#categories" title="Categories">Categories</a>: <i>
      - String</i>
    <a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicebusruleid" title="ServicebusRuleId">ServicebusRuleId</a>: <i>String</i>
    <a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicy.md">RetentionPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Categories

List of categories of the logs.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

List of regions for which Activity Log events are stored or streamed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Log Profile. Changing this forces a
new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicebusRuleId

The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="retentionpolicy.md">RetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


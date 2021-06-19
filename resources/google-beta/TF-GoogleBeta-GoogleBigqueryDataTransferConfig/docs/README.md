# TF::GoogleBeta::GoogleBigqueryDataTransferConfig

CloudFormation equivalent of google_bigquery_data_transfer_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleBigqueryDataTransferConfig",
    "Properties" : {
        "<a href="#datarefreshwindowdays" title="DataRefreshWindowDays">DataRefreshWindowDays</a>" : <i>Double</i>,
        "<a href="#datasourceid" title="DataSourceId">DataSourceId</a>" : <i>String</i>,
        "<a href="#destinationdatasetid" title="DestinationDatasetId">DestinationDatasetId</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#notificationpubsubtopic" title="NotificationPubsubTopic">NotificationPubsubTopic</a>" : <i>String</i>,
        "<a href="#params" title="Params">Params</a>" : <i>[ <a href="paramsdefinition.md">ParamsDefinition</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>" : <i>String</i>,
        "<a href="#emailpreferences" title="EmailPreferences">EmailPreferences</a>" : <i>[ <a href="emailpreferencesdefinition.md">EmailPreferencesDefinition</a>, ... ]</i>,
        "<a href="#scheduleoptions" title="ScheduleOptions">ScheduleOptions</a>" : <i>[ <a href="scheduleoptionsdefinition.md">ScheduleOptionsDefinition</a>, ... ]</i>,
        "<a href="#sensitiveparams" title="SensitiveParams">SensitiveParams</a>" : <i>[ <a href="sensitiveparamsdefinition.md">SensitiveParamsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleBigqueryDataTransferConfig
Properties:
    <a href="#datarefreshwindowdays" title="DataRefreshWindowDays">DataRefreshWindowDays</a>: <i>Double</i>
    <a href="#datasourceid" title="DataSourceId">DataSourceId</a>: <i>String</i>
    <a href="#destinationdatasetid" title="DestinationDatasetId">DestinationDatasetId</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#notificationpubsubtopic" title="NotificationPubsubTopic">NotificationPubsubTopic</a>: <i>String</i>
    <a href="#params" title="Params">Params</a>: <i>
      - <a href="paramsdefinition.md">ParamsDefinition</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#serviceaccountname" title="ServiceAccountName">ServiceAccountName</a>: <i>String</i>
    <a href="#emailpreferences" title="EmailPreferences">EmailPreferences</a>: <i>
      - <a href="emailpreferencesdefinition.md">EmailPreferencesDefinition</a></i>
    <a href="#scheduleoptions" title="ScheduleOptions">ScheduleOptions</a>: <i>
      - <a href="scheduleoptionsdefinition.md">ScheduleOptionsDefinition</a></i>
    <a href="#sensitiveparams" title="SensitiveParams">SensitiveParams</a>: <i>
      - <a href="sensitiveparamsdefinition.md">SensitiveParamsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DataRefreshWindowDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationDatasetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationPubsubTopic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: Yes

_Type_: List of <a href="paramsdefinition.md">ParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailPreferences

_Required_: No

_Type_: List of <a href="emailpreferencesdefinition.md">EmailPreferencesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleOptions

_Required_: No

_Type_: List of <a href="scheduleoptionsdefinition.md">ScheduleOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveParams

_Required_: No

_Type_: List of <a href="sensitiveparamsdefinition.md">SensitiveParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Name

Returns the <code>Name</code> value.


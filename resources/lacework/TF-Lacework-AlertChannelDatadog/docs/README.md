# TF::Lacework::AlertChannelDatadog

The Datadog alert channel provides a unified view of your metrics, logs, and performance data combined with your cloud security data.

To find more information about the Datadog alert channel integration, see the [Lacework support documentation](https://support.lacework.com/hc/en-us/articles/360036989953-Datadog).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelDatadog",
    "Properties" : {
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#datadogservice" title="DatadogService">DatadogService</a>" : <i>String</i>,
        "<a href="#datadogsite" title="DatadogSite">DatadogSite</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelDatadog
Properties:
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#datadogservice" title="DatadogService">DatadogService</a>: <i>String</i>
    <a href="#datadogsite" title="DatadogSite">DatadogSite</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ApiKey

The Datadog api key required to submit metrics and events to Datadog.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatadogService

The level of detail of logs or event stream.  `Logs Detail`, `Logs Summary`, or `Events Summary`. Defaults to `Logs Detail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatadogSite

Where to store your logs, either the US or Europe. Must be one of `com` or `eu`. Defaults to `com`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

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

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.


# TF::AzureRM::EventgridEventSubscription WebhookEndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activedirectoryappidoruri" title="ActiveDirectoryAppIdOrUri">ActiveDirectoryAppIdOrUri</a>" : <i>String</i>,
    "<a href="#activedirectorytenantid" title="ActiveDirectoryTenantId">ActiveDirectoryTenantId</a>" : <i>String</i>,
    "<a href="#maxeventsperbatch" title="MaxEventsPerBatch">MaxEventsPerBatch</a>" : <i>Double</i>,
    "<a href="#preferredbatchsizeinkilobytes" title="PreferredBatchSizeInKilobytes">PreferredBatchSizeInKilobytes</a>" : <i>Double</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#activedirectoryappidoruri" title="ActiveDirectoryAppIdOrUri">ActiveDirectoryAppIdOrUri</a>: <i>String</i>
<a href="#activedirectorytenantid" title="ActiveDirectoryTenantId">ActiveDirectoryTenantId</a>: <i>String</i>
<a href="#maxeventsperbatch" title="MaxEventsPerBatch">MaxEventsPerBatch</a>: <i>Double</i>
<a href="#preferredbatchsizeinkilobytes" title="PreferredBatchSizeInKilobytes">PreferredBatchSizeInKilobytes</a>: <i>Double</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### ActiveDirectoryAppIdOrUri

The Azure Active Directory Application ID or URI to get the access token that will be included as the bearer token in delivery requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectoryTenantId

The Azure Active Directory Tenant ID to get the access token that will be included as the bearer token in delivery requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEventsPerBatch

Maximum number of events per batch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBatchSizeInKilobytes

Preferred batch size in Kilobytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Specifies the url of the webhook where the Event Subscription will receive events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


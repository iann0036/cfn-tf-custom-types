# TF::MongoDBAtlas::ThirdPartyIntegration

`mongodbatlas_third_party_integration` Provides a Third-Party Integration Settings for the given type.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

-> **NOTE:** Slack integrations now use the OAuth2 verification method and must be initially configured, or updated from a legacy integration, through the Atlas third-party service integrations page. Legacy tokens will soon no longer be supported.[Read more about slack setup](https://docs.atlas.mongodb.com/tutorial/third-party-service-integrations/)

~> **IMPORTANT** Each project can only have one configuration per {INTEGRATION-TYPE}.

~> **IMPORTANT:** All arguments including the secrets will be stored in the raw state as plain-text. [Read more about sensitive data in state.](https://www.terraform.io/docs/state/sensitive-data.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::ThirdPartyIntegration",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#apitoken" title="ApiToken">ApiToken</a>" : <i>String</i>,
        "<a href="#channelname" title="ChannelName">ChannelName</a>" : <i>String</i>,
        "<a href="#flowname" title="FlowName">FlowName</a>" : <i>String</i>,
        "<a href="#licensekey" title="LicenseKey">LicenseKey</a>" : <i>String</i>,
        "<a href="#orgname" title="OrgName">OrgName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#readtoken" title="ReadToken">ReadToken</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#routingkey" title="RoutingKey">RoutingKey</a>" : <i>String</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>String</i>,
        "<a href="#servicekey" title="ServiceKey">ServiceKey</a>" : <i>String</i>,
        "<a href="#teamname" title="TeamName">TeamName</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#writetoken" title="WriteToken">WriteToken</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::ThirdPartyIntegration
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#apitoken" title="ApiToken">ApiToken</a>: <i>String</i>
    <a href="#channelname" title="ChannelName">ChannelName</a>: <i>String</i>
    <a href="#flowname" title="FlowName">FlowName</a>: <i>String</i>
    <a href="#licensekey" title="LicenseKey">LicenseKey</a>: <i>String</i>
    <a href="#orgname" title="OrgName">OrgName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#readtoken" title="ReadToken">ReadToken</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#routingkey" title="RoutingKey">RoutingKey</a>: <i>String</i>
    <a href="#secret" title="Secret">Secret</a>: <i>String</i>
    <a href="#servicekey" title="ServiceKey">ServiceKey</a>: <i>String</i>
    <a href="#teamname" title="TeamName">TeamName</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#writetoken" title="WriteToken">WriteToken</a>: <i>String</i>
</pre>

## Properties

#### AccountId

Unique identifier of your New Relic account.
* `write_token` - Your Insights Insert Key.
* `read_token`  - Your Insights Query Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

Your API Key.
* `routing_key` - An optional field for your Routing Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiToken

Your API Token.
* `org_name` - Your Flowdock organization name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowName

Your Flowdock Flow name.
* `api_token` - Your API Token.
* `org_name` - Your Flowdock organization name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseKey

Your License Key.
* `account_id`  - Unique identifier of your New Relic account.
* `write_token` - Your Insights Insert Key.
* `read_token`  - Your Insights Query Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgName

Your Flowdock organization name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to get all Third-Party service integrations.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadToken

Your Insights Query Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Indicates which API URL to use, either US or EU. Opsgenie will use US by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingKey

An optional field for your Routing Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

An optional field for your webhook secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceKey

Your Service Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Third-Party Integration Settings type
* PAGER_DUTY
* DATADOG
* NEW_RELIC
* OPS_GENIE
* VICTOR_OPS
* FLOWDOCK
* WEBHOOK.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Your webhook URL.
* `secret` - An optional field for your webhook secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteToken

Your Insights Insert Key.
* `read_token`  - Your Insights Query Key.

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


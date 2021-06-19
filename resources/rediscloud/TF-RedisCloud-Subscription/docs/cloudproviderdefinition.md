# TF::RedisCloud::Subscription CloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>" : <i>String</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>[ <a href="regiondefinition.md">RegionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>: <i>String</i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>
      - <a href="regiondefinition.md">RegionDefinition</a></i>
</pre>

## Properties

#### CloudAccountId

Cloud account identifier. Default: Redis Labs internal cloud account
(using Cloud Account ID = 1 implies using Redis Labs internal cloud account). Note that a GCP subscription can be created
only with Redis Labs internal cloud account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

The cloud provider to use with the subscription, (either `AWS` or `GCP`). Default: ‘AWS’.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: List of <a href="regiondefinition.md">RegionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::Aiven::ServiceIntegrationEndpoint DatadogUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datadogapikey" title="DatadogApiKey">DatadogApiKey</a>" : <i>String</i>,
    "<a href="#disableconsumerstats" title="DisableConsumerStats">DisableConsumerStats</a>" : <i>String</i>,
    "<a href="#maxpartitioncontexts" title="MaxPartitionContexts">MaxPartitionContexts</a>" : <i>String</i>,
    "<a href="#site" title="Site">Site</a>" : <i>String</i>,
    "<a href="#datadogtags" title="DatadogTags">DatadogTags</a>" : <i>[ <a href="datadogtagsdefinition.md">DatadogTagsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#datadogapikey" title="DatadogApiKey">DatadogApiKey</a>: <i>String</i>
<a href="#disableconsumerstats" title="DisableConsumerStats">DisableConsumerStats</a>: <i>String</i>
<a href="#maxpartitioncontexts" title="MaxPartitionContexts">MaxPartitionContexts</a>: <i>String</i>
<a href="#site" title="Site">Site</a>: <i>String</i>
<a href="#datadogtags" title="DatadogTags">DatadogTags</a>: <i>
      - <a href="datadogtagsdefinition.md">DatadogTagsDefinition</a></i>
</pre>

## Properties

#### DatadogApiKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableConsumerStats

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPartitionContexts

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Site

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatadogTags

_Required_: No

_Type_: List of <a href="datadogtagsdefinition.md">DatadogTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


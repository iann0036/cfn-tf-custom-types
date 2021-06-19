# TF::Panos::PanoramaLogForwardingProfile ActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>" : <i>[ <a href="azureintegrationdefinition.md">AzureIntegrationDefinition</a>, ... ]</i>,
    "<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>" : <i>[ <a href="taggingintegrationdefinition.md">TaggingIntegrationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>: <i>
      - <a href="azureintegrationdefinition.md">AzureIntegrationDefinition</a></i>
<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>: <i>
      - <a href="taggingintegrationdefinition.md">TaggingIntegrationDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureIntegration

_Required_: No

_Type_: List of <a href="azureintegrationdefinition.md">AzureIntegrationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggingIntegration

_Required_: No

_Type_: List of <a href="taggingintegrationdefinition.md">TaggingIntegrationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


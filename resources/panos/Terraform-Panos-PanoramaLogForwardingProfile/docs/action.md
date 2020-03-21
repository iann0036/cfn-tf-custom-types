# Terraform::Panos::PanoramaLogForwardingProfile Action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>" : <i>[ &lt;a href=&#34;action-azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;, ... ]</i>,
    "<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>" : <i>[ &lt;a href=&#34;action-taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>: <i>
      - &lt;a href=&#34;action-azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;</i>
<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>: <i>
      - &lt;a href=&#34;action-taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;</i>
</pre>

## Properties

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureIntegration

_Required_: No
_Type_: List of &lt;a href=&#34;action-azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggingIntegration

_Required_: No
_Type_: List of &lt;a href=&#34;action-taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


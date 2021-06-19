# TF::AzureRM::NetworkConnectionMonitor TestGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationendpoints" title="DestinationEndpoints">DestinationEndpoints</a>" : <i>[ String, ... ]</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sourceendpoints" title="SourceEndpoints">SourceEndpoints</a>" : <i>[ String, ... ]</i>,
    "<a href="#testconfigurationnames" title="TestConfigurationNames">TestConfigurationNames</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationendpoints" title="DestinationEndpoints">DestinationEndpoints</a>: <i>
      - String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sourceendpoints" title="SourceEndpoints">SourceEndpoints</a>: <i>
      - String</i>
<a href="#testconfigurationnames" title="TestConfigurationNames">TestConfigurationNames</a>: <i>
      - String</i>
</pre>

## Properties

#### DestinationEndpoints

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEndpoints

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestConfigurationNames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


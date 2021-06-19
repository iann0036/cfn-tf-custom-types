# TF::AWS::AthenaWorkgroup ConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bytesscannedcutoffperquery" title="BytesScannedCutoffPerQuery">BytesScannedCutoffPerQuery</a>" : <i>Double</i>,
    "<a href="#enforceworkgroupconfiguration" title="EnforceWorkgroupConfiguration">EnforceWorkgroupConfiguration</a>" : <i>Boolean</i>,
    "<a href="#publishcloudwatchmetricsenabled" title="PublishCloudwatchMetricsEnabled">PublishCloudwatchMetricsEnabled</a>" : <i>Boolean</i>,
    "<a href="#resultconfiguration" title="ResultConfiguration">ResultConfiguration</a>" : <i>[ <a href="resultconfigurationdefinition.md">ResultConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bytesscannedcutoffperquery" title="BytesScannedCutoffPerQuery">BytesScannedCutoffPerQuery</a>: <i>Double</i>
<a href="#enforceworkgroupconfiguration" title="EnforceWorkgroupConfiguration">EnforceWorkgroupConfiguration</a>: <i>Boolean</i>
<a href="#publishcloudwatchmetricsenabled" title="PublishCloudwatchMetricsEnabled">PublishCloudwatchMetricsEnabled</a>: <i>Boolean</i>
<a href="#resultconfiguration" title="ResultConfiguration">ResultConfiguration</a>: <i>
      - <a href="resultconfigurationdefinition.md">ResultConfigurationDefinition</a></i>
</pre>

## Properties

#### BytesScannedCutoffPerQuery

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceWorkgroupConfiguration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishCloudwatchMetricsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResultConfiguration

_Required_: No

_Type_: List of <a href="resultconfigurationdefinition.md">ResultConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


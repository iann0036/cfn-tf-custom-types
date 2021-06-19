# TF::AWS::ImagebuilderDistributionConfiguration DistributionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#licenseconfigurationarns" title="LicenseConfigurationArns">LicenseConfigurationArns</a>" : <i>[ String, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#amidistributionconfiguration" title="AmiDistributionConfiguration">AmiDistributionConfiguration</a>" : <i>[ <a href="amidistributionconfigurationdefinition.md">AmiDistributionConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#licenseconfigurationarns" title="LicenseConfigurationArns">LicenseConfigurationArns</a>: <i>
      - String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#amidistributionconfiguration" title="AmiDistributionConfiguration">AmiDistributionConfiguration</a>: <i>
      - <a href="amidistributionconfigurationdefinition.md">AmiDistributionConfigurationDefinition</a></i>
</pre>

## Properties

#### LicenseConfigurationArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmiDistributionConfiguration

_Required_: No

_Type_: List of <a href="amidistributionconfigurationdefinition.md">AmiDistributionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


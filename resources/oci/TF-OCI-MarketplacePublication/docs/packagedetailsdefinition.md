# TF::OCI::MarketplacePublication PackageDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
    "<a href="#packageversion" title="PackageVersion">PackageVersion</a>" : <i>String</i>,
    "<a href="#eula" title="Eula">Eula</a>" : <i>[ <a href="euladefinition.md">EulaDefinition</a>, ... ]</i>,
    "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>[ <a href="operatingsystemdefinition.md">OperatingSystemDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
<a href="#packageversion" title="PackageVersion">PackageVersion</a>: <i>String</i>
<a href="#eula" title="Eula">Eula</a>: <i>
      - <a href="euladefinition.md">EulaDefinition</a></i>
<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>
      - <a href="operatingsystemdefinition.md">OperatingSystemDefinition</a></i>
</pre>

## Properties

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eula

_Required_: No

_Type_: List of <a href="euladefinition.md">EulaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

_Required_: No

_Type_: List of <a href="operatingsystemdefinition.md">OperatingSystemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


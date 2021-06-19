# TF::AWS::EcsCluster ExecuteCommandConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>String</i>,
    "<a href="#logconfiguration" title="LogConfiguration">LogConfiguration</a>" : <i>[ <a href="logconfigurationdefinition.md">LogConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
<a href="#logging" title="Logging">Logging</a>: <i>String</i>
<a href="#logconfiguration" title="LogConfiguration">LogConfiguration</a>: <i>
      - <a href="logconfigurationdefinition.md">LogConfigurationDefinition</a></i>
</pre>

## Properties

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfiguration

_Required_: No

_Type_: List of <a href="logconfigurationdefinition.md">LogConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


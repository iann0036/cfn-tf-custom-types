# TF::GoogleBeta::GoogleCloudbuildTrigger SecretDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kmskeyname" title="KmsKeyName">KmsKeyName</a>" : <i>String</i>,
    "<a href="#secretenv" title="SecretEnv">SecretEnv</a>" : <i>[ <a href="secretenvdefinition.md">SecretEnvDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#kmskeyname" title="KmsKeyName">KmsKeyName</a>: <i>String</i>
<a href="#secretenv" title="SecretEnv">SecretEnv</a>: <i>
      - <a href="secretenvdefinition.md">SecretEnvDefinition</a></i>
</pre>

## Properties

#### KmsKeyName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretEnv

_Required_: No

_Type_: List of <a href="secretenvdefinition.md">SecretEnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


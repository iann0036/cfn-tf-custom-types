# TF::AWS::CodebuildProject EnvironmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#computetype" title="ComputeType">ComputeType</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#imagepullcredentialstype" title="ImagePullCredentialsType">ImagePullCredentialsType</a>" : <i>String</i>,
    "<a href="#privilegedmode" title="PrivilegedMode">PrivilegedMode</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>" : <i>[ <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a>, ... ]</i>,
    "<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>" : <i>[ <a href="registrycredentialdefinition.md">RegistryCredentialDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#computetype" title="ComputeType">ComputeType</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#imagepullcredentialstype" title="ImagePullCredentialsType">ImagePullCredentialsType</a>: <i>String</i>
<a href="#privilegedmode" title="PrivilegedMode">PrivilegedMode</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>: <i>
      - <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a></i>
<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>: <i>
      - <a href="registrycredentialdefinition.md">RegistryCredentialDefinition</a></i>
</pre>

## Properties

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullCredentialsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivilegedMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariable

_Required_: No

_Type_: List of <a href="environmentvariabledefinition.md">EnvironmentVariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryCredential

_Required_: No

_Type_: List of <a href="registrycredentialdefinition.md">RegistryCredentialDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


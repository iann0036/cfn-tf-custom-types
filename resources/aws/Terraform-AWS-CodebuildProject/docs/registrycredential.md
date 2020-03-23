# Terraform::AWS::CodebuildProject RegistryCredential

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#credential" title="Credential">Credential</a>" : <i>String</i>,
    "<a href="#credentialprovider" title="CredentialProvider">CredentialProvider</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#credential" title="Credential">Credential</a>: <i>String</i>
<a href="#credentialprovider" title="CredentialProvider">CredentialProvider</a>: <i>String</i>
</pre>

## Properties

#### Credential

The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialProvider

The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


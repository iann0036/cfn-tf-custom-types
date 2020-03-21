# Terraform::AWS::AppsyncGraphqlApi AdditionalAuthenticationProvider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
    "<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>" : <i>[ <a href="additionalauthenticationprovider-openidconnectconfig.md">OpenidConnectConfig</a>, ... ]</i>,
    "<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>" : <i>[ <a href="additionalauthenticationprovider-userpoolconfig.md">UserPoolConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>: <i>
      - <a href="additionalauthenticationprovider-openidconnectconfig.md">OpenidConnectConfig</a></i>
<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>: <i>
      - <a href="additionalauthenticationprovider-userpoolconfig.md">UserPoolConfig</a></i>
</pre>

## Properties

#### AuthenticationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidConnectConfig

_Required_: No

_Type_: List of <a href="additionalauthenticationprovider-openidconnectconfig.md">OpenidConnectConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolConfig

_Required_: No

_Type_: List of <a href="additionalauthenticationprovider-userpoolconfig.md">UserPoolConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


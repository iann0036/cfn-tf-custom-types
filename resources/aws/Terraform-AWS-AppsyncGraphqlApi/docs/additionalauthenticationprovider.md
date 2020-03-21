# Terraform::AWS::AppsyncGraphqlApi AdditionalAuthenticationProvider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
    "<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>" : <i>[ &lt;a href=&#34;additionalauthenticationprovider-openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>" : <i>[ &lt;a href=&#34;additionalauthenticationprovider-userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>: <i>
      - &lt;a href=&#34;additionalauthenticationprovider-openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;</i>
<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>: <i>
      - &lt;a href=&#34;additionalauthenticationprovider-userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;</i>
</pre>

## Properties

#### AuthenticationType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidConnectConfig

_Required_: No
_Type_: List of &lt;a href=&#34;additionalauthenticationprovider-openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolConfig

_Required_: No
_Type_: List of &lt;a href=&#34;additionalauthenticationprovider-userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::AWS::AppsyncGraphqlApi

CloudFormation equivalent of aws_appsync_graphql_api

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppsyncGraphqlApi",
    "Properties" : {
        "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#xrayenabled" title="XrayEnabled">XrayEnabled</a>" : <i>Boolean</i>,
        "<a href="#additionalauthenticationprovider" title="AdditionalAuthenticationProvider">AdditionalAuthenticationProvider</a>" : <i>[ &lt;a href=&#34;additionalauthenticationprovider.md&#34;&gt;AdditionalAuthenticationProvider&lt;/a&gt;, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>" : <i>[ &lt;a href=&#34;openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>" : <i>[ &lt;a href=&#34;userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppsyncGraphqlApi
Properties:
    <a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#xrayenabled" title="XrayEnabled">XrayEnabled</a>: <i>Boolean</i>
    <a href="#additionalauthenticationprovider" title="AdditionalAuthenticationProvider">AdditionalAuthenticationProvider</a>: <i>
      - &lt;a href=&#34;additionalauthenticationprovider.md&#34;&gt;AdditionalAuthenticationProvider&lt;/a&gt;</i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;</i>
    <a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>: <i>
      - &lt;a href=&#34;openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;</i>
    <a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>: <i>
      - &lt;a href=&#34;userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;</i>
</pre>

## Properties

#### AuthenticationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalAuthenticationProvider

_Required_: No

_Type_: List of &lt;a href=&#34;additionalauthenticationprovider.md&#34;&gt;AdditionalAuthenticationProvider&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidConnectConfig

_Required_: No

_Type_: List of &lt;a href=&#34;openidconnectconfig.md&#34;&gt;OpenidConnectConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolConfig

_Required_: No

_Type_: List of &lt;a href=&#34;userpoolconfig.md&#34;&gt;UserPoolConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### Uris

Returns the &lt;code&gt;Uris&lt;/code&gt; value.


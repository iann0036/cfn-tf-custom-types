# TF::AWS::AppsyncGraphqlApi

Provides an AppSync GraphQL API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AppsyncGraphqlApi",
    "Properties" : {
        "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#xrayenabled" title="XrayEnabled">XrayEnabled</a>" : <i>Boolean</i>,
        "<a href="#additionalauthenticationprovider" title="AdditionalAuthenticationProvider">AdditionalAuthenticationProvider</a>" : <i>[ <a href="additionalauthenticationproviderdefinition.md">AdditionalAuthenticationProviderDefinition</a>, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfigdefinition.md">LogConfigDefinition</a>, ... ]</i>,
        "<a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>" : <i>[ <a href="openidconnectconfigdefinition.md">OpenidConnectConfigDefinition</a>, ... ]</i>,
        "<a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>" : <i>[ <a href="userpoolconfigdefinition.md">UserPoolConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AppsyncGraphqlApi
Properties:
    <a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#schema" title="Schema">Schema</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#xrayenabled" title="XrayEnabled">XrayEnabled</a>: <i>Boolean</i>
    <a href="#additionalauthenticationprovider" title="AdditionalAuthenticationProvider">AdditionalAuthenticationProvider</a>: <i>
      - <a href="additionalauthenticationproviderdefinition.md">AdditionalAuthenticationProviderDefinition</a></i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfigdefinition.md">LogConfigDefinition</a></i>
    <a href="#openidconnectconfig" title="OpenidConnectConfig">OpenidConnectConfig</a>: <i>
      - <a href="openidconnectconfigdefinition.md">OpenidConnectConfigDefinition</a></i>
    <a href="#userpoolconfig" title="UserPoolConfig">UserPoolConfig</a>: <i>
      - <a href="userpoolconfigdefinition.md">UserPoolConfigDefinition</a></i>
</pre>

## Properties

#### AuthenticationType

The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A user-supplied name for the GraphqlApi.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

The schema definition, in GraphQL schema language format. Terraform cannot perform drift detection of this configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayEnabled

Whether tracing with X-ray is enabled. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalAuthenticationProvider

_Required_: No

_Type_: List of <a href="additionalauthenticationproviderdefinition.md">AdditionalAuthenticationProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfigdefinition.md">LogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidConnectConfig

_Required_: No

_Type_: List of <a href="openidconnectconfigdefinition.md">OpenidConnectConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolConfig

_Required_: No

_Type_: List of <a href="userpoolconfigdefinition.md">UserPoolConfigDefinition</a>

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

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uris

Returns the <code>Uris</code> value.


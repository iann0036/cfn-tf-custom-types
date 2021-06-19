# TF::AWS::Apigatewayv2DomainName

Manages an Amazon API Gateway Version 2 domain name.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

-> **Note:** This resource establishes ownership of and the TLS settings for
a particular domain name. An API stage can be associated with the domain name using the `aws_apigatewayv2_api_mapping` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2DomainName",
    "Properties" : {
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#domainnameconfiguration" title="DomainNameConfiguration">DomainNameConfiguration</a>" : <i>[ <a href="domainnameconfigurationdefinition.md">DomainNameConfigurationDefinition</a>, ... ]</i>,
        "<a href="#mutualtlsauthentication" title="MutualTlsAuthentication">MutualTlsAuthentication</a>" : <i>[ <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2DomainName
Properties:
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#domainnameconfiguration" title="DomainNameConfiguration">DomainNameConfiguration</a>: <i>
      - <a href="domainnameconfigurationdefinition.md">DomainNameConfigurationDefinition</a></i>
    <a href="#mutualtlsauthentication" title="MutualTlsAuthentication">MutualTlsAuthentication</a>: <i>
      - <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DomainName

The domain name. Must be between 1 and 512 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the domain name. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNameConfiguration

_Required_: No

_Type_: List of <a href="domainnameconfigurationdefinition.md">DomainNameConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MutualTlsAuthentication

_Required_: No

_Type_: List of <a href="mutualtlsauthenticationdefinition.md">MutualTlsAuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiMappingSelectionExpression

Returns the <code>ApiMappingSelectionExpression</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.


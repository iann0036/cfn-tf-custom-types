# Terraform::AWS::ApiGatewayMethod

CloudFormation equivalent of aws_api_gateway_method

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayMethod",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>" : <i>Boolean</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>String</i>,
        "<a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>" : <i>String</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#requestmodels" title="RequestModels">RequestModels</a>" : <i>[ &lt;a href=&#34;requestmodels.md&#34;&gt;RequestModels&lt;/a&gt;, ... ]</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>" : <i>String</i>,
        "<a href="#requestvalidatorid" title="RequestValidatorId">RequestValidatorId</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayMethod
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>: <i>Boolean</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>String</i>
    <a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>: <i>
      - String</i>
    <a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>: <i>String</i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#requestmodels" title="RequestModels">RequestModels</a>: <i>
      - &lt;a href=&#34;requestmodels.md&#34;&gt;RequestModels&lt;/a&gt;</i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;</i>
    <a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>: <i>String</i>
    <a href="#requestvalidatorid" title="RequestValidatorId">RequestValidatorId</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKeyRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestModels

_Required_: No

_Type_: List of &lt;a href=&#34;requestmodels.md&#34;&gt;RequestModels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

_Required_: No

_Type_: List of &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParametersInJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestValidatorId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


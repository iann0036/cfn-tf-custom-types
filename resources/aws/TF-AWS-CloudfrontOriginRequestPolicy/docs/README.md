# TF::AWS::CloudfrontOriginRequestPolicy

CloudFormation equivalent of aws_cloudfront_origin_request_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudfrontOriginRequestPolicy",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#cookiesconfig" title="CookiesConfig">CookiesConfig</a>" : <i>[ <a href="cookiesconfigdefinition.md">CookiesConfigDefinition</a>, ... ]</i>,
        "<a href="#headersconfig" title="HeadersConfig">HeadersConfig</a>" : <i>[ <a href="headersconfigdefinition.md">HeadersConfigDefinition</a>, ... ]</i>,
        "<a href="#querystringsconfig" title="QueryStringsConfig">QueryStringsConfig</a>" : <i>[ <a href="querystringsconfigdefinition.md">QueryStringsConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudfrontOriginRequestPolicy
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#cookiesconfig" title="CookiesConfig">CookiesConfig</a>: <i>
      - <a href="cookiesconfigdefinition.md">CookiesConfigDefinition</a></i>
    <a href="#headersconfig" title="HeadersConfig">HeadersConfig</a>: <i>
      - <a href="headersconfigdefinition.md">HeadersConfigDefinition</a></i>
    <a href="#querystringsconfig" title="QueryStringsConfig">QueryStringsConfig</a>: <i>
      - <a href="querystringsconfigdefinition.md">QueryStringsConfigDefinition</a></i>
</pre>

## Properties

#### Comment

Comment to describe the origin request policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique name to identify the origin request policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookiesConfig

_Required_: No

_Type_: List of <a href="cookiesconfigdefinition.md">CookiesConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadersConfig

_Required_: No

_Type_: List of <a href="headersconfigdefinition.md">HeadersConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringsConfig

_Required_: No

_Type_: List of <a href="querystringsconfigdefinition.md">QueryStringsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


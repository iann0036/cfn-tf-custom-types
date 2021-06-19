# TF::AWS::CloudfrontCachePolicy ParametersInCacheKeyAndForwardedToOriginDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableacceptencodingbrotli" title="EnableAcceptEncodingBrotli">EnableAcceptEncodingBrotli</a>" : <i>Boolean</i>,
    "<a href="#enableacceptencodinggzip" title="EnableAcceptEncodingGzip">EnableAcceptEncodingGzip</a>" : <i>Boolean</i>,
    "<a href="#cookiesconfig" title="CookiesConfig">CookiesConfig</a>" : <i>[ <a href="cookiesconfigdefinition.md">CookiesConfigDefinition</a>, ... ]</i>,
    "<a href="#headersconfig" title="HeadersConfig">HeadersConfig</a>" : <i>[ <a href="headersconfigdefinition.md">HeadersConfigDefinition</a>, ... ]</i>,
    "<a href="#querystringsconfig" title="QueryStringsConfig">QueryStringsConfig</a>" : <i>[ <a href="querystringsconfigdefinition.md">QueryStringsConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableacceptencodingbrotli" title="EnableAcceptEncodingBrotli">EnableAcceptEncodingBrotli</a>: <i>Boolean</i>
<a href="#enableacceptencodinggzip" title="EnableAcceptEncodingGzip">EnableAcceptEncodingGzip</a>: <i>Boolean</i>
<a href="#cookiesconfig" title="CookiesConfig">CookiesConfig</a>: <i>
      - <a href="cookiesconfigdefinition.md">CookiesConfigDefinition</a></i>
<a href="#headersconfig" title="HeadersConfig">HeadersConfig</a>: <i>
      - <a href="headersconfigdefinition.md">HeadersConfigDefinition</a></i>
<a href="#querystringsconfig" title="QueryStringsConfig">QueryStringsConfig</a>: <i>
      - <a href="querystringsconfigdefinition.md">QueryStringsConfigDefinition</a></i>
</pre>

## Properties

#### EnableAcceptEncodingBrotli

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAcceptEncodingGzip

_Required_: No

_Type_: Boolean

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


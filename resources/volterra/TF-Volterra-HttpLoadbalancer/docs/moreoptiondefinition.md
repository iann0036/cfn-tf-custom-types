# TF::Volterra::HttpLoadbalancer MoreOptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customerrors" title="CustomErrors">CustomErrors</a>" : <i>[ <a href="customerrorsdefinition.md">CustomErrorsDefinition</a>, ... ]</i>,
    "<a href="#disabledefaulterrorpages" title="DisableDefaultErrorPages">DisableDefaultErrorPages</a>" : <i>Boolean</i>,
    "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
    "<a href="#maxrequestheadersize" title="MaxRequestHeaderSize">MaxRequestHeaderSize</a>" : <i>Double</i>,
    "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>" : <i>[ <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>, ... ]</i>,
    "<a href="#compressionparams" title="CompressionParams">CompressionParams</a>" : <i>[ <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a>, ... ]</i>,
    "<a href="#javascriptinfo" title="JavascriptInfo">JavascriptInfo</a>" : <i>[ <a href="javascriptinfodefinition.md">JavascriptInfoDefinition</a>, ... ]</i>,
    "<a href="#jwt" title="Jwt">Jwt</a>" : <i>[ <a href="jwtdefinition.md">JwtDefinition</a>, ... ]</i>,
    "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>, ... ]</i>,
    "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customerrors" title="CustomErrors">CustomErrors</a>: <i>
      - <a href="customerrorsdefinition.md">CustomErrorsDefinition</a></i>
<a href="#disabledefaulterrorpages" title="DisableDefaultErrorPages">DisableDefaultErrorPages</a>: <i>Boolean</i>
<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
<a href="#maxrequestheadersize" title="MaxRequestHeaderSize">MaxRequestHeaderSize</a>: <i>Double</i>
<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>: <i>
      - String</i>
<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>: <i>
      - <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a></i>
<a href="#compressionparams" title="CompressionParams">CompressionParams</a>: <i>
      - <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a></i>
<a href="#javascriptinfo" title="JavascriptInfo">JavascriptInfo</a>: <i>
      - <a href="javascriptinfodefinition.md">JavascriptInfoDefinition</a></i>
<a href="#jwt" title="Jwt">Jwt</a>: <i>
      - <a href="jwtdefinition.md">JwtDefinition</a></i>
<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a></i>
<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a></i>
</pre>

## Properties

#### CustomErrors

_Required_: No

_Type_: List of <a href="customerrorsdefinition.md">CustomErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDefaultErrorPages

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestHeaderSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferPolicy

_Required_: No

_Type_: List of <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionParams

_Required_: No

_Type_: List of <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavascriptInfo

_Required_: No

_Type_: List of <a href="javascriptinfodefinition.md">JavascriptInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jwt

_Required_: No

_Type_: List of <a href="jwtdefinition.md">JwtDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::AWS::CloudwatchEventConnection AuthParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>[ <a href="apikeydefinition.md">ApiKeyDefinition</a>, ... ]</i>,
    "<a href="#basic" title="Basic">Basic</a>" : <i>[ <a href="basicdefinition.md">BasicDefinition</a>, ... ]</i>,
    "<a href="#invocationhttpparameters" title="InvocationHttpParameters">InvocationHttpParameters</a>" : <i>[ <a href="invocationhttpparametersdefinition.md">InvocationHttpParametersDefinition</a>, ... ]</i>,
    "<a href="#oauth" title="Oauth">Oauth</a>" : <i>[ <a href="oauthdefinition.md">OauthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>
      - <a href="apikeydefinition.md">ApiKeyDefinition</a></i>
<a href="#basic" title="Basic">Basic</a>: <i>
      - <a href="basicdefinition.md">BasicDefinition</a></i>
<a href="#invocationhttpparameters" title="InvocationHttpParameters">InvocationHttpParameters</a>: <i>
      - <a href="invocationhttpparametersdefinition.md">InvocationHttpParametersDefinition</a></i>
<a href="#oauth" title="Oauth">Oauth</a>: <i>
      - <a href="oauthdefinition.md">OauthDefinition</a></i>
</pre>

## Properties

#### ApiKey

_Required_: No

_Type_: List of <a href="apikeydefinition.md">ApiKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Basic

_Required_: No

_Type_: List of <a href="basicdefinition.md">BasicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvocationHttpParameters

_Required_: No

_Type_: List of <a href="invocationhttpparametersdefinition.md">InvocationHttpParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oauth

_Required_: No

_Type_: List of <a href="oauthdefinition.md">OauthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


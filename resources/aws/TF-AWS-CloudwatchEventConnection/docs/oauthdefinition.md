# TF::AWS::CloudwatchEventConnection OauthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>" : <i>String</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
    "<a href="#clientparameters" title="ClientParameters">ClientParameters</a>" : <i>[ <a href="clientparametersdefinition.md">ClientParametersDefinition</a>, ... ]</i>,
    "<a href="#oauthhttpparameters" title="OauthHttpParameters">OauthHttpParameters</a>" : <i>[ <a href="oauthhttpparametersdefinition.md">OauthHttpParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>: <i>String</i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
<a href="#clientparameters" title="ClientParameters">ClientParameters</a>: <i>
      - <a href="clientparametersdefinition.md">ClientParametersDefinition</a></i>
<a href="#oauthhttpparameters" title="OauthHttpParameters">OauthHttpParameters</a>: <i>
      - <a href="oauthhttpparametersdefinition.md">OauthHttpParametersDefinition</a></i>
</pre>

## Properties

#### AuthorizationEndpoint

A username for the authorization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

A password for the authorization. Created and stored in AWS Secrets Manager.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientParameters

_Required_: No

_Type_: List of <a href="clientparametersdefinition.md">ClientParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthHttpParameters

_Required_: No

_Type_: List of <a href="oauthhttpparametersdefinition.md">OauthHttpParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


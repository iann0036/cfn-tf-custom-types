# TF::Cloudflare::AccessGroup ExcludeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anyvalidservicetoken" title="AnyValidServiceToken">AnyValidServiceToken</a>" : <i>Boolean</i>,
    "<a href="#authmethod" title="AuthMethod">AuthMethod</a>" : <i>String</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>Boolean</i>,
    "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
    "<a href="#deviceposture" title="DevicePosture">DevicePosture</a>" : <i>[ String, ... ]</i>,
    "<a href="#email" title="Email">Email</a>" : <i>[ String, ... ]</i>,
    "<a href="#emaildomain" title="EmailDomain">EmailDomain</a>" : <i>[ String, ... ]</i>,
    "<a href="#everyone" title="Everyone">Everyone</a>" : <i>Boolean</i>,
    "<a href="#geo" title="Geo">Geo</a>" : <i>[ String, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>[ String, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ String, ... ]</i>,
    "<a href="#loginmethod" title="LoginMethod">LoginMethod</a>" : <i>[ String, ... ]</i>,
    "<a href="#servicetoken" title="ServiceToken">ServiceToken</a>" : <i>[ String, ... ]</i>,
    "<a href="#azure" title="Azure">Azure</a>" : <i>[ <a href="azuredefinition.md">AzureDefinition</a>, ... ]</i>,
    "<a href="#github" title="Github">Github</a>" : <i>[ <a href="githubdefinition.md">GithubDefinition</a>, ... ]</i>,
    "<a href="#gsuite" title="Gsuite">Gsuite</a>" : <i>[ <a href="gsuitedefinition.md">GsuiteDefinition</a>, ... ]</i>,
    "<a href="#okta" title="Okta">Okta</a>" : <i>[ <a href="oktadefinition.md">OktaDefinition</a>, ... ]</i>,
    "<a href="#saml" title="Saml">Saml</a>" : <i>[ <a href="samldefinition.md">SamlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anyvalidservicetoken" title="AnyValidServiceToken">AnyValidServiceToken</a>: <i>Boolean</i>
<a href="#authmethod" title="AuthMethod">AuthMethod</a>: <i>String</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>Boolean</i>
<a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
<a href="#deviceposture" title="DevicePosture">DevicePosture</a>: <i>
      - String</i>
<a href="#email" title="Email">Email</a>: <i>
      - String</i>
<a href="#emaildomain" title="EmailDomain">EmailDomain</a>: <i>
      - String</i>
<a href="#everyone" title="Everyone">Everyone</a>: <i>Boolean</i>
<a href="#geo" title="Geo">Geo</a>: <i>
      - String</i>
<a href="#group" title="Group">Group</a>: <i>
      - String</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - String</i>
<a href="#loginmethod" title="LoginMethod">LoginMethod</a>: <i>
      - String</i>
<a href="#servicetoken" title="ServiceToken">ServiceToken</a>: <i>
      - String</i>
<a href="#azure" title="Azure">Azure</a>: <i>
      - <a href="azuredefinition.md">AzureDefinition</a></i>
<a href="#github" title="Github">Github</a>: <i>
      - <a href="githubdefinition.md">GithubDefinition</a></i>
<a href="#gsuite" title="Gsuite">Gsuite</a>: <i>
      - <a href="gsuitedefinition.md">GsuiteDefinition</a></i>
<a href="#okta" title="Okta">Okta</a>: <i>
      - <a href="oktadefinition.md">OktaDefinition</a></i>
<a href="#saml" title="Saml">Saml</a>: <i>
      - <a href="samldefinition.md">SamlDefinition</a></i>
</pre>

## Properties

#### AnyValidServiceToken

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevicePosture

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailDomain

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Everyone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Geo

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginMethod

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceToken

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Azure

_Required_: No

_Type_: List of <a href="azuredefinition.md">AzureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Github

_Required_: No

_Type_: List of <a href="githubdefinition.md">GithubDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gsuite

_Required_: No

_Type_: List of <a href="gsuitedefinition.md">GsuiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Okta

_Required_: No

_Type_: List of <a href="oktadefinition.md">OktaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Saml

_Required_: No

_Type_: List of <a href="samldefinition.md">SamlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


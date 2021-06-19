# TF::OneLogin::AuthServers ConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesstokenexpirationminutes" title="AccessTokenExpirationMinutes">AccessTokenExpirationMinutes</a>" : <i>Double</i>,
    "<a href="#audiences" title="Audiences">Audiences</a>" : <i>[ String, ... ]</i>,
    "<a href="#refreshtokenexpirationminutes" title="RefreshTokenExpirationMinutes">RefreshTokenExpirationMinutes</a>" : <i>Double</i>,
    "<a href="#resourceidentifier" title="ResourceIdentifier">ResourceIdentifier</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesstokenexpirationminutes" title="AccessTokenExpirationMinutes">AccessTokenExpirationMinutes</a>: <i>Double</i>
<a href="#audiences" title="Audiences">Audiences</a>: <i>
      - String</i>
<a href="#refreshtokenexpirationminutes" title="RefreshTokenExpirationMinutes">RefreshTokenExpirationMinutes</a>: <i>Double</i>
<a href="#resourceidentifier" title="ResourceIdentifier">ResourceIdentifier</a>: <i>String</i>
</pre>

## Properties

#### AccessTokenExpirationMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audiences

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTokenExpirationMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


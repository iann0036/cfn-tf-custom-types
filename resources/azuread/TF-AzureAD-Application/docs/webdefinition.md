# TF::AzureAD::Application WebDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>" : <i>String</i>,
    "<a href="#logouturl" title="LogoutUrl">LogoutUrl</a>" : <i>String</i>,
    "<a href="#redirecturis" title="RedirectUris">RedirectUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#implicitgrant" title="ImplicitGrant">ImplicitGrant</a>" : <i>[ <a href="implicitgrantdefinition.md">ImplicitGrantDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>: <i>String</i>
<a href="#logouturl" title="LogoutUrl">LogoutUrl</a>: <i>String</i>
<a href="#redirecturis" title="RedirectUris">RedirectUris</a>: <i>
      - String</i>
<a href="#implicitgrant" title="ImplicitGrant">ImplicitGrant</a>: <i>
      - <a href="implicitgrantdefinition.md">ImplicitGrantDefinition</a></i>
</pre>

## Properties

#### HomepageUrl

Home page or landing page of the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrl

The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUris

A list of URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImplicitGrant

_Required_: No

_Type_: List of <a href="implicitgrantdefinition.md">ImplicitGrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

